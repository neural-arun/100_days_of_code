# Tip calculator
print("Welcome to Tip calculator!")
total_bill = float(input("Enter Total Bill: "))
tip_percent = int(input("What percentage of Total bill you want to tip: "))
tip = total_bill * (tip_percent / 100)
total_amt = total_bill + tip
split_bill = int(input("Enter number of people splitting it: "))

splitted_bill = total_amt / split_bill

per_person_bill = (round(splitted_bill , 2))

print(f"Each person has to Pay: {per_person_bill}")
