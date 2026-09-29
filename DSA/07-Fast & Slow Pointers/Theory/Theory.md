# Theory - Fast & Slow Pointers (Floyd's Cycle Detection)

Fast & Slow Pointers is a subset of the Two Pointers pattern, almost exclusively used on Linked Lists and arrays where values act as indices (implicit graphs).

## Where is it commonly used?
1. **Finding the Middle of a Linked List:** A prerequisite step in algorithms like Merge Sort for Linked Lists or Reorder List.
2. **Cycle Detection:** Checking if a Linked List has a loop.
3. **Finding the Start of a Cycle:** Finding the exact node where a loop begins (e.g., Find the Duplicate Number).
4. **Finding the N-th node from the end:** (Usually using a fixed-gap two-pointer approach, closely related).

## Strong signals to look for
- Linked List problems asking for the middle.
- Linked List problems involving cycles/loops.
- Array problems where `1 <= nums[i] <= n` (which implies values can be treated as valid next indices).

## Finding the Cycle Entry Point

This is the famous math trick of Floyd's algorithm.

1. Phase 1: Move `slow` by 1, `fast` by 2 until they meet. This proves a cycle exists.
2. Phase 2: Leave `slow` at the meeting point. Move `fast` back to the `head` of the list.
3. Move BOTH `slow` and `fast` by 1 step at a time. The exact node where they meet again is the start of the cycle!

**Math Intuition:** The distance from the `head` to the cycle start is exactly equal to the distance from the `meeting point` to the cycle start (if you trace the math of the remaining distance).

### Template: Floyd's Cycle Detection

```java
public ListNode detectCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    boolean hasCycle = false;
    
    // Phase 1: Detect Cycle
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            hasCycle = true;
            break;
        }
    }
    
    if (!hasCycle) return null;
    
    // Phase 2: Find the Entry Point
    ListNode slow2 = head;
    while (slow != slow2) {
        slow = slow.next;
        slow2 = slow2.next;
    }
    
    return slow; // The start of the cycle
}
```

# Your interview cheat code

```text
1. Is it a Linked List?
                  ↓
2. Do you need the middle? OR Is there a loop/cycle?
                  ↓
           FAST & SLOW POINTERS (Tortoise & Hare)
```
