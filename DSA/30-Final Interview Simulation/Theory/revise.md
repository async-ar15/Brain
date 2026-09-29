# Final Interview Simulation — Revision Sheet

---

## 30-Day Recap: The Core Patterns

If you can recognize these patterns, you can pass any DSA interview.

1. **Sliding Window:** Array/String problem asking for the *longest/shortest* contiguous subarray or substring satisfying a condition.
2. **Two Pointers:** Array is *sorted*, asking for pairs that sum to a target, or removing duplicates in-place.
3. **Fast & Slow Pointers:** Linked List cycle detection, finding the middle of a Linked List.
4. **Merge Intervals:** Given start and end times, sort by start time, and merge if `current.start <= previous.end`.
5. **Cyclic Sort:** Array contains numbers in a given range (e.g., 1 to N). Place every number at its correct index `i = nums[i] - 1`.
6. **In-place Reversal of a LinkedList:** `prev = null`, `curr = head`. Loop: `next = curr.next`, `curr.next = prev`, `prev = curr`, `curr = next`.
7. **Tree BFS:** Level-order traversal using a Queue.
8. **Tree DFS:** Finding depth, paths, or checking properties recursively (Pre-order, In-order, Post-order).
9. **Two Heaps:** Finding the median of a number stream (Max-Heap for lower half, Min-Heap for upper half).
10. **Subsets / Permutations:** Backtracking. `DO -> RECURSE -> UNDO`.
11. **Modified Binary Search:** Array is sorted but rotated, or finding bounds. 
12. **Top 'K' Elements:** Use a Min-Heap of size K.
13. **K-way Merge:** Merging multiple sorted arrays/lists using a Min-Heap.
14. **0/1 Knapsack (DP):** Given items with weights and values, find maximum value within a capacity. `dp[i][c] = max(include, exclude)`.
15. **Topological Sort:** Given directed dependencies (A must happen before B). Use Kahn's Algorithm (In-Degree Array + Queue).

## Final Affirmation

I have practiced consistently.
I understand the underlying concepts, not just memorized code.
I can communicate my technical thoughts clearly.
I am ready for the interview. 

**Go get that offer!**
