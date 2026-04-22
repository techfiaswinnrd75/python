x = float(input('Enter the current in units'))
if x<=200:
    print('the amount is ',x*0.50)
elif x<=400:
    print('the amount is ',100 + (x-200)*0.65)
elif x<=600:
    print('The amount is ',230+(x-400)*0.80)
else:
    print('the amount is ',425+(x-600)*1.25)