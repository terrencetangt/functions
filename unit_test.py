#https://www.coursera.org/learn/python-operating-system/supplement/3WDVq/unit-test-cheat-sheet
#https://docs.python.org/3/library/unittest.html#



import unittest
from function import palindrome




class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "1001"
        expected = True
        self.assertEqual(palindrome(testcase), expected)

unittest.main()
