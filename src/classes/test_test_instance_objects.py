"""Class Definition Syntax.

@see: https://docs.python.org/3/tutorial/classes.html#instance-objects
"""


def test_instance_objects():
    """Instance Objects.

    Now what can we do with instance objects? The only operations understood by instance objects
    are attribute references. There are two kinds of valid attribute names:
    - data attributes
    - methods.
    """

    # DATA ATTRIBUTES need not be declared; like local variables, they spring into existence when
    # they are first assigned to. 

    # pylint: disable=too-few-public-methods
    class DummyClass:
        """Dummy class"""
        num1 = 0

    dummy_instance = DummyClass()

    # pylint: disable=attribute-defined-outside-init
    dummy_instance.temporary_attribute = 1
    assert dummy_instance.num1 == 0
    assert dummy_instance.temporary_attribute == 1
    del dummy_instance.temporary_attribute
