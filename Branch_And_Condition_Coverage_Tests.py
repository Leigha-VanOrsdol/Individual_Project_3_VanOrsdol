import Leap_Year as ly
import unittest

class BranchCondition_Coverage(unittest.TestCase):
    #a is true; b is true; c is false
    def test1(self):
        self.assertTrue(ly.Leap_Year_BranchCondition(2004))
    #a is false; b is true; c is false
    def test2(self):
        self.assertFalse(ly.Leap_Year_BranchCondition(2001))
    #a is true; b is false; c is false
    def test3(self):
        self.assertFalse(ly.Leap_Year_BranchCondition(1900))
        
if __name__ == '__main__':
    unittest.main()