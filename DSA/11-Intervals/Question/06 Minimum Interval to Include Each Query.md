# [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

**Difficulty:** HARD

You are given a 2D integer array `intervals`, where `intervals[i] = [lefti, righti]` describes the `ith` interval starting at `lefti` and ending at `righti` **(inclusive)**. The **size** of an interval is defined as the number of integers it contains, or more formally `righti - lefti + 1`.

You are also given an integer array `queries`. The answer to the `jth` query is the **size of the smallest interval** `i` such that `lefti <= queries[j] <= righti`. If no such interval exists, the answer is `-1`.

Return *an array containing the answers to the queries*.

**Example 1:**

```
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
```

**Example 2:**

```
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
```

**Constraints:**

* `1 <= intervals.length <= 105`
* `1 <= queries.length <= 105`
* `intervals[i].length == 2`
* `1 <= lefti <= righti <= 107`
* `1 <= queries[j] <= 107`

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
