# Fast & Slow Pointers — Revision Sheet

---

## 01. Linked List Cycle

**In My Words:** Given `head`, determine if the linked list has a cycle in it.

**The Bridge:** If two runners are on a circular track, the faster one will eventually lap the slower one. If the track is straight, the fast one finishes.

**Optimized Intuition:** `slow` takes 1 step, `fast` takes 2 steps. If `fast` ever equals `slow` (comparing nodes by reference), return true. If `fast` hits null, return false.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) return true;
        }
        
        return false;
    }
}
```

---

## 02. Middle of the Linked List

**In My Words:** Given the `head` of a linked list, return the middle node. If there are two middle nodes, return the second middle node.

**The Bridge:** If `fast` moves twice as fast as `slow`, when `fast` reaches the end, `slow` must be at the halfway point.

**Optimized Intuition:** Standard fast & slow template. Because we want the *second* middle node for even lengths, we just use the standard `fast != null && fast.next != null` condition, which naturally leaves `slow` on the second middle node.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow; // The middle
    }
}
```

---

## 03. Find the Duplicate Number

**In My Words:** Given an array of integers `nums` containing $n + 1$ integers where each integer is in the range $[1, n]$, there is only one duplicate number. Find it without modifying the array and using $O(1)$ space.

**Constraint Whispers:**
- $O(1)$ space $\rightarrow$ no HashSets.
- No modifying array $\rightarrow$ no sorting!
- Values are in $[1, n]$ $\rightarrow$ They are valid indices!

**The Bridge:** Because the values are valid indices, the array is essentially a Linked List. `nums[i]` is a pointer to the next index. Because there are $n+1$ values in $n$ slots, by the Pigeonhole Principle, multiple indices point to the SAME next index. That forms a cycle! The start of the cycle is the duplicate number.

**Optimized Intuition:** Apply Floyd's Cycle Detection. Phase 1: `slow = nums[slow]`, `fast = nums[nums[fast]]`. Phase 2: Once they meet, reset `slow2 = 0`. Move `slow` and `slow2` by 1 step until they meet. That meeting point is the cycle start (the duplicate).

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int findDuplicate(int[] nums) {
        // Phase 1: Detect cycle
        int slow = 0, fast = 0;
        
        // We use a do-while loop because they both start at 0
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        // Phase 2: Find cycle start (the duplicate)
        int slow2 = 0;
        while (slow != slow2) {
            slow = nums[slow];
            slow2 = nums[slow2];
        }
        
        return slow;
    }
}
```

---

## 04. Happy Number

**In My Words:** Write an algorithm to determine if a number `n` is happy. A happy number is replaced by the sum of the squares of its digits until it equals 1, or it loops endlessly.

**The Bridge:** A number "looping endlessly" means it enters a cycle. Generating the next number (sum of squares of digits) is exactly like finding the `next` node in a linked list!

**Optimized Intuition:** Use fast and slow pointers. `slow` generates the next number once. `fast` generates the next number twice. If `fast == 1`, it's happy. If `fast == slow`, we are stuck in a cycle (not happy).

**Time:** $O(\log N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = getNext(n);
        
        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        
        return fast == 1;
    }
    
    private int getNext(int n) {
        int totalSum = 0;
        while (n > 0) {
            int d = n % 10;
            n = n / 10;
            totalSum += d * d;
        }
        return totalSum;
    }
}
```
