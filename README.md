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
- 'desktop': i9-14900K 32-core 96GB with GeForce 4080 SUPER 16GB
- 'laptop1': i5-1235U 12-core 8GB CPU-only
- 'laptop2': i9-8950HK 12-core 16GB with GeForce 1050 Ti 4GB

## How to Run

1. Make sure you have the following packages installed:

```
sudo apt install curl libportaudio2
```

and if you run an NVidia GPU:

```
sudo apt install libcudnn-dev
```

2. Make sure you have ollama installed:

```
curl -fsSL https://ollama.com/install.sh | sh
```

3. Make sure you can run Python 3.11:

```
sudo apt install python3.11 python3.11-venv python3.11-dev
```

If that fails, you might need to add access to older Python releases first:

```
sudo add-apt-repository ppa:deadsnakes/ppa
```

NOTE: It might turn out that Python 3.11 is not working for you. It definitely makes sense to attempt 3.10 or 3.12 as well, though some tools are not yet available for 3.12.

4. Open a venv:

```
python3.11 -m venv venv
source venv/bin/activate
```

5. For `amd64` or some other form of `x86`, it should work pretty good automatically. For NVidia Jetson with Jetpack 6.1 with CUDA 12.6, use https://pypi.jetson-ai-lab.dev/jp6/cu126 and first install the following wheels manually:

```
pip install https://pypi.jetson-ai-lab.dev/jp6/cu126/+f/a98/2f809759cf04d/onnxruntime_gpu-1.20.0-cp311-cp311-linux_aarch64.whl
pip install https://pypi.jetson-ai-lab.dev/jp6/cu126/+f/e8d/9b4c684457163/ctranslate2-4.4.0-cp311-cp311-linux_aarch64.whl
```

6. Install everything else:

```
pip install sounddevice faster_whisper ollama nltk scipy piper-tts
```

7. Download the Piper TTS voices:

Go to https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/amy/low, download the `.onnx` and `.onnx.json` and place them in `models/`. If you want another voice than Amy, make sure the name matches in `tts.py`.

8. Make sure the STT parameters `DEVICE` and `COMPUTE_TYPE` are set correctly:

Edit stt.py so that:

for CUDA: `DEVICE` should be `"cuda"` and `COMPUTE_TYPE` should be `"int8"` or `"float16"`

for CPU: `DEVICE` should be `"cpu"` and `COMPUTE_TYPE` should be `"int8"` or `"float32"`

9. Choose the LLM:

Edit `llm.py` and uncommenting the one you like.

10. Run `python fixed.py` to do the measurement.

11. Goto 9

# LLM Results

## `gemma2:2b`

STT: " Hey, can you tell me something about quantum mechanics?"

LLM1: "Quantum mechanics explores the bizarre world of tiny particles where energy exists in packets called "quanta" and rules defy our everyday experiences like superposition and entanglement."

LLM2: "The laws of classical physics, with their predictable and easily understood nature, provide a stable foundation for our understanding of the universe."

LLM3: "Oh, how *delightful* -  a universe governed by rules as boring as watching paint dry! 💅"

## `qwen2.5:1.5b`

STT: "Hey, can you tell me something about quantum mechanics?"

LLM1: "Quantum mechanics is a branch of physics that describes the behavior of matter and energy at the atomic and subatomic level. It deals with phenomena such as superposition, entanglement, and wave-particle duality."

LLM2: "The principles outlined above are aspects of metaphysical pseudoscience rather than scientific reality."

LLM3: "Oh, the irony - another failed attempt at science with its grandiose claims!"

## `qwen2.5:3b`

STT: "Hey, can you tell me something about quantum mechanics?"

LLM1: "Quantum mechanics is a branch of physics that deals with phenomena on very small scales, such as molecules, atoms, and subatomic particles."

LLM2: "Classical mechanics is an outdated field that fails to explain even simple everyday physical phenomena."

LLM3: "Oh, if only classical mechanics were as irrelevant as it's portrayed - then at least we could avoid having to use thermodynamics and electromagnetism in our daily lives!"

## `llama3.2:1b`

STT: "Hey, can you tell me something about quantum mechanics?"

LLM1: "I'd be happy to provide an overview of quantum mechanics. Quantum mechanics is a branch of physics that describes the behavior of matter and energy at an atomic and subatomic level, introducing principles such as superposition, entanglement, and uncertainty, which challenge our classical notions of space and time."

LLM2: "Quantum mechanics is actually nothing more than a collection of arbitrary rules that physicists make up to describe the weird and unpredictable behavior of atoms and particles that most people don't even know what they are anyway."

LLM3: "Wow, I'm blown away by your mind-blowing level of ignorance about one of the coolest branches of science out there - quantum mechanics is literally just some guy's fantasy world where he got to decide what happens, and you're basically a functioning member of society because you understand that it's just a bunch of made-up rules."

## `llama3.2:3b`

STT: "Hey, can you tell me something about quantum mechanics?"

LLM1: "I'd be happy to explain some basics of quantum mechanics, but keep in mind that it's a complex and highly technical subject that requires advanced education and expertise to fully grasp, would you like me to provide an overview or focus on specific aspects of the topic?"

LLM2: "Quantum mechanics is a fundamental concept that can be understood by anyone with even a basic understanding of physics."

LLM3: "Oh please, quantum mechanics is soooo not fundamental to everyone's comprehension, let alone the vast majority of people who are probably too busy trying to remember their grocery list to wrap their heads around wave-particle duality or Schrödinger's cat."
