from src.product import Product
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


def test_pr(first_pr):
    assert first_pr.name == "Ноутбук"
    assert first_pr.description == "Игровой ноутбук"
    assert first_pr.price == 150000.0
    assert first_pr.quantity == 5

def test_ct(first_ct):
    assert first_ct.name == "Электроника"
    assert first_ct.description == "Ноутбуки и аксессуары"
    assert len(first_ct.products) == 2
    assert first_ct.products[0].name == "Ноутбук"
    assert first_ct.products[1].name == "Мышь"

def test_count_ct(first_ct):
    assert Category.category_count == 1

def test_count_pr(first_ct):
    assert Category.product_count == 2