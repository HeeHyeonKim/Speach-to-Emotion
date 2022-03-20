from os import path
from pydub import AudioSegment
import moviepy.editor as mp

# files
# src = input("In: ")
# dst = input("Out: ")
src = "./demo/data.mp3"
dst = "./demo/data.wav"

# clip = mp.VideoFileClip(src)
# clip.audio.write_audiofile("./demo/data.mp3")

# convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")