from pyqybe.expressions import Ex
from pyqybe.statements import Where
from pyqybe.tests.pyqybe_test_case import PyQyBeTestCase


class TestStatementWhere(PyQyBeTestCase):

    def test_select_from_where(self):
        """Assert if query builder handles SELECT and FROM statements"""
        scenarios = [
            {'expected': 'WHERE A == 1', 'elements': ('A == 1', )},
            {'expected': 'WHERE A == 1', 'elements': (Ex({'A': 1}),)},

            # {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',
            #  'elements': ('REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'', )},
            # {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',
            #  'elements': (Ex('REFERENCE_DAY').between('20170101', '20170731'),)},
            #
            # {'expected': 'WHERE A == 1 OR B == 1', 'elements': ('A == 1 OR B == 1', )},
            # {'expected': 'WHERE A == 1 OR B == 1', 'elements': (Ex(A).equal(1).EqOr(B).equal(1),)}
        ]
        for scenario in scenarios:

            elements = scenario['elements']
            expected = scenario['expected']

            statement = Where().add(*elements)
            actual = statement.parse()
            self.assertEqualQueries(expected, actual)
