#! /usr/bin/env python3
# coding: utf-8
"""
Project 5
App Pur beurre
"""
import mysql.connector
from tkinter import *
from libs.select_data import Select_data


def display_cat(db):
    """ display category """
    cat = Select_data(db)
    cat.select_cat()
    print(cat)


def init_window():
    """ windows config """
    window = Tk()
    window.title('Pur Beurre')
    window.geometry("800x600")

    return window


def main():
    """ running app """
    init_window()
    display_cat(mysql)

    label = Label(init_window, text="Application pur beurre")
    label.pack()

    init_window.mainloop()


if __name__ == "__main__":
    main()




    def choice_number(self):
        global choice_num
        choice = 0
        while choice == 0:
            choice_num = input("Choisissez un chiffre entre (1 & 10) ou 11 pour quitter: ")
            try:
                choice_num = int(choice_num)
                if 1 <= choice_num <= 10:
                    print("Produits de la catégorie")
                    break
                else:
                    print("Un nombre entre 1 & 11")
                    break
            except ValueError:
                print("Un nombre entre 1 & 11")
                break

        self.choice_num = choice_num