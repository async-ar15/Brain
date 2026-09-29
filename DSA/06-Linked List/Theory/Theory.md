# Theory - Linked List

Working with Linked Lists is almost entirely about **Pointer Manipulation**. The logic is rarely complex mathematically; the difficulty comes from changing pointers in the correct order without breaking the chain or causing a `NullPointerException`.

## Where is it commonly used?
- Implementing Stacks and Queues.
- Reversing segments of data efficiently.
- Detecting cycles in data.
- LRU Caches (using Doubly Linked Lists).

## The Dummy Node Pattern

This is the single most important trick in Linked List problems.

Many problems ask you to modify a list in a way that might change the `head` (e.g., removing the first node, merging lists). Dealing with the edge case of "what if the head changes?" requires annoying `if` statements.

**The Solution:** Create a `Dummy Node` that points to the head. You do all your operations on `dummy.next`. At the end, you just return `dummy.next`!

```java
public ListNode dummyNodeTemplate(ListNode head) {
    ListNode dummy = new ListNode(0); // Value doesn't matter
    dummy.next = head;
    
    ListNode prev = dummy;
    ListNode curr = head;
    
    while (curr != null) {
        // Do pointer manipulation
        // prev gives you access to the node BEFORE curr
    }
    
    return dummy.next; // Safely returns the (possibly new) head
}
```

## The "Save the Next Node" Rule

When reversing a list or changing where a node points, the moment you do `curr.next = newTarget`, you have **destroyed** the link to the rest of the list!

You MUST save the original next node in a temporary variable before changing pointers.

```java
// Reversing a linked list snippet
ListNode curr = head;
ListNode prev = null;

while (curr != null) {
    ListNode nextNode = curr.next; // 1. SAVE THE NEXT NODE!
    
    curr.next = prev;              // 2. REVERSE THE POINTER
    
    prev = curr;                   // 3. MOVE PREV FORWARD
    curr = nextNode;               // 4. MOVE CURR FORWARD (using saved node)
}
```

## Fast and Slow Pointers (Tortoise and Hare)

We will cover this extensively in Day 7, but it is heavily used in Linked List problems to:
- Find the middle of a list (Fast moves 2x, Slow moves 1x. When Fast hits the end, Slow is in the middle).
- Detect cycles (If Fast overtakes Slow, there is a cycle).

# Your interview cheat code

```text
1. Are you changing the structure of the list (deleting/reordering)?
                  ↓
           USE A DUMMY NODE
           
2. Are you changing where a node points?
                  ↓
           SAVE `curr.next` IN A TEMP VARIABLE FIRST
```
