# import required modules
from tkinter import *
import time as tm
from pydub import *
from pydub.playback import _play_with_simpleaudio

song = AudioSegment.from_file("Music-player/piddling-simple-drums-full-house_126bpm.wav")
song = song.set_sample_width(2)

playback = _play_with_simpleaudio(song)

# end playback after 3 seconds
tm.sleep(3)
playback.stop()