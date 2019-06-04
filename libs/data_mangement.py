from libs.connectbdd import ConnectBdd


class DataManagement:
    def __init__(self):
        """ constructor select """
        self.categories = []
        self.food = []
        self.sub_food = []
        self.select_sub_food = []
        self.ssf = []

    def select_cat(self):
        """ select cat in bdd purbeurre """
        query = "SELECT * FROM categorie"
        db = ConnectBdd()
        categorie = db.execute_mysql_sel(query)
        db.destroy_mysql()
        self.categories = categorie

    def display_cat(self):
        """ display category """
        for line in self.categories:
            print(line)

    def select_food_for_cat(self, id_categorie):
        """ select cat in bdd purbeurre """
        query = "SELECT id, name, description, id_categorie, shops, nutriscore FROM food WHERE id_categorie=%s ORDER " \
                "BY RAND () " \
                "LIMIT 10" % id_categorie
        db = ConnectBdd()
        food = db.execute_mysql_sel(query)
        db.destroy_mysql()
        self.food = food

    def display_food_for_cat(self):
        """ display product off """
        id = 1
        for line in self.food:
            print(id, line[1], line[2], line[3])
            id += 1

    def select_sub_food_cat(self, product, listfood):
        """ select sub food """
        product = product - 1
        letter = "%" + listfood[product][2][:4] + "%"
        id_food = listfood[product][0]
        id_cat = listfood[product][3]
        query = "SELECT * FROM food WHERE id_categorie = %s AND name LIKE '%s' AND id != %s ORDER BY nutriscore " \
                "LIMIT 5" % (id_cat, letter, id_food)
        db = ConnectBdd()
        sub_food = db.execute_mysql_sel(query)
        db.destroy_mysql()
        self.sub_food = sub_food

    def display_sub_food_cat(self):
        """ display sub food """
        id = 1
        for line in self.sub_food:
            print(id, line[1], line[3], line[7])
            id += 1

    def save_sub_food(self, product, listfood, num_sub_f, listsubfood):
        """ Save substitute """
        sub_product = listfood[product][0]
        num_sub_f = num_sub_f - 1
        substitute = listsubfood[num_sub_f][0]
        if not self.check_data_sub_food(sub_product, substitute):
            query = "INSERT INTO substitutes (id_produit, id_substitute) VALUES (%s, %s)" % (sub_product, substitute)
            db = ConnectBdd()
            db.execute_mysql_ins(query)
            db.destroy_mysql()
        else:
            print(""
                  "Cette substitution existe déjà !"
                  "")

    def check_data_sub_food(self, produit_sub, substitute):
        """ Check substitute exist """
        query = "SELECT * FROM substitutes WHERE id_produit=%s AND id_substitute=%s" % (produit_sub, substitute)
        db = ConnectBdd()
        check = db.execute_mysql_sel(query)
        db.destroy_mysql()
        return check

    def select_fav_food(self):
        """ select fav food """
        query = "SELECT * FROM substitutes LIMIT 5"
        db = ConnectBdd()
        select_sub_food = db.execute_mysql_sel(query)
        db.destroy_mysql()
        self.select_sub_food = select_sub_food

    def select_fav_food_bis(self):
        """ select fav food """
        sel_ssf = []
        for line in self.select_sub_food:
            id_prod = line[1]
            id_sub = line[2]
            query = "SELECT food.name, food.nutriscore as food FROM food INNER JOIN substitutes ON " \
                    "substitutes.id_produit = food.id WHERE food.id = %s UNION  SELECT food.name, food.nutriscore " \
                    "as food FROM food INNER JOIN substitutes ON substitutes.id_substitute = food.id WHERE food.id = " \
                    "%s " % (id_prod, id_sub)
            db = ConnectBdd()
            sel_fav = db.execute_mysql_sel(query)
            db.destroy_mysql()
            sel_ssf.append(sel_fav)
        self.ssf = sel_ssf

    def display_fav_food(self):
        """ display fav food """
        id = 0
        for line in self.ssf:
            print("-------------------------")
            print("Le produit substitué : " + line[0][0], ", nutriscore : " + line[0][1])
            print("Le substitut : " + line[1][0], ", nutriscore : " + line[1][1])
            print("-------------------------")
            id += 1
