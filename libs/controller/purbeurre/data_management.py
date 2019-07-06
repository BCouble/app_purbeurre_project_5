from libs.connectbdd import ConnectBdd
from libs.view.message import *


class DataManagement:
    """Category of db pur_beurre"""

    def __init__(self):
        self.category = []
        self.product = []
        self.choice_product = int()
        self.substitute = []
        self.all_category = []
        self.favorites = []
        self.id_food = int()

    def select_category_s0(self):
        """select category"""
        query = "SELECT * FROM s0_category"
        db = ConnectBdd()
        self.category = db.execute_mysql_sel(query)
        db.destroy_mysql()

    def select_all_category(self):
        """select category"""
        query = "SELECT s2_category.name, s1_category.name, s0_category.name " \
                "FROM pur_beurre.s2_category " \
                "INNER JOIN " \
                "pur_beurre.s1_category " \
                "ON s1_category_id = idsous_categorie " \
                "INNER JOIN pur_beurre.s0_category " \
                "ON s0_category_id = idcategorie "
        db = ConnectBdd()
        self.all_category = db.execute_mysql_sel(query)
        db.destroy_mysql()

    def select_product(self, id_category):
        """ select product in bdd purbeurre """
        query = "SELECT idfood, name, dsc, cat_s2, shop, nutriscore FROM pur_beurre.food " \
                "WHERE cat_s2 IN (SELECT " \
                "ids2_categorie FROM pur_beurre.s2_category " \
                "WHERE s1_category_id IN (SELECT idsous_categorie FROM " \
                "pur_beurre.s1_category WHERE s0_category_id=%s )) " \
                "ORDER BY RAND () LIMIT 10" % id_category
        db = ConnectBdd()
        self.product = db.execute_mysql_sel(query)
        db.destroy_mysql()

    def select_substitute(self, id_food):
        """ select product in bdd purbeurre """
        self.id_food = self.get_id_food(id_food)
        query = "SELECT idfood, name, dsc, cat_s2, shop, nutriscore FROM food " \
                "WHERE cat_s2=(SELECT cat_s2 FROM " \
                "pur_beurre.food WHERE idfood=%s) AND idfood != %s ORDER " \
                "BY RAND () " \
                "LIMIT 5" % (self.id_food, self.id_food)
        db = ConnectBdd()
        self.substitute = db.execute_mysql_sel(query)
        db.destroy_mysql()

    def get_id_food(self, id_food):
        """id food in self.product"""
        return self.product[id_food][0]

    def save_substitute(self, id_substitute):
        """save substitute"""
        id_substitute = self.get_id_substitute(id_substitute)
        if not self.checks_if_substituted(self.id_food):
            query = "INSERT INTO favorites (id_food, id_substitute) " \
                    "VALUES (%s, %s)" % (self.id_food, id_substitute)
            db = ConnectBdd()
            db.execute_mysql_ins(query)
            db.destroy_mysql()
            return save_substitution()
        else:
            return substitution_exists()

    def get_id_substitute(self, id_substitute):
        """id food in self.product"""
        return self.substitute[id_substitute][0]

    def checks_if_substituted(self, id_food):
        """checks if the product is already substituted"""
        query = "SELECT * FROM favorites WHERE id_food = %s" % id_food
        db = ConnectBdd()
        food_search = db.execute_mysql_sel(query)
        db.destroy_mysql()

        return food_search

    def select_favorite(self):
        """select category"""
        query = "SELECT food.name, food.nutriscore " \
                "FROM pur_beurre.food WHERE idfood = (" \
                "SELECT id_food FROM pur_beurre.favorites " \
                "WHERE id_food = food.idfood " \
                "UNION " \
                "SELECT id_substitute FROM pur_beurre.favorites " \
                "WHERE id_substitute = food.idfood)"
        db = ConnectBdd()
        self.favorites = db.execute_mysql_sel(query)
        db.destroy_mysql()
