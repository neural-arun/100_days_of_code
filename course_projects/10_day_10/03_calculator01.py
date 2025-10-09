# CALCULATOR
n1 = int(input("What is your first number? "))



# add

def add(n1 , n2):
    return n1 + n2

#subtract 
def subtract(n1 , n2):
    return n1 - n2

#multiplication
def multiply(n1 , n2):
    return n1 * n2

# divide
def divide(n1 , n2):
    return n1 / n2



operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}



for operation in operations:
    print(operation)
user_operation = input("Choose one of the above operations ? ")
n2 = int(input("What is your second number? "))
result = operations[user_operation](n1 , n2)
print(f"{n1} {user_operation} {n2} = {result}")
