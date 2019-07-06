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


def create_cat(self):
    """category s0 of open food fact"""
    category = []
    select_cat = requests.get(BASE_URL + CATEGORY).json()
    i = 0
    id = 1
    while i < NB_CAT:
        cat = select_cat['tags'][i]['name']
        if 6 < len(cat) < 8:
            category.append((cat, id))
            id += 1
        i += 1
    print(category)
    self.category = category

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
