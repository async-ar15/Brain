# 08. Stack - Pre-requisites

## What is a Stack?

A Stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle.
Think of a stack of plates in a cafeteria:
- The last plate you put on top is the first plate you take off.
- You cannot easily access the plate at the bottom without taking off all the plates above it.

## Key Operations

1. **Push:** Add an element to the top of the stack. ($O(1)$)
2. **Pop:** Remove and return the top element of the stack. ($O(1)$)
3. **Peek/Top:** Look at the top element without removing it. ($O(1)$)
4. **isEmpty:** Check if the stack is empty. ($O(1)$)

## The Java `Stack` Class (and why you shouldn't use it)

Java has a built-in `Stack` class, but it extends `Vector` and is synchronized (thread-safe), which makes it unnecessarily slow.

**Best Practice:** Always use the `ArrayDeque` class as your stack implementation in Java.

```java
import java.util.ArrayDeque;
import java.util.Deque;

Deque<Integer> stack = new ArrayDeque<>();

stack.push(10); // [10]
stack.push(20); // [20, 10]
stack.push(30); // [30, 20, 10]

int top = stack.peek(); // 30
int removed = stack.pop(); // Removes and returns 30. Stack is now [20, 10]

boolean empty = stack.isEmpty(); // false
```

## How to Visualize a Stack in Problems

A stack is essentially a **"Waitlist" or "Memory"**.
When you process data sequentially (left to right) and you encounter something that you cannot fully process YET because you need more information from the future, you `push` it onto the stack.

When that future information arrives, you look at the top of the stack (`peek` or `pop`) and resolve the pending items.
