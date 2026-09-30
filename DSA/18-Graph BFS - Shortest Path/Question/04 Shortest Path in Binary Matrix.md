# [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

**Difficulty:** MEDIUM

Given an `n x n` binary matrix `grid`, return *the length of the shortest **clear path** in the matrix*. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

* All the visited cells of the path are `0`.
* All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)

```
Input: grid = [[0,1],[1,0]]
Output: 2
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)

```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

**Example 3:**

```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

**Constraints:**

* `n == grid.length`
* `n == grid[i].length`
* `1 <= n <= 100`
* `grid[i][j] is 0 or 1`

---

# understanding the question 

Pointing out these things:
- i. Draw examples
- ii. Clarify edge cases
- iii. Confirm input/output
- iv. Important key words for the approach 
- v. basic level of understanding of the question & what kinda solution might work for us 

# understanding the constraints

Pointing out these things: 
- i. Time complexity
- ii. Space complexity
- iii. Input space, output space
- iv. What kind of data structure or algorithm can be used here
- v. how constraints help us to find the solution 

# Solution 

## Brute force 

- Intution for the brute force 
- pseudo code for the brute  force 
- draw the dry run for the brute force
- Time complexity and space complexity of the brute force approach 
- solution code 

## better code (if there)

- how  we are optimising from the brute force
- Intution 
- pseudo code for the better approach 
- draw the dry run for the better approach
- Time complexity and space complexity of the better approach 
- solution code 

## optimised code (if there)

- how  we are optimising from the better code
- Intution 
- pseudo code for the optimised approach 
- draw the dry run for the optimised approach
- Time complexity and space complexity of the optimised approach 
- solution code 

# question where I went wrong & what is the correction 
