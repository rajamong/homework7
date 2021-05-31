# imports the unittest functionality
import unittest
# import fizzbuzz function from fizzbuzz class
from fizzbuzz import fizzbuzz # type: ignore


class testCase(unittest.TestCase):
    # tests the functionality of the fizz,
    # ensures it prints fizz for values that
    # are evenly divisible by 3
    def testfizz(self):
        for number in [3, 12, 21]:
            assert fizzbuzz(number) == 'Fizz'

    # tests the functionality of the buzz,
    # ensures it prints buzz for values that
    # are evenly divisible by 5
    def testbuzz(self):
        for number in [5, 50, 100]:
            assert fizzbuzz(number) == 'Buzz'


if __name__ == "__main__":
    unittest.main()