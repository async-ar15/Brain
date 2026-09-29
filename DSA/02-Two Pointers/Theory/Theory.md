# Theory - Two Pointers pattern

We use two pointers/references to traverse or compare elements in a controlled way, so we can avoid unnecessary nested loops. Using this approach, you can reduce the time complexity of many array and string problems from $O(n^2)$ to $O(n)$, or to $O(n \log n)$ when sorting is required first.

## Where is it commonly used?
A Two-Pointer algorithm is generally applied to linear data structures:
- Arrays
- Strings
- Linked Lists

Especially when the data is sorted or can be sorted.

## Strong signals to look for (When to use Two Pointers)
1. **Sorted array with pair/triplet finding:** Find a pair with a given condition (e.g. Two Sum II, 3Sum).
2. **In-place array modification:** Remove duplicates, rearrange or partition elements without using extra space.
3. **Palindrome or symmetry checking:** Compare elements from both ends.
4. **Subarray problems with monotonic conditions:** Closest pair / maximum area type problems (e.g. Container With Most Water).

## Sorting is a big clue
If the array can be sorted, Two Pointers often becomes much easier because sorting gives us a direction for pointer movement (Monotonicity).
- If the sum is too small, move left pointer to increase it.
- If the sum is too big, move right pointer to decrease it.

## Common Two-Pointer structures & Variants

### 1. Opposite direction (Converging Pointers)

```text
L →        ← R
[1  2  3  4  5  6]
```
One pointer starts at the beginning, the other at the end. They adjust based on comparisons.

**Think:** Pair Sum, Palindrome, Container With Most Water.

```java
public void oppositeDirectionTemplate(int[] nums) {
    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
        int sum = nums[left] + nums[right];

        if (sum == target) {
            return;
        } else if (sum < target) {
            left++; // Need a bigger number
        } else {
            right--; // Need a smaller number
        }
    }
}
```

### 2. Same direction (Fast/Slow or Read/Write)

```text
slow → 
fast → 
[1  2  3  4  5  6]
```
Both pointers start at the same end. One is a read pointer (fast) and the other is a write/boundary pointer (slow).

**Think:** Removing duplicates, Move Zeroes.

```java
public int sameDirectionTemplate(int[] nums) {
    int slow = 0; // Tracks where to write

    for (int fast = 0; fast < nums.length; fast++) {
        if (shouldKeep(nums[fast])) {
            nums[slow] = nums[fast];
            slow++;
        }
    }
    return slow; // The new length
}
```

# Your interview cheat code

```text
1. Is it an Array / String / Linked List?
                  ↓
2. Is there a Pair / Triplet / Quadruplet?
                  ↓
3. Is the data sorted or can sorting help?
                  ↓
4. Am I comparing elements from opposite ends?
                  ↓
           TWO POINTERS (O(N) Time, O(1) Space)
```
