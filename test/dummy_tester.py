import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from src.app import Dummy
import unittest


class DummyTester(unittest.TestCase):
    def test_name (self):
        obj = Dummy(name = "Abir")
        self.assertEqual(obj.name,"abir")

if __name__ == '__main__':
    unittest.main()
