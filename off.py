import requests

value = "granola"

params = (
    ('search_terms', value),
    ('search_simple', '1'),
    ('action', 'process'),
    ('json', '1'),
)

response = requests.get('https://fr.openfoodfacts.org/api/v0/cgi/search.pl', params=params)
print(response.text)

# nous avons la requete de recherche à partir d'un mot clé

# on récupère l'id, le code barre du produit 
# nous lancons une autre requete avec le code barre
# nous construison la requete api
# la page du produit est aussi récupérable
# https://fr.openfoodfacts.org/produit/3017760756198/

# 1 nous récupérons les informations sur le produit
# 
# Creat list produit par rapport à la recherche 
# Trie par catégorie
# 	TRie du résultat par rapport à la qualité energetique des produits
# Choix catégorie
# proposition du produit du plus sein au moin bien...

# 2 le produit plait :
# On enregistre en bdd purbeurre 
# historique du produit à substitué
# substitue choisi
