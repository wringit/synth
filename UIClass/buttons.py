from tkinter import *

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from notes import NOTE_NAMES_LIST



class ButtonsColumn:
    def __init__(self, window, octave=0):
        self.buttons=[]
        self.window = window
        self.octave = 0
        self.column = Frame(window)

        self.notesDict = {note: False for note in NOTE_NAMES_LIST}
        for i in range(1, len(NOTE_NAMES_LIST)):
            button = Button(self.column)
            button.config(command=lambda note=NOTE_NAMES_LIST[i], button=button: self.toggle_note(note, button))
            print(NOTE_NAMES_LIST[i])
            self.buttons += [button]
            button.pack()

    def toggle_note(self, note, button): 
        self.notesDict[note] = not self.notesDict[note]
        print(f"{note} is now {self.notesDict[note]}")
        button.config(bg="red" if self.notesDict[note] else "SystemButtonFace")