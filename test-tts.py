from tts import TTS
import time

tts = TTS()

tts.put_utterance("Hello, how are you?")

print("press CTRL-C to quit")

while True:
    time.sleep(0.1)