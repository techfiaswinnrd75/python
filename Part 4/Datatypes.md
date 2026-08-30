### Data Types

These core data types govern how information is stored and manipulated.

* **`int` (Integer):** Whole numbers without a fractional part (e.g., `5`, `-42`). In Python 3, they have arbitrary precision, meaning they are limited only by available system memory.
* **`float` (Floating Point):** Numbers with a decimal point (e.g., `3.14`, `-0.001`). They are subject to floating-point precision limitations, meaning operations like `0.1 + 0.2` will yield `0.30000000000000004` rather than exactly `0.3`.
* **`str` (String):** Immutable sequences of Unicode characters (e.g., `"hello"`, `'Python'`). Because they are immutable, any operation that appears to modify a string actually creates a completely new string in memory.

---

### Operators

Operators manipulate data, but their behavior heavily depends on the data types involved.

**Arithmetic Operators**

* `+` : Addition (Also concatenates strings)
* `-` : Subtraction
* `*` : Multiplication (Also repeats strings, e.g., `"A" * 3` results in `"AAA"`)
* `/` : True Division (Always returns a `float`, even if the numbers divide evenly)
* `//` : Floor Division (Rounds down to the nearest integer)
* `%` : Modulo (Returns the remainder of a division)
* `` : Exponentiation (e.g., `2  3` is 8)

**Comparison Operators**

* `==` : Equal to (Compares the actual values, not the memory addresses)
* `!=` : Not equal to
* `>` : Greater than
* `<` : Less than
* `>=` : Greater than or equal to
* `<=` : Less than or equal to

**Logical Operators**

* `and` : Returns True if both operands evaluate to true
* `or` : Returns True if at least one operand evaluates to true
* `not` : Reverses the boolean state of the operand

---

### Operator Precedence

When multiple operators are used in an expression, Python evaluates them based on a strict hierarchy. Parentheses `()` can always be used to override this order.

| Precedence (Highest to Lowest) | Operator(s) | Description |
| --- | --- | --- |
| 1 | `**` | Exponentiation |
| 2 | `+x`, `-x` | Positive, Negative (Unary operations) |
| 3 | `*`, `/`, `//`, `%` | Multiplication, Division, Floor Division, Modulo |
| 4 | `+`, `-` | Addition, Subtraction |
| 5 | `<`, `<=`, `>`, `>=`, `==`, `!=` | Comparisons |
| 6 | `not` | Logical NOT |
| 7 | `and` | Logical AND |
| 8 | `or` | Logical OR |