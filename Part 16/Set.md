## 🟢 SET

### 1. What is a Set?

A **set** is an unordered collection of **unique elements**.

```python
s = {10, 20, 30, 40}
```

### Key characteristics

| Feature              | Set                   |
| -------------------- | --------------------- |
| Ordered              | ❌                     |
| Mutable              | ✅                     |
| Allows duplicates    | ❌                     |
| Indexing             | ❌                     |
| Slicing              | ❌                     |
| Different data types | ✅                     |
| Duplicate values     | Automatically removed |

```python
s = {10, 20, 10, 30, 20}
print(s)
# {10, 20, 30}
```

---

## 2. Creating a Set

```python
s = {1, 2, 3}
```

### Empty set ⚠️

```python
s = set()
```

❌ This is **not** an empty set:

```python
s = {}
```

`{}` creates an empty **dictionary**.

---

# 3. Adding Elements

### `add()`

Adds a single element.

```python
s = {10, 20, 30}

s.add(40)

print(s)
# {10, 20, 30, 40}
```

### `update()`

Adds multiple elements.

```python
s.update([40, 50, 60])

print(s)
# {10, 20, 30, 40, 50, 60}
```

You can use another set, list, tuple, etc.

```python
s.update({70, 80})
```

---

# 4. Removing Elements

### `remove()`

```python
s = {10, 20, 30}

s.remove(20)
```

⚠️ If the element doesn't exist → `KeyError`.

---

### `discard()`

```python
s.discard(20)
```

If the element doesn't exist, **no error** occurs.

### Difference

| Method      | Element exists | Element doesn't exist |
| ----------- | -------------- | --------------------- |
| `remove()`  | Removes        | ❌ Error               |
| `discard()` | Removes        | ✅ No error            |

---

### `pop()`

Removes and returns an **arbitrary element**.

```python
s = {10, 20, 30}

x = s.pop()

print(x)
```

Don't assume `pop()` removes the first or last element.

---

### `clear()`

Removes everything.

```python
s.clear()

print(s)
# set()
```

---

# 5. Set Operations ⭐

Suppose:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### Union

All elements from both sets.

```python
A | B
```

or

```python
A.union(B)
```

Result:

```text
{1, 2, 3, 4, 5, 6}
```

---

### Intersection

Common elements.

```python
A & B
```

or

```python
A.intersection(B)
```

Result:

```text
{3, 4}
```

---

### Difference

Elements in A but not B.

```python
A - B
```

or

```python
A.difference(B)
```

Result:

```text
{1, 2}
```

---

### Symmetric Difference

Elements present in either set, but **not both**.

```python
A ^ B
```

or

```python
A.symmetric_difference(B)
```

Result:

```text
{1, 2, 5, 6}
```

---

# 6. Set Relationship Methods

### `issubset()`

Checks whether all elements of one set are present in another.

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
# True
```

Operator:

```python
A <= B
```

---

### `issuperset()`

Checks whether a set contains all elements of another set.

```python
print(B.issuperset(A))
# True
```

Operator:

```python
B >= A
```

---

### `isdisjoint()`

Checks whether two sets have **no common elements**.

```python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))
# True
```

---

# 7. Membership

```python
s = {10, 20, 30}

print(20 in s)
# True

print(50 not in s)
# True
```

# 🎯 Quick Method Cheat Sheet

```python
s.add(x)                    # Add one
s.update(iterable)          # Add multiple
s.remove(x)                 # Remove, error if absent
s.discard(x)                # Remove, no error if absent
s.pop()                     # Remove arbitrary element
s.clear()                   # Remove all

s.union(t)                  # Union
s.intersection(t)           # Intersection
s.difference(t)             # Difference
s.symmetric_difference(t)   # Symmetric difference

s.issubset(t)
s.issuperset(t)
s.isdisjoint(t)
```