# LeetCode #2 — Add Two Numbers

## Problem

Given two non-empty linked lists representing two non-negative integers, add the two numbers and return the result as a linked list.

The digits are stored in **reverse order**, meaning the first node represents the least significant digit.

For example:

```text
l1 = [2, 4, 3]
l2 = [5, 6, 4]

Result = [7, 0, 8]
```

This represents:

```text
342 + 465 = 807
```

## Approach

The solution simulates normal addition from right to left.

Because the linked lists store digits in reverse order, we can process both lists from their heads.

For every pair of digits:

1. Get the current digit from `l1`.
2. Get the current digit from `l2`.
3. Add both digits and the previous `carry`.
4. Store the last digit of the result in a new node.
5. Calculate the new `carry`.
6. Move to the next nodes.
7. If a carry remains after both lists are finished, create one final node.

### Example

```text
l1:  2 → 4 → 3
l2:  5 → 6 → 4

2 + 5 = 7
4 + 6 = 10 → write 0, carry 1
3 + 4 + 1 = 8

Result:

7 → 0 → 8
```

## Complexity

* **Time Complexity:** `O(max(n, m))`
* **Space Complexity:** `O(max(n, m))`

Where `n` and `m` are the lengths of the two linked lists.

## Key Concepts

* Linked Lists
* Traversal
* Carry handling
* Modular arithmetic
* Integer division
* Creating and connecting nodes

## Solution

See [`solution.py`](solution.py).
