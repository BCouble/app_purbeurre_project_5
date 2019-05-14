class Interaction:
    def __init__(self):
        choice_menu = ""
        choice_num = ""
        self.choice_menu = choice_menu
        self.choice_num = choice_num

    def choice_bdd(self):
        global choice_menu
        choice = True
        while choice:
            choice_menu = input("choisissez bdd(0) or fav(1) : ")
            try:
                choice_menu = int(choice_menu)
                if choice_menu == 0:
                    print("Produits de l'Open Food Fact")
                    break
                if choice_menu == 1:
                    print("Produits en favoris")
                    break
                else:
                    print("Choisir 0 ou 1")
                    break
            except ValueError:
                print("Choisir 0 ou 1")
                break

        self.choice_menu = choice_menu

    def choice_number(self):
        global choice_num
        choice = 0
        while choice == 0:
            choice_num = input("Choisissez un chiffre entre (1 & 10) ou 11 pour quitter: ")
            try:
                choice_num = int(choice_num)
                if 1 <= choice_num <= 11:
                    print("Produits de la catégorie")
                    break
                else:
                    print("Un nombre entre 1 & 11")
                    break
            except ValueError:
                print("Un nombre entre 1 & 11")
                break

        self.choice_num = choice_num
