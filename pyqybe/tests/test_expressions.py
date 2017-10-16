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
    def test_and_or_combination(self):
        expected = ['(A == 1 AND (B == 2 OR C == 3))']
        actual = Ex({'A': 1}, ExOr({'B': 2, 'C': 3}, order=['B', 'C']))
        self.assertListEqual(expected, actual)

    def test_and_or_combination_2(self):
        expected = ['(A == 1 AND (B == 2 OR C == 3))']
        actual = Ex(Ex({'A': 1}), ExOr({'B': 2, 'C': 3}, order=['B', 'C']))
        self.assertListEqual(expected, actual)

    def test_or_and_combination(self):
        expected = ['(A == 1 OR (B == 2 AND C == 3))']
        actual = ExOr({'A': 1}, Ex({'B': 2, 'C': 3}, order=['B', 'C']))
        self.assertListEqual(expected, actual)

    def test_deep_nested(self):
        expected = ['(A == 1 AND (B == 2 AND (C == 3 OR D == 4 OR (E == 5 OR F == 6))))']
        actual = Ex({'A': 1},
                    Ex({'B': 2},
                       ExOr({'C': 3, 'D': 4},
                            ExOr({'E': 5, 'F': 6}, order=['E', 'F']),
                            order=['C', 'D']
                            )
                       )
                    )
        self.assertListEqual(expected, actual)


class TestExpressionMultipleCalls(unittest.TestCase):
    def test_multiple_calls(self):
        expected = ['A == 1', 'B == 1']
        actual = Ex({'A': 1}).add(Ex({'B': 1}))
        self.assertListEqual(expected, actual)

    def test_multiple_calls_nested(self):
        expected = ['(A == 1 AND (B == 2 OR C == 3))', '(D == 1 OR E == 2)']
        actual = Ex({'A': 1}, ExOr({'B': 2, 'C': 3}, order=['B', 'C'])) \
            .add(ExOr({'D': 1, 'E': 2}, order=['D', 'E']))
        self.assertListEqual(expected, actual)


class TestSumExpressions(unittest.TestCase):
    def test_sum_expressions(self):
        expected = ['A == 1', 'B == 1']
        actual = Ex({'A': 1}) + Ex({'B': 1})
        self.assertListEqual(expected, actual)

    def test_sum_expressions_2(self):
        expected = ['(A == 1 AND (B == 2 OR C == 3))', '(D == 1 OR E == 2)']
        actual = Ex({'A': 1}, ExOr({'B': 2, 'C': 3}, order=['B', 'C'])) + ExOr({'D': 1, 'E': 2}, order=['D', 'E'])
        self.assertListEqual(expected, actual)
