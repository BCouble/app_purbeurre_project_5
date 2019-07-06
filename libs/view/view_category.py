from libs.controller.purbeurre.data_management import DataManagement


class DisplayViewPort:
    def __init__(self):
        self.data = " rrttee "
        self.cat = DataManagement()

    def display_cat_s0(self):
        """recovers the data from pur beurre : s0_category"""
        self.cat.select_category_s0()

        return '\n'.join('{}: {}'.format(*line[1]) for line in enumerate(self.cat.category, 1))

    def display_start_app(self):
        """message start app"""
        data = "Welcome to the pur beurre application\n " \
               "Enter 0 to access the pur beurre database\n " \
               "Enter 1 to access the pur beurre favoris "

        return data

    def display_product(self, id_category):
        """recovers the data from pur beurre : s0_category"""
        self.cat.select_product(id_category)
        data = self.cat.product
        dt = []
        id = 0
        for line in data:
            d = (id, line[1], line[0], line[5])
            dt.append(d)
            id += 1
        dt = '\n'.join('{}: {} {}'.format(*line[1]) for line in enumerate(dt, 1))

        return dt

    def display_substitute(self, id_food):
        """recovers the data from pur beurre : s0_category"""
        self.cat.select_substitute(id_food)
        data = self.cat.substitute
        dt = []
        id = 0
        for line in data:
            d = (id, line[1], line[0], line[5])
            dt.append(d)
            id += 1
        dt = '\n'.join('{}: {} {}'.format(*line[1]) for line in enumerate(dt, 1))

        return dt

    def d_save_substitute(self, id_substitute):
        """rec id_food & id_substitute"""
        message = self.cat.save_substitute(id_substitute)

        return message

    def display_favorites(self):
        """rec id_food & id_substitute"""
        self.cat.select_favorite()
        favorites = self.cat.favorites
        list_favorite = []
        id = 1
        for line in favorites:
            if id%2 != 0:
                l = ("Produit", line[0], "nutriscore", line[1])
                list_favorite.append(l)
            if id%2 == 0:
                l = ("Substitut", line[0], "nutriscore", line[1])
                list_favorite.append(l)
            id += 1

        list_favorite = '\n'.join('{}: {} | {}: {}'.format(*line[1]) for line in enumerate(list_favorite, 1))

        return list_favorite
