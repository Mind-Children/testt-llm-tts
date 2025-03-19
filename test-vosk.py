#!/usr/bin/env python3

import queue
import sys
import sounddevice as sd

from vosk import Model, KaldiRecognizer

q = queue.Queue()

def callback(indata,frames,time,status):
    if status:
        print(status,file=sys.stderr)
    q.put(bytes(indata))

try:
    device_info = sd.query_devices(kind="input")
    samplerate = int(device_info["default_samplerate"])
    model = Model(lang="en-us")
    rec = KaldiRecognizer(model,samplerate)
    with sd.RawInputStream(samplerate=samplerate,blocksize=8000,device=sd.default.device,dtype="int16",channels=1,callback=callback):
        print("press Ctrl+C to stop recording")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.Result())
            else:
                print(rec.PartialResult())

except KeyboardInterrupt:
    print("done")
    exit(0)

except Exception as e:
    print("exception: ",e)
    exit(-1)
