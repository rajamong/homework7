# imports unittest functionality
import unittest
# imports leapyear class from leapyear program
from leapyear import leapyear 

class testCase(unittest.TestCase):
    # tests the leap year checking functionality with a valid leap year
    def validyear(self):
        for year in [2020]:
            assert leapyear(year) == 'True'

    # tests the leap year checking functionality with an invalid leap year
    def invalidyear(self):
        for year in [2019]:
            assert leapyear(year) == 'False'


if __name__ == "__main__":
    unittest.main()



