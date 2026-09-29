# 2D Dynamic Programming — Revision Sheet

---

## 01. Unique Paths

**In My Words:** A robot is located at the top-left corner of an $m \times n$ grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?

**The Bridge:** If you are at cell `(r, c)`, the only ways to get there are from the cell above `(r-1, c)` or the cell to the left `(r, c-1)`. Therefore, the number of unique paths to reach `(r, c)` is exactly the sum of the unique paths to reach the cell above PLUS the cell to the left. `dp[r][c] = dp[r-1][c] + dp[r][c-1]`.

**Optimized Intuition:** Initialize an $m \times n$ array with 1s in the first row and first column (there is only 1 way to travel purely right or purely down). Loop `r` from 1 to m-1, `c` from 1 to n-1. `dp[r][c] = dp[r-1][c] + dp[r][c-1]`. Return `dp[m-1][n-1]`.

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$ (can be optimized to $O(N)$ with 1D array)

**Code Solution:**
```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        // Base cases: first row and first col are 1
        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        
        return dp[m - 1][n - 1];
    }
}
```

---

## 02. Longest Common Subsequence

**In My Words:** Given two strings `text1` and `text2`, return the length of their longest common subsequence.

**The Bridge:** This is the exact template problem for String DP. If the characters match, `1 + dp[i+1][j+1]`. If they don't, `max(dp[i+1][j], dp[i][j+1])`.

**Optimized Intuition:** Initialize `dp[m+1][n+1]` with 0s. Iterate backwards. If match: diagonal + 1. Else: max of right and down. Return `dp[0][0]`.

**Template:** String Comparison 2D DP

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$ (can be optimized to $O(\min(M, N))$ space)

**Code Solution:**
```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1]; // +1 handles out of bounds / empty string cases
        
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        
        return dp[0][0];
    }
}
```

---

## 03. Edit Distance

**In My Words:** Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. Operations: Insert, Delete, Replace character.

**The Bridge:** If characters match, cost is 0, just move both pointers (Diagonal). If they don't match, we have 3 choices:
1. Insert: Advance `word2` pointer, cost 1. (Right cell)
2. Delete: Advance `word1` pointer, cost 1. (Down cell)
3. Replace: Advance both pointers, cost 1. (Diagonal cell)
We want the `min` of these three choices + 1!

**Optimized Intuition:** Bottom-up matrix `dp[m+1][n+1]`. Base cases are the edges: converting a string to an empty string requires exactly string.length deletions. So `dp[m][j] = n - j`, `dp[i][n] = m - i`. Loop backwards. If match: `dp[i][j] = dp[i+1][j+1]`. Else: `dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])`.

**Time:** $O(M \cdot N)$ | **Space:** $O(M \cdot N)$

**Code Solution:**
```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        
        // Base cases: transforming to/from empty string
        for (int i = 0; i <= m; i++) dp[i][n] = m - i;
        for (int j = 0; j <= n; j++) dp[m][j] = n - j;
        
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (word1.charAt(i) == word2.charAt(j)) {
                    dp[i][j] = dp[i + 1][j + 1]; // Cost is 0, advance both
                } else {
                    // 1 + min(Delete, Insert, Replace)
                    dp[i][j] = 1 + Math.min(dp[i + 1][j], // Delete (advance word1)
                                   Math.min(dp[i][j + 1], // Insert (advance word2)
                                            dp[i + 1][j + 1])); // Replace (advance both)
                }
            }
        }
        
        return dp[0][0];
    }
}
```

---

## 04. Target Sum

**In My Words:** You are given an integer array `nums` and an integer `target`. You want to build an expression out of `nums` by adding one of the symbols '+' and '-' before each integer in `nums`. Return the number of different expressions that evaluate to `target`.

**Constraint Whispers:**
- Classic 0/1 Knapsack variation. Every item has two choices: Add or Subtract.

**The Bridge:** The recursive state needs index `i` and `currentSum`. So it's a 2D DP. However, a traditional matrix is hard because `currentSum` can be negative! Instead of a matrix, we can use a HashMap (Memoization) or arrays with an offset. The elegant Knapsack reduction changes this to finding a subset of `nums` that equals a specific positive sum.

**Optimized Intuition (Memoization with Map):**
Helper `dfs(i, currentSum)`. Base case: `if (i == nums.length)` return `currentSum == target ? 1 : 0`.
Memoization key: `"i,currentSum"`. If in map, return.
Calculate: `dfs(i+1, currentSum + nums[i]) + dfs(i+1, currentSum - nums[i])`. Put in map, return.

**Time:** $O(N \cdot \text{TotalSum})$ | **Space:** $O(N \cdot \text{TotalSum})$

**Code Solution:**
```java
class Solution {
    Map<String, Integer> memo;
    
    public int findTargetSumWays(int[] nums, int target) {
        memo = new HashMap<>();
        return dfs(nums, target, 0, 0);
    }
    
    private int dfs(int[] nums, int target, int i, int currentSum) {
        if (i == nums.length) {
            return currentSum == target ? 1 : 0;
        }
        
        String key = i + "," + currentSum;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        
        int add = dfs(nums, target, i + 1, currentSum + nums[i]);
        int sub = dfs(nums, target, i + 1, currentSum - nums[i]);
        
        memo.put(key, add + sub);
        return add + sub;
    }
}
```
