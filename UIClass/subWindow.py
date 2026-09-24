from tkinter import *
class SubWindow():
    def __init__(self, root):
        self.windowOpened = False
        self.subWindow = None
        self.root = root
        self.components = {}
        # self.openWindow()

    def openWindow(self):
        if self.windowOpened == False:
            self.openWindowHelper()
            self.windowOpened = True

    def openWindowHelper(self):
            self.subWindow = Toplevel(self.root)
            self.subWindow.protocol("WM_DELETE_WINDOW", self.setOpenWindowFalse)
    def setOpenWindowFalse(self):
        self.windowOpened = False
        self.subWindow.destroy()