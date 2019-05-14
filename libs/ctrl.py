from libs.select_data import SelectData


class ManagementData:
    def __init__(self):
        """ constructor obj """
        cat = ""
        self.cat = cat

    def category_dysplay(self):
        self.cat = SelectData()
        self.cat.select_cat()
        self.cat.display_cat()


