import unittest
from unittest import TestCase

from Adder import Adder


class TestAdder(TestCase):
    def test_result(self):
        a = 10
        b = 20
        r = Adder(a, b).result()
        self.assertEqual(r, 30)


if __name__ == '__main__':
    unittest.main()
