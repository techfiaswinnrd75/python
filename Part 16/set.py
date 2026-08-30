s = {1, 3, 5, 7}

s.add(9)
print(s)

s.update((11, 13, 15, 17, 19))
print(s)

s.add(4)
print(s)

s.remove(4)
s.discard(4)
print(s)

print(s.pop())
print(s)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1|s2)    # Union                 s1.union(s2)
print(s1&s2)    # Intersection          s1.intersection(s2)
print(s1-s2)    # Difference            s1.difference(s2)
print(s1^s2)    # Symmetric Difference  s1.symmetric_difference(s2)     (s1 - s2) + (s2 - s1)

print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))