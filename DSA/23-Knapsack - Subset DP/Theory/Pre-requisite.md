# 23. Knapsack / Subset DP - Pre-requisites

## The Knapsack Problem

The 0/1 Knapsack problem is the most famous Dynamic Programming pattern in computer science.

**The Setup:** A thief is robbing a store. They have a knapsack that can carry a maximum weight of `W`. The store has `n` items, each with a specific `weight` and `value`. The thief wants to maximize the total value they steal without exceeding weight `W`.

**The "0/1" Constraint:** You can either take an item (1), or leave it (0). You cannot take half of an item.

## The State Variables

To solve this, we need to make a decision at every item.
If we are at item `i`, our choices depend on how much capacity `c` we have left in the bag.
Therefore, our recursive state requires TWO variables: `solve(i, c)`.

Because it requires two variables, it is a 2D DP problem!

## Translating Knapsack to Arrays

LeetCode rarely asks the literal "rob a store" problem. Instead, they disguise it using integer arrays:
- **Partition Equal Subset Sum:** Can you find a subset of numbers that adds up exactly to `sum / 2`? (This is knapsack where the bag capacity is `sum / 2`, and item weights are the array values).
- **Target Sum:** Can you assign +/- to numbers to reach a target? (This reduces to finding a subset that equals a specific math target).
