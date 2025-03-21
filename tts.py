from styletts2.tts import StyleTTS2
import sounddevice as sd
import numpy as np
import time
import threading

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
                    output = self.model.inference(utterance,"ben.wav",alpha=0.1,beta=0.1)
                    sd.play(output,samplerate=24000)
                    sd.wait()
                else:
                    time.sleep(0.1)

    def put_utterance(self,utterance):
        self.utterance_queue.append(utterance)