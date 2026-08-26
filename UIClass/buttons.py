from tkinter import *
from ..notes import NOTE_NAMES_LIST


class ButtonsColumn:
    def __init__(self, window, octave=0):
        self.buttons=[]
        self.window = window
        self.octave = 0
        self.column = Frame(window)

        self.notesDict = {note: False for note in NOTE_NAMES_LIST}
        for i in range(12):
            button = Button(self.column, command=lambda: self.toggle_note(NOTE_NAMES_LIST[i]))
            buttons += [button]
            button.pack()

    def toggle_note(self, note): 
        self.notesDict[note] = not self.notesDict[note]
        