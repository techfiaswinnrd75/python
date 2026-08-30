l = [5, 9, 10, 100, 43, 23, 50, 64, 42, 21]

print(len(l))

l.append(105)
print(l)

l.extend([10, 20, 30, 40, 50])
print(l)

l.insert(5, 53)
print(l)

val = l.pop(6)
print(val, l)

l.remove(64)
print(l)

l.reverse()
print(l)

print(l.count(10))

l1 = l.copy()

print(id(l), id(l1))

l.sort()
print(l)

l.clear()
print(l)