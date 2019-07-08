from libs.controller.purbeurre.data_management import DataManagement


class DisplayViewPort:
    def __init__(self):
        self.cat = DataManagement()
        self.nb_product = int()
        self.nb_substitute = int()

    def display_cat_s0(self):
        """recovers the data from pur beurre : s0_category"""
        self.cat.select_category_s0()

        return '\n'.join('{}: {}'.format(*line[1]) for line in enumerate(self.cat.category, 1))

    def display_start_app(self):
        """message start app"""
        text = "Welcome to the pur beurre application\n " \
               "Enter 0 to access the pur beurre database\n " \
               "Enter 1 to access the pur beurre favoris "

        return text

    def display_product(self, id_category):
        """recovers the data from pur beurre : s0_category"""
        self.cat.select_product(id_category)
        text = []
        id = 0
        for line in self.cat.product:
            d = (id, line[1], line[5], line[0])
            text.append(d)
            id += 1

        self.nb_product = id
        return '\n'.join('{}: {} | nutriscore: {}'.format(*line[1]) for line in enumerate(text, 1))

    def display_substitute(self, id_food):
        """recovers the data from pur beurre : s0_category"""
        self.cat.select_substitute(id_food)
        text = []
        id = 0
        for line in self.cat.substitute:
            d = (id, line[1], line[5], line[0])
            text.append(d)
            id += 1

        self.nb_substitute = id
        return '\n'.join('{}: {} [ nutriscore: {}'.format(*line[1]) for line in enumerate(text, 1))

    def d_save_substitute(self, id_substitute):
        """rec id_food & id_substitute"""
        message = self.cat.save_substitute(id_substitute)

        return message

    def display_favorites(self):
        """rec id_food & id_substitute"""
        self.cat.select_favorite()
        list_favorite = []
        id = 1
        for line in self.cat.favorites:
            if id%2 != 0:
                l = ("Produit", line[0], "nutriscore", line[1])
                list_favorite.append(l)
            if id%2 == 0:
                l = ("Substitut", line[0], "nutriscore", line[1])
                list_favorite.append(l)
            id += 1

        return '\n'.join('{}: {} | {}: {}'.format(*line[1]) for line in enumerate(list_favorite, 1))
