n = int(input("Enter number of Numbers: "))

sum = 0
count = 1

while count <= n:
    i = int(input("Enter the number: "))
    sum = sum + i
    count = count + 1

avg = sum / n

print(avg)