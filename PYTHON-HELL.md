# HOW TO FIX ALL THE PYTHON ISSUES YOU MIGHT ENCOUNTER

`pip` and what they call 'packages' is one giant flaming mountain of lazy-ass crap...

Depending on the target platform (hardware, Jetpack version, Linux version, etc.) you might need to play around with different versions of python to get the right mix that works. For the Jetson Orin, I managed to make it work with Ubuntu 22.04, python 3.10, Jetpack 6.1, CUDA 12.6

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

## `_pickle.UnpicklingError: Weights only load failed. This file can still be loaded, to do so you have two options, do those steps only if you trust the source of the checkpoint.`

This requires some hacking in the package that gives the error. The actual error does not occur in torch, but in calling `torch.load`, because they updated a parameter. For instance, if the package is StyleTTS, edit the file `venv/lib/python3.11/site-packages/styletts2/models.py`. Edit all occurrances of `torch.load` and att the parameter `weights_only=False` to the function call.

