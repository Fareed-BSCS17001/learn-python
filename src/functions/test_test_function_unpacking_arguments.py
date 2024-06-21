"""Unpacking Argument Lists

@see: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

Unpacking arguments may be executed via * and ** operators. See below for further details.
"""


def test_function_unpacking_arguments():
    """Unpacking Argument Lists"""

    # The situation may occur when the arguments are already in a list or tuple but need to be
    # unpacked for a function call requiring separate positional arguments.
    # if separate arguments are not available, write the function call with the *-operator to unpack the arguments out
    # of a list or tuple:

    def num_sum(firstnum, secondnum):
    	return firstnum+ secondnum
    	
    # Normal call with separate arguments:
    assert num_sum(3, 6) == 9

    # Call with arguments unpacked from a list.
    arguments_list = [3, 6]
    assert num_sum(*arguments_list) == 9

    # In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
    def num_function_that_receives_names_arguments(first_word, second_word):
        return first_word + second_word

    arguments_dictionary = {'first_word': 3, 'second_word': 9}
    assert num_function_that_receives_names_arguments(**arguments_dictionary) == 12
