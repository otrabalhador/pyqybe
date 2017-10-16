from pyqybe.operators import Operators


class Expression(list):
    def __init__(self, *expressions, order=None, join_str):
        super().__init__()
        self._expressions = []
        self.join_str = join_str
        self.parse_expressions(*expressions, order=order)

    def parse_expressions(self, *expressions, order):
        equations = []
        for expression in expressions:

            if isinstance(expression, list):
                equations.extend(expression)

            else:
                if not order:
                    order = expression.keys()

                for column in order:
                    operator, value = Operators().equal, expression[column]
                    equations.append(operator(column, value))

                order = None

        self.extend(equations)

        return self

    def extend(self, equations):
        self_contain = True if len(equations) > 1 else False

        formatted_equation = self.join_str.join(equations)
        if self_contain:
            formatted_equation = '({})'.format(formatted_equation)

        super().append(formatted_equation)


class Ex(Expression):
    JOIN_STR = ' AND '

    def __init__(self, *expressions, order=None):
        super().__init__(*expressions, order=order, join_str=self.JOIN_STR)


class ExOr(Expression):
    JOIN_STR = ' OR '

    def __init__(self, *expressions, order=None):
        super().__init__(*expressions, order=order, join_str=self.JOIN_STR)
