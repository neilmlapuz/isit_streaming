import unittest
import sys
import os


class TestLookUp(unittest.TestCase):
    def test_command(self):
        result1 = os.system('python scripts/main.py -l spiderman > test.txt')
        # result2 = os.system('python scripts/main.py -l spiderman > test2.txt -r au,ca')

        self.assertTrue(result1 == 0 )

if __name__ == '__main__':
    unittest.main()