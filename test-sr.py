import queue
import time
import sys
import speech_recognition as sr
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
from scipy.io.wavfile import write

q = queue.Queue()

def callback(indata,frames,time,status):
    if status:
        print(status,file=sys.stderr)
    q.put(indata)

try:
    device_info = sd.query_devices(kind="input")
    model = WhisperModel("small.en", download_root="./models", device="auto",compute_type="int8")
    with sd.RawInputStream(samplerate=48000,blocksize=8000,device=0,dtype="int16",channels=1,callback=callback):
        print("press Ctrl+C to stop recording")
        while True:
            audio = bytes()
            got_audio = False
            time_start = time.time()
            while not got_audio or time.time() - time_start < -1.:
                while not q.empty():
                    audio += q.get()
                    got_audio = True
            tensor = np.frombuffer(audio,dtype=np.int16).flatten()
            write("test.wav",48000,tensor)
            data = tensor.astype(np.float32) / 32768.0
            segments,info = model.transcribe(data)
            for segment in segments:
                print(segment.text)

except KeyboardInterrupt:
    print("done")
    exit(0)

except Exception as e:
    print("exception: ",e)
    exit(-1)
