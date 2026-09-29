# Theory - 1D Dynamic Programming

1D DP problems are characterized by needing to track a single "state" variable (usually just the index `i` of an array). 

## Where is it commonly used?
1. **Climbing Stairs / Fibonacci variants:** Ways to reach the end.
2. **House Robber / Maximum sum with constraints:** Maximizing profit when you can't pick adjacent elements.
3. **Word Break / String parsing:** Can a string be split into dictionary words?

## Strong signals to look for
- "Find the **Maximum / Minimum**..."
- "Find the **Number of Ways**..."
- The constraints are too big for Backtracking/Recursion ($N > 20$), but perfectly fine for $O(N)$ or $O(N^2)$ array iteration ($N \le 10^4$).

## The 5 Steps to solve ANY DP Problem

If you stare at a DP problem trying to instantly write a `for` loop, you will fail. You must build it systematically.

1. **Visualize the Decision Tree / Recursion:** What are my choices at index `i`? 
   - E.g. (House Robber): At house `i`, I can either ROB it (and jump to `i-2`), or SKIP it (and jump to `i-1`).
2. **Write the Recursive State:** 
   - `maxProfit(i) = max(nums[i] + maxProfit(i - 2), maxProfit(i - 1))`
3. **Identify Base Cases:** 
   - `if (i < 0) return 0; if (i == 0) return nums[0];`
4. **Convert to Bottom-Up (Tabulation):** 
   - Create a `dp` array of size `N`. 
   - Put base cases at `dp[0]` and `dp[1]`.
   - Write a `for` loop from `2` to `N-1`.
   - Replace function calls with array lookups: `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`.
5. **(Optional) Memory Optimization:** 
   - If `dp[i]` only ever looks at `dp[i-1]` and `dp[i-2]`, do you really need a whole array of size N? No! You just need two variables: `prev1` and `prev2`. This reduces space complexity from $O(N)$ to $O(1)$.

## Example: House Robber Memory Optimization

```java
public int rob(int[] nums) {
    if (nums.length == 0) return 0;
    if (nums.length == 1) return nums[0];
    
    int rob1 = 0; // Represents dp[i-2]
    int rob2 = 0; // Represents dp[i-1]
    
    // [rob1, rob2, n, n+1, ...]
    for (int n : nums) {
        // Choice: Rob current + rob1, OR skip current and keep rob2
        int temp = Math.max(n + rob1, rob2);
        
        // Shift pointers forward for the next iteration
        rob1 = rob2;
        rob2 = temp;
    }
    
    return rob2; // The final answer is in rob2
}
```

# Your interview cheat code

```text
1. Is it asking for Max/Min/Ways AND backtracking would TLE?
                  ↓
2. Write the raw recursive math equation FIRST.
                  ↓
3. Make an array `dp[]` and turn the equation into a `for` loop.
```
