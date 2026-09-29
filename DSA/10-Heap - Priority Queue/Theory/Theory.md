# Theory - Heap / Priority Queue

Heaps are the ultimate solution for **"Top K"** problems or problems where you constantly need access to the running maximum or minimum of a dynamic data set.

## Where is it commonly used?
1. **Top K Elements:** Kth largest element in an array, Top K frequent elements, K closest points to origin.
2. **Merging K Sorted Lists:** Combining multiple sorted structures into one.
3. **Running Median:** Maintaining the median of a stream of numbers (using Two Heaps).
4. **Dijkstra's Shortest Path:** The core data structure for finding the nearest unvisited node in $O(\log V)$.

## Strong signals to look for
- "Find the **$K^{th}$ largest / smallest** element."
- "Find the **Top K** frequent elements."
- The data is arriving in a **stream**, and you need to constantly output the max/min/median.
- You need to repeatedly extract the min/max and re-insert a modified value (e.g., Last Stone Weight).

## The "Keep size K" Pattern

If a problem asks for the "$K^{th}$ largest element", you don't need a Max-Heap of size $N$. 
Instead, you can use a **Min-Heap of size K**.

Wait, a Min-Heap for the largest elements? YES!
1. Add elements to the Min-Heap.
2. If the size of the heap exceeds $K$, `poll()` (remove) the top element.
3. Because it's a Min-Heap, you just removed the SMALLEST element from the heap.
4. What's left in the heap? The $K$ largest elements! And the top of the Min-Heap is exactly the $K^{th}$ largest.

Why do this? Because maintaining a heap of size $K$ takes $O(\log K)$ per insertion, instead of $O(\log N)$.
Total time: $O(N \log K)$. If $K \ll N$, this is massive.

### Template: Top K Pattern

```java
public int findKthLargest(int[] nums, int k) {
    // Min-Heap
    PriorityQueue<Integer> heap = new PriorityQueue<>();
    
    for (int num : nums) {
        heap.offer(num);
        
        // If heap size exceeds K, evict the smallest element
        if (heap.size() > k) {
            heap.poll();
        }
    }
    
    // The top of the Min-Heap is the Kth largest element
    return heap.peek();
}
```

## Custom Objects in Priority Queue

Often, you need to store objects or arrays in the heap (e.g., frequencies, distances). You MUST provide a custom comparator.

```java
// Example: Storing [value, frequency] arrays, sorted by frequency ascending
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));

// Example: Storing custom Point objects, sorted by distance to origin
PriorityQueue<Point> pq = new PriorityQueue<>((p1, p2) -> 
    Integer.compare(p1.x * p1.x + p1.y * p1.y, p2.x * p2.x + p2.y * p2.y)
);
```

# Your interview cheat code

```text
1. Are you looking for Top K, Kth smallest/largest?
                  ↓
2. Do you need to constantly access max/min in a changing dataset?
                  ↓
           HEAP / PRIORITY QUEUE (O(N log K) Time)
```
