def test_creation_logger_mixin(capsys):
    product = Product("Test Product", "Test Description", 100.0, 10)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
