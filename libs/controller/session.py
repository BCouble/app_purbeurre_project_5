

class Session:
    """management of navigation steps"""
    def __init__(self):
        self.session = []
        self.session_category = int()
        self.session_food = []

    def start_session(self):
        """init session"""
        start_session = 0

        self.session = start_session

    def select_category(self, id_category):
        """select category"""

        self.session_category = id_category

    def proposed_product(self, rand_food):
        """rand product of catégory"""

        self.session_food = rand_food

    def select_product(self):
        """select product"""
        pass

    def select_substitute(self):
        """select substitute"""
        pass

    def delete_category(self):
        """delete category"""
        pass

    def delete_product(self):
        """delete product"""
        pass

    def delete_substitute(self):
        """delete substitute"""
        pass
