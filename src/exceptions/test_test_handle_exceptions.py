"""Errors and Exceptions.

@see: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt
is made to execute it. Errors detected during execution are called exceptions and are not
unconditionally fatal.

It is possible to write programs that handle selected exceptions.
"""


def test_handle_exceptions():
    """Handling of exceptions

    The try statement works as follows.

    - First, the try clause (the statement(s) between the try and except keywords) is executed.

    - If no exception occurs, the except clause is skipped and execution of the try statement
    is finished.

    - If an exception occurs during execution of the try clause, the rest of the clause is skipped.
    Then if its type matches the exception named after the except keyword, the except clause is
    executed, and then execution continues after the try statement.

    - If an exception occurs which does not match the exception named in the except clause, it is
    passed on to outer try statements; if no handler is found, it is an unhandled exception and
    execution stops with a message.
    """

    # assertion error
    exception_has_been_handled = False
    try:
        assert False == True
        
    except AssertionError:
    	exception_has_been_handled = True
    
    assert exception_has_been_handled == True

    # AttributeError 
    class Attributes():
        pass

    exception_has_been_handled = False
    try:
        object = Attributes()
        object.attribute
    except AttributeError:
        exception_has_been_handled = True

    assert exception_has_been_handled

