import sys
sys.path.append('../')

from src.app import Dummy
import unittest


class DummyTester(unittest.TestCase):
    def test_name (self):
        obj = Dummy(name = "Abir")
        self.assertEqual(obj.name,"Abir")

if __name__ == '__main__':
    unittest.main()
