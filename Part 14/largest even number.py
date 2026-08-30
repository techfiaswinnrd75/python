# Identify largest even number in a list


l = [10, 4, 5, 3, 100, 103]
n = -9998

for i in l:
    if not(i % 2) and i > n:
        n = i

print(n)