# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for num in range(2,number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is not prime number!")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Enter your number: ")) # Check this number
prime_checker(number=n)