def test_lawngrass_initialization():
    lawn_grass = LawnGrass("Газонная трава", "Идеальная для садов", 1000.0, 20, "Россия", 7, "Зелёный")
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 7
    assert lawn_grass.color == "Зелёный"