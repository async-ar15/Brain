# Theory - 2D Dynamic Programming

2D DP problems are intimidating because visualizing a 2D matrix filling up is harder than a 1D array. But the 5-step process is identical!

## Where is it commonly used?
1. **LCS / Edit Distance:** Comparing two strings for similarity.
2. **Unique Paths:** Finding paths through a grid with obstacles.
3. **0/1 Knapsack:** (e.g. Target Sum).

## The String Comparison Pattern (Longest Common Subsequence)

This pattern applies to almost every "compare two strings" DP problem (Edit Distance, Interleaving String, Distinct Subsequences).

**The Setup:** We are comparing `text1` at index `i`, and `text2` at index `j`.

**The Logic:**
1. If the characters match (`text1[i] == text2[j]`), great! We found a common character. The total is `1 + answer for the rest of both strings`. `dp[i][j] = 1 + dp[i+1][j+1]`.
2. If they DO NOT match, we have a choice. We can either skip the character in `text1`, or skip the character in `text2`. We want the maximum of those two choices. `dp[i][j] = max(dp[i+1][j], dp[i][j+1])`.

### Template: Bottom-Up 2D DP (String Comparison)

We usually iterate backwards from the end of the strings to the front. The matrix size is `+1` to hold the base cases (out of bounds / empty strings = 0).

```java
public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length();
    int n = text2.length();
    
    // Size m+1 by n+1 initialized to 0
    int[][] dp = new int[m + 1][n + 1];
    
    // Start from bottom right (excluding the +1 base case row/col)
    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            
            if (text1.charAt(i) == text2.charAt(j)) {
                // Diagonal + 1
                dp[i][j] = 1 + dp[i + 1][j + 1];
            } else {
                // Max of Right or Down
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
            }
            
        }
    }
    
    // The answer bubbles up to the top left (index 0, 0)
    return dp[0][0];
}
```

## Space Optimization (The 1D Array trick)

Look at the `dp[i][j]` equations.
- `dp[i+1][j+1]` is the cell diagonally down-right.
- `dp[i+1][j]` is the cell directly below.
- `dp[i][j+1]` is the cell directly to the right.

Notice that to compute the current row `i`, we ONLY ever need values from the *current* row, and the *next* row (`i+1`). We never need row `i+2` or `i+3`. 

Therefore, we don't need an $M \times N$ matrix. We only need two 1D arrays of size $N$: `currentRow` and `nextRow`. This reduces Space Complexity from $O(M \cdot N)$ to $O(N)$!

# Your interview cheat code

```text
1. Are you comparing two strings or navigating a grid?
                  ↓
2. Define the recursive state: `solve(i, j)`.
                  ↓
3. Build an `[m+1][n+1]` matrix. Iterate backwards.
                  ↓
4. If it matches -> Diagonal. If it doesn't -> Max(Right, Down).
```
