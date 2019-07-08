""" URL """
"""
----------------------------------------
Exemple url :

# Category
# https://fr.openfoodfacts.org/categories.json
# Sous category
# https://fr.openfoodfacts.org/categorie/sauces/categories.json
# Food 
# https://fr.openfoodfacts.org/cgi/search.pl?category=sauces&page_size=50&search_simple=1&action=process&page=2&json=1
----------------------------------------
"""
# Base
GEOLOC = "fr"
BASE_URL = "https://"+GEOLOC+".openfoodfacts.org/"

# Category
BASE_URL_S_CAT = BASE_URL+"/categorie//"
CATEGORY = "categories.json"

# Food
CGI = "cgi/search.pl?"
FOOD = "page_size=50&search_simple=1&action=process&page=2&json=1"

""" CONFIG CATEGORIE """

LEN_CATEGORY = 20
NB_CAT = 75
NB_S_CAT = 50

""" CONFIG FOOD """

NB_FOOD = 50