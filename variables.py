__author__ = "Abner"

# Declaring an integer variable
age = 26
print(age)

name = "Abner"
print("My name is %s and I'm %d years old" % (name, age))

# Reassigning variable to string is allowed
age = "I am 26 years old"
print(age)

# Declaring a float variable
pi = 3.14 # or pi = float(3.14)
print(pi)

# Declare strings with '' or ""
mystring = "Don't worry about apostrophes"
print(mystring)

# Declaring multiple variables
a, b = 3, 4
print(a, b)

# None
nonevar = None

myfloat = float(30.0)

if isinstance(myfloat, float):
    print("Float %f" % myfloat)
    
# Lists
fruits = ["Pineaple", "Apple"]
fruits.append("Lemon")

print(fruits[0]) # Prints Pineaple

# Throws out of range exception: fruit[10]

for fruit in fruits:
    print(fruit)
    
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]

numbers = even_numbers + odd_numbers
print(numbers)

numbers.sort()
print numbers
print numbers[:4]  # Prints indexes 0, 1, 2, 3
print numbers[4:8] # Prints indexes 4, 5, 6, 7

person = ("John Doe", 50)
print(person[0])

class Person:
    name
    age
    
johh = Person()
johh.name = "John"

x = 2
print(x**2)

a = 4
b = 2
print(a / b)
print(a // b)

# Iteration
for i in range(1, 4):
    print(i)

