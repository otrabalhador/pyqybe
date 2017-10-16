import collections

from .components import (
    Select,
    Where,
    GroupBy,
    Having,
    OrderBy,
)
from .utils import clean_query


class OracleQueryBuilder:
    COMPONENT_ORDER = {
        1: Select,
        2: Where,
        3: GroupBy,
        4: Having,
        5: OrderBy
    }

    def __init__(self):
        self.components = {
            Select: [],
        }

    def __str__(self):
        return self.build_query()

    @property
    def query(self):
        return self.build_query()

    @property
    def plain_query(self):
        return clean_query(self.build_query())

    def select(self, *args):
        """
        This method will receive arguments and key arguments
        for columns and aliased for columns for the
        OracleQueryBuilder object
        :param args: Columns to select
            example:
                with the following arguments
                    args = FOO, BAR
                the parsed query will be
                    SELECT
                        FOO,
                        BAR

        :return: An OracleQueryBuilder object with the component SELECT
        """
        self.components[Select].extend(args)

        return self

    def from_table(self, *args):
        pass

    def build_query(self):
        query = ''
        ordered_components = collections.OrderedDict(sorted(self.COMPONENT_ORDER.items()))
        for _, component in ordered_components.items():
            query += component().parse(self.components.get(component))

        return query
