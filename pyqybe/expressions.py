from pyqybe.operators import Operators


class Expression(list):
    def __init__(self, expressions=None, order=None):
        super().__init__()
        self.parse_expression(expressions, order)

    def parse_expression(self, expressions, order):
        if not order:
            order = expressions.keys()

        equations = []
        for column in order:
            operator, value = Operators().equal, expressions[column]
            equations.append(operator(column, value))

        self.extend(equations)


class Ex(Expression):
    def __init__(self, expressions, order=None):
        super().__init__(expressions, order)


class ExOr(Expression):
    def __init__(self, expressions, order=None):
        super().__init__(expressions, order)

    def extend(self, equations):
        formatted_equation = ' OR '.join(equation for equation in equations)
        super().append(formatted_equation)
