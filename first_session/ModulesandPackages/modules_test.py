# Modules: A file containing Python code. A module can define functions, classes, and variables. It can also include runnable code.


# Packages: A way of structuring Python’s module namespace by using “dotted module names”. A package is a collection of modules.

import math
print(math.sqrt(16))  # 4.0


import math
print(math.factorial(5))  # 120
print(math.pi)            # 3.141592653589793


import datetime
now = datetime.datetime.now()
print(now)  # Current date and time


# Creating Custom Modules:

# mymodule.py
def greet(name):
    return f"Hello, {name}!"


import mymodule
print(mymodule.greet("Alice"))  # Hello, Alice!

# Creating Packages:
# Create a directory structure:

# mypackage/
#     __init__.py
#     module1.py
#     module2.py


# module1.py
def func1():
    return "This is function 1"

# module2.py
def func2():
    return "This is function 2"



from mypackage import module1, module2
print(module1.func1())  # This is function 1
print(module2.func2())  # This is function 2



# What is a module in Python and how do you use it?
# Explain the difference between a module and a package.
# How do you import specific functions from a module?
# What is the purpose of the __init__.py file in a package?
# How can you structure a large Python project using packages?