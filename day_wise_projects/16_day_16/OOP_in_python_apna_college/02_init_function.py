# creating a class
class Student:
    name = "Arun Yadav"
    job =  "Medical AI builder"

# creating objects inside class
s1 = Student()  # this is object 1
print(s1.name)

s2 = Student()  # this is obejct 2
print(s2.job)

# crating another class
class neetprepGPT:
    type = "telegram bot + simple web app"
    job = "Make questions for students based on thier performance"


# creating objects from class factory
# object 1 of factory
f1 = neetprepGPT()
print(f1.type)

# object 2 of factory
f2 = neetprepGPT()
print(f2.job)