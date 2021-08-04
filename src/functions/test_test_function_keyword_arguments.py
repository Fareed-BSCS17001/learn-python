"""Keyword Arguments

@see: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

Functions can be called using keyword arguments of the form kwarg=value.
"""

import pytest


def num_sum(number1, number2 = 10, number3 = 50, number4 = 100):
    """Example of multi-argument function

    This function accepts one required argument (number1) and three optional arguments
    (number2, number3, number4).
    """

    
    return number1 + number2 + number3 + number4


def test_function_keyword_arguments():
    """Test calling function with specifying keyword arguments"""


    sum1 = 5 + 10 + 50 + 100
    # 1 positional argument
    assert num_sum(5) == sum1
    # 1 keyword argument
    assert num_sum(number1 = 1000) == 1000 +10 + 50 + 100

 
    sum2 = 100 + 10 + 50 + 1000
    # 2 keyword arguments
    assert num_sum(number1 = 100, number4 = 1000) == sum2
    # 2 keyword arguments
    assert num_sum(number4 = 1000, number1 = 100) == sum2



    # When a final formal parameter of the form **name is present, it receives a dictionary
    # containing all keyword arguments except for those corresponding to a formal parameter.
    # This may be combined with a formal parameter of the form *name which receives a tuple
    # containing the positional arguments beyond the formal parameter list.
    # (*name must occur before **name.) For example, if we define a function like this:
    
    def test_sum(first_param, *arguments, **keywords):
        """This function accepts its arguments through "arguments" tuple amd keywords dictionary."""
        assert first_param == 100
        assert arguments == (50, 10)
        assert keywords == {
            'fourth_param_name': 20,
            'fifth_param_name': 20
        }
        return first_param + arguments[0] + arguments[1] + keywords['fourth_param_name'] + keywords['fifth_param_name']

    assert test_sum(
        100,
        50,
        10,
        fourth_param_name=20,
        fifth_param_name=20,
    ) == 100 + 50 + 10 + 20 + 20
