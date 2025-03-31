import unittest
from testing_completion import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 0)
        
    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)
        
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        
    def test_factorial_negative(self):
        with self.assertRaises(RecursionError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()