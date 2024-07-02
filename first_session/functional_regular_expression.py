# Map: The map function applies a given function to all items in an input list (or any other iterable) and returns a list (or iterator) of the results.

    # Syntax: map(function, iterable)
    # Example: Applying a function to double each item in a list.


# Filter: The filter function constructs an iterator from elements of an iterable for which a function returns true.

    # Syntax: filter(function, iterable)
    # Example: Filtering out even numbers from a list.

# Reduce: The reduce function, from the functools module, applies a binary function to the items of an iterable, from left to right, so as to reduce the iterable to a single cumulative value.

    # Syntax: reduce(function, iterable)
    # Example: Summing all elements in a list.


def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]


def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # [2, 4, 6]



from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # 15


# What is the map function and how does it work?
# How does the filter function differ from map?
# Explain the reduce function and give an example of its usage.
# What are lambda expressions and where are they commonly used?
# How can you use lambda expressions with map, filter, and reduce?


# Regular Expressions (Regex): A sequence of characters that forms a search pattern. They can be used for string searching and manipulation.


# Using the re Module

# import re: To use regular expressions in Python, you need to import the re module.
# Functions in re module:
# re.match(): Checks for a match only at the beginning of the string.
# re.search(): Searches the string for a match.
# re.findall(): Finds all matches in the string.
# re.sub(): Replaces one or many matches with a string.

#match
import re

pattern = r'hello'
string = 'hello world'
match = re.match(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

#search

pattern = r'world'
string = 'hello world'
match = re.search(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")



#findall

pattern = r'\d+'
string = 'There are 42 apples and 12 oranges'
matches = re.findall(pattern, string)
print("Matches found:", matches)  # ['42', '12']



#sub

pattern = r'apples'
replacement = 'bananas'
string = 'I like apples'
new_string = re.sub(pattern, replacement, string)
print(new_string)  # I like bananas



# Program to validate email addresses using regular expressions
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

emails = ["test@example.com", "invalid-email@", "user@domain.co"]
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")


# What are regular expressions and why are they used?
# How do you match a pattern at the beginning of a string using regex?
# Explain the difference between re.match() and re.search().
# How can you find all occurrences of a pattern in a string using regex?
# What function would you use to replace substrings in a string using regex?