from stt import STT
import time

stt = STT()

print("press CTRL-C to quit")

while True:
    if not stt.is_empty():
        utterance = stt.get_utterance()
        print(utterance)
    else:
        time.sleep(0.1)
