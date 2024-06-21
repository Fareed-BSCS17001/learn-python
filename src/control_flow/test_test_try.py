"""TRY statement

@see: https://www.w3schools.com/python/python_try_except.asp

"try" statement is used for exception handling.
When an error occurs, or exception as we call it, Python will normally stop and generate an error
message. These exceptions can be handled using the try statement.

The "try" block lets you test a block of code for errors.
The "except" block lets you handle the error.
The "else" block lets you execute the code if no errors were raised.
The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
"""


def test_try():
    """TRY statement"""

    # The try block will generate an error, because x is not defined:
    message = ""

    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
        #print("")
    except:
        message += "Exception caught. "
    else:
    	message += "Exception not caught. "
    finally:
    	message += "Try block finished."

    assert message == 'Exception caught. Try block finished.'
    #assert message == 'Exception not caught. Try block finished.'
