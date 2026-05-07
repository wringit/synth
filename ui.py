from tkinter import *
from tkinter.filedialog import askopenfilename
import song
import voices
import oscillators

root = Tk(screenName="Tinjug's Music Thing", baseName=None, className="Tk",useTk=1)

def projectWindow(song, name="Untitled"):
    sub = Toplevel(root)
    sub.title(name)
    sub.geometry()


barMenu = Menu(root)
root.config(menu=barMenu)

file = ""

def readSong(path):
    voices = []
    with open(path, "r") as f:
        lines = f.readlines()
        oscillator = oscillators[lines[0]]
        del lines[0]
        for line in lines:
            voiceArray = line.split()
            voices = voices + voiceArray
            
    song = Song()

def getFile():
    file=askopenfilename()
    print(file)

# Menu
fileMenu = Menu(root)
barMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open...", command=getFile)


root.mainloop()


