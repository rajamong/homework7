# imports unittest functionality
import unittest
# imports leapyear class from leapyear program
from leapyear import checkyear # type: ignore

class testCase(unittest.TestCase):
    def setUp(self):
        self.leap = leapyear()

    # tests the leap year checking functionality with a valid leap year
    def validyear(self):
        self.assertEqual(self.leap.checkyear(2020), (True))


if __name__ == "__main__":
    unittest.main()



