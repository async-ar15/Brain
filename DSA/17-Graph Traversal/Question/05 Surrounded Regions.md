# [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

**Difficulty:** MEDIUM

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

* **Connect**: A cell is connected to adjacent cells horizontally or vertically.
* **Region**: To form a region **connect every** `'O'` cell.
* **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed** by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

**Example 1:**

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

**Example 2:**

**Input:** board = [["X"]]

**Output:** [["X"]]

**Constraints:**

* `m == board.length`
* `n == board[i].length`
* `1 <= m, n <= 200`
* `board[i][j]` is `'X'` or `'O'`.

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
