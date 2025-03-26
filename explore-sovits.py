from gpt_sovits import TTS, TTS_Config
import sounddevice as sd

sovits_configs = {"default": {"device": "cuda", "is_half": True,"t2s_weights_path":"models/s1bert25hz-2kh-longer-epoh=68e-step=50232.ckpt","vits_weights_path":"models/s2G488k.pth","cnhubert_base_path":"models/chinese-hubert-base","bert_base_path":"models/chinese-roberta-wmm-ext-large"}}
tts_config = TTS_Config(sovits_configs)
tts_pipeline = TTS(tts_config)
params = {"text": "Let me see what I can do... It really looks like you finally got the audio samples to play correctly! Way to go!","text_lang":"en","ref_audio_path":"voices/scarlett.wav"}
tts_generator = tts_pipeline.run(params)
sr,audio_data = next(tts_generator)

with sd.RawOutputStream(samplerate=48000,channels=1,dtype=np.int16):
    sd.play(audio_data,samplerate=48000)
    sd.wait()
