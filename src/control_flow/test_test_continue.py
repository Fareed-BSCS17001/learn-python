"""CONTINUE statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The continue statement is borrowed from C, continues with the next iteration of the loop.
"""


def test_continue_statement():
    """CONTINUE statement in FOR loop"""

    # Let's

    divisible_numbers = []
    # This list will contain every other numbers (in this case - ods).
    rest_of_the_numbers = []

    for number in range(50):
        if number % 10 == 0:
            divisible_numbers.append(number)
            # Stop current loop iteration and go to the next one immediately.
            continue

        rest_of_the_numbers.append(number)

    assert divisible_numbers == [0, 10, 20, 30, 40]
    
