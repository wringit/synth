from tkinter import *
from tkinter.filedialog import askopenfilename
# import song
# import voices
# import oscillators

root = Tk(screenName="Tinjug's Music Thing", baseName=None, className="Tk",useTk=1)

def projectWindow(song=None, name="Untitled"):
    sub = Toplevel(root)
    sub.title(name)
    sub.geometry("900x600")


def noteColumn(window):
    column = Frame(window)
    buttons = []
    for i in range(12):
        button = Button(window)
        buttons += [button]

def songProperties(window):
    propertiesPane = Frame(window)
    titleLabel = Label(propertiesPane)
    editButton = Button(propertiesPane, text="Rename")
    

def voiceProperties(window):
    propertiesPane = Frame(window)
    volumeScale = Scale(propertiesPane, from_=0, to_=10, orient="vertical")
    pass

barMenu = Menu(root)
root.config(menu=barMenu)

file = ""

# def readSong(path):
#     voices = []
#     with open(path, "r") as f:
#         lines = f.readlines()
#         oscillator = oscillators[lines[0]]
#         del lines[0]
#         for line in lines:
#             voiceArray = line.split()
#             voices = voices + voiceArray
            
#     song = Song()

def getFile():
    file=askopenfilename()
    print(file)

# Menu
fileMenu = Menu(root)
barMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open...", command=getFile)
projectWindow()

root.mainloop()


