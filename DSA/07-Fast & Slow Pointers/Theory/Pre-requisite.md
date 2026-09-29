# 07. Fast & Slow Pointers - Pre-requisites

## The "Two Runners" Analogy

Imagine two runners on a track.
- **Slow Runner (Tortoise):** Takes 1 step at a time.
- **Fast Runner (Hare):** Takes 2 steps at a time.

### Finding the Middle

If the track is a straight line, what happens when the Fast Runner reaches the finish line?
Because the Fast Runner is moving exactly twice as fast, the Slow Runner must be exactly halfway through the track!

This is the standard algorithm to find the middle of a Linked List in one pass.

### Detecting a Cycle (Floyd's Algorithm)

What if the track is a circle?
- The Fast Runner will keep going in circles.
- The Slow Runner will eventually enter the circle.
- Since the Fast Runner is faster, he will eventually "lap" the Slow Runner.
- If they ever meet at the exact same spot, it **proves** there is a cycle. If the Fast Runner reaches a dead end (`null`), there is no cycle.

## Pointer Mechanics in Java

When setting up Fast & Slow pointers, we usually initialize them both at the `head` of the list.

```java
ListNode slow = head;
ListNode fast = head;
```

**Crucial Loop Condition for Fast & Slow:**
Because `fast` is taking two steps (`fast.next.next`), you MUST ensure that `fast` is not null AND `fast.next` is not null before taking the steps. Otherwise, you will get a `NullPointerException`.

```java
while (fast != null && fast.next != null) {
    slow = slow.next;         // 1 step
    fast = fast.next.next;    // 2 steps
}
```
