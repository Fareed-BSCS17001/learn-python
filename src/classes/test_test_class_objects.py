"""Class Definition Syntax.

@see: https://docs.python.org/3/tutorial/classes.html#class-objects

After defining the class attributes to a class, the class object can be created by assigning the
object to a variable. The created object would have instance attributes associated with it.
"""


def test_class_objects():
    """Class Objects.

    Class objects support two kinds of operations:
    - attribute references
    - instantiation.
    """


    class Calculator:
        """Example of the Calculator class"""

        num1 = 10
        num2 = 20

        def get_num1(self):
            """Return num1."""
            return self.num1

        def get_num2(self):
            """Return num2."""
            return self.num2
            
        def get_sum(self):
            '''Return sum of num1 and num2'''
            return self.num1 + self.num2

    assert Calculator.num1 == 10

    # __doc__ is also a valid attribute, returning the docstring belonging to the class
    assert Calculator.__doc__ == 'Example of the Calculator class'

    Calculator.num1 = 30
    assert Calculator.num1 == 30

    # CLASS INSTANTIATION uses function notation. Just pretend that the class object is a
    # parameterless function that returns a new instance of the class. For example
    # (assuming the above class):
    cal1 = Calculator()

    assert cal1.num1 == 30
    assert cal1.get_num1() == 30

    assert cal1.get_sum() == 50

    # The instantiation operation (“calling” a class object) creates an empty object. Many classes
    # like to create objects with instances customized to a specific initial state. Therefore a
    # class may define a special method named __init__(), like this:

    class CalculatorWithConstructor:
        """Example of the class with constructor"""
        def __init__(self, num_1, num_2):
            self.num1 = num_1
            self.num2 = num_2

        def get_num1(self):
            """Return num1."""
            return self.num1

        def get_num2(self):
            """Return num2."""
            return self.num2

        def get_sum(self):
            '''returns sum of num1 and num2'''
            return self.num1 + self.num2

    cal2 = CalculatorWithConstructor(3.0, 5.6)
    assert cal2.get_num1, cal2.get_num2 == (3.0, 5.6)
    assert cal2.get_sum() == 8.6
