import unittest

from pyqybe.statements import Statement
from pyqybe.utils import clean_query


class TestStatement(unittest.TestCase):
    def test_statement(self):
        statement = Statement('FROM', 'foo', 'bar').add('pip')
        expected = clean_query('FROM foo, bar, pip')
        actual = clean_query(statement.parse())

        self.assertEqual(expected, actual)

    def test_statement_with_sep(self):
        statement = Statement('FROM', 'foo', 'bar', sep=' AND').add('pip')
        expected = clean_query('FROM foo AND bar AND pip')
        actual = clean_query(statement.parse())

        self.assertEqual(expected, actual)

    def test_statement_empty(self):
        expected = ''
        actual = Statement().parse()
        self.assertEqual(expected, actual)
