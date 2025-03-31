import sys
import time
from stt import STT
from llm import LLM
from tts import TTS

stt = STT()
llm = LLM()
tts = TTS()

start_time = time.time()

# STT: transcribe fixed audio sample
text = stt.convert("fixed_input.wav")

print(f"STT: \"{text}\"")

# stt_time is the time it took to transcribe
stt_time = time.time()


# LLM: run the first prompt
PROMPT = "You are a government official helping a citizen with their problem. Summarize your answer in one or two sentences."
result1 = llm.complete(text,PROMPT)

# llm1_time is the time it took to run the first prompt
llm1_time = time.time()

print(f"LLM1: \"{result1}\"")


# LLM: run the second prompt
PROMPT = "You are a famous painter. Say the exact opposite of the user message in one or two sentences."
result2 = llm.complete(result1,PROMPT)

# llm2_time is the time it took to run the second prompt
llm2_time = time.time()

print(f"LLM2: \"{result2}\"")


# LLM: run the third prompt
PROMPT = "Summarize in one or two very opinionated and sarcastic sentences."
result3 = llm.complete(result2,PROMPT)

# llm3_time is the time it took to run the third prompt
llm3_time = time.time()

print(f"LLM3: \"{result3}\"")


# TTS: generate audio from the last result
output = tts.convert(result3)


end_time = time.time()


print(f"\nREPORT:")
print(f"    STT: {((stt_time - start_time) * 1000.0):.2f}ms")
print(f"    LLM1: {((llm1_time - stt_time) * 1000.0):.2f}ms")
print(f"    LLM2: {((llm2_time - llm1_time) * 1000.0):.2f}ms")
print(f"    LLM3: {((llm3_time - llm2_time) * 1000.0):.2f}ms")
print(f"    LLM1+LLM2+LLM3: {((llm3_time - llm1_time) * 1000.0):.2f}ms")
print(f"    TTS: {((end_time - llm3_time) * 1000.0):.2f}ms")
print(f"    Total: {(end_time - start_time) * 1000.0:.2f}ms")
