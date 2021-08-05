"""Lambda Expressions

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Small anonymous functions can be created with the lambda keyword. Lambda functions can be used
wherever function objects are required. They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function definition. Like nested function
definitions, lambda functions can reference variables from the containing scope.
"""


def test_lambda_expressions():
    """Lambda Expressions"""

    def make_power_function(delta):
        """This example uses a lambda expression to return a function"""
        return lambda number: number ** delta

    power_function = make_power_function(2)

    assert power_function(0) == 0
    assert power_function(1) == 1
    assert power_function(2) == 4
    assert power_function(3) == 9

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = list(map(lambda x: x ** 2, numbers))
    assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
