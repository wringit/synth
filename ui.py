

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from UIClass import buttons
from oscillators import oscillatorsDict
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
    root.resizable(False,False)
    songPropertiesPane = songProperties(root)
    voicePropertiesPane = voiceProperties(root)
    songPropertiesPane.grid(column=0,row=0, sticky="n")
    voicePropertiesPane.grid(column=0,row=1, sticky="n")
    # Have number of 
    #buttons.ButtonsColumn(root)
    renderEditor(1,1,2)

def addOscillatorWindow():
    # TODO: Add padding, grid layout for components, create functionality
    window = Toplevel(root)
    options = oscillatorsDict.keys()

    typeText = Label(window, text="Type: ")
    typeCombo = ttk.Combobox(window, values=options)

    nameText = Label(window, text="Name: ")
    nameInput = Entry(window, width=30)

    createButton = Button(window, text="Create")

    typeText.pack()
    typeCombo.pack()
    nameText.pack()
    nameInput.pack()
    createButton.pack()

    window.resizable(False, False)

    return window

def renderEditor(rowsAbove=0, rowsBelow = 0, columns=1):
    # e
    editor = Frame(root)
    editor.grid(column=1,row=0)
    # buttons.ButtonsColumn(editor)
    for i in range(columns):
        for j in range(rowsAbove):
            octave = buttons.ButtonsColumn(editor, rowsAbove - j, j, i) 
        middleOctave = buttons.ButtonsColumn(editor, 0, rowsAbove, i)
        for j in range(rowsBelow):
            octave = buttons.ButtonsColumn(editor, 0 - j, rowsAbove + rowsBelow + j, i)
    #editor.pack()



def songProperties(window, name="Untitled"):
    # TODO: "add voice" button functionality (open window)

    propertiesPane = Frame(window)
    titleFrame = Frame(propertiesPane)
    titleLabel = Label(titleFrame,text="Name: " + name)
    renameButton = Button(titleFrame, text="Rename")
    titleLabel.grid(row=0,column=0)
    renameButton.grid(row=0,column=1)
    voicesLabel = Label(propertiesPane, text="Voices: ")
    voiceListbox = Listbox(propertiesPane)
    addVoiceButton = Button(propertiesPane, text="Add voice", command=addOscillatorWindow)
    titleFrame.pack()
    voicesLabel.pack()
    voiceListbox.pack()
    addVoiceButton.pack()
    
    return propertiesPane


def voiceProperties(window):
    propertiesPane = Frame(window)

    volumeLabel = Label(propertiesPane, text="Volume:")
    volumeScale = Scale(propertiesPane, from_=0, to_=10, orient="vertical")

    oscillatorFrame = Frame(propertiesPane)
    oscillatorLabel = Label(oscillatorFrame, text="Oscillator:")
    oscillatorVar = StringVar(oscillatorFrame)
    oscillatorVar.set("(none)")
    oscillatorDropdown = OptionMenu(oscillatorFrame, oscillatorVar, "(none)")
    changeOscillatorButton = Button(oscillatorFrame, text="Change oscillator")

    volumeLabel.pack(side=TOP, pady=4)
    volumeScale.pack(side=TOP, pady=4)
    oscillatorLabel.pack(side=LEFT)
    oscillatorDropdown.pack(side=LEFT, padx=6)
    changeOscillatorButton.pack(side=LEFT, padx=6)
    oscillatorFrame.pack(fill=X, pady=8)

    return propertiesPane

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


