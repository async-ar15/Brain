# 04. Prefix Sum - Pre-requisites

## The Problem with Multiple Queries

Imagine you have an array `[1, 2, 3, 4, 5]` and you are asked a series of questions:
1. "What is the sum from index 1 to 3?" (2 + 3 + 4 = 9)
2. "What is the sum from index 0 to 4?" (1 + 2 + 3 + 4 + 5 = 15)

If you use a `for` loop to calculate the sum for *every* query, and there are $Q$ queries, the time complexity becomes $O(N \times Q)$. If $N$ and $Q$ are both $10^5$, this is $10^{10}$ operations (Time Limit Exceeded).

## The Prefix Sum Concept

Prefix sum is a precomputation technique. We spend $O(N)$ time upfront to build a new array that stores cumulative sums. Once this array is built, we can answer ANY range sum query in **$O(1)$ constant time**.

- Original: `[ 1,  2,  3,  4,  5]`
- Prefix:   `[ 1,  3,  6, 10, 15]`

At index `i`, the prefix sum array stores the sum of all elements from index `0` up to index `i`.

## Math Formula for Range Sum

How do we find the sum from index `L` to `R` using the prefix array?

`Sum(L, R) = Prefix[R] - Prefix[L - 1]`

*Wait, what if L is 0?* `Prefix[-1]` would be out of bounds. 
To avoid this, we often create the Prefix array with size `N + 1`, shifting everything by 1 index so `Prefix[0] = 0`.

```java
// Building a Prefix Sum array in Java
int[] nums = {1, 2, 3, 4, 5};
int[] prefix = new int[nums.length];

prefix[0] = nums[0];
for (int i = 1; i < nums.length; i++) {
    prefix[i] = prefix[i - 1] + nums[i];
}

// Sum from index 1 to 3 (which is 2+3+4 = 9)
int L = 1, R = 3;
int sum = prefix[R] - prefix[L - 1]; // prefix[3] - prefix[0] = 10 - 1 = 9
```
