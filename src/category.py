from src.product import Product


class Category:
    """Класс для категорий"""

    # Переменная на уровне класса для подсчета количества категорий
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)


    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        new_products_list = []
        for product in self.__products:
            new_products_list.append(f"{product.name}, {product.price}руб. Остаток: {product.quantity} шт.\n")

        return "".join(new_products_list)

