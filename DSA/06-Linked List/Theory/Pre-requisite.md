# 06. Linked List - Pre-requisites

## What is a Linked List?

A Linked List is a linear data structure where elements are not stored in contiguous memory locations. Instead, each element (node) contains two things:
1. The **Data** (value).
2. A **Pointer** (or reference) to the memory address of the next node in the sequence.

### Arrays vs Linked Lists

| Feature | Arrays | Linked Lists |
| :--- | :--- | :--- |
| **Memory Allocation** | Contiguous block | Scattered nodes |
| **Random Access** | $O(1)$ (e.g. `arr[4]`) | $O(N)$ (Must traverse from Head) |
| **Insert/Delete at Head**| $O(N)$ (Requires shifting) | $O(1)$ (Just change pointers) |
| **Size** | Fixed (unless Dynamic) | Dynamic (Grows/Shrinks on the fly) |

## The Node Definition

In Java, a node is just an object defined by a simple class. You will see this exact class in almost every LeetCode problem.

```java
public class ListNode {
    int val;
    ListNode next;
    
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
```

## Traversing a Linked List

You NEVER want to lose the `head` pointer. If you move `head`, you lose access to the start of the list. Always create a dummy pointer (usually called `curr` or `current`) to traverse.

```java
// How to print all elements in a Linked List
ListNode curr = head;
while (curr != null) {
    System.out.println(curr.val);
    curr = curr.next; // Move to the next node
}
```

## Types of Linked Lists
1. **Singly Linked List:** `A -> B -> C -> null`. Nodes only point forward.
2. **Doubly Linked List:** `A <-> B <-> C`. Nodes point forward AND backward (has a `prev` pointer).
3. **Circular Linked List:** The last node points back to the head `A -> B -> C -> A`. (Detecting this is the famous Floyd's Cycle Detection algorithm).
