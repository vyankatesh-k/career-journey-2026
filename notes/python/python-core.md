# Python Core – Fundamentals (Revision Notes)

These notes cover Python core concepts from an **interview and real-world usage** perspective.  
The focus is on **clarity, behavior, and common pitfalls**, not syntax memorization.

---

## 1. Python Philosophy

- High-level, interpreted programming language
- Dynamically typed
- Strong emphasis on readability and simplicity
- Follows the concept of **duck typing**

> Duck typing: If an object behaves like a particular type, Python treats it as that type.

---

## 2. Variables & Data Types

### Common Built-in Data Types
- `int`, `float`
- `str`
- `bool`
- `None`

```python
x = 10
y = "hello"
z = None

### Key Concepts
- Variables are references to objects, not containers
- Type is associated with the object, not the variable
- Variables can be reassigned to different object types

a = 10
a = "text"   # valid in Python

## 3. Mutability vs Immutability
### Immutable Types
- int
- float
- str
- tuple
- frozenset

### Mutable Types
- list
- dict
- set

a = "hello"
a = a + " world"   # creates a new string object

lst = [1, 2]
lst.append(3)      # modifies the same list object

### Why This Matters
- Impacts performance
- Important for function arguments
- Explains many side-effect bugs

## 4. Truthy & Falsy Values
### Falsy Values
- False
- None
- 0, 0.0
- ""
- [], {}, set()

### Everything else is truthy.

if []:
    print("This will not execute")


## 5. Collections Overview
### List vs Tuple
- list → mutable
- tuple → immutable, hashable (if elements are hashable)

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

### Set vs Dictionary
- set → stores unique values
- dict → stores key-value pairs

my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

### Dictionary Internals (High Level)
- Implemented using hash tables
- Average lookup, insert, delete time: O(1)
- Hash collisions handled internally

## 6. Shallow Copy vs Deep Copy
### Shallow Copy

import copy
new_list = copy.copy(old_list)

Copies references to nested objects

### Deep Copy

import copy
new_list = copy.deepcopy(old_list)

Recursively copies all nested objects

## 7. Control Flow
### Conditional Statements

if x > 0:
    pass
elif x == 0:
    pass
else:
    pass

### Loops

for i in range(5):
    print(i)

while condition:
    break

Loop Keywords
- break → exits the loop
- continue → skips current iteration
- pass → placeholder statement

## 8. Functions
### Basic Function

def add(a, b):
    return a + b

### Default Argument Pitfall (IMPORTANT)

def add_item(item, lst=[]):   # ❌ bad practice
    lst.append(item)
    return lst

Correct approach:

def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

## 9. *args and **kwargs

def func(*args, **kwargs):
    print(args)
    print(kwargs)

*args → variable number of positional arguments
**kwargs → variable number of keyword arguments

## 10. Pythonic Utilities
### enumerate

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

### zip

for a, b in zip([1, 2], [3, 4]):
    print(a, b)

any / all
any([True, False])   # True
all([True, False])   # False

## 11. Exception Handling

try:
    risky_operation()
except ValueError:
    handle_error()
else:
    run_if_no_exception()
finally:
    cleanup()

### Best Practices
- Catch specific exceptions
- Do not suppress exceptions silently
- Exceptions should represent exceptional cases

## 12. Imports & Execution Model

Import Styles

import math
from math import sqrt

Entry Point Guard

if __name__ == "__main__":
    main()


- Ensures code runs only when file is executed directly

- Essential for modular and reusable code

## Interview Notes (Very Important)
- Python variables are references, not containers
- Mutable default arguments create shared state bugs
- Dictionary and set lookups are O(1) on average due to hashing
- Strings are immutable for safety and performance
- Readable code is preferred over clever one-liners
- Exceptions should not replace normal control flow

## TODO (Future Enhancements)
- Python memory model (reference counting, garbage collection)
- Performance implications of mutability
- Python object model and method resolution order (MRO)
