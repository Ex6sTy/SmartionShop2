from src.product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)  # Вызов конструктора родителя должен идти ПОСЛЕ

    def __str__(self):
        return (
            f"{self.name} ({self.country}), срок прорастания: {self.germination_period} дней, "
            f"цвет: {self.color}, {self.price} руб. Остаток: {self.quantity} шт."
        )
