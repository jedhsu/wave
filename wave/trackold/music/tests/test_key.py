from ..key import Key


class TestKey:
    def test_init(self):
        key = Key.from_name("A")
        assert isinstance(key, Key)
        assert key == Key.from_name("A")

    def test_repr(self):
        key = Key.from_name("As")
        assert repr(key) == "A\u266f"

    def test_add(self):
        key = Key.from_name("A")
        assert key + 1 == Key.from_name("As")
        assert key + 7 == Key.from_name("E")
        assert key + 11 == Key.from_name("Gs")
