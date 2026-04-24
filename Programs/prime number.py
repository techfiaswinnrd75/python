x = int(input('Enter amnumber:'))
prime = True
for i in range(2,x):
    if x%i == 0:
        prime = False
        break

if prime :
    print("Number is Prime")
else:
    print("Number is Not Prime")