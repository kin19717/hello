import unittest
from ModuleA_q1 import is_prime
from ModuleA_q2 import is_composite
from ModuleA_q2 import count_is_composite


class Primestestcases(unittest.TestCase):

    def test_negative_number(self):
    	self.assertFalse(is_prime(-1))
    	self.assertFalse(is_prime(-2))
    	self.assertFalse(is_composite(-1))
    	self.assertFalse(is_composite(-2))
    
    def test_is_zero_not_prime_or_composite(self):
    	self.assertFalse(is_prime(0))
    	self.assertFalse(is_composite(0))

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5), msg='Five is prime')

    def test_is_ten_non_prime(self):
        self.assertFalse(is_prime(10), msg='Ten is not prime')
    
    def test_is_five_non_composite(self):
        self.assertFalse(is_composite(5), msg='Five is no composite')

    def test_is_ten_composite(self):
        self.assertTrue(is_composite(10), msg='Ten is composite')

    def test_count_composite_numbers_in_a_range(self):
        self.assertEqual(count_is_composite(10), '5', "Should be 5")

    def test_count_composite_numbers_in_a_range(self):
        self.assertEqual(count_is_composite(100000), '90407', "Should be 90407") 

# Expected to be wrong in this case
#    def test_count_composite_numbers_in_a_range(self):
#        self.assertEqual(count_is_composite(100), '72', "Should be 73")

if __name__ == '__main__':
    unittest.main()