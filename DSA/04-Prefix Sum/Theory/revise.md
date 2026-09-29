# Prefix Sum — Revision Sheet

---

## 01. Running Sum of 1D Array

**In My Words:** Given an array `nums`, return an array where `result[i]` is the sum of all elements from `nums[0]` to `nums[i]`.

**The Bridge:** This is the absolute basics of Prefix Sum. You just keep adding the current element to the sum of the previous elements.

**Optimized Intuition:** We can even modify the array in place since `nums[i] = nums[i-1] + nums[i]`.

**Time:** $O(N)$ | **Space:** $O(1)$ (in-place)

**Code Solution:**
```java
class Solution {
    public int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] = nums[i - 1] + nums[i];
        }
        return nums;
    }
}
```

---

## 02. Range Sum Query - Immutable

**In My Words:** Design a class that initializes with an integer array, and can answer multiple queries for the sum of elements between indices `left` and `right` inclusive.

**Constraint Whispers:**
- The class will be instantiated once, and `sumRange` will be called multiple times. 
- $10^4$ calls to `sumRange`. A loop inside `sumRange` gives $O(N \times Q)$ → TLE.

**The Bridge:** Since the array doesn't change (immutable), we can spend $O(N)$ time upfront in the constructor to calculate a prefix sum array. Then, every query takes $O(1)$ time.

**Optimized Intuition:** Create `prefix[]`. `prefix[i]` stores sum of `nums[0...i-1]`. So `sumRange(L, R)` is just `prefix[R + 1] - prefix[L]`.

**Time:** $O(N)$ init, $O(1)$ query | **Space:** $O(N)$

**Code Solution:**
```java
class NumArray {
    private int[] prefix;

    public NumArray(int[] nums) {
        // Size N+1 to easily handle left = 0 without out of bounds checks
        prefix = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
}
```

---

## 03. Subarray Sum Equals K

**In My Words:** Given an array of integers and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

**Constraint Whispers:**
- Array can contain negative numbers! (Sliding Window is instantly disqualified because shrinking the window doesn't guarantee the sum will decrease).

**Brute Force:** Two nested loops to calculate the sum of every possible subarray. $O(N^2)$ time.

**The Bridge:** We need to find how many times a subarray ending at index `i` sums to `K`. If `Prefix[i] - Prefix[j] = K`, then the subarray from `j+1` to `i` sums to `K`. Rearranging the equation: `Prefix[j] = Prefix[i] - K`. We just need to know how many times we've seen `Prefix[i] - K` in the past!

**Optimized Intuition:** Use a HashMap to store `<Prefix Sum, Frequency>`. Iterate through the array, tracking the running sum. Check if `runningSum - k` is in the map. If yes, add its frequency to our total count. Finally, add the current `runningSum` to the map.

**Gotcha:** Must initialize map with `<0, 1>` to account for subarrays that start from index 0.

**Time:** $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int runningSum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        // Crucial base case: A sum of 0 exists 1 time (empty prefix)
        map.put(0, 1);
        
        for (int i = 0; i < nums.length; i++) {
            runningSum += nums[i];
            
            // Check if (runningSum - k) exists in the map
            int requiredPrefix = runningSum - k;
            if (map.containsKey(requiredPrefix)) {
                count += map.get(requiredPrefix);
            }
            
            // Add current runningSum to map
            map.put(runningSum, map.getOrDefault(runningSum, 0) + 1);
        }
        
        return count;
    }
}
```

---

## 04. Find Pivot Index

**In My Words:** Find the index where the sum of all elements to the left is strictly equal to the sum of all elements to the right.

**The Bridge:** Total Sum = Left Sum + Pivot + Right Sum. Therefore, Right Sum = Total Sum - Left Sum - Pivot. If we precalculate the Total Sum, we can just maintain a Left Sum as we iterate and check if `Left Sum == Total Sum - Left Sum - nums[i]`.

**Optimized Intuition:** Calculate total sum first $O(N)$. Iterate tracking left sum. If `leftSum == totalSum - leftSum - nums[i]`, return index. Else `leftSum += nums[i]`.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        
        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            int rightSum = totalSum - leftSum - nums[i];
            
            if (leftSum == rightSum) {
                return i;
            }
            
            leftSum += nums[i];
        }
        
        return -1;
    }
}
```
