from src.product import Product
from src.category import Category


def main():
    # Примеры создания продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Пример создания категории
    category = Category(
        "Смартфоны",
        "Современные устройства для связи и развлечений",
        [product1, product2, product3],
    )

    # Вывод категории
    print(f"Категория: {category.name}")
    print(f"Описание: {category.description}")
    print(f"Количество продуктов: {len(category.products)}")

    # Вывод продуктов в категории
    print("\nСписок продуктов:")
    for product in category.products:
        print(f"- {product.name} ({product.price} руб.)")

    # Пример загрузки данных из JSON
    print("\nЗагрузка данных из файла JSON...")
    categories = Category.load_from_json("products.json")

    # Вывод категорий и продуктов из JSON
    for idx, category in enumerate(categories, start=1):
        print(f"\nКатегория {idx}: {category.name}")
        print(f"Описание: {category.description}")
        print("Продукты:")
        for product in category.products:
            print(f"- {product.name} ({product.price} руб., {product.quantity} шт.)")

    # Вывод глобальных счётчиков
    print(f"\nОбщее количество категорий: {Category.category_count}")
    print(f"Общее количество продуктов: {Category.product_count}")


if __name__ == "__main__":
    main()
