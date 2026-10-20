import Leap_Year as ly
import unittest

#never tests if year is less than 0
class Statement_Coverage(unittest.TestCase):
    #True at divisible by 4, skip rest of statement
    def test_1_3(self):
        self.assertTrue(ly.Leap_Year(2004))
    #False at divisible by 4, false at divisible by 400
    def test_1_4(self):
        self.assertFalse(ly.Leap_Year(2001))
if __name__ == '__main__':
    unittest.main()