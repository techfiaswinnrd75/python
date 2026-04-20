import math
a = int(input('Enter the length of one side:'))
b = int(input('Enter the length of the another side:'))
c = int(input('Enter the length of the other side:'))
perimeter = a+b+c
s = (a+b+c)/2
area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
print(perimeter,area)