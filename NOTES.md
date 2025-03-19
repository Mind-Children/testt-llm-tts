# NOTES

## STT - Whisper

It's not natively a streaming ASR solution, so we will hack it:

thread 1:
    add audio chunks with now() and order number to big buffer

thread 2:
    loop:
        copy what's currently in the audio buffer
        remove silence from start and end
        if anything remains:
            Whisper inference on entire buffer, note the most recent timestamp and order number
            compare the output text to the previous output text
                the first characters are the same = certain text
                the characters that are different and extra = uncertain text
                compare the certain text to the previous certain text and output the new words with the timestamp
                if the certain text contains '.' remove all audio chunks before that from the audio buffer
                if the audio buffer becomes too big, remove the oldest chunks

thread 3:
    receive incoming words with timestamps
