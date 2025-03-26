from piper.voice import PiperVoice
import sounddevice as sd
import numpy as np

model = PiperVoice.load("models/en_US-amy-low.onnx","models/en_US-amy-low.onnx.json",use_cuda=True)

text = "Let me see what I can do... It really looks like you finally got the audio samples to play correctly! Way to go!"

output = bytes()
for chunk in model.synthesize_stream_raw(text):
    output += chunk
output = np.frombuffer(output,dtype=np.int16)

with sd.RawOutputStream(samplerate=48000,channels=1,dtype=np.int16):
    sd.play(output,samplerate=16000)
    sd.wait()
#device.write((output * 32767).astype(np.int16))
