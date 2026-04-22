a, b, c = map(int, input('Enter three numbers').split(","))
x = b**2-(4*a*c)
if x<0:
    print('the equation do not has real solutions:')
elif x==0:
    print('The equation has two same real solutions')
else:
    print('Ther equation has two distinct real solutions:')

    