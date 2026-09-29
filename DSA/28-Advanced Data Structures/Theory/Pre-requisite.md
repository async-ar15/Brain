# 26. System Design - Pre-requisites

## What is System Design?

In early DSA problems, you are given a massive dataset and asked to write a single algorithm to process it in memory.
In System Design (and Object-Oriented Design) problems, you aren't given a dataset upfront. Instead, you are asked to build a **Class** that will handle a *stream* of data being added, removed, and queried over time.

You are the architect of a mini-database or a specific service.

## The Trade-off

The core theme of every design problem is **Trade-offs**.
You usually have to implement two or three methods. It is often impossible to make all of them $O(1)$ time. 
You must choose which method to optimize based on how often it will be called.

- **Read-Heavy System:** `get()` is called 99% of the time. `add()` is called 1% of the time. You should make `add()` slow ($O(N)$) so that you can pre-calculate the answer and make `get()` incredibly fast ($O(1)$).
- **Write-Heavy System:** `add()` is called 99% of the time. `get()` is rare. You should make `add()` fast ($O(1)$) by just dumping data into a list, and let `get()` do the heavy lifting of searching ($O(N)$).

## Object-Oriented Principles (Java)

When designing classes in Java for interviews:
1. **Encapsulation:** Make your internal data structures `private`.
2. **Initialization:** Always initialize your data structures in the constructor, not inline.
3. **Choosing the right tool:** Knowing Java's built-in collections is half the battle.
   - Need ordered uniqueness? `TreeSet`.
   - Need insertion-order preservation? `LinkedHashMap`.
   - Need $O(1)$ access and $O(1)$ deletion of a random element? `HashMap` + `ArrayList`.
