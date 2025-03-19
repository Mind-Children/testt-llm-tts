#!/usr/bin/env python3

import queue
import sys
import sounddevice as sd
import numpy as np
from transformers import pipeline,AutoModelForSpeechSeq2Seq,AutoProcessor
from scipy.io.wavfile import write
import torch
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

SAMPLE_RATE = 48000
BLOCK_DURATION = 30
BLOCK_SIZE = int(SAMPLE_RATE * BLOCK_DURATION / 1000)

q = queue.Queue()

def callback(indata,frames,time,status):
    if status:
        print(status,file=sys.stderr)
    print(indata.shape)
    q.put(indata)

try:
    model_id = "distil-whisper/distil-small.en"
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id,
        quantization_config=None,
        low_cpu_mem_usage=True,
        use_safetensors=True,
        attn_implementation="flash_attention_2",
        torch_dtype=torch.bfloat16,
        device_map="cuda",
    )
    processor = AutoProcessor.from_pretrained(model_id)
    pipeline = pipeline("automatic-speech-recognition",model=model,chunk_length_s=1,tokenizer=processor.tokenizer,feature_extractor=processor.feature_extractor,model_kwargs={"use_flash_attention_2":True},device_map="cuda")
    with sd.InputStream(samplerate=SAMPLE_RATE,blocksize=BLOCK_SIZE,device=0,dtype="float32",channels=1,callback=callback):
        print("press Ctrl+C to stop recording")
        while True:
            result = pipeline(q.get())
            print(result)

except KeyboardInterrupt:
    print("done")
    exit(0)

except Exception as e:
    print("exception: ",e)
    exit(-1)
