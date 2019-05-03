"""import openfoodfacts
from constant import *
import json
import requests"""
"""categories = openfoodfacts.facets.get_categories('france')
id_cat = categories[0]["id"]
print(id_cat)
#if 'fr:' in id_cat :
with open('categories.json', 'w') as f: 
    f.write(json.dumps(categories, indent=4))

languages = openfoodfacts.facets.get_languages()
with open('languages.json', 'w') as f: 
    f.write(json.dumps(languages, indent=4))

packagings = openfoodfacts.facets.get_packaging()
with open('packagings.json', 'w') as f: 
    f.write(json.dumps(packagings, indent=4))

states = openfoodfacts.facets.get_states()
with open('states.json', 'w') as f: 
    f.write(json.dumps(states, indent=4))

places = openfoodfacts.facets.get_purchase_places()
with open('places.json', 'w') as f: 
    f.write(json.dumps(places, indent=4))

entry_dates = openfoodfacts.facets.get_entry_dates()
with open('entry_dates.json', 'w') as f: 
    f.write(json.dumps(entry_dates, indent=4))"""

#products = openfoodfacts.products.get_by_facets({'trace': 'egg', 'country': 'france', 'state': 'complete', 'place': 'Paris', 'entry_date': '2019'})
"""products = openfoodfacts.products.get_by_country("France", 2)
products2 = openfoodfacts.products.get_by_facets({'category': 'Boissons', 'country': 'france'})
products3 = openfoodfacts.products.get_by_facets({'country': 'france'})
with open('test2.json', 'w') as f: 
    f.write(json.dumps(products, indent=4))"""

#products = openfoodfacts.products.get_by_country("France", 2)
#print(products)
"""food = 0
while food < 20:
            products = openfoodfacts.products.get_by_facets({'category': 'Boissons', 'country': 'france'})
            for product in products :
                print(products[food]['product_name'])
                print(products[food]['categories'])
                print(products[food]['countries'])
                food += 1"""


"""search_result = openfoodfacts.products.advanced_search({
  "search_terms":"*",
  "countries":"france",
  "page":"2",
  "page_size":"1000"
})"""

""" TEST CATEGORIE """
"""categories = []
i = 0
select_cat = requests.get(BASE_URL+CATEGORY).json()
#data_tags = select_cat.get('tags')

while i < NB_CAT:
    categories.append(select_cat['tags'][i]['name'])
    i += 1

print(categories)"""

""" TEST FOOD """
"""foods = []
search = requests.get(BASE_URL+CGI+FOOD).json()
with open('search.json', 'w') as f: 
    f.write(json.dumps(search, indent=4))"""

fruits = [{"pommes":21, "melons":3, "poires":31},
          {"pommes":45, "melons":32, "poires":1}]

for row in fruits:
    print(row)
    for value in row.values():
        print(value)

    def insert_food(self):
        """ insert food in mysql """
        self.cursor = self.db.cursor()
        for food in self.foods:
            query = ("INSERT INTO food (name, description, id_categorie, shops, date_save, url_page_off, nutriscore)"
                     "VALUES ({name}, {description}, {id_categorie}, {shops}, {date_save}, {url_page_off}, {nutriscore})").format(name=food['name'], description=food['description'], id_categorie=food["id_categorie"], shops=food["shops"], date_save=food["date_save"], url_page_off=food["url_page_off"], nutriscore=food["nutriscore"])
            #data = (food["name"], food["description"], food["id_categorie"], food["shops"], food["date_save"], food["url_page_off"], food["nutriscore"])
            self.cursor.execute(query)
            self.db.commit()
        self.cursor.close()

    def insert_food(self):
        """ insert food in mysql """
        self.cursor = self.db.cursor()
        for food in self.foods:
            query = ("INSERT INTO food (name, description, id_categorie, shops, date_save, url_page_off, nutriscore)"
                     "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            data = (food["name"], food["description"], food["id_categorie"], food["shops"], food["date_save"], food["url_page_off"], food["nutriscore"])
            self.cursor.execute(query, data)
            self.db.commit()
        self.cursor.close()
