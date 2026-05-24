from tkinter import *
from tkinter.filedialog import askopenfilename
# import song
# import voices
# import oscillators
# # USE PYGAME FOR IN-SESSION AUDIO
root = Tk(screenName="Tinjug's Music Thing", baseName=None, className="Tk",useTk=1)
root.title("Tinjug's Music Thing")

def projectWindow(song=None, name="Untitled"):
    # sub = Toplevel(root)
    # sub.title(name)
    root.geometry("900x600")
    propertiesPane = songProperties(root)
    propertiesPane.grid(column=0,row=0)

def noteColumn(window):
    column = Frame(window)
    buttons = []
    for i in range(12):
        button = Button(column)
        buttons += [button]

def songProperties(window, name="Untitled"):
    propertiesPane = Frame(window)
    titleFrame = Frame(propertiesPane)
    titleLabel = Label(titleFrame,text="Name: " + name)
    renameButton = Button(titleFrame, text="Rename")
    titleLabel.grid(row=0,column=0)
    renameButton.grid(row=0,column=1)
    voicesLabel = Label(propertiesPane, text="Voices: ")
    voiceListbox = Listbox(propertiesPane)
    addVoiceButton = Button(propertiesPane, text="Add voice")
    titleFrame.pack()
    voicesLabel.pack()
    voiceListbox.pack()
    addVoiceButton.pack()
    return propertiesPane


def voiceProperties(window):
    propertiesPane = Frame(window)
    
    volumeLabel = Label(propertiesPane, text="Volume:")
    volumeScale = Scale(propertiesPane, from_=0, to_=10, orient="vertical")

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


