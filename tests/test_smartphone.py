from src.smartphone import Smartphone

def test_smartphone_initialization():
    """Проверка инициализации класса Smartphone."""
    smartphone = Smartphone("iPhone 15", "Флагманский смартфон", 200000.0, 5, 95, "Pro Max", 256, "Silver")
    assert smartphone.name == "iPhone 15"
    assert smartphone.efficiency == 95
    assert smartphone.model == "Pro Max"
    assert smartphone.memory == 256
    assert smartphone.color == "Silver"
