from styletts2.tts import StyleTTS2
import sounddevice as sd
import numpy as np
import time
import threading
import nltk

#nltk.download('punkt_tab')

#VOICE = "arnold"
#VOICE = "ben"
VOICE = "scarlett"
#VOICE = "obi-wan"
#VOICE = "louisck"
#VOICE = "silverhand"
#VOICE = "data"

#devices = sd.query_devices()
#print(devices)

class TTS:
    def __init__(self):
        self.model = StyleTTS2()
        self.utterance_queue = []
        threading.Thread(target=self.streaming_thread).start()

    def streaming_thread(self):
        with sd.RawOutputStream(samplerate=48000,channels=1,dtype=np.int16):
            while True:
                if len(self.utterance_queue) > 0:
                    utterance = self.utterance_queue.pop(0)
                    output = self.model.inference(utterance,f"voices/{VOICE}.wav",beta=0.7)
                    sd.play(output,samplerate=24000)
                    sd.wait()
                else:
                    time.sleep(0.1)

    def put_utterance(self,utterance):
        self.utterance_queue.append(utterance)
