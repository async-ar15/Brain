# Binary Search — Revision Sheet

---

## 01. Binary Search

**In My Words:** Given a sorted array, return the index of a target value, or -1 if it doesn't exist.

**The Bridge:** It's the textbook definition of binary search. Find mid, compare, adjust left/right.

**Template:** Exact Match

**Time:** $O(\log N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        
        return -1;
    }
}
```

---

## 02. Search a 2D Matrix

**In My Words:** Search for a target in an $M \times N$ matrix. The matrix is sorted left-to-right, and the first integer of each row is greater than the last integer of the previous row.

**Constraint Whispers:**
- $M \times N \le 10^4$, required time $O(\log(M \times N))$.

**The Bridge:** Because of the strict sorting rules, this 2D matrix can be perfectly flattened mentally into a 1D sorted array of size $M \times N$. We just need a way to map a 1D index back to 2D coordinates: `row = idx / cols`, `col = idx % cols`.

**Optimized Intuition:** Run standard 1D binary search from index 0 to $M \times N - 1$. Map the 1D `mid` index to a 2D coordinate to get the value.

**Template:** Exact Match

**Time:** $O(\log(M \times N))$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) return false;
        
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        int left = 0;
        int right = rows * cols - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            // Map 1D index to 2D coordinates
            int midValue = matrix[mid / cols][mid % cols];
            
            if (midValue == target) return true;
            else if (midValue < target) left = mid + 1;
            else right = mid - 1;
        }
        
        return false;
    }
}
```

---

## 03. Koko Eating Bananas

**In My Words:** Koko loves bananas. There are $N$ piles. She has $H$ hours to eat them all. Find the minimum integer eating speed $K$ (bananas/hr) that allows her to finish all piles within $H$ hours.

**Constraint Whispers:**
- $H \ge \text{piles.length}$, so she always has at least 1 hour per pile.
- Piles can be up to $10^9$. A linear scan $O(N)$ over speeds will TLE.

**The Bridge:** The array of piles is NOT sorted, but the ANSWER SPACE is. Can she eat them at speed 1? No (False). Speed 2? False. Speed 3? False. Speed 4? True! Speed 5? True! The answer space is `[F, F, F, T, T, T]`. We need to find the **FIRST True**. This is Binary Search on Answer.

**Optimized Intuition:** 
- Min possible speed = 1.
- Max possible speed = max(piles) (since eating faster than the biggest pile doesn't save any more time).
- Binary search between `left = 1` and `right = max(piles)`.
- For a `mid` speed, calculate hours needed: `Math.ceil((double) pile / speed)`.
- If `hours <= H` (True), record it and try a smaller speed (`right = mid - 1`). If `hours > H` (False), try a larger speed (`left = mid + 1`).

**Template:** Finding a Boundary (First True)

**Time:** $O(N \log(\text{max\_pile}))$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 1;
        for (int pile : piles) {
            right = Math.max(right, pile);
        }
        
        int res = right; // Store the best valid speed
        
        while (left <= right) {
            int k = left + (right - left) / 2;
            long hours = 0; // Use long to prevent overflow
            
            for (int pile : piles) {
                hours += Math.ceil((double) pile / k);
            }
            
            if (hours <= h) {
                res = k; // Valid speed! Can we do better (slower)?
                right = k - 1;
            } else {
                left = k + 1; // Too slow, need to eat faster
            }
        }
        
        return res;
    }
}
```

---

## 04. Find Minimum in Rotated Sorted Array

**In My Words:** A sorted array was rotated at some unknown pivot. Find the minimum element in $O(\log N)$ time.

**Constraint Whispers:**
- Must run in $O(\log N)$ time → Strict requirement for Binary Search.

**The Bridge:** Even though the whole array isn't sorted, we can divide it into two sorted portions: a "left sorted portion" and a "right sorted portion". The minimum value is always the first element of the "right sorted portion". If we compare `mid` to `right`, we can figure out which portion we are in.

**Optimized Intuition:** 
- If `nums[mid] > nums[right]`, we are in the left sorted portion. The minimum MUST be to our right. `left = mid + 1`.
- If `nums[mid] <= nums[right]`, we are in the right sorted portion. `mid` itself could be the minimum, so `right = mid`.

**Template:** Finding a Boundary (Modified)

**Gotcha:** Because we use `right = mid`, the loop condition must be `left < right` (no equals), otherwise it can infinite loop.

**Time:** $O(\log N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] > nums[right]) {
                // We are in the left sorted portion
                left = mid + 1;
            } else {
                // We are in the right sorted portion
                // mid might be the minimum, so we don't do mid - 1
                right = mid;
            }
        }
        
        // left and right will converge to the minimum
        return nums[left];
    }
}
```
