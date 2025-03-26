import torch
from TTS.api import TTS
import sounddevice as sd
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"

model = TTS("tts_models/en/jenny/jenny").to(device)

text = "Let me see what I can do... It really looks like you finally got the audio samples to play correctly! Way to go!"

output = model.tts(text)

with sd.RawOutputStream(samplerate=48000,channels=1,dtype=np.int16):
    sd.play(output,samplerate=48000)
    sd.wait()
