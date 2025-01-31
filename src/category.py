import json
import os
from itertools import product

from src.product import Product
from src.category_iterator import CategoryIterator

class ZeroQuantityError(Exception):
    """
    Исключенние для обработки попытки добавить товар с нулевым количеством.
    """
    pass


class Category:
    """
    Класс для описания категории продуктов.
    """

    # Глобальные счётчики
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список объектов Product
        """
        self.name = name
        self.description = description
        self.__products = [] # Приватный список продуктов
        Category.category_count += 1

    def __str__(self):
        """
        Строковое представление категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        """
        Возвращает итератор для продуктов категории.
        """
        return CategoryIterator(self)

    @staticmethod
    def load_from_json(file_path):
        Category.category_count = 0
        Category.product_count = 0  # 🔄 Сбрасываем счётчики перед загрузкой

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        categories = []
        for category_data in data["categories"]:
            category = Category(category_data["name"], category_data["description"])
            for product_data in category_data["products"]:
                product = Product(
                    product_data["name"],
                    product_data["description"],
                    product_data["price"],
                    product_data["quantity"],
                )
                category.add_product(product)
            categories.append(category)

        print(f"Загружено продуктов: {Category.product_count}")  # DEBUG
        return categories

    def add_product(self, product):
        """Добавляет продукт в категорию."""
        try:
            if product.quantity == 0:
                raise ZeroQuantityError(f"Товар {product.name} с нулевым количеством не может быть добавлен.")
        except ZeroQuantityError as e:
            print(e)
        else:
            if not isinstance(product, Product):
                raise TypeError("Добавлять можно только объекты класса Product или его наследников.")
            self.__products.append(product)
            Category.product_count += product.quantity
        finally:
            print(f"Category.product_count после добавления: {Category.product_count}")
            print("Обработка добавления товара завершена.")

    @property
    def products(self):
        """
        Возвращает строку со всеми продуктами в категории.
        """
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def get_product_objects(self):
        """
        Возвращает список объектов продуктов.
        """
        return self.__products

    def __str__(self):
        """
        Строковое представление категории.
        """
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."

    def calculate_average_price(self):
        """
        Подсчитывает среднюю цену товаров в категории.
        """
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0


# if __name__ == "__main__":
#     # Определяем путь к JSON-файлу
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, "../products.json")
#
#     try:
#         # Загружаем категории из файла
#         categories = Category.load_from_json(file_path)
#         print("Категории успешно загружены!")
#
#         # Вывод категорий и продуктов
#         for idx, category in enumerate(categories, start=1):
#             print(f"\nКатегория {idx}: {category.name}")
#             print(f"Описание: {category.description}")
#             print("Продукты:")
#             for product in category.products:
#                 print(f"- {product.name} ({product.price} руб., {product.quantity} шт.)")
#
#         # Вывод глобальных счётчиков
#         print(f"\nОбщее количество категорий: {Category.category_count}")
#         print(f"Общее количество продуктов: {Category.product_count}")
#
#     except FileNotFoundError as e:
#         print(e)
#     except json.JSONDecodeError as e:
#         print(f"Ошибка чтения JSON-файла: {e}")
#     except Exception as e:
#         print(f"Неожиданная ошибка: {e}")
#