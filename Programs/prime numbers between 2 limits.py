start = int(input('Enter a number:'))
end = int(input('Enter another number:'))
v = 1
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            v = 0
            break
    if v == 1:
        print(i)