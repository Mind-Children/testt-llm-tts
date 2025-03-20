from bark import SAMPLE_RATE, generate_audio, preload_models
import sounddevice as sd
import numpy as np

preload_models()

text = "Let me see what I can do... It really looks like you finally got the audio samples to play correctly! Way to go! The last missing component is going to be the LLM."

output = generate_audio(text)

with sd.RawOutputStream(samplerate=SAMPLE_RATE,channels=1,dtype=np.int16):
    sd.play(output,samplerate=SAMPLE_RATE)
    sd.wait()
