# Variables: Variables are symbolic names that are references or pointers to objects. Variables are created the moment you assign a value to them.

# Variable Assignment:
# Case-Sensitive : can distinguishes between uppercase and lowercase letters in identifiers

age = 25
height = 5.9
name = "John"
is_student = False

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

#string :
greeting = "Hello"
target = "World"
message = greeting + " " + target + "!"
print(message)  # Hello World!


# Multi Words Variable Names:

# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"


# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Built-in Data Types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Data Type Identification:
print(type(age))       
print(type(height))    
print(type(name))      
print(type(is_student)) 



# Python - Slicing Strings
# https://www.w3schools.com/python/python_strings_methods.asp

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:5])



# Slice From the Start
b = "Hello, World!"
print(b[:5])


# Slice To the End
b = "Hello, World!"
print(b[2:])


# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])



#boolen values
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#operators:

# Arithmetic operators
a = 10
b = 5

print(a + b)  # Addition: 15
print(a - b)  # Subtraction: 5
print(a * b)  # Multiplication: 50
print(a / b)  # Division: 2.0
print(a % b)  # Modulus: 0
print(a ** b) # Exponentiation: 100000
print(a // b) # Floor division: 2



# Assignment operators
x = 10      # Assign: 10
x += 5      # Add and assign: 15
x -= 3      # Subtract and assign: 12
x *= 2      # Multiply and assign: 24
x /= 4      # Divide and assign: 6.0
x %= 3      # Modulus and assign: 0.0
x **= 2     # Exponent and assign: 0.0
x //= 2     # Floor divide and assign: 0.0



# Comparison operators
a = 10
b = 5

print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# Logical operators
x = True
y = False

print(x and y)  # Logical AND: False
print(x or y)   # Logical OR: True
print(not x)    # Logical NOT: False



# Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # Identity: False (different objects)
print(a is c)  # Identity: True (same objects)
print(a is not b)  # Identity: True

# Membership operators
a = [1, 2, 3, 4, 5]

print(3 in a)     # Membership: True
print(6 in a)     # Membership: False
print(3 not in a) # Membership: False

# Bitwise operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)  # Bitwise AND: 0 (0000)
print(a | b)  # Bitwise OR: 14 (1110)
print(a ^ b)  # Bitwise XOR: 14 (1110)
print(~a)     # Bitwise NOT: -11 (inverts all bits)
print(a << 1) # Bitwise left shift: 20 (10100)
print(a >> 1) # Bitwise right shift: 5 (0101)


# Python Functions:
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function:
def my_function():
  print("Hello from a function")

my_function()


# Arguments:
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# Arbitrary Arguments, *args:
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Python Lambda:
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#questions for interviews/exams or for reference:
# What is a variable in Python and how is it different from a constant?
# How does Python handle different data types?
# Can you change the type of a variable once it has been set?
# What is the difference between if-elif-else and a series of if statements?
# How does a for loop differ from a while loop?
# Can you write a nested loop to print a pattern?
# Explain break and continue statements in loops.
# What is an infinite loop and how can it be avoided?
# What are the advantages of using functions in Python?
# How do you pass arguments to a function?
# Explain the concept of default arguments.
# What are lambda functions and where are they used?
# How can you return multiple values from a function?
