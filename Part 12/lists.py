lis = [1, 2, 3, 4, 5]
print(lis)

lis = [0] * 10
print(lis)

lis = ["Aswin", "Appu", "Achu"]
print(lis)

lis = ["Aswin", 100, 10.86]
print(lis)

lis1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#       0      1   2     3    4    5   6     7    8    9
#       -10   -9  -8    -7   -6   -5  -4    -3   -2   -1

print(lis1[-3])

print(lis1[2:8:2])

l = [i**2 for i in range(100) if i % 5 == 0]


print(l)