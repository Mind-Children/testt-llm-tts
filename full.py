from stt import STT
from tts import TTS
from ollama import chat,generate
import time

stt = STT()
tts = TTS()

model = 'llama3:8b'

def complete(prompt,system_prompt):
    response = chat(model,messages=[{'role':'system','content':system_prompt},{'role':'user','content':prompt}])
    return response['message']['content']

FIRST = "You are a university math professor that speaks in very convoluted sentences. Answer in one or two very short sentences."

SECOND = "Say the exact opposite of the user's message in one or two very short and simple sentences."

THIRD = "Say the same thing as the user's message in one or two very short and simple sentences using 1950s robotic speech."

print("press CTRL-C to quit")

try:
    while True:
        if not stt.is_empty():
            utterance = stt.get_utterance()
            response = complete(utterance,FIRST)
            #print(f"FIRST: {response}\n")
            response = complete(response,SECOND)
            #print(f"SECOND: {response}\n")
            response = complete(response,THIRD)
            print(response)
            tts.put_utterance(response)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("done")
except Exception as e:
    print(e)
