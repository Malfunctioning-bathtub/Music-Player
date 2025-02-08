# import required modules
import tkinter as tk
import time as tm
from pygame.mixer import *

init()

root = tk.Tk()

music.load("piddling-simple-drums-full-house_126bpm.wav")

def onMainButtonPressed():
    if music.get_busy():
        music.pause()
    else:
        music.unpause()
        if not music.get_busy():
            music.play()




playButton = tk.Button(root, text='Play', width=25, command=onMainButtonPressed)
playButton.pack()


root.mainloop()