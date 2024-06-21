"""factorial module.

@see: https://docs.python.org/3/tutorial/modules.html

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.
"""


def factorial(number):
   '''return the factorial of the number.'''
   result = 1
   for i in range(number,0,-1):
      result *= i
      
   return result

# When you run a Python module with:
#
# >>> python fibonacci.py <arguments>
#
# the code in the module will be executed, just as if you imported it, but with
# the __name__ set to "__main__". That means that by adding this code at the end of your module
# you can make the file usable as a script as well as an importable module, because the code that
# parses the command line only runs if the module is executed as the “main” file:
#

if __name__ == '__main__':
    import sys
    print(factorial(int(sys.argv[1])))
