from pyqybe.expressions import Ex, ExOr
from pyqybe.operators import Operator as op
from pyqybe.statements import Where
from tests.pyqybe_test_case import PyQyBeTestCase


class TestStatementWhere(PyQyBeTestCase):
    def test_select_from_where(self):
        """Asserts Statement object Where"""
        scenarios = [
            {'expected': 'WHERE A == 1', 'elements': ('A == 1',)},
            {'expected': 'WHERE A == 1', 'elements': (Ex({'A': 1}),)},
            {'expected': 'WHERE A == 1', 'elements': (Ex({'A': op.equal(1)}),)},
            {'expected': 'WHERE A > 1', 'elements': (Ex({'A': op.bigger(1)}),)},
            {'expected': 'WHERE A >= 1', 'elements': (Ex({'A': op.bigger_or_equal(1)}),)},
            {'expected': 'WHERE A < 1', 'elements': (Ex({'A': op.smaller(1)}),)},
            {'expected': 'WHERE A <= 1', 'elements': (Ex({'A': op.smaller_or_equal(1)}),)},
            {'expected': 'WHERE A <> 1', 'elements': (Ex({'A': op.different(1)}),)},

            {'expected': 'WHERE DAY IN (20, 30, 40)', 'elements': (Ex({'DAY': [20, 30, 40]}),)},
            {'expected': 'WHERE DAY IN (20, 30, 40)', 'elements': (Ex({'DAY': op.in_operator([20, 30, 40])}),)},
            {'expected': 'WHERE DAY IN (\'20\', \'30\', \'40\')', 'elements': (Ex({'DAY': ['20', '30', '40']}),)},

            {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',
             'elements': ('REFERENCE_DAY BETWEEN \'20170101\' AND \'20170731\'',)},
            {'expected': 'WHERE REFERENCE_DAY BETWEEN \'20170701\' AND \'20170731\'',
             'elements': (Ex({'REFERENCE_DAY': op.between('20170701', '20170731')}),)},

            {'expected': 'WHERE A == 1 OR B == 1', 'elements': ('A == 1 OR B == 1',)},
            {'expected': 'WHERE (A == 1 OR B == 1)', 'elements': (ExOr({'A': 1, 'B': 1}, order=['A', 'B']),)},
            {'expected': 'WHERE (A == 1 AND (B == 2 OR C == 3))',
             'elements': (Ex(Ex({'A': 1}), ExOr({'B': 2, 'C': 3}, order=['B', 'C'])),)},

            {'expected': 'WHERE A == 1 AND B == 2', 'elements': (Ex({'A': 1}).add(Ex({'B': 2})),)},
            {'expected': 'WHERE A == 1 AND B == 2', 'elements': (Ex({'A': 1}) + Ex({'B': 2}),)}
        ]
        for scenario in scenarios:
            elements = scenario['elements']
            expected = scenario['expected']

            statement = Where().add(*elements)
            actual = statement.parse()
            self.assertEqualQueries(expected, actual)
