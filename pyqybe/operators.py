class Operators:
    def equal(self, column, value):
        return '{} == {}'.format(
            column,
            self.parse_type(value)
        )

    def between(self, arg1, arg2):

        return '{} BETWEEN {} AND {}'.format(
            self.column,
            self.parse_type(arg1),
            self.parse_type(arg2)
        )

    @staticmethod
    def parse_type(value):
        if isinstance(value, str):
            return '\'{}\''.format(value)

        return value
