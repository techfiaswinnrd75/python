t = (1, 2, 3, 4, 5, 6, 7)

t = 5,

# print(type(t))

# l = [2]
# print(type(l))

x, *z = (1, 2, 3)
print(f"x: {x}, z: {z}")
print(type(x), type(z))

t = 5, "Aswin", "Python", 3.14
print(t)

print(t[1])
print(t[1:3])
print(t[-2])

l = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5, 4, 4)

l[2] = 10
print(l)

# t[2] = 10
print(t)

print(t.count(4))
print(t.index(5))

print(len(t))
print(max(t))
print(min(t))
print(sum(t))