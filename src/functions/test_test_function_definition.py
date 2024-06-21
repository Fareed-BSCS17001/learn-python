"""Function Definition

@see: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

The keyword def introduces a function definition. It must be followed by the function name and the
parenthesized list of formal parameters. The statements that form the body of the function start at
the next line, and must be indented.
"""


def factorial_definition(number):
    """The function will return the factorial of the number passed as the argument
    e.g. if number = 5, then the function will return 5*4*3*2*1."""
    if number < 0:
    	raise Exception("number cannot be negative")
    
    result = 1
    
    for i in range(number, 0, -1):
    	result *= i
    	
    return result
    

def test_function_definition():
    """Function Definition"""

    # Now call the function we just defined.
    assert factorial_definition(5) == (5*4*3*2*1)



    # A function definition introduces the function name in the current symbol table. The value of
    # the function name has a type that is recognized by the interpreter as a user-defined function.
    # This value can be assigned to another name which can then also be used as a function. This
    # serves as a general renaming mechanism
    factorial_definition_clone = factorial_definition
    assert factorial_definition_clone(6) == (6*5*4*3*2*1)

    # In Python, functions are first class citizens, they are objects and that means we can do a
    # lot of useful stuff with them.

    # Assign functions to variables.

    def greet(name):
        return 'Hello, ' + name

    greet_someone = greet

    assert greet_someone('John') == 'Hello, John'

    # Define functions inside other functions.

    def factorial(number):
        def ispositive(number):
            return number >= 0
            
        if ispositive(number):
            result = 1
    
            for i in range(number, 0, -1):
    	        result *= i
    	
            return result
        else:
            raise Exception("Negative number not allowed")
            
    assert factorial(5) == (5*4*3*2*1)

    # Functions can be passed as parameters to other functions.

    def greet_one_more(name):
        return 'Hello, ' + name

    def call_func(func):
        other_name = 'John'
        return func(other_name)

    assert call_func(greet_one_more) == 'Hello, John'

    # Functions can return other functions. In other words, functions generating other functions.

    def compose_greet_func():
        def get_message():
            return 'Hello there!'

        return get_message

    greet_function = compose_greet_func()
    assert greet_function() == 'Hello there!'

    # Inner functions have access to the enclosing scope.

    # More commonly known as a closure. A very powerful pattern that we will come across while
    # building decorators. Another thing to note, Python only allows read access to the outer
    # scope and not assignment. Notice how we modified the example above to read a "name" argument
    # from the enclosing scope of the inner function and return the new function.

    def factorial(number):
        def ispositive():
            return number >= 0
            
        if ispositive():
            result = 1
    
            for i in range(number, 0, -1):
    	        result *= i
    	
            return result
        else:
            raise Exception("Negative number not allowed")
            
    assert factorial(5) == (5*4*3*2*1)

