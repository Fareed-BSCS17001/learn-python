"""Class Definition Syntax.

@see: https://docs.python.org/3/tutorial/classes.html#method-objects

Classes can have two types of attribute references: data or methods. Class methods are called
by [variable_name].[method_name]([parameters]) as opposed to class data which lacks the ().
"""


class MyCounter:
    """A simple example of the counter class"""
    counter = 10

    def get_counter(self):
        """Return the counter"""
        return self.counter

    def decrement_counter(self):
        """decrement the counter"""
        self.counter -= 1
        return self.counter


def test_method_objects():
    """Method Objects."""

    # The other kind of instance attribute reference is a method. A method is a function that
    # “belongs to” an object. (In Python, the term method is not unique to class instances: other
    # object types can have methods as well. For example, list objects have methods called append,
    # insert, remove, sort, and so on. However, in the following discussion, we’ll use the term
    # method exclusively to mean methods of class instance objects, unless explicitly stated
    # otherwise.)

    # But be aware that counter.get_counter() is not the same thing as MyCounter.get_counter() —
    # it is a method object, not a function object.

    # Usually, a method is called right after it is bound
    counter = MyCounter()
    assert counter.get_counter() == 10

    # However, it is not necessary to call a method right away: counter.get_counter() is a method
    # object, and can be stored away and called at a later time. For example:
    get_counter = counter.get_counter
    assert get_counter() == 10

    counter.decrement_counter()
    assert get_counter() == 9
    assert MyCounter.get_counter(counter) == 9
