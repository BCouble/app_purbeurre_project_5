import openfoodfacts
import json

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
products = openfoodfacts.products.get_by_country("France", 2)
products2 = openfoodfacts.products.get_by_facets({'category': 'Boissons', 'country': 'france'})

with open('france_2.json', 'w') as f: 
    f.write(json.dumps(products, indent=4))

#products = openfoodfacts.products.get_by_country("France", 2)
#print(products)