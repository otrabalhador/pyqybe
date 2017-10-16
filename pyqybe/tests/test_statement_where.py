import unittest
from pyqybe.statements import Where
from pyqybe.expressions import Eq
from pyqybe.utils import clean_query


class TestStatementWhere(unittest.TestCase):
    def assertEqualQueries(self, first, second, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        first = clean_query(first)
        second = clean_query(second)
        assertion_func = self._getAssertEqualityFunc(first, second)
        assertion_func(first, second, msg=msg)

    def test_select_from_where(self):
        """Assert if query builder handles SELECT and FROM statements"""
        scenarios = [
            {'expected': 'WHERE A == 1', 'elements': ('A == 1', )},
            {'expected': 'WHERE A == 1', 'elements': (Eq('A').equal(1),)},
            {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',
             'elements': ('REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'', )},
            {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',
             'elements': (Eq('REFERENCE_DAY').between('20170101', '20170731'), )}
        ]
        for scenario in scenarios:

            elements = scenario['elements']
            expected = scenario['expected']

            statement = Where().add(*elements)
            actual = statement.parse()
            self.assertEqualQueries(expected, actual)
