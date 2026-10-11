class Product:
    """Класс для продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, one_product: dict) -> "Product":
        """класс-метод,  принимает словарь с данными товара и возвращает объект Product, созданный из этого словаря"""
        product = cls(**one_product)
        return product

    @property
    def price(self) -> float:
        new_price = self.__price
        return new_price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price




