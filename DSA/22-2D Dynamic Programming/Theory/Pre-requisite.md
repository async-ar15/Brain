# 23. 2D Dynamic Programming - Pre-requisites

## From 1D to 2D

In 1D DP, we only needed to track one changing variable (usually the index `i` of an array) to define our state.
In 2D DP, our recursive state relies on **two changing variables**.

Common scenarios:
1. **Two Arrays/Strings:** You are comparing string A and string B. You need index `i` for A, and index `j` for B.
2. **Grid Traversal:** You are moving through a 2D matrix. You need row `r` and column `c`.
3. **Knapsack Problems:** You have an array of items (index `i`), and a constrained capacity/target (weight `w`).

## The 2D Cache (Memoization)

If a function is defined as `solve(int i, int j)`, then to memoize the results, you need a 2D array (or a HashMap with a string key `"i,j"`).

```java
int[][] memo = new int[m][n];
// Fill with -1 initially to denote "uncalculated"
for (int[] row : memo) {
    Arrays.fill(row, -1);
}

int solve(int i, int j) {
    if (memo[i][j] != -1) return memo[i][j];
    
    // ... calculate ...
    memo[i][j] = result;
    return result;
}
```

## Matrix Initialization Gotcha

When doing Bottom-Up Tabulation for 2D DP (especially string problems), you often need to initialize the DP matrix to size `[m + 1][n + 1]`. 

Why the `+1`? It acts as the "Base Case" for when one of the strings is empty!
- `dp[0][0]` often represents comparing an empty string to an empty string.
- This prevents out-of-bounds errors when your DP equation looks backwards to `dp[i-1][j-1]`.
