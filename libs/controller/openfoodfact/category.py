from libs.controller.connectbdd import ConnectBdd
from libs.controller.openfoodfact.constant import *
import requests


class CreateCategory:
    """select, import data off"""
    def __init__(self):
        self.category = [('Viandes', 1), ('Gâteaux', 2), ('Yaourts', 3), ('Poulets', 4), ('Jambons', 5), ('Graines', 6)]
        self.all_category = []
        self.s1category = []
        self.s2category = []

    def create_s1_cat(self):
        """select category s1"""
        s1category = []
        id = 1
        for row in self.category:
            obj = row[0]
            id_s0 = row[1]
            select_s1_cat = requests.get(BASE_URL_S_CAT + obj + "//" + CATEGORY).json()
            i = 0
            while i < NB_S_CAT:
                s1_cat = select_s1_cat['tags'][i]['name']
                # 20 to limit the number of subcategories
                if obj in s1_cat and s1_cat != obj and len(s1_cat) < LEN_CATEGORY:
                    s1category.append((s1_cat, id_s0, id))
                    id += 1
                i += 1

        self.s1category = s1category

    def create_s2_cat(self):
        """select category s2"""
        s2category = []
        for row in self.s1category:
            obj = row[0]
            select_s2_cat = requests.get(BASE_URL_S_CAT + obj + "//" + CATEGORY).json()
            max_cat = select_s2_cat['count']
            i = 0
            while i < max_cat:
                if 10 < select_s2_cat['tags'][i]['products'] < 20 and len(select_s2_cat['tags'][i]['name']) > 0:
                    s2category.append((select_s2_cat['tags'][i]['name'], row[2]))
                i += 1

        self.s2category = s2category

    def insert_cat(self):
        """insert category in mysql"""
        db = ConnectBdd()
        for row in self.category:
            obj = row[0]
            query = "INSERT INTO s0_category (name) VALUES (\"%s\")" % obj
            print(query)
            db.execute_mysql_ins(query)
        db.destroy_mysql()

    def insert_s1_cat(self):
        """insert category in mysql"""
        db = ConnectBdd()
        for row in self.s1category:
            name = row[0]
            s0 = row[1]
            query = "INSERT INTO s1_category (name, s0_category_id) VALUES (\"%s\", %s)" % (name, s0)
            print(query)
            db.execute_mysql_ins(query)
        db.destroy_mysql()

    def insert_s2_cat(self):
        """insert category in mysql"""
        db = ConnectBdd()
        for row in self.s2category:
            name = row[0]
            s1 = row[1]
            query = "INSERT INTO s2_category (name, s1_category_id) VALUES (\"%s\", %s)" % (name, s1)
            print(query)
            db.execute_mysql_ins(query)
        db.destroy_mysql()
