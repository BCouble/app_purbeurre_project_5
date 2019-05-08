#! /usr/bin/env python3
# coding: utf-8
"""
Project 5
App Pur beurre
"""

from libs.select_data import Select_data


def display_category():
    """ display category """
    cat = Select_data()
    cat.select_cat()
    cat.display_cat()

def display_food_for_cat(cat):
    """ display food """
    food = Select_data()
    food.select_food_for_cat(cat)
    food.display_food_for_cat()

def choice_category():
    chiffre = input("Choisissez un chiffre : ")
    chiffre = int(chiffre)

    return chiffre

def main():
    """ running app """
    nav_app = True
    cat = 0
    while nav_app:
        if cat == 0:
            print("Veuillez choisir une catégorie : ")
            display_category()
            cat = choice_category()
        if 1 <= cat <= 10:
            print("Quel ingredient voulez-vous substituer ?")
            display_food_for_cat(cat)
            cat = choice_category()




if __name__ == "__main__":
    main()
