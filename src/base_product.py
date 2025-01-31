from abc import ABC, abstractmethod


class BaseProduct(ABC):

    """
    Абстрактный базовый класс для всех продуктов
    """

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_total_value(self):
        """
        Абстрактный метод для получения общей стоимости продуктов на складе
        """
        pass

    def __str__(self):
        return f"{self.name}, {self.price} руб.Остаток: {self.quantity} шт."

