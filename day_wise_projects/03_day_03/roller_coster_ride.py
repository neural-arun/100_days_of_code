print("Welcome to Roller Coster Ride, You are in here for a treat.")
height = int(input("Please, Enter Your Height(cm): "))
bill = 0
if height > 120:
    print("Welcome to ride.")
    age = int(input("Plese, Enter Your age: "))
    if age < 12:
        print("Roller coster for young is 7$.")
        bill = 7
    elif 12 <= age <18:
        print("Teen's ticket is for 12$.")
        bill = 12
    else:
        print("Your ticket is for 15$.")
        bill = 15

    want_photo = input("Do you want a picture? (yes/no) ").lower()
    if want_photo == "yes":
        bill = bill + 3
    elif want_photo == "no":
        bill = bill
    print(f"Your total cost is {bill}$")    


    



else:
    print("Sorry, you have to grow taller ro ride here")