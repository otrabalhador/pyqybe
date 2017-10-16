import unittest

from pyqybe.expressions import Ex, ExOr


class TestExpressions(unittest.TestCase):
    def test_ex(self):
        expected = ['A == 1']
        actual = Ex({'A': 1})
        self.assertEqual(expected, actual)

    def test_ex_with_order(self):
        expected = ['A == 1', 'B == 1', 'C == 1']
        actual = Ex({'A': 1, 'B': 1, 'C': 1}, order=['A', 'B', 'C'])
        self.assertEqual(expected, actual)


class TestExOr(unittest.TestCase):
    def test_ex_or(self):
        expected = ['A == 1 OR B == 1']
        actual = ExOr({'A': 1, 'B': 1}, order=['A', 'B'])
        self.assertListEqual(expected, actual)
