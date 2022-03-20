import requests, json
from decouple import config
import librosa
import soundfile as sf

def open_wav_with_resample(file_name, new_rate):
    data, rate = sf.read(file_name)
    data = data.T
    data = librosa.resample(data, rate, new_rate)
    return data, new_rate
    
SECRET_KEY = config('SECRET_KEY')

url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
headers = {
    'Host': 'kakaoi-newtone-openapi.kakao.com',
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": f"KakaoAK {SECRET_KEY}",
}

"""
# 카카오는 16000 HZ 샘플링을 사용하기 때문에 resampling이 필요하다.
# 기존의 44100 HZ 샘플링을 그대로 사용할 경우 제대로 STT를 수행하지 못한다.
data, new_rate= open_wav_with_resample("./demo/M_000001.wav", 16000)
sf.write('./new_file.wav', data, new_rate)
"""

# data = open("./demo/Emotional_conversation/Male/M_000001.wav", "rb").read()
data = open("./demo/M_000001.wav", "rb").read()

res = requests.post(url, headers=headers, data=data)
print(res.text)


