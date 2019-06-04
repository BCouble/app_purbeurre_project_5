# ! /usr/bin/env python3
# coding: utf-8
"""
Project 5
App Pur beurre
"""
from libs.obj_management import ObjManagement
from libs.interaction import Interaction
from libs.data_mangement import DataManagement


class App:
    def __init__(self):
        self.go = False
        self.choice = Interaction()
        self.select_data = DataManagement()
        self.ctrl = ObjManagement()

    def start_app(self):
        self.go = True
        self.loop_app()

    def loop_app(self):
        while self.go:
            self.choice.choice_bdd()
            if self.choice.choice_menu == 0:
                self.ctrl.category_dysplay()
                self.choice.choice_number()
                num_cat = self.choice.choice_num
                if 1 <= num_cat <= 10:
                    listfood = self.ctrl.display_food_for_category(num_cat)
                    self.choice.choice_number()
                    num_food = self.choice.choice_num
                    if 1 <= num_food <= 10:
                        listsubfood = self.ctrl.display_sub_food_category(num_food, listfood)
                        self.choice.choice_sub_food()
                        num_sub_f = self.choice.choice_sub_f
                        if 1 <= num_sub_f <= 5:
                            self.select_data.save_sub_food(num_food, listfood, num_sub_f, listsubfood)
                        else:
                            print("not save")
            else:
                if self.choice.choice_menu == 1:
                    self.ctrl.display_test()

    def stop_app(self):
        self.go = False


if __name__ == "__main__":
    Application = App()
    Application.start_app()
