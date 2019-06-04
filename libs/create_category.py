
import requests
import mysql.connector

from libs.constant import *
from libs.connectbdd import *


class CreateCategory:
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

        self.categories = categories

    def insert_cat(self):
        """ insert categories in mysql """
        self.cursor = self.db.cursor()
        for obj in self.categories:
            query = "INSERT INTO categorie (name) VALUES (\"%s\")" % obj
            self.cursor.execute(query)
            self.db.commit()
        self.cursor.close()