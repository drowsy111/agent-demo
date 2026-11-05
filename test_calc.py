import unittest

from calc import add, multiply


class AddTests(unittest.TestCase):
    def test_add_positive(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self) -> None:
        self.assertEqual(add(-2, -3), -5)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)


if __name__ == "__main__":
    unittest.main()
