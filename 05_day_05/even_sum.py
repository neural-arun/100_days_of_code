a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
even_sum = 0
for i in range(a,b+1):
    if i % 2 == 0:
        even_sum += i

print(even_sum)