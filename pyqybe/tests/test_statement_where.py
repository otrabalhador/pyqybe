from pyqybe.expressions import Ex, ExOr
from pyqybe.statements import Where
from pyqybe.tests.pyqybe_test_case import PyQyBeTestCase


class TestStatementWhere(PyQyBeTestCase):
    def test_select_from_where(self):
        """Assert if query builder handles SELECT and FROM statements"""
        scenarios = [
            {'expected': 'WHERE A == 1', 'elements': ('A == 1',)},
            {'expected': 'WHERE A == 1', 'elements': (Ex({'A': 1}),)},

            # {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',
            #  'elements': ('REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'', )},
            # {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',
            #  'elements': (Ex('REFERENCE_DAY').between('20170101', '20170731'),)},
            #
            {'expected': 'WHERE A == 1 OR B == 1', 'elements': ('A == 1 OR B == 1',)},
            {'expected': 'WHERE (A == 1 OR B == 1)', 'elements': (ExOr({'A': 1, 'B': 1}, order=['A', 'B']),)},
            {'expected': 'WHERE (A == 1 AND (B == 2 OR C == 3))',
             'elements': (Ex(
                 Ex({'A': 1}),
                 ExOr({'B': 2, 'C': 3}, order=['B', 'C'])
             ),)},
        ]
        for scenario in scenarios:
            elements = scenario['elements']
            expected = scenario['expected']

            statement = Where().add(*elements)
            actual = statement.parse()
            self.assertEqualQueries(expected, actual)
