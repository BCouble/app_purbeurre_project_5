# ! /usr/bin/env python3
# coding: utf-8
"""
Project 5
App Pur beurre
"""
from libs.ctrl import ManagementData
from libs.interaction import Interaction
from libs.select_data import SelectData


class App:
    def __init__(self):
        self.go = False
        self.db = SelectData()
        self.choice = Interaction()
        self.select_data = SelectData()
        self.ctrl = ManagementData()

    def start_app(self):
        self.go = True
        self.loop_app()

    def loop_app(self):
        while self.go:
            self.choice.choice_bdd()
            if self.choice.choice_menu == 0:
                self.ctrl.category_dysplay()
                num = self.choice.choice_number()
                if num == 11:
                    print("quit")
                else:
                    print(num)
            else:
                if self.choice.choice_menu == 1:
                    print("test 1")

    def stop_app(self):
        self.go = False


if __name__ == "__main__":
    Application = App()
    Application.start_app()
