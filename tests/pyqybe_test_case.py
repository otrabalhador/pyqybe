import unittest

from pyqybe.utils import clean_query


class PyQyBeTestCase(unittest.TestCase):
    def assertEqualQueries(self, first_query, second_query, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        first_query = clean_query(first_query)
        second_query = clean_query(second_query)
        assertion_func = self._getAssertEqualityFunc(first_query, second_query)
        assertion_func(first_query, second_query, msg=msg)
