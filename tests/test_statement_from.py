import unittest
from pyqybe.statements import From
from pyqybe.utils import clean_query


class TestFromStatement(unittest.TestCase):
    def test_from_table(self):
        scenarios = [('foo',), ('foo', 'bar',)]
        for scenario in scenarios:
            expected = clean_query('FROM ' + ', '.join(scenario))
            statement = From(*scenario)
            actual = clean_query(statement.parse())

            self.assertEqual(expected, actual)

    def test_from_table_add(self):
        statement = From().add('foo').add('bar').add('pip')
        actual = clean_query(statement.parse())
        expected = clean_query('FROM foo, bar, pip')
        self.assertEqual(expected, actual)
