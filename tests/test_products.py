from src.product import Product
from src.product import Smartphone
from src.product import LawnGrass
from src.category import Category
import pytest


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def first_pr():
    return Product("Ноутбук", "Игровой ноутбук", 150000.0, 5)


@pytest.fixture
def second_pr():
    return Product("Мышь", "Беспроводная мышь", 2500.0, 10)


@pytest.fixture
def first_ct(first_pr, second_pr):
    return Category("Электроника", "Ноутбуки и аксессуары", [first_pr, second_pr])

@pytest.fixture
def first_sm():
    return Smartphone("Samsung", "Смартфон", 50000.0, 2, 5, "JA-700", 8, "gold")

@pytest.fixture
def second_sm():
    return Smartphone("Readme", "Смартфон", 45000.0, 5, 4, "J-720", 16, "black")

@pytest.fixture
def first_lg():
    return LawnGrass("Газонная трава", "Быстрорастущая", 500.0, 20, "Россия", "7 дней", "зелёный")


def test_pr(first_pr):
    assert first_pr.name == "Ноутбук"
    assert first_pr.description == "Игровой ноутбук"
    assert first_pr.price == 150000.0
    assert first_pr.quantity == 5


def test_ct(first_ct):
    assert first_ct.name == "Электроника"
    assert first_ct.description == "Ноутбуки и аксессуары"
    assert "Ноутбук" in first_ct.products
    assert "Мышь" in first_ct.products


def test_count_ct(first_ct):
    assert Category.category_count == 1


def test_count_pr(first_ct):
    assert Category.product_count == 2


def test_add_product(first_ct):
    pr_3 = Product("Клавиатура", "Механическая", 5000.0, 3)
    first_ct.add_product(pr_3)
    assert Category.product_count == 3
    assert "Клавиатура" in first_ct.products

def test_products(first_ct):
    assert type(first_ct.products) == str
    assert "Ноутбук" in first_ct.products
    assert "Мышь" in first_ct.products

def test_new_product():
    dict_1 = {"name":"Клавиатура", "description": "Механическая", "price": 5000.0, "quantity":3}
    product = Product.new_product(dict_1)
    assert isinstance(product, Product)
    assert product.name == "Клавиатура"
    assert product.description == "Механическая"
    assert product.price == 5000.0
    assert product.quantity == 3

def test_price(first_pr):
    assert first_pr.price == 150000.0

def test_set_price_right(first_pr):
    first_pr.price = 100
    assert first_pr.price == 100

def test_set_price_wrong(first_pr):
    first_pr.price = -50
    assert first_pr.price == 150000.0

def test_str_product(first_pr):
    assert str(first_pr) == "Ноутбук, 150000.0 руб. Остаток: 5 шт."

def test_str_category(first_ct):
    assert str(first_ct) == "Электроника, количество продуктов: 15 шт."

def test_add(first_pr,second_pr):
    assert first_pr + second_pr == 775000.0

def test_smartphone(first_sm):
    assert first_sm.name == "Samsung"
    assert first_sm.description == "Смартфон"
    assert first_sm.price == 50000.0
    assert first_sm.quantity == 2
    assert first_sm.efficiency == 5
    assert first_sm.model == "JA-700"
    assert first_sm.memory == 8
    assert first_sm.color == "gold"

def test_LawnGrass(first_lg):
    assert first_lg.name == "Газонная трава"
    assert first_lg.description == "Быстрорастущая"
    assert first_lg.price == 500.0
    assert first_lg.quantity == 20
    assert first_lg.country == "Россия"
    assert first_lg.germination_period == "7 дней"
    assert first_lg.color == "зелёный"

def test_add_with_if_product_wrong(first_sm, first_lg):
    with pytest.raises(TypeError):
        first_sm + first_lg

def test_add_with_if_product_right(first_sm, second_sm):
    assert first_sm + second_sm == 325000

def test_add_with_if_category_wrong(first_ct):
    with pytest.raises(TypeError):
        first_ct.add_product(5)



