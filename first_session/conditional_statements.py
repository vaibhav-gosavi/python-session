# if Statement: Executes a block of code if a condition is true.
age = 18
if age >= 18:
    print("You are an adult.")

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# if-else Statement: Executes one block of code if a condition is true, and another block if it is false.
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# if-elif-else Statement: Checks multiple conditions.
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")



# Loops
# for Loop: Iterates over a sequence (like a list, tuple, or string).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while Loop: Repeats a block of code as long as a condition is true.
count = 1
while count <= 5:
    print(count)
    count += 1


# Nested Loops: Loop inside another loop.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")



# What are the basic data types in Python?
# How do you declare a variable in Python?
# Explain the difference between == and is in Python.
# How do you perform string concatenation in Python?
# What is the difference between list and tuple?
# Explain the use of if-elif-else statements in Python.
# How do you create a for loop that iterates over a list?
# Describe the purpose of the while loop.
# How do you define a function in Python?
# What are lambda functions and how are they used in Python?