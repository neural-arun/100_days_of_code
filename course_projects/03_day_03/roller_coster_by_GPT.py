print("Welcome to the Roller Coaster Ride, you are in for a treat!")

# Use a try-except block to handle non-numeric input
try:
    height = int(input("Please enter your height in cm: "))
    bill = 0

    if height >= 120:  # Changed to >= to include people who are exactly 120cm
        print("You can ride the roller coaster!")
        age = int(input("Please enter your age: "))

        if age < 12:
            bill = 7
            print("Child tickets are $7.")
        elif age < 18: # No need for '12 <= age' as the previous 'if' already handled age < 12
            bill = 12
            print("Youth tickets are $12.")
        else:
            bill = 15
            print("Adult tickets are $15.")

        want_photo = input("Do you want a photo taken? (yes/no) ").lower()
        if want_photo == "yes":
            # Use the shorthand operator for addition
            bill += 3

        # Use conventional currency formatting
        print(f"Your final bill is ${bill}")

    else:
        print("Sorry, you have to grow taller to ride.")

except ValueError:
    # This message is shown if the user enters text instead of a number
    print("Invalid input. Please enter a valid number for height and age.")