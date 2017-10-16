import unittest

from pyqybe.exceptions import InvalidOperator
from pyqybe.operators import (
    Operator,
    OperatorParser,
    EQUAL_OPERATOR_STR,
    BIGGER_OPERATOR_STR,
    BIGGER_OR_EQUAL_OPERATOR_STR,
    SMALLER_OPERATOR_STR,
    SMALLER_OR_EQUAL_OPERATOR_STR,
    DIFFERENT_OPERATOR_STR,
    IN_OPERATOR_STR,
    LIKE_OPERATOR_STR,
    BETWEEN_OPERATOR_STR,
)


class TestOperators(unittest.TestCase):
    def test_like_operator(self):
        expected = LIKE_OPERATOR_STR, '%WORKER%'
        actual = Operator.like('%WORKER%')
        self.assertEqual(expected, actual)

    def test_equal_operator(self):
        expected = EQUAL_OPERATOR_STR, 'Uberaba'
        actual = Operator.equal('Uberaba')
        self.assertEqual(expected, actual)

    def test_between_operator(self):
        expected = BETWEEN_OPERATOR_STR, ('20170701', '20170731')
        actual = Operator.between('20170701', '20170731')
        self.assertEqual(expected, actual)

    def test_in_operator_single_element_provided(self):
        expected = IN_OPERATOR_STR, ['BRAZIL']
        actual = Operator.in_operator('BRAZIL')
        self.assertEqual(expected, actual)

    def test_in_operator_args_provided(self):
        expected = IN_OPERATOR_STR, ['BRAZIL', 'NETHERLANDS', 'FINLAND']
        actual = Operator.in_operator('BRAZIL', 'NETHERLANDS', 'FINLAND')
        self.assertEqual(expected, actual)

    def test_in_operator_list_provided(self):
        expected = IN_OPERATOR_STR, ['BRAZIL', 'NETHERLANDS', 'FINLAND']
        actual = Operator.in_operator(['BRAZIL', 'NETHERLANDS', 'FINLAND'])
        self.assertEqual(expected, actual)


class TestOperatorParser(unittest.TestCase):
    def test_equal_operator_parser(self):
        expected = 'CITY == \'Uberaba\''
        actual = OperatorParser(EQUAL_OPERATOR_STR).parse('CITY', 'Uberaba')
        self.assertEqual(expected, actual)

    def test_in_operator_parser(self):
        expected = 'COUNTRY IN (\'BRAZIL\', \'NETHERLANDS\', \'FINLAND\')'
        actual = OperatorParser(IN_OPERATOR_STR).parse('COUNTRY', ['BRAZIL', 'NETHERLANDS', 'FINLAND'])
        self.assertEqual(expected, actual)

    def test_like_operator_parser(self):
        expected = 'NAME LIKE \'%WORKER%\''
        actual = OperatorParser(LIKE_OPERATOR_STR).parse('NAME', '%WORKER%')
        self.assertEqual(expected, actual)

    def test_between_operator_parser(self):
        expected = 'REFERENCE_DATE BETWEEN \'20170701\' AND \'20170731\''
        actual = OperatorParser(BETWEEN_OPERATOR_STR).parse('REFERENCE_DATE', ('20170701', '20170731'))
        self.assertEqual(expected, actual)


class TestOperatorSniffer(unittest.TestCase):
    def test_should_sniff_single_argument(self):
        expected = EQUAL_OPERATOR_STR, 1
        actual = Operator().sniff(1)
        self.assertEqual(expected, actual)

    def test_should_sniff_list(self):
        expected = IN_OPERATOR_STR, [1, 2]
        actual = Operator().sniff([1, 2])
        self.assertEqual(expected, actual)

    def test_should_sniff_tuple(self):
        expected = IN_OPERATOR_STR, [1, 2]
        actual = Operator().sniff(1, 2)
        self.assertEqual(expected, actual)

    def test_should_sniff_operator(self):
        scenarios = [
            {'expected': (EQUAL_OPERATOR_STR, 1,), 'call_args': Operator.equal(1)},
            {'expected': (BIGGER_OPERATOR_STR, 1,), 'call_args': Operator.bigger(1)},
            {'expected': (BIGGER_OR_EQUAL_OPERATOR_STR, 1,), 'call_args': Operator.bigger_or_equal(1)},
            {'expected': (SMALLER_OPERATOR_STR, 1,), 'call_args': Operator.smaller(1)},
            {'expected': (SMALLER_OR_EQUAL_OPERATOR_STR, 1,), 'call_args': Operator.smaller_or_equal(1)},
            {'expected': (DIFFERENT_OPERATOR_STR, 1,), 'call_args': Operator.different(1)},
            {'expected': (IN_OPERATOR_STR, [1, 2, 3],), 'call_args': Operator.in_operator(1, 2, 3)},
            {'expected': (IN_OPERATOR_STR, [1, 2, 3],), 'call_args': Operator.in_operator([1, 2, 3])},
            {'expected': (LIKE_OPERATOR_STR, '%WORKA%',), 'call_args': Operator.like('%WORKA%')},
            {'expected': (BETWEEN_OPERATOR_STR, ('20170701', '20170731',),),
             'call_args': Operator.between('20170701', '20170731')},
        ]
        for scenario in scenarios:
            expected = scenario['expected']
            call_args = scenario['call_args']
            actual = Operator.sniff(call_args)
            self.assertEqual(expected, actual)

    def test_should_sniff_raise_exception(self):
        invalid_call_args = [
            (('type', 1),),  # Invalid type
        ]
        for invalid_call_arg in invalid_call_args:
            with self.assertRaises(InvalidOperator):
                Operator.sniff(invalid_call_arg)
