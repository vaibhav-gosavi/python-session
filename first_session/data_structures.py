# Python Lists
# https://www.w3schools.com/python/python_lists_methods.asp
# Lists are used to store multiple items in a single variable.
#for tuple one more way is to add tuple to tuple
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

thislist = ["apple", "banana", "cherry"]
print(thislist)


# The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Accesing elements
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append Items:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del (can be used to delete the entire list)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear (empties the list and no element in the list but in the memory the space is still stored )
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#list compression
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#sort() , reverse() , sort(reverse= True)



# Tuple
# https://www.w3schools.com/python/python_tuples_methods.asp
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)



#adding a value to the tuple 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# loop through tuple 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#while 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 



# Python Sets
# https://www.w3schools.com/python/python_sets_methods.asp
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# this has a duplicate value and will be remove when the code is run 
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#true and 1 is the same in set 
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Access items 
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#add items 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


#add set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


#add any iterables
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


#remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


#pop method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# del and clear methods
thisset.clear()
del thisset


#loop items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)



# Python Dictionaries
# https://www.w3schools.com/python/python_dictionaries_methods.asp
# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])# accessing the elements


#Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# another example
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)



#Accessing Items

# Get Keys: The keys() method will return a list of all the keys in the dictionary.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change



# Get Values
# The values() method will return a list of all the values in the dictionary.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})



# Removing Items
# There are several methods to remove items from a dictionary:

#pop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


#popitems
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#del !..
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


#clear ..
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop Through a Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)


# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#getting the value of dict 
print(myfamily["child2"]["name"])

#looping through the dict
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


#dict compression
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Program to convert a list of strings to a dictionary with string lengths
words = ["apple", "banana", "cherry"]
length_dict = {word: len(word) for word in words}
print(length_dict)  # {'apple': 5, 'banana': 6, 'cherry': 6}


# What are list comprehensions and how do they differ from traditional list creation?
# Can you use list comprehensions to create nested lists?
# What is a dictionary comprehension and when would you use it?
# How do you add conditions in list comprehensions?
# Can list comprehensions be used to replace map() and filter() functions?