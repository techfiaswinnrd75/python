x,y,z = map(int,input('Enter three numbers:').split())
if x>y:
    y = x
if y>z:
    print(y,'is the largest number:')
else:
    print(z,'is the largest number:')    
    