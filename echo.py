from stt import STT
from tts import TTS
import time

stt = STT()
tts = TTS()

print("press CTRL-C to quit")
try:
    while True:
        if not stt.is_empty():
            utterance = stt.get_utterance()
            print(utterance)
            tts.put_utterance(utterance)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("done")
except Exception as e:
    print(e)
