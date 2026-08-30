Memorizing a laundry list of list methods is a colossal waste of time if you don't understand that Python lists are mutable reference types, meaning you will accidentally destroy your own data if you aren't careful. Confidence: 10/10.

I disagree because asking for "all built-in functions" turns your notes into a dictionary rather than a functional mental model. Here's what I'd do instead: categorize these methods strictly by how they mutate the data structure in-place versus how they query it. The risk in your approach is treating a list like a string and wondering why calling `.sort()` returned `None` and crashed your program instead of giving you sorted data.

### The Nature of Lists

A Python list is a dynamic, ordered array of pointers. It is mutable, meaning it can be changed in place without creating a new object in memory (unlike strings).

---

### In-Place Mutation: Adding Data

These methods change the list directly. They do not return a new list; they return `None`.

* **`append(x)`:** Adds a single item `x` to the absolute end of the list. Fast and efficient.
* *Trap:* If you append a list `[2, 3]` to `[1]`, you get `[1, [2, 3]]`, not `[1, 2, 3]`.


* **`extend(iterable)`:** Takes another collection (like a list or string) and unpacks its elements, adding each one individually to the end of the list.
* **`insert(i, x)`:** Insets item `x` at a specific index `i`.
* *Performance note:* You will overuse this. Inserting at the beginning of a massive list (e.g., `insert(0, item)`) forces Python to shift every single subsequent element in memory. It is slow.



---

### In-Place Mutation: Removing Data

Like adding, these directly alter the original list.

* **`pop([i])`:** Removes and *returns* the item at the given index. If you don't provide an index (just `pop()`), it removes and returns the very last item. This is the only mutating method that routinely returns a useful value instead of `None`.
* **`remove(x)`:** Searches for the *first occurrence* of the value `x` and deletes it. If `x` isn't in the list, it throws a `ValueError` and halts execution. It does not return the removed item.
* **`clear()`:** Nukes the entire list, leaving you with `[]`.

---

### In-Place Mutation: Reordering

Do not chain these methods.

* **`sort(key=None, reverse=False)`:** Sorts the items in ascending order by default. It modifies the existing list and returns `None`. If you write `my_list = my_list.sort()`, you have just overwritten your data with `None`.
* **`reverse()`:** Flips the elements of the list back-to-front. Returns `None`.

---

### Querying (Non-Mutating)

These methods read the list but do not change its underlying structure.

* **`index(x[, start[, end]])`:** Returns the zero-based index of the *first* item whose value is `x`. Like `remove()`, it throws a fatal `ValueError` if the item doesn't exist.
* **`count(x)`:** Scans the entire list and returns an integer representing how many times the value `x` appears.

---

### The Reference Trap

You will eventually try to duplicate a list by typing `list_b = list_a`. You have not copied the list; you have created two variables pointing to the exact same block of memory. Mutating `list_b` will identically mutate `list_a`.

* **`copy()`:** Returns a shallow copy of the list. This creates a new list in memory, but if your list contains other lists (nested structures), the inner lists are still linked by reference.