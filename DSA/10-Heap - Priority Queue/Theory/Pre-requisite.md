# 10. Heap / Priority Queue - Pre-requisites

## What is a Heap?

A Heap is a specialized Tree-based data structure (usually implemented as an array) that satisfies the **Heap Property**. It is the data structure used to implement a **Priority Queue**.

1. **Max-Heap:** The value of every parent node is $\ge$ the values of its children. The absolute MAXIMUM value is always at the root.
2. **Min-Heap:** The value of every parent node is $\le$ the values of its children. The absolute MINIMUM value is always at the root.

**It is NOT a fully sorted array.**
A Max-Heap guarantees that the largest element is at index 0. It makes NO guarantees about the exact order of the remaining elements, other than parents being larger than children.

## Why use a Heap instead of Sorting?

If you just need the $K^{th}$ largest element, sorting the array takes $O(N \log N)$ time.
A Heap allows you to extract the largest element in $O(\log N)$ time. If you do this $K$ times, it takes $O(K \log N)$. If $K$ is small compared to $N$, the Heap is much faster!

Furthermore, Heaps are dynamic. You can constantly add new elements and remove the largest/smallest element efficiently.

| Operation | Array (Unsorted) | Array (Sorted) | Heap |
| :--- | :--- | :--- | :--- |
| **Insert** | $O(1)$ | $O(N)$ | $O(\log N)$ |
| **Get Max/Min** | $O(N)$ | $O(1)$ | $O(1)$ |
| **Remove Max/Min**| $O(N)$ | $O(1)$ | $O(\log N)$ |
| **Heapify (Build)**| - | $O(N \log N)$ | $O(N)$ |

## Java `PriorityQueue`

In Java, `PriorityQueue` is a Min-Heap by default.

```java
import java.util.PriorityQueue;

// MIN HEAP (Default)
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
minHeap.offer(5);
minHeap.offer(1);
minHeap.offer(10);
System.out.println(minHeap.poll()); // Prints 1

// MAX HEAP
// We use a custom comparator (a, b) -> b - a (or Integer::compare(b, a))
PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
maxHeap.offer(5);
maxHeap.offer(1);
maxHeap.offer(10);
System.out.println(maxHeap.poll()); // Prints 10
```
