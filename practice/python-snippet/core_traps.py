"""
core_traps.py
-------------
Purpose:
- A compact set of Python core "interview traps" with runnable examples.
- Keep it simple, readable, and revision-friendly.

How to run:
    python core_traps.py

Tip:
- Read the printed output and the comments together.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import List, Dict, Optional


# ------------------------------------------------------------
# 1) Mutable Default Argument Trap
# ------------------------------------------------------------
def add_item_bad(item: int, bucket: List[int] = []) -> List[int]:
    """
    ❌ BAD: The default list is created ONCE at function definition time.
    So it gets reused across calls.
    """
    bucket.append(item)
    return bucket


def add_item_good(item: int, bucket: Optional[List[int]] = None) -> List[int]:
    """
    ✅ GOOD: Use None, then create a new list per call when needed.
    """
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


def demo_mutable_default_arg() -> None:
    print("\n--- 1) Mutable Default Argument Trap ---")
    print("Bad calls (notice the list keeps growing):")
    print("add_item_bad(1):", add_item_bad(1))
    print("add_item_bad(2):", add_item_bad(2))
    print("add_item_bad(3):", add_item_bad(3))

    print("\nGood calls (each call is independent by default):")
    print("add_item_good(1):", add_item_good(1))
    print("add_item_good(2):", add_item_good(2))
    print("add_item_good(3):", add_item_good(3))


# ------------------------------------------------------------
# 2) `is` vs `==` (Identity vs Equality)
# ------------------------------------------------------------
def demo_is_vs_equals() -> None:
    print("\n--- 2) `is` vs `==` ---")

    a = [1, 2, 3]
    b = [1, 2, 3]
    print("a == b:", a == b)  # True: values equal
    print("a is b:", a is b)  # False: different objects

    # Integers may appear to behave oddly due to interning/caching (implementation detail).
    x = 256
    y = 256
    print("\nSmall int example (may be interned):")
    print("x == y:", x == y)  # True
    print("x is y:", x is y)  # Often True, but don't rely on it

    m = 10_000
    n = 10_000
    print("\nLarger int example (interning not guaranteed):")
    print("m == n:", m == n)  # True
    print("m is n:", m is n)  # Often False in some contexts

    # Correct usage:
    val = None
    print("\nCorrect identity check with None:")
    print("val is None:", val is None)


# ------------------------------------------------------------
# 3) Shallow Copy vs Deep Copy
# ------------------------------------------------------------
def demo_shallow_vs_deep_copy() -> None:
    print("\n--- 3) Shallow Copy vs Deep Copy ---")

    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)       # top-level list copied; inner lists shared
    deep = copy.deepcopy(original)      # everything copied recursively

    original[0].append(99)  # mutate an inner list

    print("original:", original)
    print("shallow :", shallow, "  <-- changed too (shared inner lists)")
    print("deep    :", deep, "  <-- unchanged (separate inner lists)")


# ------------------------------------------------------------
# 4) List Aliasing Trap (shared references)
# ------------------------------------------------------------
def demo_list_aliasing() -> None:
    print("\n--- 4) List Aliasing Trap ---")

    a = [0] * 3
    a[0] = 7
    print("a = [0] * 3 then a[0]=7 ->", a, "(this is fine)")

    # Common trap: nested lists
    grid_bad = [[0] * 3] * 3  # ❌ all rows reference the same inner list
    grid_bad[0][0] = 9
    print("\nBad grid (rows are same object):")
    print("grid_bad:", grid_bad)

    # Correct way:
    grid_good = [[0] * 3 for _ in range(3)]  # ✅ each row is a new list
    grid_good[0][0] = 9
    print("\nGood grid (independent rows):")
    print("grid_good:", grid_good)


# ------------------------------------------------------------
# 5) Exception Catching Too Broad
# ------------------------------------------------------------
def demo_broad_exception() -> None:
    print("\n--- 5) Catching Exceptions Too Broadly ---")

    def parse_int_bad(s: str) -> int:
        try:
            return int(s)
        except Exception:  # ❌ Too broad; hides programming errors too
            return 0

    def parse_int_good(s: str) -> int:
        try:
            return int(s)
        except ValueError:  # ✅ Specific; only catches expected conversion issue
            return 0

    print("parse_int_bad('123') :", parse_int_bad("123"))
    print("parse_int_bad('abc') :", parse_int_bad("abc"))
    print("parse_int_good('123'):", parse_int_good("123"))
    print("parse_int_good('abc'):", parse_int_good("abc"))


# ------------------------------------------------------------
# 6) Late Binding in Closures (lambda in loops)
# ------------------------------------------------------------
def demo_late_binding_closure() -> None:
    print("\n--- 6) Late Binding in Closures (lambda in loops) ---")

    funcs_bad = []
    for i in range(3):
        funcs_bad.append(lambda: i)  # ❌ i is looked up when called, not when created

    print("Bad closures (all return the same final i):")
    print([f() for f in funcs_bad])  # typically [2, 2, 2]

    funcs_good = []
    for i in range(3):
        funcs_good.append(lambda i=i: i)  # ✅ bind i at definition time

    print("Good closures (capture each i correctly):")
    print([f() for f in funcs_good])  # [0, 1, 2]


# ------------------------------------------------------------
# 7) Dict iteration while mutating (runtime error)
# ------------------------------------------------------------
def demo_mutating_dict_while_iterating() -> None:
    print("\n--- 7) Mutating dict while iterating ---")

    d = {"a": 1, "b": 2, "c": 3}

    print("Original dict:", d)
    print("Safe approach: iterate over a list of keys to delete.")
    for k in list(d.keys()):
        if d[k] % 2 == 1:
            del d[k]
    print("After deletion:", d)

    # NOTE: Directly mutating while iterating can raise:
    # RuntimeError: dictionary changed size during iteration


# ------------------------------------------------------------
# 8) Float precision surprise
# ------------------------------------------------------------
def demo_float_precision() -> None:
    print("\n--- 8) Float Precision ---")
    print("0.1 + 0.2 =", 0.1 + 0.2)
    print("0.1 + 0.2 == 0.3 ?", (0.1 + 0.2) == 0.3)

    # If needed, use rounding or decimal module for financial calculations.
    print("Round to 2 decimals:", round(0.1 + 0.2, 2))


# ------------------------------------------------------------
# 9) dataclass default values (mutable default again)
# ------------------------------------------------------------
@dataclass
class BasketBad:
    items: List[int] = []  # ❌ shared across instances (same trap)


@dataclass
class BasketGood:
    items: List[int] = None  # will fix in __post_init__

    def __post_init__(self) -> None:
        if self.items is None:
            self.items = []


def demo_dataclass_mutable_default() -> None:
    print("\n--- 9) dataclass Mutable Default Trap ---")
    b1 = BasketBad()
    b2 = BasketBad()
    b1.items.append(1)
    print("BasketBad b1.items:", b1.items)
    print("BasketBad b2.items:", b2.items, "  <-- oops, shared list!")

    g1 = BasketGood()
    g2 = BasketGood()
    g1.items.append(1)
    print("\nBasketGood g1.items:", g1.items)
    print("BasketGood g2.items:", g2.items, "  <-- separate lists ✅")


# ------------------------------------------------------------
# 10) Function argument mutation (caller side effects)
# ------------------------------------------------------------
def append_in_place(nums: List[int]) -> None:
    nums.append(999)


def demo_argument_mutation() -> None:
    print("\n--- 10) Mutating Arguments In-Place ---")
    data = [1, 2, 3]
    append_in_place(data)
    print("After append_in_place:", data, "  <-- caller data changed")

    # Safe approach: return a new list
    data2 = [1, 2, 3]
    new_data2 = data2 + [999]
    print("Original:", data2)
    print("New     :", new_data2)


# ------------------------------------------------------------
# Main runner
# ------------------------------------------------------------
def main() -> None:
    demo_mutable_default_arg()
    demo_is_vs_equals()
    demo_shallow_vs_deep_copy()
    demo_list_aliasing()
    demo_broad_exception()
    demo_late_binding_closure()
    demo_mutating_dict_while_iterating()
    demo_float_precision()
    demo_dataclass_mutable_default()
    demo_argument_mutation()


if __name__ == "__main__":
    main()
