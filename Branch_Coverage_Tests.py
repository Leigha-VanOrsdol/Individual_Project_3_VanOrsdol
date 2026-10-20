import Leap_Year as ly
import unittest
#Does not test every value that could be true or false, just the branch as a whole
class Branch_Coverage(unittest.TestCase):
    #Whole statement is true
    def test1(self):
        self.assertTrue(ly.Leap_Year(2004))
    #Whole statement is false
    def test2(self):
        self.assertFalse(ly.Leap_Year(2001))
if __name__ == '__main__':
    unittest.main()