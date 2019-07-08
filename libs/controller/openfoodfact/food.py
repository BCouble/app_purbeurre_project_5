import openfoodfacts
from libs.controller.connectbdd import ConnectBdd
from libs.controller.purbeurre.data_management import DataManagement


class CreateFood:
    def __init__(self):
        self.all_category = []
        self.search_result = []
        self.food = []
        self.nb_category = int()
        self.foods = []

    def import_category_pb(self):
        """select category of purbeurre"""
        all_cat = DataManagement()
        all_cat.select_all_category()

        self.all_category = all_cat.all_category

    def search_food(self):
        """search in openfoodfact"""
        products_result = []
        nb_category = 0
        for row in self.all_category:
            nb_category += 1
            search_result = openfoodfacts.products.advanced_search({
                "search_terms": (row[2], row[1], row[0]),
                "tagtype_0": "categories",
                "page_size": "200"
            })
            nb_product = search_result['count']
            products = search_result['products']
            products_result.append((nb_product, products))

        self.nb_category = nb_category
        self.search_result = products_result

    def create_food(self):
        """create food in purbeurre"""
        for nb_cat in range(self.nb_category - 1):
            search_cat = self.search_result[nb_cat]
            self.check_data_off(search_cat[1], nb_cat)

    def check_data_off(self, data_food, category):
        """object to search in off"""
        for product in data_food:
            food = {"product_name_fr": "", "generic_name_fr": "", "id_s2_category": "", "stores": "", "url": "",
                    "nutrition_grade_fr": ""}
            for key in food:
                if key in product:
                    food[key] = product[key]
                if key == "id_s2_category":
                    food[key] = category + 1
            self.foods.append(food)

    def insert_food(self):
        """ insert food in mysql """
        db = ConnectBdd()
        count_food = 0
        for food in self.foods:
            if "" not in food.values():
                query = ("INSERT INTO food (name, dsc, cat_s2, shop, url_page, nutriscore)"
                         "VALUES (%(product_name_fr)s, %(generic_name_fr)s, %(id_s2_category)s, %(stores)s,"
                         " %(url)s, %(nutrition_grade_fr)s)")
                db.execute_mysql_ins_data(query, food)
            else:
                count_food += 1

        print(count_food)
        db.destroy_mysql()

