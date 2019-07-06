from libs.view.tkinter import Interface
from tkinter import *
from libs.controller.session import Session


class App:
    def __init__(self):
        self.go = False
        self.session = Session()

    def start_app(self):
        self.go = True
        self.init_tkinter()

    def init_tkinter(self):
        """init window tkinter"""
        window = Tk()
        interface = Interface(window)
        interface.mainloop()
        interface.destroy()

    def stop_app(self):
        self.go = False


if __name__ == "__main__":
    Application = App()
    Application.start_app()