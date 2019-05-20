from libs.create_category import CreateCategory
from libs.create_food import CreateFood

cat = CreateCategory()
cat.create_cat()
cat.insert_cat()

food = CreateFood()
food.select_cat()
food.create_food()
food.check_value()