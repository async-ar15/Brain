# Heap / Priority Queue — Revision Sheet

---

## 01. Kth Largest Element in an Array

**In My Words:** Given an integer array `nums` and an integer `k`, return the $k^{th}$ largest element in the array. Note that it is the $k^{th}$ largest element in the sorted order, not the $k^{th}$ distinct element.

**Constraint Whispers:**
- $O(N \log N)$ sorting is trivial, but the interviewer wants to see if you can do better, especially if $K$ is small.
- QuickSelect can achieve $O(N)$ average time, but Heap is $O(N \log K)$ and usually easier to write in an interview.

**The Bridge:** If we use a Min-Heap of size $K$, the heap will eventually hold the $K$ largest elements of the array. The smallest of those $K$ largest elements (the top of the Min-Heap) is exactly the $K^{th}$ largest element overall!

**Optimized Intuition:** Initialize a Min-Heap. Iterate through the array. Add each element. If the heap size exceeds $K$, remove the minimum element (`poll()`). Return the top of the heap.

**Template:** Keep size K

**Time:** $O(N \log K)$ | **Space:** $O(K)$

**Code Solution:**
```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        
        return minHeap.peek();
    }
}
```

---

## 02. Top K Frequent Elements

**In My Words:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

**The Bridge:** We first need the actual frequencies. A HashMap solves that in $O(N)$. Next, we need the "Top K" of those frequencies. That immediately signals a Heap! We can push the map entries into a Min-Heap (sorted by frequency). If size > K, pop. 
*(Alternatively, Bucket Sort achieves strict $O(N)$ time by creating an array of lists where index = frequency).*

**Optimized Intuition (Heap):** 
1. Build frequency map $O(N)$.
2. Create Min-Heap containing map entries, comparing by value (frequency).
3. Push entries, if size > K, poll. $O(U \log K)$ where U is unique elements.
4. Extract K elements from heap.

**Time:** $O(N + U \log K)$ | **Space:** $O(N + K)$

**Code Solution:**
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        
        // Min-Heap sorting by frequency (map.getValue())
        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.getValue(), b.getValue())
        );
        
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = minHeap.poll().getKey();
        }
        return res;
    }
}
```

---

## 03. Last Stone Weight

**In My Words:** You have an array of stones. In each turn, you smash the two heaviest stones together. If they have the same weight, both are destroyed. If different, the smaller is destroyed, and the larger gets `y - x` weight. Return the weight of the last remaining stone (or 0 if none left).

**The Bridge:** We constantly need the TWO MAX elements. After an operation, we insert a NEW element, and need the max again. Sorting doesn't work because inserting into a sorted array is $O(N)$. A Max-Heap can extract max in $O(\log N)$ and insert in $O(\log N)$.

**Optimized Intuition:** Dump all stones into a Max-Heap. While size > 1: pop the top two stones. If they are not equal, push the difference back into the heap. Return the remaining element (if any).

**Time:** $O(N \log N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        // Max-Heap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        
        for (int stone : stones) {
            maxHeap.offer(stone);
        }
        
        while (maxHeap.size() > 1) {
            int y = maxHeap.poll(); // Heaviest
            int x = maxHeap.poll(); // Second heaviest
            
            if (y > x) {
                maxHeap.offer(y - x);
            }
        }
        
        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}
```

---

## 04. Find Median from Data Stream

**In My Words:** Design a data structure that allows adding numbers from a data stream and finding the median of the numbers so far.

**Constraint Whispers:**
- Adding elements to a sorted array takes $O(N)$ per insert. Getting median is $O(1)$.
- Heaps insert in $O(\log N)$. But how do you find the exact *middle* using heaps?

**The Bridge:** The median divides the data into a lower half and an upper half. If we use a **Max-Heap** for the lower half, we have instant access to the largest number of the lower half. If we use a **Min-Heap** for the upper half, we have instant access to the smallest number of the upper half. The median is just the average of these two tops!

**Optimized Intuition:**
- `smallHeap` (Max-Heap): Stores the smaller half of numbers.
- `largeHeap` (Min-Heap): Stores the larger half of numbers.
- **Rule 1 (Order):** Every element in `smallHeap` MUST be $\le$ every element in `largeHeap`.
- **Rule 2 (Size):** The sizes must be equal, or `smallHeap` can have exactly 1 more element than `largeHeap`.
- To insert: add to `smallHeap`. Immediately `poll` from `smallHeap` and `offer` to `largeHeap` (satisfies Rule 1). If `largeHeap` is now bigger than `smallHeap`, `poll` from `largeHeap` and `offer` to `smallHeap` (satisfies Rule 2).
- Median: if sizes are equal, average the two peaks. If not, return `smallHeap` peak.

**Time:** $O(\log N)$ addNum, $O(1)$ findMedian | **Space:** $O(N)$

**Code Solution:**
```java
class MedianFinder {
    private PriorityQueue<Integer> smallHeap; // Max-Heap
    private PriorityQueue<Integer> largeHeap; // Min-Heap

    public MedianFinder() {
        smallHeap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        largeHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        // Step 1: Add to small, then pass the largest in small to large
        smallHeap.offer(num);
        largeHeap.offer(smallHeap.poll());
        
        // Step 2: Ensure smallHeap is always >= largeHeap in size
        if (largeHeap.size() > smallHeap.size()) {
            smallHeap.offer(largeHeap.poll());
        }
    }
    
    public double findMedian() {
        if (smallHeap.size() == largeHeap.size()) {
            return (double) (smallHeap.peek() + largeHeap.peek()) / 2.0;
        } else {
            return smallHeap.peek(); // Since smallHeap is allowed to be 1 element bigger
        }
    }
}
```
