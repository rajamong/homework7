import unittest
import fizzbuzz 

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz, 'Fizz')


if __name__ == '__main__':
    unittest.main()