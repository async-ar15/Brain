# [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

**Difficulty:** MEDIUM

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return *an edge that can be removed so that the resulting graph is a tree of* `n` *nodes*. If there are multiple answers, return the answer that occurs last in the input.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg)

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg)

```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

**Constraints:**

* `n == edges.length`
* `3 <= n <= 1000`
* `edges[i].length == 2`
* `1 <= ai < bi <= edges.length`
* `ai != bi`
* There are no repeated edges.
* The given graph is connected.

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
