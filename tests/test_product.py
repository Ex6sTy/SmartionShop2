import pytest
from src.product import Product

def test_product_initialization():
    """Проверка корректного создания продукта."""
    product = Product("iPhone 15", "Флагманский смартфон", 200000.0, 5)
    assert product.name == "iPhone 15"
    assert product.description == "Флагманский смартфон"
    assert product.price == 200000.0
    assert product.quantity == 5

def test_product_string_representation():
    """Проверка строкового представления продукта."""
    product = Product("MacBook Pro", "Ноутбук Apple", 300000.0, 3)
    assert str(product) == "MacBook Pro, 300000.0 руб. Остаток: 3 шт."

def test_product_negative_price():
    """Проверка выброса исключения при отрицательной цене."""
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        Product("Xiaomi", "Смартфон", -10000, 10)

def test_product_zero_quantity():
    """Проверка выброса исключения при нулевом количестве."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Apple Watch", "Умные часы", 50000.0, 0)

def test_product_price_setter_positive():
    """Проверка изменения цены через сеттер."""
    product = Product("Sony Headphones", "Беспроводные наушники", 20000.0, 7)
    product.price = 25000.0
    assert product.price == 25000.0

def test_product_price_setter_negative():
    """Проверка невозможности установки отрицательной цены."""
    product = Product("iPad", "Планшет Apple", 100000.0, 4)
    product.price = -50000.0
    assert product.price == 100000.0  # Цена не должна была измениться

def test_product_total_value():
    """Проверка расчёта общей стоимости товаров."""
    product = Product("iPhone 15", "Флагманский смартфон", 200000.0, 3)
    assert product.get_total_value() == 600000.0

def test_product_addition():
    """Проверка сложения стоимости двух продуктов."""
    product1 = Product("Samsung", "Смартфон", 100000.0, 3)
    product2 = Product("Xiaomi", "Смартфон", 80000.0, 2)
    assert product1 + product2 == 440000.0  # (100000 * 3 + 80000 * 2)

def test_price_negative():
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        Product("Test Product", "Description", -100, 10)

def test_price_reduction_with_confirmation(monkeypatch):
    product = Product("Test Product", "Description", 100, 10)

    # Симулируем согласие на изменение цены
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 50
    assert product.price == 50

    # Симулируем отказ от изменения цены
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 30
    assert product.price == 50  # Цена не изменилась