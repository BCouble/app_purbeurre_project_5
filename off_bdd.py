from constant import *
import json
import requests
import mysql.connector

class Bdd_off:
    """ select, import data off """
    def __init__(self):
        """ Constructor """
        self.db = mysql.connector.connect(user=USER, password=PASSWD, host=HOST, database=DATABASE)
        self.categories = []

    def create_cat(self):
        """ categorie of open food fact """
        categories = []
        select_cat = requests.get(BASE_URL+CATEGORY).json()
        i = 0
        while i < NB_CAT:
            categories.append(select_cat['tags'][i]['name'])
            i += 1
        print("la liste des catégories à été crée")

        self.categories = categories

    def insert_cat(self):
        """ insert categories in mysql """
        print(self.categories)
        self.cursor = self.db.cursor()
        for obj in self.categories:
            query = ("INSERT INTO Categorie (name) VALUES (\"%s\")") % (obj)
            print(query)
            self.cursor.execute(query)
            self.db.commit()
        self.cursor.close()
        print("la liste des catégories à été importée")

    def create_food(self):
        """ data of open food fact """
        foods = []
        while page < 100:
            products = openfoodfacts.products.get_by_country("France", page)
            page += 1
            print(products['product_name'])

    def insert_food(self):
        """ insert dat in purbeurre """
