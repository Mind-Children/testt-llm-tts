import sys
import time
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

SAMPLE_RATE = 48000
SILENCE_THRESHOLD = 0.1

audio_queue = []

previous_text = ""

last_timestamp = 0
index = 0

def read_audio(indata,frames,_time,status):
    if status:
        print(status,file=sys.stderr)
    buffer = np.frombuffer(indata,dtype=np.int16).flatten()
    resampled = np.interp(np.arange(0,len(buffer),SAMPLE_RATE / 16000),np.arange(0,len(buffer)),buffer)
    audio_queue.append((time.time(),resampled.astype(np.float32) / 32768.0))

def find_terminator(text):
    # find terminator ('.', '!' or '?' but not '...')
    period = text.find(".")
    ellipsis = text.find("...")
    if period != -1 and ellipsis == -1:
        return period
    question = text.find("?")
    if question != -1:
        return question
    exclam = text.find("!")
    if exclam != -1:
        return exclam
    return -1

try:
    device_info = sd.query_devices(kind="input")
    model = WhisperModel("small.en", download_root="./models", device="cuda",compute_type="float16")
    with sd.RawInputStream(samplerate=48000,blocksize=8000,device=0,dtype="int16",channels=1,callback=read_audio):
        print("press Ctrl+C to stop recording")
        while True:

            # drop initial chunks from audio_buffer that are too silent
            while len(audio_queue) > 0:
                max = np.max(np.abs(audio_queue[0][1]))
                if max < SILENCE_THRESHOLD:
                    audio_queue.pop(0)
                else:
                    break

            #print(f"queue length: {len(audio_queue)}")

            if len(audio_queue) > 0:

                timestamp = audio_queue[-1][0]

                #print(f"timestamp: {timestamp}")

                if timestamp > last_timestamp:

                    #print(f"timestamp: {timestamp} > {last_timestamp}")

                    last_timestamp = timestamp

                    # start with empty buffer
                    buffer = np.empty(shape=[0],dtype=np.float32)

                    # concatenate what's left
                    for i in range(len(audio_queue)):
                        buffer = np.concatenate((buffer,audio_queue[i][1]))

                    #write(f"test-{index}.wav",16000,buffer)

                    # transcribe
                    segments,info = model.transcribe(buffer)

                    # concatenate segments
                    text = ""
                    for segment in segments:
                        text += segment.text
                    text = text.strip()

                    if text != "":

                        #print(f"{index}: \"{text}\" (\"{previous_text}\")")

                        # identical, so this is probably the output
                        if text == previous_text:
                            terminator_index = find_terminator(text)
                            if terminator_index != -1:
                                # identical and terminated, this is the output
                                print(f"--> \"{text}\"")
                                #for i in range(len(audio_queue) - 1):
                                #    audio_queue.pop(0)
                                audio_queue.clear()
                                previous_text = ""

                            else:

                                previous_text = text

                        # not identical, show the stable part
                        else:
                            non_matching_index = -1
                            for i in range(len(previous_text)):
                                if text[i] != previous_text[i]:
                                    non_matching_index = i
                                    break
                            stable_part = previous_text[:non_matching_index].strip()
                            terminator_index = find_terminator(stable_part)
                            if terminator_index != -1:
                                print(f"  ({stable_part}) - terminated")
                            else:
                                print(f"  ({stable_part})")

                            previous_text = text

                    index += 1

                else:
                    time.sleep(0.1)

            else:
                time.sleep(0.1)


except KeyboardInterrupt:
    print("done")
    exit(0)

except Exception as e:
    print("exception: ",e)
    exit(-1)
