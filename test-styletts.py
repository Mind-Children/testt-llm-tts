from styletts2 import tts
import alsaaudio
import nltk
import numpy as np

nltk.download('punkt_tab')

device = alsaaudio.PCM(channels=1,rate=24000,format=alsaaudio.PCM_FORMAT_S16_LE)

my_tts = tts.StyleTTS2()
out = my_tts.inference("Let me see what I can do... It really looks like you finally got the audio samples to play correctly! Way to go! The last missing component is going to be the LLM.",output_sample_rate=24000,output_wav_file="output.wav")
out = (out * 32768.0).astype(np.int16)

device.write(out.tobytes())
