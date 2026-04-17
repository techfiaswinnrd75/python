x = int(input('Enter the mark of a student'))
if x <= 100 and x >= 90:
    print('A+')
elif x< 90 and x>=80:
    print('A')
elif x<80 and x>=70:
    print('B')
elif x<70 and x>=60:
    print('C')
elif x<60 and x>=50:
    print('D')
else:
    print('Fail')