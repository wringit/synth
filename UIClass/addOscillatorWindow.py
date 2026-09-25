from tkinter import *
from tkinter import ttk
from UIClass import subWindow
#import ui
from oscillators import oscillatorsDict

options = oscillatorsDict.keys()

class AddOscillatorSubWindow(subWindow.SubWindow):
    def __init__(self, root, command):
        super().__init__(root)
        self.command = command

    def openWindowHelper(self):
        super().openWindowHelper()
        window = self.subWindow
        self.components["typeText"] = Label(window, text="Type: ")
        self.components["typeCombo"] = ttk.Combobox(window, values=list(options))

        self.components["nameText"] = Label(window, text="Name: ")
        self.components["nameInput"] = Entry(window, width=30)

        self.components["createButton"] = Button(window, text="Create", command=lambda: self.command(self))

        self.components["typeText"].pack()
        self.components["typeCombo"].pack()
        self.components["nameText"].pack()
        self.components["nameInput"].pack()
        self.components["createButton"].pack()

        window.resizable(False, False)  