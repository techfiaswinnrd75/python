n = int(input("Enter Number of Numbers you have: "))

sum = 0
for i in range(n):
    num = int(input("Enter Number: "))
    if num % 2:
        sum += num

print(sum)