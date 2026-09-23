from tkinter import *
from tkinter import ttk
from UIClass import subWindow
from oscillators import oscillatorsDict

options = oscillatorsDict.keys()

class AddOscillatorSubWindow(subWindow.SubWindow):
    def __init__(self, root):
        super().__init__(root)


    def openWindowHelper(self):
        super().openWindowHelper()
        window = self.subWindow
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