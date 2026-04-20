x = int(input('Enter the time in seconds:'))
hours = x//3600
x = x % 3600
minute = x//60
x = x % 60
print(hours, minute, x)