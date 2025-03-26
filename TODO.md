- explore RKNN toolkit/SDK to see what the path looks like to convert ONNX models to RKNN, and find STT and TTS models in their zoo

+ pull a few more models from ollama

- find few more alternatives for TTS: coqui, piper, fish, sovits

+ design the 3 LLM prompts

+ build final measuring structure with selectable STT and TTS solutions:

    - time from STT start of sample that results in the posted utterance (end of user audio) to TTS end where the output audio is available (start of agent audio)

    - time for STT from start of sample that results in the posted utterance to the utterance being posted

    - time for each LLM step

    - time of all 3 LLM steps together

    - time for TTS from sending the utterance to when output audio is available

    - memory usage

    - CPU usage

    - "how responsive it feels"

- measure on: desktop, big laptop, small laptop, Pi5, RK1, Orin Nano, Orin NX16
