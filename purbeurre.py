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
                # Display category
                self.ctrl.category_dysplay()
                # Select category
                self.choice.choice_number()
                num_cat = self.choice.choice_num
                if 1 <= num_cat <= 10:
                    # Display products
                    listfood = self.ctrl.display_food_for_category(num_cat)
                    # Select product
                    self.choice.choice_number()
                    num_food = self.choice.choice_num
                    while num_food != 0:
                        if 1 <= num_food <= 10:
                            print(num_food)
                            listsubfood = self.ctrl.display_sub_food_category(num_food, listfood)
                            if not listsubfood:
                                num_food = 0
                                print("--- Pas de substitut pour ce produit ! ---")
                            else:
                                self.choice.choice_sub_food()
                                num_sub_f = self.choice.choice_sub_f
                                if 1 <= num_sub_f <= 5:
                                    print(num_food)
                                    self.select_data.save_sub_food(num_food, listfood, num_sub_f, listsubfood)
                                    num_food = 0
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
