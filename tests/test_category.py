import pytest
from src.category import Category
from src.product import Product

def test_category_initialization():
    """Проверка создания категории."""
    category = Category("Смартфоны", "Мобильные устройства", [])
    assert category.name == "Смартфоны"
    assert category.description == "Мобильные устройства"
    assert len(category.get_product_objects()) == 0

def test_category_add_product():
    """Добавление продукта в категорию."""
    category = Category("Гаджеты", "Умные устройства", [])
    product = Product("Apple Watch", "Умные часы", 50000.0, 5)
    category.add_product(product)
    assert len(category.get_product_objects()) == 1

def test_category_add_invalid_product():
    """Попытка добавить некорректный объект в категорию."""
    category = Category("Гаджеты", "Умные устройства", [])
    with pytest.raises(TypeError, match="Добавлять можно только объекты класса Product или его наследников."):
        category.add_product("Invalid Product")

def test_category_str_representation():
    """Проверка строкового представления категории."""
    category = Category("Компьютеры", "Ноутбуки и ПК", [])
    assert str(category) == "Компьютеры, количество продуктов: 0 шт."

def test_calculate_average_price():
    """Проверка расчёта средней цены в категории."""
    category = Category("Ноутбуки", "Офисные и игровые", [])
    category.add_product(Product("MacBook", "Apple", 150000.0, 1))
    category.add_product(Product("Asus", "Игровой", 100000.0, 1))
    assert category.calculate_average_price() == 125000.0

def test_calculate_average_price_empty_category():
    """Проверка средней цены для пустой категории."""
    category = Category("Гаджеты", "Умные устройства", [])
    assert category.calculate_average_price() == 0

