"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()




food = 0
while food < 20:
            products = openfoodfacts.products.get_by_facets({'category': 'Boissons', 'country': 'france'})
            for food in products :
                print(products[food]['product_name'])
                print(products[food]['categories'])
                print(products[food]['countries'])
                food += 1