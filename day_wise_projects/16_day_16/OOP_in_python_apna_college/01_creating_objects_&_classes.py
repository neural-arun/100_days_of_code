# creating a class
class Student:
    name = "Arun Yadav"

# creating objects inside class
s1 = Student()  # this is object 1
print(s1.name)  

s2 = Student()  # this is obejct 2
print(s2.name)

# crating another class
class factory:
    colour = "Blue"
    numbers_of_cars = 55


# creating objects from class factory
# object 1 of factory
f1 = factory()
print(f1.colour)

# object 2 of factory
f2 = factory()
print(f2.numbers_of_cars)