import sys
import time
from stt import STT
from llm import LLM
from tts import TTS

stt = STT()
llm = LLM()
tts = TTS()


start_time = time.time()


FIXED_INPUT_NAME = "fixed_input.wav"
FIXED_INPUT_MS = 2300

# STT: transcribe fixed audio sample
text = stt.convert(FIXED_INPUT_NAME)

# stt_time is the time it took to transcribe
stt_time = time.time()

print(f"STT: \"{text}\"")


# LLM: run the first prompt
PROMPT = "You are a government official helping a citizen with their problem. Summarize your answer in one sentence."
result1 = llm.complete(text,PROMPT)

# llm1_time is the time it took to run the first prompt
llm1_time = time.time()

print(f"LLM1: \"{result1}\"")


# LLM: run the second prompt
PROMPT = "You are a famous painter trying to be different. Say the exact opposite in one sentence."
result2 = llm.complete(result1,PROMPT)

# llm2_time is the time it took to run the second prompt
llm2_time = time.time()

print(f"LLM2: \"{result2}\"")


# LLM: run the third prompt
PROMPT = "Summarize in one very opinionated and sarcastic sentence."
result3 = llm.complete(result2,PROMPT)

# llm3_time is the time it took to run the third prompt
llm3_time = time.time()

print(f"LLM3: \"{result3}\"")


# TTS: generate audio from the last result
output = tts.convert(result3)


end_time = time.time()


print(f"\nREPORT:")
print(f"    STT ms: {((stt_time - start_time) * 1000.0):.2f}ms")
print(f"    STT ms/ms: {((stt_time - start_time) * 1000.0 / FIXED_INPUT_MS):.2f}")
print(f"    STT ms/char: {((stt_time - start_time) * 1000.0 / len(text)):.2f}")
print(f"    LLM1 ms: {((llm1_time - stt_time) * 1000.0):.2f}ms")
print(f"    LLM1 ms/char: {((llm1_time - stt_time) * 1000.0 / len(result1)):.2f}")
print(f"    LLM2 ms: {((llm2_time - llm1_time) * 1000.0):.2f}ms")
print(f"    LLM2 ms/char: {((llm2_time - llm1_time) * 1000.0 / len(result2)):.2f}")
print(f"    LLM3 ms: {((llm3_time - llm2_time) * 1000.0):.2f}ms")
print(f"    LLM3 ms/char: {((llm3_time - llm2_time) * 1000.0 / len(result3)):.2f}")
print(f"    LLM1+LLM2+LLM3 ms: {((llm3_time - stt_time) * 1000.0):.2f}ms")
print(f"    LLM1+LLM2+LLM3 ms/char: {((llm3_time - stt_time) * 1000.0 / (len(result1) + len(result2) + len(result3))):.2f}")
print(f"    TTS ms: {((end_time - llm3_time) * 1000.0):.2f}ms")
print(f"    TTS ms/char: {((end_time - llm3_time) * 1000.0 / len(result3)):.2f}")
print(f"    Total ms: {(end_time - start_time) * 1000.0:.2f}ms")
