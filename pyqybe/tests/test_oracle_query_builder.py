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
        query_builder = self.query_builder
        expected = "SELECT 1 AS foo"
        actual = query_builder.select(foo=1).plain_query

        self.assertEqual(expected, actual)
