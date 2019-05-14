# ! /usr/bin/env python3
# coding: utf-8
"""
Project 5
App Pur beurre
"""

from libs.select_data import SelectData


def display_category():
    """ display category """
    cat = SelectData()
    cat.select_cat()
    cat.display_cat()


def display_food_for_category(cat):
    """ display food """
    food = SelectData()
    food.select_food_for_cat(cat)
    food.display_food_for_cat()

    return food.food


def display_sub_food_category(product, listfood):
    """ display sub food """
    sub_food = SelectData()
    sub_food.select_sub_food_cat(product, listfood)


def choice_bdd():
    choice = True
    data = ""
    while choice:
        data = input("choisissez bdd(0) or fav(1) : ")
        try:
            data = int(data)
            if data == 0:
                print("Produits de l'Open Food Fact")
                break
            if data == 1:
                print("Produits en favoris")
                break
            else:
                print("Choisir 0 ou 1")
                break
        except ValueError:
            print("Choisir 0 ou 1")
            break

    return data


def choice_number():
    choice = 0
    nb_cat = ""
    while choice == 0:
        nb_cat = input("Choisissez un chiffre entre (1 & 10) ou 11 pour quitter: ")
        try:
            nb_cat = int(nb_cat)
            choice = 1
            break
        except ValueError:
            print("Un nombre entre 1 & 11")

    return nb_cat


def choice_sub():
    pass


def return_home():
    home_app = False

    return home_app


def main():
    """ running app """
    home_app = True
    while home_app:
        fav = choice_bdd()
        cat = 0
        if fav == 0:
            if cat == 0:
                print("Veuillez choisir une catégorie : ")
                display_category()
                cat = choice_number()
            if 1 <= cat <= 10:
                print("Quel ingredient voulez-vous substituer ?")
                listfood = display_food_for_category(cat)
                product = choice_number()
                if 1 <= product <= 10:
                    display_sub_food_category(product, listfood)
            if cat == 11:
                print("return home")
                return_home()
        if fav == 1:
            print("Ici affiche fav0")


if __name__ == "__main__":
    main()
