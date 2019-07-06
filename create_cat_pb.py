from libs.controller.openfoodfact.category import CreateCategory
from libs.controller.openfoodfact.food import CreateFood

Category = CreateCategory()
Category.create_s1_cat()
Category.create_s2_cat()
Category.insert_cat()
Category.insert_s1_cat()
Category.insert_s2_cat()


Food = CreateFood()
Food.import_category_pb()
Food.search_food()
Food.create_food()
Food.insert_food()