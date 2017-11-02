from pyqybe.expressions import Ex
from pyqybe.oracle_query_builder import OracleQueryBuilder
from tests.pyqybe_test_case import PyQyBeTestCase


class TestOracleQueryBuilder(PyQyBeTestCase):
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

    def test_select_from(self):
        """Assert if query builder handles SELECT and FROM statements"""
        query_builder = OracleQueryBuilder()
        query_builder.select('foo').select('bar').\
            from_table('fooTable').from_table('barTable')
        expected = 'SELECT foo, bar FROM fooTable, barTable'
        actual = query_builder.plain_query

        self.assertEqual(expected, actual)

    def test_select_from_where(self):
        """Assert if query builder handlers SELECT FROM WHERE statements"""
        actual = OracleQueryBuilder().select('foo').from_table('bar').where(Ex({'fooValue': 'banana'})).plain_query
        expected = 'SELECT foo FROM bar WHERE fooValue == \'banana\''
        self.assertEqualQueries(expected, actual)