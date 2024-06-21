"""Arbitrary Argument Lists

@see: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

Function can be called with an arbitrary number of arguments. These arguments will be wrapped up in
a tuple. Before the variable number of arguments, zero or more normal arguments may occur.
"""


def test_function_arbitrary_arguments():
    """Arbitrary Argument Lists"""

    def test_function(first_param, *arguments):
        """This function accepts its arguments through "arguments" tuple amd keywords dictionary."""
        assert first_param == 1
        assert arguments == (2, 3, 4)

    test_function(1, 2, 3, 4)

    # Normally, these variadic arguments will be last in the list of formal parameters, because
    # they scoop up all remaining input arguments that are passed to the function. Any formal
    # parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that
    # they can only be used as keywords rather than positional arguments.
    def concat(*args, sep='\t'):
        return sep.join(args)

    assert concat('earth', 'mars', 'venus') == 'earth\tmars\tvenus'
    assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'
