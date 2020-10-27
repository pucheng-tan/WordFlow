class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        y = "hello"
        assert hasattr(y, "check")

        # pytest .\PoC\services\test_api_service_classes.py