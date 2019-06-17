""" URL """

# Category
# https://fr.openfoodfacts.org/categories.json
# Sous category
# https://fr.openfoodfacts.org/categorie/sauces/categories.json

# Base
GEOLOC = "fr"
BASE_URL = "https://"+GEOLOC+".openfoodfacts.org/"

# Category
CATEGORY = "categories.json"

# Food
CGI = "cgi/search.pl?"
FOOD = "page_size=50&search_simple=1&action=process&page=2&json=1"

""" CONFIG CATEGORIE """

NB_CAT = 60

""" CONFIG FOOD """

NB_FOOD = 50
