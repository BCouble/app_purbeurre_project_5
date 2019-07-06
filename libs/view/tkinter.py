from tkinter import *
import logo
from libs.constant import BACKGROUND_COLOR, TEXT_COLOR
from libs.view.view_category import DisplayViewPort


class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, background=BACKGROUND_COLOR, width=650, height=500, **kwargs)
        self.pack(fill=BOTH, expand=1)
        self.choice = 999
        self.display_viewport = DisplayViewPort()

        # Création de nos widgets
        self.logo = Text(self, height=9, width=90, background=BACKGROUND_COLOR, foreground=TEXT_COLOR)
        self.logo.insert(INSERT, logo.create_logo())
        self.logo.pack()

        self.block_pb = Text(self, height=12, width=90, background=BACKGROUND_COLOR, foreground=TEXT_COLOR)
        self.block_pb.insert(INSERT, self.display_viewport.display_start_app())
        self.block_pb.pack()

        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()

        self.var_text = IntVar()
        self.line_text = Entry(self, textvariable=self.var_text)
        self.line_text.pack(side="left")

        self.button_ok = Button(self, text="OK", fg="red",
                                command=self.click)
        self.button_ok.pack(side="right")

        self.button_save = Button(self, text="SAVE", fg="red",
                                  command=self.save_substitute)

    def viewport_cat(self):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_cat_s0())
        self.block_pb.pack()

    def viewport_favorites(self):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_favorites())
        self.block_pb.pack()

    def viewport_product(self, id_category):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_product(id_category))
        self.block_pb.pack()

    def viewport_choice_product(self, id_food):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_substitute(id_food))
        self.block_pb.pack()
        self.button_save.pack(side="right")

    def button_return(self):
        """return state one"""

    def click(self):
        """check value send session"""
        message = "Base de données pur beurre ou favoris"
        choice = True
        while choice:
            enter_choice = self.line_text.get()
            try:
                enter_choice = int(enter_choice)
                if enter_choice == 0:
                    message = "Catégories de l'Open Food Fact"
                    self.viewport_cat()
                    self.button_ok["command"] = self.click_product
                    break
                if enter_choice == 1:
                    message = "Produits en favoris"
                    self.viewport_favorites()
                    break
                else:
                    message = enter_choice
                    break
            except ValueError:
                message = "Choisir 0 ou 1"
                break

        self.message["text"] = " {} ".format(message)

    def click_product(self):
        """check value send session"""
        message = "Choisissez un produit"
        choice = True
        while choice:
            enter_choice = self.line_text.get()
            try:
                enter_choice = int(enter_choice)
                if 1 <= enter_choice <= 6:
                    message = "Produits de l'Open Food Fact"
                    self.viewport_product(enter_choice)
                    self.button_ok["command"] = self.click_for_select_product
                    break
                else:
                    message = "Choisir un nombre entre 1 & 6"
                    break
            except ValueError:
                message = "Choisir un nombre entre 1 & 6"
                break

        self.message["text"] = " {} ".format(message)

    def click_for_select_product(self):
        """check value send session"""
        message = "Choisissez un substitut"
        choice = True
        while choice:
            enter_choice = self.line_text.get()
            try:
                enter_choice = int(enter_choice)
                if 1 <= enter_choice <= 10:
                    message = "Substituts de l'Open Food Fact"
                    self.viewport_choice_product(enter_choice)
                    self.button_ok["text"] = "new search"
                    break
            except ValueError:
                message = "Choisir un nombre entre 1 & 5"
                break

        self.message["text"] = " {} ".format(message)

    def save_substitute(self):
        """check value send session"""
        message = "Sauvegardez un substitut"
        choice = True
        while choice:
            enter_choice = self.line_text.get()
            try:
                enter_choice = int(enter_choice)
                if 1 <= enter_choice <= 5:
                    message = self.display_viewport.d_save_substitute(enter_choice)
                    break
            except ValueError:
                message = "Choisir un nombre entre 1 & 5"
                break

        self.message["text"] = " {} ".format(message)
