"""Class and Instance Variables.

@see: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

Generally speaking, instance variables are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class.
"""


def test_class_and_instance_variables():
    """Class and Instance Variables."""

    # pylint: disable=too-few-public-methods
    class Person:
        # this property is shared by all objects if the class
        education = []

        def __init__(self, name):
            self.name = name

        def add_education(self, s):
            self.education.append(s)

    john = Person('John')
    peter = Person('Peter')

    assert john.name == 'John'
    assert peter.name == 'Peter'

    john.add_education("Social Animal")
    assert peter.education == ["Social Animal"]
