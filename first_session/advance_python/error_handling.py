# Try, Except, Finally Blocks:

# try: The block of code to be tested for errors while it is being executed.
# except: The block of code to be executed if an error occurs in the try block.
# finally: The block of code to be executed regardless of whether an error occurs or not.

                        # try:
                        #     # code that may cause an exception
                        # except SomeException as e:
                        #     # code to handle the exception
                        # finally:
                        #     # code that will run no matter what


# Basic Try-Except:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")



# Try-Except-Finally:
try:
    f = open("test.txt", "r")
    f.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    print("This block will always execute")


# multiple Except Blocks:
try:
    value = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")


# Custom Exceptions:

# You can define your own exceptions by creating a new class that is derived from the built-in Exception class.

                                    # class MyCustomError(Exception):
                                    #     def __init__(self, message):
                                    #         self.message = message

                                    #     def __str__(self):
                                    #         return self.message

# Raising a Custom Exception:
class NegativeValueError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeValueError("Negative value not allowed")

try:
    check_positive(-1)
except NegativeValueError as e:
    print(f"Error: {e}")


# Custom Exception with Attributes:
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Insufficient funds: tried to withdraw {self.amount}, but the balance is only {self.balance}"

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)



# Handling Multiple Custom Exceptions:
class NegativeValueError(Exception):
    pass

class ZeroValueError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise NegativeValueError("Negative value")
    elif value == 0:
        raise ZeroValueError("Zero value")

try:
    check_value(-5)
except (NegativeValueError, ZeroValueError) as e:
    print(f"Error: {e}")



#advance program
# Program to simulate a simple banking system with custom exceptions
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Attempted to withdraw {self.amount} with only {self.balance} available"

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

try:
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(200)
except ValueError as e:
    print(f"ValueError: {e}")
except InsufficientFundsError as e:
    print(f"InsufficientFundsError: {e}")





# What is the purpose of the try block in Python?
# How do you handle exceptions in Python?
# Explain the difference between try-except and try-except-finally.
# What are custom exceptions and how do you create them?
# How can you raise an exception in Python?
# What is the finally block and when is it executed?
# How can you handle multiple exceptions in Python?
# What are some common built-in exceptions in Python?
# How do you access exception arguments in the except block?
# What are the advantages of using custom exceptions in a program?