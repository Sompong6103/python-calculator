import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_01(self):
        self.assertEqual(self.calc.add(5, -1), 4)

    def test_add_02(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract_01(self):
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtract_02(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_multiply_01(self):
        self.assertEqual(self.calc.multiply(8, 8), 64)

    def test_multiply_02(self):
        self.assertEqual(self.calc.multiply(3, -1), -3)

    def test_divide_01(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_02(self):
        self.assertEqual(self.calc.divide(-2, -2), 1)

    def test_divide_03(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_modulo_01(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_02(self):
        self.assertEqual(self.calc.modulo(100, 2), 0)

if __name__ == '__main__':
    unittest.main()