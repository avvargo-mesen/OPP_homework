from src.product import Product
from src.category import Category

# Создаем два товара
pr_1 = Product("Ноутбук", "Игровой ноутбук", 150000.0, 5)
pr_2 = Product("Мышь", "Беспроводная мышь", 2500.0, 10)

# Создаем категорию
ct_1 = Category("Электроника", "Ноутбуки и аксессуары", [pr_1, pr_2])

# Выводим Название категории
# Название первого товара в категории
# Значение Category.category_count
# Значение Category.product_count

print(ct_1.name)
print(ct_1.products[0].name)
print(Category.category_count)
print(Category.product_count)
