import os
import speech_recognition as sr
import pickle
from tqdm import tqdm


# recognize_google() : Google Web Speech API -> 사용!!
# recognize_google_cloud() : Google Cloud Speech API
# recognize_bing() : Microsoft Bing Speech API
# recognize_houndify() : SoundHound Houndify API
# recognize_ibm() : IBM Speech to Text API
# recognize_wit() : Wit.ai API
# recognize_sphinx() : CMU Sphinx (오프라인에서 동작 가능)

"""
r = sr.Recognizer()
save_dict = {}

dataset_path = "./demo/Emotional_conversation/Female"
datasets = os.listdir(dataset_path)
for wav in tqdm(datasets):
    wav_path = os.path.join(dataset_path, wav)
    korean_audio = sr.AudioFile(wav_path)

    with korean_audio as source:
        audio = r.record(source)
    text = r.recognize_google(audio_data=audio, language='ko-KR')
    save_dict[wav] = text

with open('./Female_text.pickle', 'wb') as f:
    pickle.dump(save_dict, f, pickle.HIGHEST_PROTOCOL)
"""

r = sr.Recognizer()

korean_audio = sr.AudioFile('./demo/M_000001.wav.wav')

with korean_audio as source:
    audio = r.record(source)
print(r.recognize_google(audio_data=audio, language='ko-KR'))