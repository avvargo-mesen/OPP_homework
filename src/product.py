class Product:
    """Класс для продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, one_product: dict) -> "Product":
        product = cls(**one_product)
        return product

