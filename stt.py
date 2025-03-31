import sys
import time
import sounddevice as sd
import numpy as np
import threading

# various options for STT
WHISPER = 0

# choose STT here
STT_TYPE = WHISPER

if STT_TYPE == WHISPER:

    from faster_whisper import WhisperModel
    SAMPLE_RATE = 48000
    SILENCE_THRESHOLD = 0.1
    DEVICE = "cpu"
    COMPUTE_TYPE = "int8"


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

class STT:

    def __init__(self,streaming=False):

        if STT_TYPE == WHISPER:

            self.model = WhisperModel("small.en", download_root="./models", device=DEVICE,compute_type=COMPUTE_TYPE)

        self.previous_text = ""
        self.last_timestamp = 0
        self.index = 0
        self.audio_queue = []
        self.utterance_queue = []

        if streaming:
            self.thread = threading.Thread(target=self.streaming_thread).start()

    if STT_TYPE == WHISPER:

        def read_audio(self,indata,frames,_time,status):

            if status:
                print(status,file=sys.stderr)

            buffer = np.frombuffer(indata,dtype=np.int16).flatten()
            resampled = np.interp(np.arange(0,len(buffer),SAMPLE_RATE / 16000),np.arange(0,len(buffer)),buffer)
            self.audio_queue.append((time.time(),resampled.astype(np.float32) / 32768.0))

    def convert(self,buffer):

        if STT_TYPE == WHISPER:

            segments,_ = self.model.transcribe(buffer)

            text = ""
            for segment in segments:
                text += segment.text

        return text

    def streaming_thread(self):

        with sd.RawInputStream(samplerate=48000,blocksize=8000,dtype="int16",channels=1,callback=self.read_audio):
            while True:

                while len(self.audio_queue) > 0:

                    max = np.max(np.abs(self.audio_queue[0][1]))
                    if max < SILENCE_THRESHOLD:
                        self.audio_queue.pop(0)
                    else:
                        break

                if len(self.audio_queue) > 0:

                    timestamp = self.audio_queue[-1][0]

                    if timestamp > self.last_timestamp:

                        self.last_timestamp = timestamp
                        buffer = np.empty(shape=[0],dtype=np.float32)
                        for i in range(len(self.audio_queue)):
                            buffer = np.concatenate((buffer,self.audio_queue[i][1]))

                        if STT_TYPE == WHISPER:

                            segments,_ = self.model.transcribe(buffer)

                            text = ""
                            for segment in segments:
                                text += segment.text
                            text = text.strip()

                        if text != "":

                            if text == self.previous_text:

                                terminator_index = find_terminator(text)

                                if terminator_index != -1:

                                    print(f"STT: --> \"{text}\"")
                                    self.utterance_queue.append(text)
                                    self.audio_queue.clear()
                                    self.previous_text = ""

                                else:

                                    self.previous_text = text

                            else:

                                non_matching_index = -1
                                for i in range(min(len(text),len(self.previous_text))):
                                    if text[i] != self.previous_text[i]:
                                        non_matching_index = i
                                        break

                                stable_part = self.previous_text[:non_matching_index].strip()
                                terminator_index = find_terminator(stable_part)
                                if terminator_index != -1:
                                    print(f"STT:   ({stable_part}) - terminated")
                                else:
                                    print(f"STT:   ({stable_part})")

                                self.previous_text = text

                        self.index += 1

                    else:

                        time.sleep(0.1)

                else:

                    time.sleep(0.1)

    def is_empty(self):

        return len(self.utterance_queue) == 0

    def get_utterance(self):

        return self.utterance_queue.pop(0)
