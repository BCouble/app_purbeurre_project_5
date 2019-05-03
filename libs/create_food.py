
import json
import requests
import mysql.connector

from libs.constant import *


class Create_food:
    """ select, import data off """
    def __init__(self):
        """ Constructor """
        self.db = mysql.connector.connect(user=USER, password=PASSWD, host=HOST, database=DATABASE)
        self.categories = []
        self.foods = []

    def select_cat(self):
        """ select cat in bdd purbeurre """
        self.cursor = self.db.cursor(buffered=True)
        query = ("SELECT * FROM categorie")
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.db.commit()
        self.cursor.close()
        self.categories = rows

    def create_food(self):
        """ data of open food fact """
        foods = []
        for row in self.categories:
            cat_y = "category="+row[1]+"&"
            search = requests.get(BASE_URL+CGI+cat_y+FOOD).json()
            i = 0
            while i < NB_FOOD:
                food = {"name": "", "description": "", "id_categorie": "", "shops": "", "date_save": "",
                        "url_page_off": "", "nutriscore": ""}
                if search['products'][i]['states_tags'][1] == "en:complete":
                    try:
                        food["name"] = search['products'][i]['product_name_fr']
                        food["description"] = search['products'][i]['generic_name_fr']
                        food["id_categorie"] = row[0]
                        food["shops"] = search['products'][i]['stores']
                        food["date_save"] = search['products'][i]['entry_dates_tags'][0]
                        food["url_page_off"] = search['products'][i]['url']
                        food["nutriscore"] = search['products'][i]['nutrition_grade_fr']
                    except (KeyError, TypeError):
                        pass
                    foods.append(food)
                i += 1
            self.foods = foods

    def insert_food(self, food):
        """ insert food in mysql """
        data = (
        food["name"], food["description"], food["id_categorie"], food["shops"], food["date_save"], food["url_page_off"],
        food["nutriscore"])
        query = ("INSERT INTO food (name, description, id_categorie, shops, date_save, url_page_off, nutriscore)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        self.cursor = self.db.cursor()
        self.cursor.execute(query, data)
        self.db.commit()
        self.cursor.close()

    def check_value(self):
        """ check value for row food """
        for food in self.foods:
            insert = True
            for value in food.values():
                if value == "":
                    insert = False
            if insert:
                self.insert_food(food)

