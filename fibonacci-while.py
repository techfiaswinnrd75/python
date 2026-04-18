x = int(input('Enter a number:'))
a,b = 1,1
v = 1
while v<=x:
    n = a+b
    print(n)
    a=b
    b=n
    v = v+1