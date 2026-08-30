n = int(input("Enter a 2 digit number: "))
n1 = n%10
n2 = n//10
54
if n1 > n2:
    print(n1, "is largest")

elif n2 > n1:
    print(n2, "is largest")

else:
    print(n1, "and", n2, "are same")