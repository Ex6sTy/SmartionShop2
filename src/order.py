from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """
    Абстрактный базовый класс для сущностей, связанных с магазином
    """

    @abstractmethod
    def calculate_total(self):
        pass


class Order(BaseEntity):
    """
    Класс для описания заказа.
    """

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.calculate_total()} руб."