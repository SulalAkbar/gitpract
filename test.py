import unittest

#Doing some changes .......
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 4)), 6, "Should be 6")


print("Added New Feature to test github/ Checking for conflict")

if __name__ == '__main__':
    unittest.main()