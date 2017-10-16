import unittest

from pyqybe.oracle_query_builder import OracleQueryBuilder


class TestOracleQueryBuilder(unittest.TestCase):
    def setUp(self):
        self.query_builder = OracleQueryBuilder()

    def test_should_return_empty_str(self):
        """ OracleQueryBuilder should return an empty string if OracleQueryBuilder has no argument """
        expected = ''
        actual = self.query_builder.query

        self.assertEqual(expected, actual)

    def test_should_select(self):
        scenarios = [
            {'expected': 'SELECT foo', 'args': ['foo']},
            {'expected': 'SELECT foo, bar', 'args': ['foo', 'bar']},
            {'expected': 'SELECT foo, bar, pip, pipitchu', 'args': ['foo', 'bar', 'pip', 'pipitchu']},
        ]
        for scenario in scenarios:
            query_builder = OracleQueryBuilder()

            args = list(scenario['args'])
            expected = str(scenario['expected'])

            actual = query_builder.select(*args).plain_query
            self.assertEqual(expected, actual)

    def test_can_select_more_than_one_time(self):
        query_builder = OracleQueryBuilder()
        query_builder.select('foo').select('bar').select('pip')
        expected = 'SELECT foo, bar, pip'
        actual = query_builder.plain_query

        self.assertEqual(expected, actual)
