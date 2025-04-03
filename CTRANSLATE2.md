# CUDA-support in CTranslate2

Ok, so Whisper won't work without proper CUDA support in CTranslate2, and there is no precompiled version for `arm64`.

To remedy this, we're going to compile it ourselves. First install the prerequisites:

```
sudo apt update
sudo apt install build-essential clang cmake libomp-dev
```

Clone the CTranslate2 repo:

```
git clone --recursive https://www.github.com/OpenNMT/CTranslate2.git
```

Create the makefiles:

```
cd CTranslate2
mkdir build
cd build
cmake .. -DWITH_CUDA=ON -DWITH_CUDNN=ON -DWITH_MKL=OFF
```

Make the binaries and install them:

```
make
sudo make install
```

Congratulations, you're now the proud owner of a newly minted CTranslate2.

Now build the Python wheel:

```
cd python
python3.10 -m venv venv
source venv/bin/activate
pip install -r install_requirements.txt
python setup.py bdist_wheel
deactivate
```

The file `dist/<name>.whl` is the new CTranslate2 Python wheel that you can now install in the project:

```
cd ~/testt-llm-tts
source venv/bin/activate
pip install ~/CTranslate/python/dist/*.whl --force-reinstall
```
