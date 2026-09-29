# 03. Sliding Window - Pre-requisites

## Subarrays vs Subsequences

Before learning sliding window, you must understand the difference between contiguous and non-contiguous segments of an array.

1. **Subarray / Substring (Contiguous)**
   - Elements must be next to each other in the original array.
   - Example: `[1, 2, 3]` from `[1, 2, 3, 4]` is valid.
   - Example: `[1, 3, 4]` is **INVALID** because they are not adjacent.
   - **This is where Sliding Window shines.**

2. **Subsequence (Non-contiguous)**
   - Elements can skip indices but must maintain relative order.
   - Example: `[1, 3, 4]` from `[1, 2, 3, 4]` is valid.
   - **Sliding Window DOES NOT work for subsequences.**

## The Concept of a "Window"

A "window" is simply a subarray defined by two pointers, usually `left` and `right`.
- **Window Size** = `right - left + 1`
- **Expanding the window**: Move `right` pointer forward.
- **Shrinking the window**: Move `left` pointer forward.

## State Tracking (The Window's Memory)

To avoid $O(N^2)$ time, we never recalculate the window from scratch. Instead, we maintain a "state" (like a running sum, or a HashMap of character counts) and update it as the window shifts.

- When `right` expands: Add the new element to the state.
- When `left` shrinks: Remove the old element from the state.

```java
// Example of maintaining a running sum
int runningSum = 0;
runningSum += nums[right]; // Expanding
runningSum -= nums[left];  // Shrinking
```
