"""Dictionaries.

@see: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
@see: https://www.w3schools.com/python/python_dictionaries.asp

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are
written with curly brackets, and they have keys and values.

Dictionaries are sometimes found in other languages as “associative memories” or “associative
arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used
as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since
lists can be modified in place using index assignments, slice assignments, or methods like append()
and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
to the dictionary; this is also the way dictionaries are written on output.
"""


def test_test_dictionary():
    """Dictionary"""

    num_dictionary = {
        'Fareed': 'Software Engineer',
        'Adeel': 'Graphic Designer',
        'Hamza': 'Game Developer',
    }

    assert isinstance(num_dictionary, dict)

    # You may access set elements by keys.
    assert num_dictionary['Fareed'] == 'Software Engineer'
    assert num_dictionary['Adeel'] == 'Graphic Designer'
    assert num_dictionary['Hamza'] == 'Game Developer'

    # To check whether a single key is in the dictionary, use the in keyword.
    assert 'Hamza' in num_dictionary
    assert 'Moiz' not in num_dictionary


    num_dictionary['Fareed'] = 'Team Leader'

    # Add new key/value pair to the dictionary
    num_dictionary['Moiz'] = 'Software Developer'
    assert num_dictionary['Moiz'] == 'Software Developer'

    # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
    # in insertion order (if you want it sorted, just use sorted(d) instead).
    assert list(num_dictionary) == ['Fareed', 'Adeel', 'Hamza', 'Moiz']
    assert sorted(num_dictionary) == ['Adeel', 'Fareed', 'Hamza', 'Moiz']

    # It is also possible to delete a key:value pair with del.
    del num_dictionary['Moiz']
    assert list(num_dictionary) == ['Fareed', 'Adeel', 'Hamza']

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs.
    dictionary_via_constructor = dict([('Name', 'Fareed'), ('Age', 22), ('City', 'Lahore')])

    assert dictionary_via_constructor['Name'] == 'Fareed'
    assert dictionary_via_constructor['Age'] == 22
    assert dictionary_via_constructor['City'] == 'Lahore'

    # In addition, dict comprehensions can be used to create dictionaries from arbitrary key
    # and value expressions:
    dictionary_via_expression = {x: x**3 for x in (2, 4, 6)}
    assert dictionary_via_expression[2] == 8
    assert dictionary_via_expression[4] == 64
    assert dictionary_via_expression[6] == 216

    # When the keys are simple strings, it is sometimes easier to specify pairs using
    # keyword arguments.
    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098
