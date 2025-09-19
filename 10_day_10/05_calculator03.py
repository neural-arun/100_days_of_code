from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculation():
    num1 = float(input("Enter first number: "))
    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        user_operation = input("Pick a symbol for operation: ")
        num2 = float(input("Enter next number for above operation: "))
        answer = operations[user_operation](num1,num2)

        print(f"{num1} {user_operation} {num2} = {answer}")
        a = input(f"Type 'y' for next calculation with {answer} or Type 'n' for new calculation: ")
        if a == "y":
            num1 = answer
            
            answer = operations[user_operation](answer , num2)
        else:
           should_continue = False
           calculation()

calculation()