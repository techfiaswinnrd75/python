x = input('Enter a password:')
length = len(x)
if length<6:
    print(' the password is weak:')
elif length<=10:
    print('the password is medium')
else:
     print('The password is strong')    