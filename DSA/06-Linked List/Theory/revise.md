# Linked List — Revision Sheet

---

## 01. Reverse Linked List

**In My Words:** Given the head of a singly linked list, reverse the list, and return the reversed list.

**The Bridge:** As we traverse the list, we need to change each node's `next` pointer to point to the `previous` node. But doing so breaks the link to the rest of the list. So we MUST save the `next` node in a temp variable before breaking the link.

**Optimized Intuition:** Maintain two pointers: `prev` (initially null) and `curr` (initially head). In a loop: save `curr.next`, set `curr.next = prev`, step forward by setting `prev = curr` and `curr = saved_next`. When `curr` is null, `prev` will be the new head.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode nxt = curr.next; // Save next node
            curr.next = prev;         // Reverse pointer
            prev = curr;              // Move prev forward
            curr = nxt;               // Move curr forward
        }
        
        return prev;
    }
}
```

---

## 02. Merge Two Sorted Lists

**In My Words:** Merge two sorted linked lists into one sorted linked list.

**The Bridge:** Just like merging two sorted arrays, we need two pointers, one for each list. We compare the values and attach the smaller one to our new merged list.

**Optimized Intuition:** Create a `Dummy Node`. Create a `tail` pointer pointing to the dummy. While both lists are not null, compare `list1.val` and `list2.val`. Point `tail.next` to the smaller one, and advance that list's pointer. Advance `tail`. Once the loop breaks, one list might still have remaining nodes; just append the remainder to `tail.next`.

**Template:** Dummy Node

**Time:** $O(N + M)$ | **Space:** $O(1)$ (we are just rewiring existing nodes)

**Code Solution:**
```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        
        // Attach whatever is left
        if (list1 != null) tail.next = list1;
        else if (list2 != null) tail.next = list2;
        
        return dummy.next;
    }
}
```

---

## 03. Remove Nth Node From End of List

**In My Words:** Remove the $N^{th}$ node from the end of the list and return its head.

**Constraint Whispers:**
- Can you do it in one pass?

**Brute Force:** Pass 1 to find the length of the list. Pass 2 to remove the $(Length - N)^{th}$ node. $O(N)$ time, two passes.

**The Bridge:** We want a pointer to end up exactly right BEFORE the node we want to delete. If we have a `fast` pointer that is exactly $N+1$ steps ahead of a `slow` pointer, when `fast` reaches the end (null), `slow` will be pointing exactly to the node BEFORE the target node.

**Optimized Intuition:** Use a Dummy Node (because we might delete the head itself!). `slow` and `fast` both start at dummy. Move `fast` forward $N+1$ times. Then move both `slow` and `fast` one step at a time until `fast == null`. Now, `slow` is exactly where we need it. Set `slow.next = slow.next.next`.

**Time:** $O(N)$ (One pass) | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode slow = dummy;
        ListNode fast = dummy;
        
        // Move fast ahead by n + 1 steps
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }
        
        // Move both at the same speed
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        
        // Skip the target node
        slow.next = slow.next.next;
        
        return dummy.next;
    }
}
```

---

## 04. Reorder List

**In My Words:** Given a list `L0 -> L1 -> ... -> Ln-1 -> Ln`, reorder it to `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ...`

**The Bridge:** This looks complicated but it's just a combination of three standard algorithms:
1. Find the middle of the list.
2. Reverse the second half of the list.
3. Merge the two halves back together, taking one node from each alternately.

**Optimized Intuition:**
- Use Fast/Slow pointers to find the middle (Slow will land on the middle).
- Disconnect the two halves (`slow.next = null`).
- Reverse the second half using the standard reversal algorithm.
- Merge the two halves (`list1 = head`, `list2 = reversedHead`) by alternating pointers.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        
        // 1. Find middle
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // 2. Reverse second half
        ListNode second = slow.next;
        slow.next = null; // Split the lists
        
        ListNode prev = null;
        while (second != null) {
            ListNode nxt = second.next;
            second.next = prev;
            prev = second;
            second = nxt;
        }
        
        // 3. Merge alternating
        ListNode first = head;
        second = prev; // Head of reversed second half
        
        while (second != null) {
            ListNode tmp1 = first.next;
            ListNode tmp2 = second.next;
            
            first.next = second;
            second.next = tmp1;
            
            first = tmp1;
            second = tmp2;
        }
    }
}
```
