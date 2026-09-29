# 1D Dynamic Programming — Revision Sheet

---

## 01. Climbing Stairs

**In My Words:** You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**The Bridge:** If you are at step `n`, how did you get there? You either took a 1-step from `n-1`, or a 2-step from `n-2`. So, `ways(n) = ways(n-1) + ways(n-2)`. This is literally the Fibonacci sequence.

**Optimized Intuition:** We don't need a full array, just the last two values. `one = 1` (ways to reach step 1), `two = 1` (ways to reach step 0). Loop `n-1` times. `temp = one + two`, `two = one`, `one = temp`. Return `one`.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int climbStairs(int n) {
        int one = 1;
        int two = 1;
        
        for (int i = 0; i < n - 1; i++) {
            int temp = one + two;
            two = one;
            one = temp;
        }
        
        return one;
    }
}
```

---

## 02. House Robber

**In My Words:** You are a robber planning to rob houses. You cannot rob two adjacent houses. Find the maximum amount of money you can rob tonight without alerting the police.

**The Bridge:** At house `i`, you have a choice. Rob it (which means you add `nums[i]` to the max money from house `i-2`), OR skip it (which means your max money is whatever it was at house `i-1`). `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`.

**Optimized Intuition:** Use two variables to represent `i-1` (`rob2`) and `i-2` (`rob1`). Iterate through array. `temp = max(nums[i] + rob1, rob2)`. Shift pointers: `rob1 = rob2`, `rob2 = temp`. Return `rob2`.

**Template:** 1D DP with Memory Optimization

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int rob(int[] nums) {
        int rob1 = 0;
        int rob2 = 0;
        
        for (int n : nums) {
            int temp = Math.max(n + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        
        return rob2;
    }
}
```

---

## 03. Word Break

**In My Words:** Given a string `s` and a dictionary of strings `wordDict`, return true if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**The Bridge:** Is it possible to segment `s` starting at index `i`? It is ONLY possible if there exists a dictionary word that matches a substring starting at `i` (let's say of length `L`), AND it is also possible to segment the rest of the string starting at `i + L`.

**Optimized Intuition:** Let's do this Bottom-Up. `dp[i]` is true if the substring from `i` to the end can be segmented. 
`dp[s.length()] = true` (Base case: empty string is valid).
Loop `i` BACKWARDS from `s.length() - 1` down to `0`.
For each `i`, loop through every word `w` in `wordDict`.
If the substring starting at `i` matches `w`, then `dp[i] = dp[i + w.length()]`. If it's true, `break` (we found a valid path, no need to check other words for this `i`).
Return `dp[0]`.

**Time:** $O(N^2 \cdot M)$ where N is string length, M is max word length | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[s.length()] = true; // Base case
        
        for (int i = s.length() - 1; i >= 0; i--) {
            for (String w : wordDict) {
                if (i + w.length() <= s.length() && s.substring(i, i + w.length()).equals(w)) {
                    dp[i] = dp[i + w.length()];
                }
                if (dp[i]) {
                    break; // If we found a valid path from i, move to i-1
                }
            }
        }
        
        return dp[0];
    }
}
```

---

## 04. Longest Increasing Subsequence

**In My Words:** Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**The Bridge:** For any element `nums[i]`, what is the longest increasing subsequence that ENDS at `i`? It is `1` (itself), PLUS the longest increasing subsequence ending at some index `j` (where `j < i`), strictly IF `nums[i] > nums[j]`.

**Optimized Intuition ($O(N^2)$ DP):** Initialize `dp` array of size $N$ with `1`s (every element is a subsequence of length 1). Loop `i` from 1 to $N-1$. Loop `j` from 0 to `i-1`. If `nums[i] > nums[j]`, update `dp[i] = Math.max(dp[i], 1 + dp[j])`. Keep a global max of `dp[i]`.

*(Note: There is a famous $O(N \log N)$ Binary Search solution, but the DP solution is the standard expectation for this topic).*

**Time:** $O(N^2)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        
        int maxLength = 1;
        
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], 1 + dp[j]);
                }
            }
            maxLength = Math.max(maxLength, dp[i]);
        }
        
        return maxLength;
    }
}
```
