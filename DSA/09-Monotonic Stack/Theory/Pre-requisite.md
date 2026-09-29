# 09. Monotonic Stack - Pre-requisites

## Monotonicity

The word "Monotonic" in math simply means "entirely non-increasing or non-decreasing".
- `[1, 2, 4, 7, 9]` is monotonically strictly increasing.
- `[9, 6, 4, 2, 1]` is monotonically strictly decreasing.

## The Concept of a Monotonic Stack

A Monotonic Stack is just a normal Stack (LIFO), but we enforce a strict rule before pushing a new element: **The stack must remain sorted**.

If a new element comes along that would break the sorted order, we **POP** elements off the stack until the sorted order is restored, and *then* we push the new element.

### Example: Monotonically Decreasing Stack
We want the stack to only go DOWN (e.g. `[10, 8, 5, 2]`).

Let's push elements from array: `[73, 74, 75, 71, 69, 72, 76]`

1. Push `73`. Stack: `[73]`
2. Try to push `74`. Wait! `74 > 73`, which breaks decreasing order. We must POP `73`. Stack: `[]`. Now push `74`. Stack: `[74]`
3. Try to push `75`. `75 > 74`. POP `74`. Push `75`. Stack: `[75]`
4. Try to push `71`. `71 < 75`. Order is safe. Push `71`. Stack: `[75, 71]`
5. Try to push `69`. `69 < 71`. Safe. Push `69`. Stack: `[75, 71, 69]`
6. Try to push `72`. Wait! `72 > 69`. POP `69`. Stack: `[75, 71]`. Wait! `72 > 71`. POP `71`. Stack: `[75]`. Now `72 < 75` is safe. Push `72`. Stack: `[75, 72]`

### What does the popping actually MEAN?
When `72` popped `69`, it meant: **"72 is the Next Greater Element for 69"**. 
This is the core magic of Monotonic Stacks. The element that forces another element to pop is exactly its "Next Greater/Smaller" element.
