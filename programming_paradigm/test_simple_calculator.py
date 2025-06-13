import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
        def setUp(self):
            self.calc = SimpleCalculator()

        def test_addition(self):
            self.assertEqual(self.calc.add(2, 3), 5)
            self.assertEqual(self.calc.add(-1, 1), 0)
            self.assertEqual(self.calc.add(-1, -2), -3)

        def test_subtraction(self):
            self.assertEqual(self.calc.subtract(5, 3), 2)
            self.assertEqual(self.calc.subtract(2, 3), -1)
            self.assertEqual(self.calc.subtract(-1, -2), 1)
            self.assertEqual(self.calc.subtract(-1, 1), -2)
            self.assertEqual(self.calc.subtract(3, -2), 5)

        def test_multiplication(self):
            self.assertEqual(self.calc.multiply(5, 3), 15)
            self.assertEqual(self.calc.multiply(-1, -2), 2)
            self.assertEqual(self.calc.multiply(-1, 4), -4)
            self.assertEqual(self.calc.multiply(3, -2), -6)

        def test_division(self):
            self.assertEqual(self.calc.divide(6, 3), 2)
            self.assertEqual(self.calc.divide(-2, -1), 2)
            self.assertEqual(self.calc.divide(-4, 2), -2)
            self.assertEqual(self.calc.divide(6, -2), -3)
            self.assertEqual(self.calc.divide(4, 0), None)

