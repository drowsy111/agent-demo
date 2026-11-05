import unittest

from calc import add


class AddTests(unittest.TestCase):
    def test_add_positive(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self) -> None:
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
