from libs.data_mangement import DataManagement


class ObjManagement:
    def __init__(self):
        """ constructor obj """
        cat = ""
        self.cat = cat
        food = ""
        self.food = food
        sub_food = ""
        self.sub_food = sub_food
        sel_ssf = ""
        self.sel_ssf = sel_ssf

    def category_dysplay(self):
        self.cat = DataManagement()
        self.cat.select_cat()
        self.cat.display_cat()

    def display_food_for_category(self, food_cat):
        """ display food """
        self.food = DataManagement()
        self.food.select_food_for_cat(food_cat)
        self.food.display_food_for_cat()

        return self.food.food

    def display_sub_food_category(self, product, listfood):
        """ display sub food """
        self.sub_food = DataManagement()
        self.sub_food.select_sub_food_cat(product, listfood)
        self.sub_food.display_sub_food_cat()

        return self.sub_food.sub_food

    def display_test(self):
        self.sel_ssf = DataManagement()
        self.sel_ssf.select_fav_food()
        self.sel_ssf.select_fav_food_bis()
        self.sel_ssf.display_fav_food()


