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
