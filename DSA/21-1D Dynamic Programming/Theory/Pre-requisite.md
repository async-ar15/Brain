# 22. 1D Dynamic Programming - Pre-requisites

## What is Dynamic Programming (DP)?

Dynamic Programming is a terrifying name for a very simple concept: **Remembering stuff you've already calculated so you don't have to calculate it again.**

In academic terms, DP is an optimization over plain recursion. It is used when a problem has two properties:
1. **Overlapping Subproblems:** The exact same recursive calls are made multiple times (e.g. `fib(3)` is called many times when calculating `fib(5)`).
2. **Optimal Substructure:** The optimal solution to a big problem can be built from optimal solutions of its smaller subproblems.

## The Fibonacci Sequence Example

`fib(n) = fib(n-1) + fib(n-2)`

**The Recursion Way ($O(2^n)$ Time):**
```java
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```
This is incredibly slow. `fib(40)` will take your computer noticeable seconds to compute because it redundantly calculates `fib(2)` millions of times.

## Memoization (Top-Down DP)

What if we just use a HashMap (or an array) to "memoize" (remember) the answer the *first* time we calculate it?

```java
int[] memo = new int[n + 1]; // Fill with -1 initially

int fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n]; // Oh wait, I already know this!
    
    memo[n] = fib(n - 1) + fib(n - 2); // Calculate and remember
    return memo[n];
}
```
**Time Complexity:** $O(N)$. We reduced exponential time to linear time just by remembering!

## Tabulation (Bottom-Up DP)

Recursion has overhead (Call Stack memory). What if we just start from the bottom (base cases) and build our way up using a simple `for` loop?

```java
int fib(int n) {
    if (n <= 1) return n;
    int[] dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}
```
This is the standard form of DP you will see in competitive programming.
