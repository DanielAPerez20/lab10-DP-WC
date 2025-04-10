# git@github.com:DanielAPerez20/lab10-DP-WC.git
# Partner 1: William Crotty
# Partner 2: Daniel Perez



import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mult(4,2), 8)
        self.assertEqual(mult(3,2), 6)
        self.assertEqual(mult(4,4), 16)
        
        
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,4), 2)
        self.assertEqual(div(2,6), 3)
        self.assertEqual(div(2,12), 6)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 0)
  

    # def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertEqual(hypotenuse(30,40),50)

    # def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        
        self.assertEqual(square_root(4),2)
         #fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()