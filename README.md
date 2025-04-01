# `testt-llm-tts`

Large test to see if local STT-LLM-TTS is feasible and how fast it is.

This repo explores and tests some pre-made solutions for STT, LLM and TTS that we might consider for the robot to run locally. A few requirements:

- We want to know _if_ this runs on SBCs and if it does, _how long it takes_.

- We also want to know how much memory all this requires.

- Measuring the running time should be between the moment an audio sample from the microphone is ready to be transcribed by the STT, and the moment an audio sample from the TTS is ready to be played over the speakers.

- Use a fixed pre-recorded audio input on all platforms.

- To simulate more excessive LLM shenanigans, the text should go through the LLM three times with different prompts.

- Play around with different LLMs to see which one is favorable for the robot (by expert opinion).

## Target Platforms

- 'pi5': Raspberry Pi5, 8GB
- 'nano': NVidia Jetson Orin Nano 8GB (likely the same as the "SUPER" they sell now)
- 'nx16': NVidia Jetson Orin NX 16GB
- 'rk1': Turing RK-1 32GB (Rockchip RK3588 alternative to Raspberry Pi5)
- 'desktop': i9-14900K 96GB with GeForce 4080 SUPER
- 'laptop1':
- 'laptop2':

## How to Run

1. make sure you have the following Python 3.11 packages:

```
sudo apt install python3.11 python3.11-venv python3.11-dev
```

2. Open a venv:

```
python3.11 -m venv venv
source venv/bin/activate
```

3. For `amd64` or some other form of `x86`, it should work pretty good automatically. For NVidia Jetson, use https://pypi.jetson-ai-lab.dev/jp6/cu126 and first install the following wheels manually:

```
pip install https://pypi.jetson-ai-lab.dev/jp6/cu126/+f/a98/2f809759cf04d/onnxruntime_gpu-1.20.0-cp311-cp311-linux_aarch64.whl#sha256=a982f809759cf04d5876d34d5efcc502844de847415ee48095b97c1ae363019b
pip install https://pypi.jetson-ai-lab.dev/jp6/cu126/+f/e8d/9b4c684457163/ctranslate2-4.4.0-cp311-cp311-linux_aarch64.whl#sha256=e8d9b4c684457163d7efbc637aa0b385b520700b2f24ae27238dd9068bff1447
```

4. install everything else:

```
pip install sounddevice faster_whisper ollama nltk scipy piper-tts
```
