# Object-Oriented Programming (OOP)


# Classes and Objects:

# Class: A blueprint for creating objects. A class encapsulates data for the object and methods to manipulate that data.
# Object: An instance of a class.

                            # class ClassName:
                            #     def __init__(self, param1, param2):
                            #         self.param1 = param1
                            #         self.param2 = param2

                            #     def method1(self):
                            #         # method implementation

                            # # Creating an object
                            # object_name = ClassName(param1_value, param2_value)

# The __init__() function is a special method in Python that is automatically called when an instance (object) of a class is created. This method is also known as the constructor in object-oriented programming.
# The __init__() method is defined inside a class and takes at least one argument, self, which refers to the instance being created

#classes and objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()  # Buddy says woof!


# Class with Methods
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

my_circle = Circle(5)
print("Area:", my_circle.area())  # Area: 78.5
print("Circumference:", my_circle.circumference())  # Circumference: 31.4



# Class with Private Attributes:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
account.withdraw(2000)  # Insufficient funds


# What is a class in Python and how do you create one?
# How do you create an object of a class in Python?
# Explain the concept of __init__ method.
# How can you define methods within a class?
# What is the difference between instance variables and class variables?
# How do you access and modify the attributes of an object?
# Explain the concept of private attributes in a class.
# How do you define a class method and a static method?
# Can you inherit a class in Python? If yes, how?
# What are the benefits of using classes in Python?


# Inheritance and Polymorphism:

# Inheritance: A mechanism in which one class inherits attributes and methods from another class.
# Polymorphism: The ability to use a common interface for multiple forms (data types).

                                    # class BaseClass:
                                    #     # Base class implementation

                                    # class DerivedClass(BaseClass):
                                    #     # Derived class implementation


# Simple Inheritance:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())  # Buddy says woof!


# Multiple Inheritance:
class Canine:
    def bark(self):
        print("Woof!")

class DomesticAnimal:
    def home(self):
        print("Lives in a home")

class Dog(Canine, DomesticAnimal):
    pass

my_dog = Dog()
my_dog.bark()  # Woof!
my_dog.home()  # Lives in a home


# Polymorphism with Method Overriding:
class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

birds = [Bird(), Sparrow(), Ostrich()]
for bird in birds:
    bird.fly()



# What is inheritance in Python and how is it implemented?
# Explain the concept of polymorphism with examples.
# What is method overriding and how does it work in Python?
# How do you achieve multiple inheritance in Python?
# What is the super() function and how is it used?
# Explain the concept of base class and derived class.
# How does Python handle method resolution order (MRO)?
# Can you prevent a class from being inherited?
# How do you call the parent class constructor from a child class?
# What are the benefits of using inheritance in OOP?

# Encapsulation and Abstraction:
# Encapsulation: The bundling of data and methods that operate on the data within one unit, e.g., a class. It restricts direct access to some of the object's components.
# Abstraction: The process of hiding the complex implementation details and showing only the necessary features of the object.

                            # class EncapsulationExample:
                            #     def __init__(self, param):
                            #         self.__param = param  # private variable

                            #     def get_param(self):
                            #         return self.__param

                            #     def set_param(self, value):
                            #         self.__param = value

#Encapulation:

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

student = Student("John", 20)
print(student.get_name())  # John
student.set_name("Doe")
print(student.get_name())  # Doe

# Abstraction:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())



#Advance Program
# Encapsulation and abstraction example in a banking system
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300



# What is encapsulation in OOP and why is it important?
# How do you implement encapsulation in Python?
# Explain the concept of abstraction with an example.
# What is the difference between encapsulation and abstraction?
# How do you create abstract classes and methods in Python?
# Why is it useful to hide implementation details from the user?
# What are getter and setter methods and why are they used?
# How does Python enforce encapsulation?
# Can you access private variables outside of a class?
# What are the advantages of using encapsulation and abstraction in OOP?
