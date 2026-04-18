x = int(input('Enter a number:'))
i = 1
while i<=x:
    if i % 5==0:
        print(i, 'fizz')
    else:
        print(i)
    i = i+1