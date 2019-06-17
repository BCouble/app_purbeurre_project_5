from libs.connectbdd import ConnectBdd


class Category:
    """Category of pur_beurre"""

    def __init__(self):
        self.category = []
        self.all_category = []
        self.nb_s2_category = ""

    def select_category(self):
        """select category"""
        query = "SELECT * FROM s0_category"
        db = ConnectBdd()
        category = db.execute_mysql_sel(query)
        db.destroy_mysql()
        self.category = category

    def select_all_category(self):
        """select category"""
        query = "SELECT s2_category.name, s1_category.name, s0_category.name " \
                "FROM pur_beurre.s2_category " \
                "INNER JOIN " \
                "pur_beurre.s1_category " \
                "ON s1_category_id = idsous_categorie " \
                "INNER JOIN pur_beurre.s0_category " \
                "ON s0_category_id = idcategorie "
        db = ConnectBdd()
        all_category = db.execute_mysql_sel(query)
        db.destroy_mysql()
        self.all_category = all_category

    def count_s2_category(self):
        """select category"""
        query = "SELECT COUNT(*) FROM pur_beurre.s2_category"
        db = ConnectBdd()
        nb_s2_category = db.execute_mysql_count(query)
        db.destroy_mysql()
        return nb_s2_category
