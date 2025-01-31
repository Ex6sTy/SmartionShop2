def test_category_iteration(sample_category):
    products = [p.name for p in sample_category]
    assert products == ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]
