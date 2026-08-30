start = int(input("Enter the starting value: "))
end = int(input("Enter the ending Value: "))

for i in range(start+1, end):
    if i % 3 == 0 and i % 4 == 0:
        print(i)