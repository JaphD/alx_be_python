import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        #Set up the SimpleCalculator instance before each test
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(0,0), 0)
        self.assertEqual(self.calc.add(1000,2345), 3345)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(3,5), -2)
        self.assertEqual(self.calc.subtract(0,0), 0)
        self.assertEqual(self.calc.subtract(100,100), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,4), 12)
        self.assertEqual(self.calc.multiply(-2,5), -10)
        self.assertEqual(self.calc.multiply(0,1000), 0)
        self.assertEqual(self.calc.multiply(True,7), 7)

    def test_division(self):
        self.assertEqual(self.calc.divide(10,2), 5)
        self.assertEqual(self.calc.divide(-9,3), -3)
        self.assertEqual(self.calc.divide(0,5), 0)
        self.assertEqual(self.calc.divide(1000,500), 2)
        self.assertIsNone(self.calc.divide(5, 0))

        
if __name__ == "__main__":
    unittest.main()