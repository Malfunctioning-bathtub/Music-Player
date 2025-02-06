# import required modules
import tkinter as tk
import time as tm
from pygame.mixer import *

init()

root = tk.Tk()

music.load("Music-player/piddling-simple-drums-full-house_126bpm.wav")

def onPlayButtonPressed():
    music.play()

def onPauseButtonPressed():
    music.pause()



playButton = tk.Button(root, text='Play', width=25, command=onPlayButtonPressed)
playButton.pack()

pauseButton = tk.Button(root, text='Pause', width=25, command=onPauseButtonPressed)
pauseButton.pack()



root.mainloop()