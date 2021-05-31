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

    # tests the functionality of the fizzbuzz,
    # ensures it prints fizzbuzz for values that
    # are evenly divisible by both 5 and 3
    def testfizzbuzz(self):
        for number in [15, 60, 75]:
            assert fizzbuzz(number) == 'FizzBuzz'


if __name__ == "__main__":
    unittest.main()