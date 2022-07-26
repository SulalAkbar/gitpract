import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(-1,-1),-2)
        print("Testing ....")
        print("Testing Again ....")
        print("Testing Again and Again ....")
        print("Changes made on local repository .....")


if __name__ == '__main__':
    unittest.main()
