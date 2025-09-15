import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']

no_of_letters = int(input("Enter number of letters you want in your password: "))
no_of_numbers = int(input("Enter number of num characters you want in your password: "))

no_of_symbols = int(input("Enter number of smbols you want in your password: "))
# Hard-level
password_list = []
for char in range(1,no_of_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,no_of_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1,no_of_numbers+1):
    password_list.append(random.choice(numbers))

print(password_list)

password = ""
for char in password_list:
    password += random.choice(password_list)
print(password)