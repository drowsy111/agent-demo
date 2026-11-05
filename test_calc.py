import unittest

from calc import add, multiply, safe_divide, factorial


class AddTests(unittest.TestCase):
    def test_add_positive(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self) -> None:
        self.assertEqual(add(-2, -3), -5)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)

    def test_safe_divide(self) -> None:
        self.assertEqual(safe_divide(10, 2), 5.0)
        # 期望：除以 0 时返回 0.0，而不是报错
        self.assertEqual(safe_divide(10, 0), 0.0)

    def test_factorial(self) -> None:
        self.assertEqual(factorial(5), 120)
        # 期望：负数或 0 的阶乘返回 1
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-3), 1)


if __name__ == "__main__":
    unittest.main()
