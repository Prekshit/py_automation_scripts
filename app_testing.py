import unittest

class TestExample(unittest.TestCase):

    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = 5 - 2
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
