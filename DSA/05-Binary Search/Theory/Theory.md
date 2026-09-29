# Theory - Binary Search

Binary Search isn't just for finding a number in a sorted array. It's an algorithm for **searching a monotonic search space**.

## Where is it commonly used?
1. **Classic Search:** Finding an element in a sorted array (or a 2D matrix that is sorted).
2. **Finding Boundaries:** Finding the first or last occurrence of a condition.
3. **Binary Search on Answer:** The problem asks for the "minimum maximum" or "maximum minimum" of something (e.g., Koko Eating Bananas).

## Strong signals to look for
- Array is **sorted**.
- "Find the minimum possible value such that..."
- "Find the maximum possible value such that..."
- Required time complexity is explicitly or implicitly $O(\log N)$.

## The Two Templates of Binary Search

There are two primary ways to write Binary Search, depending on what you are trying to find.

### Template 1: Exact Match (Find a specific value)
Used when you are looking for an exact target and want to return its index.

```java
public int exactMatch(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) { // Note the <=
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // Not found
}
```

### Template 2: Finding a Boundary (First True)
Used when the search space consists of a series of `false` followed by `true` (e.g., `[F, F, F, T, T, T]`), and you want to find the **first** `true`. This is deeply tied to "Binary Search on Answer".

```java
public int findBoundary(int[] nums) {
    int left = 0;
    int right = nums.length - 1;
    int result = -1; // Store the best answer so far

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (isConditionTrue(nums[mid])) {
            result = mid; // This might be the answer, record it
            right = mid - 1; // Try to find an even earlier 'true' (move left)
        } else {
            left = mid + 1; // Condition is false, the 'true' must be to the right
        }
    }
    return result;
}
```

## Binary Search on Answer
Sometimes the array isn't sorted, but the **answer space** is. 
For example, if you can eat bananas at speed $K$, can you finish all bananas in $H$ hours?
- If you can finish them at speed 5, you can definitely finish them at speed 6, 7, 8 (Monotonic: `[F, F, F, T, T, T]`).
- The problem asks for the MINIMUM speed, which means finding the *first* `True` in that boolean array!

# Your interview cheat code

```text
1. Is the array sorted? OR
2. Does the answer space have a "False False True True" (Monotonic) pattern?
                  ↓
3. Am I looking for an exact match or a boundary (min/max)?
                  ↓
           BINARY SEARCH (O(log N) Time)
```
