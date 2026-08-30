# Make a list of first 'n' Even numbers...

n = int(input("Enter Number of Numbers: "))
# l = []
l = [i for i in range(0, 2*n, 2)]

# for i in range(0, 2*n, 2):
#     l.append(i)

print(l)