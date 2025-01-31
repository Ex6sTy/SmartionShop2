from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return (
            f"{self.name} ({self.model}), {self.memory}GB, {self.color}, "
            f"{self.price} руб. Остаток: {self.quantity} шт."
        )