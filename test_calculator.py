import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) 

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_subtract_postitive(self):
        self.assertEqual(self.calc.subtract(2,2), 0)
    
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-2,-2), 0)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3,3), 9)

    def test_multiplt_negative(self):
        self.assertEqual(self.calc.multiply(-3,3),-9)

    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(4,4), 1)

    def test_divide_positive02(self):
        self.assertEqual(self.calc.divide(2,1), 2)

    def test_modulo_positive01(self):
        self.assertEqual(self.calc.modulo(3,2), 1)
        
    def test_modulo_positive02(self):
        self.assertEqual(self.calc.modulo(4,2), 0)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()