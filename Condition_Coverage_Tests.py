import Leap_Year as ly
import unittest



class Condition_Coverage(unittest.TestCase):
    #a is true; b is false; c is false
    def test1(self):
        self.assertTrue(ly.Leap_Year_condition(2004))
    #a is false; b is true; c is false
    def test2(self):
        self.assertFalse(ly.Leap_Year_condition(2001))
    #a is true, b is false; c is true
    def test3(self):
        self.assertTrue(ly.Leap_Year_condition(2000))
    #a is true; b is false; c is false
    def test4(self):
        self.assertFalse(ly.Leap_Year_condition(1900))
        
if __name__ == '__main__':
    unittest.main()