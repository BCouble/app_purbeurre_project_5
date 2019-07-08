from tkinter import *
from libs.model import logo
from libs.model.constant import BACKGROUND_COLOR, TEXT_COLOR
from libs.model.viewport import DisplayViewPort


class Interface(Frame):
    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, background=BACKGROUND_COLOR, width=650, height=500, **kwargs)
        self.pack(fill=BOTH, expand=1)
        self.choice = 999
        self.display_viewport = DisplayViewPort()

        self.logo = Text(self, height=9, width=90, background=BACKGROUND_COLOR, foreground=TEXT_COLOR)
        self.logo.insert(INSERT, logo.create_logo())
        self.logo.pack()

        self.block_pb = Text(self, height=12, width=90, background=BACKGROUND_COLOR, foreground=TEXT_COLOR)

        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()

        self.var_text = IntVar()
        self.line_text = Entry(self, textvariable=self.var_text)

        self.button_ok = Button(self, text="OK", fg="red",
                                command=self.click)

        self.button_save = Button(self, text="Save", fg="red",
                                  command=self.save_substitute)

        self.button_return = Button(self, text="Home", fg="red",
                                    command=self.viewport_start)

        self.viewport_start()

    def viewport_start(self):
        """start app"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_start_app())
        self.block_pb.pack()
        self.message["text"] = " {} ".format("Vous n'avez pas cliqué sur le bouton.")
        self.widget_text()
        self.button_validate()
        self.button_save.destroy()
        self.button_return.destroy()

    def viewport_cat(self):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_cat_s0())
        self.block_pb.pack()
        self.button_return = Button(self, text="Home", fg="red",
                                    command=self.viewport_start)
        self.button_return.pack(side="right")

    def viewport_favorites(self):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_favorites())
        self.block_pb.pack()
        self.line_text.destroy()
        self.button_ok.destroy()
        self.button_return = Button(self, text="Home", fg="red",
                                    command=self.viewport_start)
        self.button_return.pack(side="right")

    def viewport_product(self, id_category):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_product(id_category))
        self.block_pb.pack()
        self.button_return.pack(side="right")

    def viewport_choice_product(self, id_food):
        """viewport"""
        self.block_pb.delete(0.0, END)
        self.block_pb.insert(INSERT, self.display_viewport.display_substitute(id_food))
        self.block_pb.pack()
        self.button_save.pack(side="right")
        self.button_return.pack(side="right")

    def button_validate(self):
        """button ok"""
        self.button_ok.destroy()
        self.button_ok = Button(self, text="OK", fg="red",
                                command=self.click)
        self.button_ok.pack(side="right")

    def widget_text(self):
        """widget text"""
        self.line_text.destroy()
        self.line_text = Entry(self, textvariable=self.var_text)
        self.line_text.pack(side="left")

    def click(self):
        """check value send session"""
        message = "Base de données pur beurre ou favoris"
        choice = True
        while choice:
            enter_choice = self.line_text.get()
            try:
                enter_choice = int(enter_choice)
                if enter_choice == 0:
                    message = "Catégories de Pur Beurre"
                    self.viewport_cat()
                    self.button_ok["command"] = self.click_product
                    break
                if enter_choice == 1:
                    message = "Produits en favoris"
                    self.viewport_favorites()
                    break
                if not 1 or not 0:
                    message = "Choisir 0 ou 1"
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
                    self.button_save = Button(self, text="Save", fg="red",
                                              command=self.save_substitute)
                    self.button_ok["command"] = self.click_for_select_product
                    break
                if enter_choice == 0 or enter_choice > 6:
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
            nb_prod = self.display_viewport.nb_product - 1
            try:
                enter_choice = int(enter_choice)
                if 0 <= enter_choice <= nb_prod:
                    message = "Substituts de l'Open Food Fact"
                    self.viewport_choice_product(enter_choice)
                    self.button_ok["text"] = "new search"
                    break
                if enter_choice > nb_prod:
                    message = " {} ".format("Choisir un nombre entre 0 & " + str(nb_prod))
                    break
            except ValueError:
                message = " {} ".format("Choisir un nombre entre 0 & " + str(nb_prod))
                break

        self.message["text"] = " {} ".format(message)

    def save_substitute(self):
        """check value send session"""
        message = "Sauvegardez un substitut"
        choice = True
        while choice:
            enter_choice = self.line_text.get()
            nb_sub = self.display_viewport.nb_substitute - 1
            try:
                enter_choice = int(enter_choice)
                if 0 <= enter_choice <= nb_sub:
                    message = self.display_viewport.d_save_substitute(enter_choice)
                    self.button_save.destroy()
                    self.button_ok.destroy()
                    break
                if enter_choice > nb_sub:
                    message = " {} ".format("Choisir un nombre entre 0 & "+str(nb_sub))
                    break
            except ValueError:
                message = " {} ".format("Choisir un nombre entre 0 & "+str(nb_sub))
                break

        self.message["text"] = " {} ".format(message)
