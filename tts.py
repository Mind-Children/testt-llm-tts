import sounddevice as sd
import numpy as np
import time
import threading
import nltk
import scipy.io.wavfile as wavfile

# various options for TTS
BARK = 0
PIPER = 1
STYLETTS = 2

# choose TTShere
TTS_TYPE = PIPER

if TTS_TYPE == BARK:

    from bark import SAMPLE_RATE, generate_audio, preload_models

elif TTS_TYPE == PIPER:

    from piper.voice import PiperVoice
    SAMPLE_RATE = 24000

elif TTS_TYPE == STYLETTS:

    from styletts2.tts import StyleTTS2
    SAMPLE_RATE = 24000

    #VOICE = "arnold"
    #VOICE = "ben"
    VOICE = "scarlett"
    #VOICE = "obi-wan"
    #VOICE = "louisck"
    #VOICE = "silverhand"
    #VOICE = "data"

    #nltk.download('punkt_tab')

#devices = sd.query_devices()
#print(devices)

class TTS:

    def __init__(self,streaming=False):

        if TTS_TYPE == BARK:

            preload_models()

        elif TTS_TYPE == PIPER:

            self.model = PiperVoice.load("models/en_US-amy-low.onnx","models/en_US-amy-low.onnx.json",use_cuda=True)

        elif TTS_TYPE == STYLETTS:

            self.model = StyleTTS2()

        self.utterance_queue = []

        if streaming:
            threading.Thread(target=self.streaming_thread).start()

    def convert(self,utterance):

        if TTS_TYPE == BARK:

            output = generate_audio(utterance)

        elif TTS_TYPE == PIPER:

            output = bytes()
            for chunk in self.model.synthesize_stream_raw(utterance):
                output += chunk
            output = np.frombuffer(output,dtype=np.int16)

        elif TTS_TYPE == STYLETTS:

            output = self.model.inference(utterance,f"voices/{VOICE}.wav",beta=0.7)

        wavfile.write("output.wav",SAMPLE_RATE,output) # to check on machines that have no audio out

        return output

    def streaming_thread(self):

        with sd.RawOutputStream(samplerate=48000,channels=1,dtype=np.int16):
            while True:

                if len(self.utterance_queue) > 0:

                    utterance = self.utterance_queue.pop(0)

                    output = self.convert(utterance)

                    sd.play(output,samplerate=SAMPLE_RATE)
                    sd.wait()

                else:

                    time.sleep(0.1)

    def put_utterance(self,utterance):

        self.utterance_queue.append(utterance)
