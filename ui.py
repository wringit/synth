from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk(screenName="Tinjug's Music Thing", baseName=None, className="Tk",useTk=1)

def projectWindow(song, name="Untitled"):
    sub = Toplevel(root)
    sub.title(name)
    sub.geometry()


barMenu = Menu(root)
root.config(menu=barMenu)

file = ""

def readSong(path):
    pass

def getFile():
    file=askopenfilename()
    print(file)

# Menu
fileMenu = Menu(root)
barMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open...", command=getFile)


root.mainloop()


