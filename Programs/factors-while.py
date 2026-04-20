x = int(input('Enter a number:'))
v = 1
while v<=x:
    if x%v==0:
        print(v, 'is a factor')
    v = v+1