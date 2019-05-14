from libs.connect_bdd import Connect_bdd


class SelectData:
    def __init__(self):
        """ constructor select """
        self.categories = []
        self.food = []
        self.sub_food = []

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
        query = "SELECT id, name, shops, nutriscore FROM food WHERE id_categorie=%s LIMIT 10" % (id_categorie)
        db = Connect_bdd()
        food = db.execute_mysql(query)
        db.destroy_mysql()
        self.food = food

    def create_food_for_sub(self):
        """ create list product off """
        id = 1
        sub_food = []
        for line in self.food:
            line_food = (id, line[0], line[1], line[2], line[3])
            sub_food.append(line_food)
            id += 1

        self.sub_food = sub_food

    def display_food_for_cat(self):
        """ display product off """
        id = 1
        for line in self.food:
            print(id, line[1], line[2], line[3])
            id += 1

    def select_sub_food_cat(self, product, listfood):
        """ select sub food """
        print(listfood[product])

