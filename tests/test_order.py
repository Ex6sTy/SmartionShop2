from src.order import Order
from src.product import Product

def test_order_creation():
    """Проверка создания заказа."""
    product = Product("MacBook", "Ноутбук Apple", 200000.0, 3)
    order = Order(product, 2)
    assert order.calculate_total() == 400000.0
    assert str(order) == "Заказ: MacBook, Количество: 2, Итоговая стоимость: 400000.0 руб."
