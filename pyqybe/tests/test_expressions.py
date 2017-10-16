import unittest

from pyqybe.expressions import Ex, ExOr


class TestExpressions(unittest.TestCase):
    def test_ex(self):
        expected = ['A == 1']
        actual = Ex({'A': 1})
        self.assertEqual(expected, actual)

    def test_ex_with_order(self):
        expected = ['(A == 1 AND B == 1 AND C == 1)']
        actual = Ex({'A': 1, 'B': 1, 'C': 1}, order=['A', 'B', 'C'])
        self.assertEqual(expected, actual)


class TestExOr(unittest.TestCase):
    def test_ex_or(self):
        expected = ['(A == 1 OR B == 2)']
        actual = ExOr({'A': 1, 'B': 2}, order=['A', 'B'])
        self.assertListEqual(expected, actual)

    def test_or_2(self):
        expected = ['(A == 1 OR B == 2)']
        actual = ExOr({'A': 1}, {'B': 2})
        self.assertListEqual(expected, actual)


class TestAndOr(unittest.TestCase):
    def test_and_or(self):
        expected = ['(A == 1 AND (B == 2 OR C == 3))']
        actual = Ex({'A': 1}, ExOr({'B': 2, 'C': 3}, order=['B', 'C']))
        self.assertListEqual(expected, actual)

    def test_and_or_2(self):
        expected = ['(A == 1 AND (B == 2 OR C == 3))']
        actual = Ex(Ex({'A': 1}), ExOr({'B': 2, 'C': 3}, order=['B', 'C']))
        self.assertListEqual(expected, actual)

    def test_and_or_3(self):
        expected = ['(A == 1 OR (B == 2 AND C == 3))']
        actual = ExOr({'A': 1}, Ex({'B': 2, 'C': 3}, order=['B', 'C']))
        self.assertListEqual(expected, actual)
