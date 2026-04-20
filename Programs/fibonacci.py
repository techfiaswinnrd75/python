x = int(input('Enter a number'))
a,b = 1,1
print(a)
print(b)
for i in range(x):
    n = a+b
    print(n)
    a = b
    b = n
