#1
class Dog:
    pass
d1 = Dog ()
d2 = Dog ()
d3 = Dog ()
print (d1) 
print (d2)
print (d3)

#2 
class Dog:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
d1 = Dog ("Buddy", 3)
d2 = Dog ("John", 7,)
print (d1.name)
print (d1. age)
print (d2.name)
print (d2. age)

#3
class Dog:
    def __init__ (self, name) :
        self.name = name

    def bark (self):
        print (self.name, "says Woof!",)
    def sleep (self):
        print (self.name, "Snores... ZZzzZzzZ")
d1 = Dog ("Buddy")
d1.bark()
d1.sleep()

#4
class Calculator:
    def add (self, a, b) :
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        return a / b
    
c = Calculator()
print(c.add(2, 3))
print(c.multiply(4, 5))
print(c.subtract(7, 5))
print(c.divide(4, 8))

#5
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def display(self):
        print(self.owner, "has", self.balance)


acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.display()

#6
class Counter:
    def __init__ (self):
        self.count = 0
    def increment(self):
        self.count += 1
    def display(self):
        print ("Count:", self. count)
    def decrement(self):
        self.count -= 1

c = Counter()
c.increment()
c.increment()
c.decrement()
c.display()

#7

class Car:
    def __init__ (self, brand, speed):
        self. brand = brand
        self. speed = speed
    def accelerate (self) :
        self. speed += 10
    def brake (self):
        self. speed -= 5
        if self.speed < 0: #prevents negative speed
            self.speed = 0
    def display(self):
        print(self.brand, "speed:", self.speed)

c1 = Car("Toyota", 50)
c1.accelerate()
c1.display()

#1: A class is sort of a template for creating objects, with attributes 

#2: An object is a specific application class. The class is the blueprint and the object is the actual house built from it. 
# Each object has its own values for the attributes defined in the class.

#3: A method is a function defined inside a class that describes the behavior or action of an object.

#4: The state of an object is defined by its attributes (Speed, name, age). Methods can change this state by updating attribute values.




