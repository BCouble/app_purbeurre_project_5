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
        self.manage_choice = Interaction()
        self.manage_data = DataManagement()
        self.manage_obj = ObjManagement()

    def start_app(self):
        self.go = True
        self.loop_app()

    def loop_app(self):
        while self.go:
            self.manage_choice.choice_bdd()
            if self.manage_choice.choice_menu == 0:
                print("Welcome in bdd pur beurre")
                self.manage_obj.category_dysplay()
                print("Vous pouvez choisir une catégorie : ")
                self.manage_choice.choice_number()
                num_cat = self.manage_choice.choice_num
                if 1 <= num_cat <= 10:
                    list_food = self.manage_obj.display_food_for_category(num_cat)
            else:
                print("Welcom in Favoris")

    def stop_app(self):
        self.go = False


if __name__ == "__main__":
    Application = App()
    Application.start_app()

"""object to search in off"""
foods = []
food = {"product_name_fr": "", "generic_name_fr": "", "id_s2_category": "", "stores": "", "'entry_dates_tags'][0": "",
        "url": "", "nutrition_grade_fr": ""}
obj_to_search = ["product_name_fr", "generic_name_fr", "id_s2_category", "stores", "'entry_dates_tags'][0", "url",
                 "nutrition_grade_fr"]
number_p = 0
while number_p < (nb_product - 1):
    num_ch = 0
    while num_ch < 6:
        if obj_to_search[num_ch - 1] in data_food[number_p]:
            food[obj_to_search[num_ch - 1]] = data_food[number_p][obj_to_search[num_ch - 1]]
        else:
            food[obj_to_search[num_ch - 1]] = "NULL"
        num_ch += 1
        food[obj_to_search[2]] = category
    foods.append(food)
    number_p += 1
print(foods)

product_name_fr = food["product_name_fr"]
generic_name_fr = food["generic_name_fr"]
id_s2_category = food["id_s2_category"]
stores = food["stores"]
entry_dates_tags = food["entry_dates_tags[0]"]
url = food["url"]
nutrition_grade_fr = food["nutrition_grade_fr"]