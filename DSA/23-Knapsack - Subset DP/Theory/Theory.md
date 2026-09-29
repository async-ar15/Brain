# Theory - Knapsack / Subset DP

Knapsack problems are notoriously difficult to see at first glance.

## Where is it commonly used?
1. **Subset Sum:** Finding if a subset adds up to a specific target.
2. **Coin Change (Unbounded Knapsack):** When you can pick an item an UNLIMITED number of times (unlike 0/1 Knapsack where you can only pick it once).

## The Core Recurrence Relation

For every item `i`, we have a choice:
1. **Exclude it:** The max value is just whatever we could get from the remaining items with the same capacity. `dp[i+1][c]`
2. **Include it:** (Only if `weight[i] <= c`). The value is the item's value PLUS whatever we can get from the remaining items with our NEW reduced capacity. `value[i] + dp[i+1][c - weight[i]]`

We take the `max` of these two choices!

## 1D Space Optimization

A full 2D matrix for Knapsack is $O(N \cdot C)$ space, where $C$ is the capacity. If capacity is large, this memory limit exceeds (MLE).

**The Trick:** Notice that calculating row `i` ONLY depends on values from row `i-1` (the previous row). We can crush the 2D matrix into a single 1D array of size `C+1`!

**CRITICAL RULE FOR 1D KNAPSACK:** When crushing 0/1 Knapsack into a 1D array, you MUST iterate through the capacity `c` **BACKWARDS** (from max capacity down to the item's weight). If you iterate forwards, you might process the same item multiple times, which turns it into an Unbounded Knapsack problem (Coin Change)!

### Template: 1D Optimized 0/1 Knapsack (Subset Sum)

```java
// Can we find a subset in `nums` that sums exactly to `target`?
public boolean canPartition(int[] nums, int target) {
    boolean[] dp = new boolean[target + 1];
    dp[0] = true; // Base case: we can always make sum 0 by picking nothing
    
    for (int num : nums) {
        // Iterate BACKWARDS to prevent reusing the same number
        for (int sum = target; sum >= num; sum--) {
            // We can make `sum` if we could ALREADY make `sum`, 
            // OR if we could make `sum - num`.
            dp[sum] = dp[sum] || dp[sum - num];
        }
    }
    
    return dp[target];
}
```

# Your interview cheat code

```text
1. Are you picking a subset of items to meet a specific sum/capacity?
                  ↓
2. It's a 0/1 Knapsack variant.
                  ↓
3. Use a 1D `dp[]` array of size `Target + 1`.
4. Iterate elements. Inner loop: iterate capacities BACKWARDS.
```
