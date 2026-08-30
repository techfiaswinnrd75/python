# Python Tuples — Session Cheat Sheet

## 1. What is a Tuple?

A **tuple** is an ordered, immutable collection of elements in Python.

```python
my_tuple = (10, 20, 30, 40)
```

### Key characteristics

| Feature                     | Tuple |
| --------------------------- | ----- |
| Ordered                     | ✅     |
| Mutable                     | ❌     |
| Allows duplicates           | ✅     |
| Allows different data types | ✅     |
| Indexing                    | ✅     |
| Slicing                     | ✅     |

**Easy way to explain:**

> "A tuple is like a list that cannot be changed after it is created."

---

## 2. Creating Tuples

```python
t1 = (1, 2, 3)
t2 = ("Python", "Java", "C")
t3 = (10, "Hello", 3.14, True)
```

### Empty tuple

```python
t = ()
```

### Single-element tuple ⚠️

The comma is important:

```python
t = (10,)     # Tuple
x = (10)      # Integer
```

```python
print(type(t))  # <class 'tuple'>
print(type(x))  # <class 'int'>
```

---

## 3. Accessing Tuple Elements

Tuples use **indexing**, starting from `0`.

```python
t = (10, 20, 30, 40)

print(t[0])    # 10
print(t[2])    # 30
```

### Negative indexing

```python
print(t[-1])   # 40
print(t[-2])   # 30
```

Visual:

```text
Tuple:    10    20    30    40
Index:     0     1     2     3
Negative: -4    -3    -2    -1
```

---

## 4. Tuple Slicing

Syntax:

```python
tuple[start:stop:step]
```

Example:

```python
t = (10, 20, 30, 40, 50)

print(t[1:4])    # (20, 30, 40)
print(t[:3])     # (10, 20, 30)
print(t[2:])     # (30, 40, 50)
print(t[::-1])   # (50, 40, 30, 20, 10)
```

**Remember:** `stop` index is excluded.

---

# 5. Tuple Immutability ⭐

This is the most important concept.

```python
t = (10, 20, 30)

t[0] = 100
```

❌ Error:

```text
TypeError: 'tuple' object does not support item assignment
```

Unlike lists:

```python
lst = [10, 20, 30]
lst[0] = 100

print(lst)
# [100, 20, 30]
```

### Why use tuples?

* Protect data from accidental modification
* Can be used as dictionary keys (when their elements are hashable)
* Often useful for fixed collections of values

---

# 6. Tuple Methods

Python tuples have **only two built-in methods**.

## `count()`

Returns the number of times an element occurs.

```python
t = (10, 20, 10, 30, 10)

print(t.count(10))
```

Output:

```text
3
```

### Syntax

```python
tuple.count(value)
```

---

## `index()`

Returns the index of the **first occurrence** of an element.

```python
t = (10, 20, 30, 20, 40)

print(t.index(20))
```

Output:

```text
1
```

Even though `20` occurs twice, `index()` returns the first position.

### Syntax

```python
tuple.index(value)
```

You can also specify where to search:

```python
t = (10, 20, 30, 20, 40)

print(t.index(20, 2))
```

Output:

```text
3
```

---

# 7. Useful Built-in Functions

These aren't tuple **methods**, but they're commonly used with tuples.

```python
t = (10, 20, 30, 40)
```

### `len()`

```python
len(t)
# 4
```

### `max()`

```python
max(t)
# 40
```

### `min()`

```python
min(t)
# 10
```

### `sum()`

```python
sum(t)
# 100
```

### `sorted()`

```python
t = (30, 10, 40, 20)

print(sorted(t))
```

Output:

```text
[10, 20, 30, 40]
```

⚠️ `sorted()` returns a **list**, not a tuple.

---

# 8. Tuple Operations

### Concatenation

```python
a = (1, 2)
b = (3, 4)

print(a + b)
```

Output:

```text
(1, 2, 3, 4)
```

### Repetition

```python
t = (1, 2)

print(t * 3)
```

Output:

```text
(1, 2, 1, 2, 1, 2)
```

### Membership

```python
t = (10, 20, 30)

print(20 in t)
# True

print(50 not in t)
# True
```

---

# 9. Tuple Packing & Unpacking ⭐

### Packing

```python
student = ("Aswin", 21, "CSE")
```

Multiple values are packed into a tuple.

### Unpacking

```python
name, age, branch = student

print(name)
print(age)
print(branch)
```

Output:

```text
Aswin
21
CSE
```

### Extended unpacking

```python
numbers = (1, 2, 3, 4, 5)

a, *b, c = numbers

print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

---

# 10. Tuple vs List ⭐

A very useful comparison for your session:

| Feature               | List  | Tuple  |
| --------------------- | ----- | ------ |
| Syntax                | `[ ]` | `( )`  |
| Mutable               | ✅     | ❌      |
| Ordered               | ✅     | ✅      |
| Duplicates            | ✅     | ✅      |
| Indexing              | ✅     | ✅      |
| Slicing               | ✅     | ✅      |
| Methods               | Many  | Only 2 |
| Can be dictionary key | ❌     | ✅*     |

`*` The tuple must contain only hashable elements.

### Simple rule

> **Need to change it? → List**
> **Data should stay fixed? → Tuple**

---

# 11. Important Trick Question

```python
t = (1, 2, [3, 4])
```

Can we modify the list?

```python
t[2].append(5)

print(t)
```

Output:

```text
(1, 2, [3, 4, 5])
```

**Why?**

The tuple itself is immutable, but the **list inside the tuple is mutable**.

This is a great example to ask students.

---

# 12. Common Mistakes

### ❌ Forgetting comma for single-element tuple

```python
t = (5)
```

This is not a tuple.

```python
t = (5,)
```

This is a tuple.

### ❌ Trying to modify a tuple

```python
t[0] = 100
```

Raises `TypeError`.

### ❌ Assuming `sorted()` returns a tuple

```python
sorted((3, 1, 2))
```

Returns:

```python
[1, 2, 3]
```