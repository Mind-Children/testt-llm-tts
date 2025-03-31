from styletts2 import tts
import alsaaudio
import numpy as np
import nltk

nltk.download('punkt_tab')

device = alsaaudio.PCM(channels=1,rate=24000,format=alsaaudio.PCM_FORMAT_S16_LE)

# yeah, so, in line 604 of venv/lib64/python3.12/site-packages/styletts2/models.py, add `weights_only=False` to the `torch.load` function call
model = tts.StyleTTS2()

text = "Let me see what I can do... It really looks like you finally got the audio samples to play correctly! Way to go! The last missing component is going to be the LLM."

output = model.inference(text,"ben.wav",alpha=0.1,beta=0.1)

device.write((output * 32767).astype(np.int16))
