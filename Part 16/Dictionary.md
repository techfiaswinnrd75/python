# 🟡 DICTIONARY - Cheat Sheet

## 1. What is a Dictionary?

A **dictionary** stores data as **key-value pairs**.

```python
student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE"
}
```

Think of it as:

```text
Key       Value
----------------
name  →   Rahul
age   →   20
branch →  CSE
```

### Key characteristics

| Feature               | Dictionary |
| --------------------- | ---------- |
| Key-value pairs       | ✅          |
| Mutable               | ✅          |
| Ordered               | ✅*         |
| Duplicate keys        | ❌          |
| Duplicate values      | ✅          |
| Indexing              | ❌          |
| Keys must be hashable | ✅          |

* Dictionaries preserve insertion order in modern Python (3.7+).

---

# 2. Creating a Dictionary

```python
student = {
    "name": "Rahul",
    "age": 20
}
```

Empty dictionary:

```python
d = {}
```

or

```python
d = dict()
```

---

# 3. Accessing Values

```python
student = {
    "name": "Rahul",
    "age": 20
}

print(student["name"])
# Rahul
```

### Using `get()`

```python
print(student.get("name"))
# Rahul
```

Difference:

```python
print(student["marks"])
```

❌ `KeyError`

But:

```python
print(student.get("marks"))
```

Returns:

```text
None
```

You can provide a default:

```python
print(student.get("marks", 0))
# 0
```

---

# 4. Adding Values

Simply assign a new key.

```python
student["marks"] = 85
```

Now:

```python
{
    "name": "Rahul",
    "age": 20,
    "marks": 85
}
```

---

# 5. Updating Values

```python
student["age"] = 21
```

The existing value is replaced.

### `update()`

```python
student.update({"age": 21, "marks": 90})
```

You can also add new keys:

```python
student.update({"city": "Kollam"})
```

---

# 6. Removing Dictionary Elements

### `pop()`

Removes a specific key and returns its value.

```python
student = {
    "name": "Rahul",
    "age": 20
}

age = student.pop("age")

print(age)
# 20
```

---

### `popitem()`

Removes and returns the **last inserted key-value pair**.

```python
student.popitem()
```

---

### `del`

```python
del student["age"]
```

Removes the key-value pair.

---

### `clear()`

```python
student.clear()
```

Removes everything.

---

# 7. Important Dictionary Methods ⭐

## `keys()`

Returns all keys.

```python
student.keys()
```

Example:

```python
print(student.keys())
```

---

## `values()`

Returns all values.

```python
student.values()
```

---

## `items()`

Returns key-value pairs.

```python
student.items()
```

Example:

```python
for key, value in student.items():
    print(key, value)
```

---

## `get()`

Safely retrieves a value.

```python
student.get("name")
```

---

## `update()`

Adds or modifies key-value pairs.

```python
student.update({"age": 21})
```

---

## `setdefault()`

Returns the value of a key. If the key doesn't exist, it creates it.

```python
student = {"name": "Rahul"}

student.setdefault("age", 20)

print(student)
```

Output:

```python
{'name': 'Rahul', 'age': 20}
```

---

# 8. Looping Through Dictionary

### Keys

```python
for key in student:
    print(key)
```

### Values

```python
for value in student.values():
    print(value)
```

### Both

```python
for key, value in student.items():
    print(key, ":", value)
```

---

# 9. Checking Keys

```python
student = {
    "name": "Rahul",
    "age": 20
}

print("name" in student)
# True
```

⚠️ `in` checks **keys**, not values.

```python
print("Rahul" in student)
# False
```

For values:

```python
print("Rahul" in student.values())
# True
```

---

# 10. Nested Dictionary ⭐

A dictionary can contain another dictionary.

```python
students = {
    "student1": {
        "name": "Rahul",
        "age": 20
    },
    "student2": {
        "name": "Anu",
        "age": 21
    }
}
```

Access:

```python
print(students["student1"]["name"])
# Rahul
```

---

# 11. Set vs Dictionary ⭐

This is a good exam/interview comparison:

| Feature    | Set         | Dictionary       |
| ---------- | ----------- | ---------------- |
| Stores     | Values      | Key-value pairs  |
| Syntax     | `{1, 2, 3}` | `{"a": 1}`       |
| Mutable    | ✅           | ✅                |
| Duplicates | ❌           | Keys ❌, Values ✅ |
| Indexing   | ❌           | ❌                |
| `add()`    | ✅           | ❌                |
| `update()` | ✅           | ✅                |
| `pop()`    | ✅           | ✅                |
| `clear()`  | ✅           | ✅                |

---

# 🎯 Quick Method Cheat Sheet

```python
d.get(key)                  # Get value safely
d.keys()                    # All keys
d.values()                  # All values
d.items()                   # Key-value pairs
d.update(other)             # Add/update pairs
d.setdefault(key, value)    # Get/create key
d.pop(key)                  # Remove key
d.popitem()                 # Remove last pair
d.clear()                   # Remove all
```