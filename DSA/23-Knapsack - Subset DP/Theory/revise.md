# Knapsack / Subset DP — Revision Sheet

---

## 01. Partition Equal Subset Sum

**In My Words:** Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Constraint Whispers:**
- Finding a subset that equals half the total sum is exactly the 0/1 Knapsack problem!

**The Bridge:** Calculate total sum. If it's odd, it's impossible to partition into two integers, return false. `target = sum / 2`. Now, the problem is just: Can we find a subset in `nums` that sums exactly to `target`?

**Optimized Intuition:** 
1D DP array of size `target + 1`. `dp[0] = true`.
Outer loop: for each `num` in `nums`.
Inner loop: iterate `sum` from `target` DOWN TO `num`.
`dp[sum] = dp[sum] || dp[sum - num]`.
Return `dp[target]`.

**Template:** 1D Optimized 0/1 Knapsack

**Time:** $O(N \cdot \text{Target})$ | **Space:** $O(\text{Target})$

**Code Solution:**
```java
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        
        if (sum % 2 != 0) return false;
        
        int target = sum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num];
            }
        }
        
        return dp[target];
    }
}
```

---

## 02. Target Sum

**In My Words:** Given an integer array `nums` and an integer `target`. Build an expression out of `nums` by adding '+' or '-' before each integer. Return the number of different expressions that evaluate to `target`.

**The Bridge:** We did this with Top-Down Memoization in 2D DP. But it can be solved with 1D Tabulation! Let $S_1$ be the subset of positive numbers, and $S_2$ be the subset of negative numbers.
$S_1 - S_2 = target$
$S_1 + S_2 = totalSum$
Adding the two equations: $2 \cdot S_1 = target + totalSum$
$S_1 = (target + totalSum) / 2$
The problem reduces to: Find the number of subsets that equal exactly $S_1$! This is standard Knapsack.

**Optimized Intuition:**
Calculate total sum. If `totalSum < Math.abs(target)` or `(target + totalSum) % 2 != 0`, return 0.
`s1 = (target + totalSum) / 2`.
1D array `dp[s1 + 1]`. `dp[0] = 1` (one way to make 0).
For each `num` in `nums`, loop `sum` BACKWARDS from `s1` down to `num`.
`dp[sum] += dp[sum - num]` (Since we want the NUMBER of ways, we add, not `||`).

**Time:** $O(N \cdot S_1)$ | **Space:** $O(S_1)$

**Code Solution:**
```java
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int totalSum = 0;
        for (int n : nums) totalSum += n;
        
        // Edge cases
        if (Math.abs(target) > totalSum || (target + totalSum) % 2 != 0) {
            return 0;
        }
        
        int s1 = (target + totalSum) / 2;
        int[] dp = new int[s1 + 1];
        dp[0] = 1;
        
        for (int num : nums) {
            for (int i = s1; i >= num; i--) {
                dp[i] += dp[i - num];
            }
        }
        
        return dp[s1];
    }
}
```

---

## 03. Combination Sum IV

**In My Words:** Given an array of distinct integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`. Note that different sequences are counted as different combinations (so it's permutations, not combinations).

**The Bridge:** Because order matters (`[1, 2]` is different from `[2, 1]`), and we can pick numbers an unlimited number of times, this is NOT a 0/1 Knapsack problem. It's closer to Climbing Stairs! At any point to reach `target`, we can transition from `target - num`.

**Optimized Intuition:**
1D DP array of size `target + 1`. `dp[0] = 1`.
Outer loop: iterate `i` from 1 to `target` (FORWARD!).
Inner loop: iterate through ALL `num` in `nums`.
If `i >= num`, `dp[i] += dp[i - num]`.

*(Notice how iterating the capacity forwards vs backwards completely changes the problem from 0/1 subset sum to Unbounded permutation sum!)*

**Time:** $O(N \cdot \text{Target})$ | **Space:** $O(\text{Target})$

**Code Solution:**
```java
class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        
        // Forward loop: we can use elements unlimited times, and order matters
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (i >= num) {
                    dp[i] += dp[i - num];
                }
            }
        }
        
        return dp[target];
    }
}
```
