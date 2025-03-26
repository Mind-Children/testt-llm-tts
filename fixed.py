import sys
import time
from faster_whisper import WhisperModel
from styletts2.tts import StyleTTS2
from ollama import chat,generate
import numpy as np
import scipy.io.wavfile as wavfile

# ===load STT model ===

stt = WhisperModel("small.en", download_root="./models", device="cuda",compute_type="float16")


# === load LLM model ===

#LLM_MODEL = 'gemma3:1b'
#LLM_MODEL = 'deepseek-r1:7b' # no, we don't want the thinking explanations
#LLM_MODEL = 'deepseek-r1:1.5b'
#LLM_MODEL = 'qwen2.5:0.5b'
#LLM_MODEL = 'qwen2.5:1.5b'
LLM_MODEL = 'qwen2.5:3b'
#LLM_MODEL = 'gemma2:2b'
#LLM_MODEL = 'gemma2:9b'
#LLM_MODEL = 'tinyllama:1.1b'

def complete(prompt,system_prompt):
    response = chat(LLM_MODEL,messages=[{'role':'system','content':system_prompt},{'role':'user','content':prompt}])
    return response['message']['content']

# preload to avoid measuring the LLM loading time
complete("how is the weather?","You are a weather reporter.")


# === load TTS model ===

TTS_VOICE = "ben"
#TTS_VOICE = "scarlett"
#TTS_VOICE = "silverhand"
tts = StyleTTS2()


# === START MEASURING ===

start_time = time.time()

# STT: transcribe fixed audio sample
segments,_ = stt.transcribe("fixed_input.wav")
text = ""
for segment in segments:
    text += segment.text
text = text.strip()

print(f"STT: \"{text}\"")

# stt_time is the time it took to transcribe
stt_time = time.time()


# LLM: run the first prompt
PROMPT = "You are a government official helping a citizen with their problem. Answer in one or two paragraphs."
result1 = complete(text,PROMPT)

# llm1_time is the time it took to run the first prompt
llm1_time = time.time()

print(f"LLM1: \"{result1}\"")


# LLM: run the second prompt
PROMPT = "You are a famous painter. Say the exact opposite of the user message."
result2 = complete(result1,PROMPT)

# llm2_time is the time it took to run the second prompt
llm2_time = time.time()

print(f"LLM2: \"{result2}\"")


# LLM: run the third prompt
PROMPT = "Summarize in one or two very sarcastic sentences."
result3 = complete(result2,PROMPT)

# llm3_time is the time it took to run the third prompt
llm3_time = time.time()

print(f"LLM3: \"{result3}\"")


# TTS: generate audio from the last result
output = tts.inference(result3,f"voices/{TTS_VOICE}.wav")

# === END MEASURING ===

end_time = time.time()

# save the output to a file
wavfile.write("output.wav",24000,output)


# === PRINT REPORT ===

print(f"\nREPORT:")
print(f"    STT: {((stt_time - start_time) * 1000.0):.2f}ms")
print(f"    LLM1: {((llm1_time - stt_time) * 1000.0):.2f}ms")
print(f"    LLM2: {((llm2_time - llm1_time) * 1000.0):.2f}ms")
print(f"    LLM3: {((llm3_time - llm2_time) * 1000.0):.2f}ms")
print(f"    TTS: {((end_time - llm3_time) * 1000.0):.2f}ms")
print(f"    Total: {(end_time - start_time) * 1000.0:.2f}ms")
