"""Function Decorators.

@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

Function decorators are simply wrappers to existing functions. In the context of design patterns,
decorators dynamically alter the functionality of a function, method or class without having to
directly use subclasses. This is ideal when you need to extend the functionality of functions that
you don't want to modify. We can implement the decorator pattern anywhere, but Python facilitates
the implementation by providing much more expressive features and syntax for that.
"""


def test_function_decorators():
    """Function Decorators."""

    # This is the function that we want to decorate.
    def greeting(name):
        return "Hello, My name is {0}!".format(name)

    # This function decorates another functions output with <p> tag.
    def decorate_with_p(func):
        def function_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return function_wrapper

    # Now, let's call our decorator and pass the function we want decorate to it.
    my_get_text = decorate_with_p(greeting)

    # Here we go, we've just decorated the function output without changing the function itself.
    assert my_get_text('John') == '<p>Hello, My name is John!</p>'  # With decorator.
    assert greeting('John') == 'Hello, My name is John!'  # Without decorator.

    # decorator should be prepended with an @ symbol.

    @decorate_with_p
    def greeting_with_p(name):
        return "Hello, My name is {0}!".format(name)

    assert greeting_with_p('John') == '<p>Hello, My name is John!</p>'

    # Now let's consider we wanted to decorate our greeting function by one more functions to wrap a
    # div the string output.

    # This will be our second decorator.
    def decorate_with_H1(func):
        def function_wrapper(text):
            return "<H1>{0}</H1>".format(func(text))
        return function_wrapper

    # With the basic approach, decorating get_text would be along the lines of
    # greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p))

    # With Python's decorator syntax, same thing can be achieved with much more expressive power.
    @decorate_with_H1
    @decorate_with_p
    def greeting_with_H1_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_H1_p('John') == '<H1><p>Hello, John!</p></H1>'

    # One important thing to notice here is that the order of setting our decorators matters.
    # If the order was different in the example above, the output would have been different.



    # Passing arguments to decorators.

    # Looking back at the example before, you can notice how redundant the decorators in the
    # example are. 2 decorators(decorate_with_div, decorate_with_p) each with the same
    # functionality but wrapping the string with different tags. We can definitely do much better
    # than that. Why not have a more general implementation for one that takes the tag to wrap
    # with as a string? Yes please!

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags('H1')
    @tags('div')
    @tags('p')
    def greeting_with_tags(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_tags('John') == '<H1><div><p>Hello, John!</p></div></H1>'
