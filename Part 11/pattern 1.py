'''             n = 5
    A           4   n-1
   A B          3   n-2
  A B C             n-i
 A B C D
A B C D E
'''

n = int(input("Enter number of Lines: "))
char = ord("A") - 1
for i in range(1, n+1):
    print(" " * (n-i), end = "")
    for j in range(1, i+1):
        print(chr(char+j), end=" ")
    print()
