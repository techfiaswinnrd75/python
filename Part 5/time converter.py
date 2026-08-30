sec = int(input("Enter time in seconds: "))

min = sec // 60
sec %= 60           # sec = sec % 60

hr = min // 60
min %= 60

print("Hour:", hr)
print("Minuite:", min)
print("Seconds:", sec)

# hr = sec // 3600
# sec %= 3600

# min = sec // 60
# sec %= 60

# print("Hour:", hr)
# print("Minuite:", min)
# print("Seconds:", sec)