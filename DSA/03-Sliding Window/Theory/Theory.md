# Theory - Sliding Window

Sliding Window is an extension of the Same-Direction Two Pointers pattern. It is used to find a contiguous subarray or substring that satisfies a specific condition, while maintaining an $O(N)$ time complexity.

## Where is it commonly used?
- Arrays and Strings.
- Problems asking for the **Maximum/Minimum/Longest/Shortest** contiguous subarray or substring.
- Problems where calculating the condition can be updated incrementally (e.g., sum, product, character frequencies).

## Strong signals to look for
- "Contiguous subarray" or "Substring"
- "Maximum sum of size K"
- "Longest substring with at most K distinct characters"

## When NOT to use Sliding Window
- When the problem asks for a *subsequence* (order matters, but not contiguous).
- When the array has negative numbers AND you are looking for a target sum. (Negative numbers break the monotonic property of the window sum, requiring prefix sums instead).

## The Two Types of Sliding Windows

### 1. Fixed Size Window
The window size is strictly `K`. We expand until we hit size `K`, then we slide the entire window by moving both `left` and `right` at the same time.

**Template (Fixed Size):**
```java
public int fixedWindow(int[] nums, int k) {
    int left = 0;
    int currentSum = 0;
    int maxSum = Integer.MIN_VALUE;

    for (int right = 0; right < nums.length; right++) {
        // 1. Add current element to the window state
        currentSum += nums[right];

        // 2. If the window has reached size K
        if (right - left + 1 == k) {
            // Process the valid window
            maxSum = Math.max(maxSum, currentSum);

            // 3. Remove the element going out of the window
            currentSum -= nums[left];
            left++; // Slide the window
        }
    }
    return maxSum;
}
```

### 2. Variable Size Window
The window size changes. We expand `right` until a condition is violated. Then we shrink `left` until the condition is valid again.

**Template (Variable Size):**
```java
public int variableWindow(int[] nums, int target) {
    int left = 0;
    int currentSum = 0;
    int minLength = Integer.MAX_VALUE;

    for (int right = 0; right < nums.length; right++) {
        // 1. Add current element to the window state
        currentSum += nums[right];

        // 2. While the condition is INVALID (or valid, depending on the problem)
        // Shrink from the left until it's valid again
        while (currentSum >= target) { 
            // Process the valid window before/while shrinking
            minLength = Math.min(minLength, right - left + 1);

            // Remove left element and shrink
            currentSum -= nums[left];
            left++;
        }
    }
    return minLength == Integer.MAX_VALUE ? 0 : minLength;
}
```

# Your interview cheat code

```text
1. Is it an Array or String?
                  ↓
2. Is it asking for a contiguous sequence?
                  ↓
3. Is it asking for a Min/Max/Longest length or target?
                  ↓
           SLIDING WINDOW (O(N) Time, O(1) or O(K) Space)
```
