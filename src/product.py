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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if  type(other) is not type(self):
            raise TypeError("Нельзя складывать товары разных классов")
        else:
            return (self.price * self.quantity) + (other.price * other.quantity)

class Smartphone(Product):
    """Класс для продукта - смартфон."""

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str, model: str, memory: float, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    """Класс для продукта - трава газонная."""
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color






