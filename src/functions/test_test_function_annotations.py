"""Function Annotations.

@see: https://docs.python.org/3/tutorial/controlflow.html#function-annotations

Function annotations are completely optional metadata information about the types used
by user-defined functions.

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no
effect on any other part of the function. Parameter annotations are defined by a colon after the
parameter name, followed by an expression evaluating to the value of the annotation. Return
annotations are defined by a literal ->, followed by an expression, between the parameter list and
the colon denoting the end of the def statement.
"""


def Sum_cal(num1: float, num2: float = 5.0) -> float:
    """Sum calculator

    This function has a positional argument, a keyword argument, and the return value annotated.
    """
    return num1 + num2


def test_function_annotations():
    """Function Annotations."""

    assert Sum_cal.__annotations__ == {'num1': float, 'num2': float, 'return': float}
