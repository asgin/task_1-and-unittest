import unittest
from ts import reverse_non_symbols
class TestAnagr(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_non_symbols('abcd efgh'), 'dcba hgfe', 'false')
    def test_2(self):
        self.assertEqual(reverse_non_symbols('a1bcd efg!h'), 'd1cba hgf!e', 'false')
    def test_3(self):
        self.assertEqual(reverse_non_symbols('123'), '123', 'false')
if __name__ == '__main__':
    unittest.main()