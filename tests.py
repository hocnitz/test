import unittest
from io import StringIO
import sys
from print_cat import print_cat
from utils import cat

class TestPrintCat(unittest.TestCase):
    def test_print_cat(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_cat()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), cat.strip())

if __name__ == '__main__':
    unittest.main()