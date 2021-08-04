"""Default Argument Values

@see: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

The most useful form is to specify a default value for one or more arguments. This creates a
function that can be called with fewer arguments than it is defined to allow.
"""


def range_sum(number1, number2 = 100):
    """ returns the sum of all the numbers between two numbers or 1 number passed and 100.

    You may notice that by default the second number if 100.
    """
    if number1 > number2:
        temp=number2
        number2 = number1
        number1 = temp
        
    sum1 = 0
    for i in range(number1,number2+1):
        sum1 += i
    
    return sum1


def test_default_function_arguments():
    """Test default function arguments"""

    # This function power_of can be called in several ways because it has default value for
    # the second argument. First we may call it omitting the second argument at all.
    assert range_sum(98) == 297
    assert range_sum(102) == 303
    # We may also want to override the second argument by using the following function calls.
    assert range_sum(5, 10) == 45
