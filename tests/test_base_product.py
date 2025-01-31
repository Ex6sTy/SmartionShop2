import pytest
from src.base_product import BaseProduct

def test_base_product_abstract_methods():
    """Проверка невозможности создания абстрактного класса."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test description", 100, 10)

