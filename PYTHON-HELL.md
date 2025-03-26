# HOW TO FIX ALL THE PYTHON ISSUES YOU MIGHT ENCOUNTER

`pip` and what they call 'packages' is one giant flaming mountain of lazy-ass crap...

To speed up your experience without having to put any faith into docker containers, here are some tips:

## Python version

I got the least amount of problems with `python3.11` on `venv`. 3.10 and 3.12 also work, although you might experience different issues. So start the journey with:

```
python3.11 -m venv venv
source venv/bin/activate
```

## `Unable to load any of {libcudnn_cnn.so.9.1.0, libcudnn_cnn.so.9.1, libcudnn_cnn.so.9, libcudnn_cnn.so}`

Someone compiled ctranslate2 with the wrong CUDA version. Install exactly version 4.4.0, and this should disappear:

```
pip install ctranslate2-4.4.0
```

## `ollama._types.ResponseError: model "<model>" not found, try pulling it first (status code: 404)`

Manually pull the model.

```
ollama pull <model>
```

## Torch

Make sure you have version <=2.5.1. Newer versions have breaking changes with the TTS/STT solutions tried.

