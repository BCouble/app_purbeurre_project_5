from libs.connect_bdd import Connect_bdd


class Select_data:
    def __init__(self):
        """ constructor select """
        self.categories = []
        self.food = []

    def select_cat(self):
        """ select cat in bdd purbeurre """
        query = "SELECT * FROM categorie"
        db = Connect_bdd()
        categorie = db.execute_mysql(query)
        db.destroy_mysql()
        self.categories = categorie

    def display_cat(self):
        """ display category """
        for line in self.categories:
            print(line)

    def select_food_for_cat(self, id_categorie):
        """ select cat in bdd purbeurre """
        query = "SELECT * FROM food WHERE id_categorie=%s LIMIT 20" % (id_categorie)
        db = Connect_bdd()
        food = db.execute_mysql(query)
        db.destroy_mysql()
        self.food = food

    def display_food_for_cat(self):
        """ display category """
        for line in self.food:
            print(line)