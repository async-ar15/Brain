# Greedy — Revision Sheet

---

## 01. Maximum Subarray (Kadane's Algorithm)

**In My Words:** Find the contiguous subarray with the largest sum and return its sum.

**The Bridge:** If the sum of the subarray we've built so far drops below zero, it is mathematically impossible for it to contribute positively to any future subarray. We should throw it away (reset to 0) and start a new subarray from the next element.

**Optimized Intuition:** Maintain a `currentSum` and `maxSum`. Iterate. Add `nums[i]` to `currentSum`. Update `maxSum`. If `currentSum < 0`, reset `currentSum = 0`.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = 0;
        
        for (int num : nums) {
            if (currentSum < 0) {
                currentSum = 0;
            }
            currentSum += num;
            maxSum = Math.max(maxSum, currentSum);
        }
        
        return maxSum;
    }
}
```

---

## 02. Jump Game

**In My Words:** You are at index 0. `nums[i]` is your max jump length. Return true if you can reach the last index.

**The Bridge:** We don't need to know *how* to get there, just IF we can get there. We just keep tracking the maximum index we can possibly reach.

**Optimized Intuition:** `maxReach = 0`. Iterate `i` from 0 to end. If `i > maxReach`, we are stuck, return false. Otherwise `maxReach = max(maxReach, i + nums[i])`. Return true at the end.
*(Alternative backwards: `goal = last index`. Iterate backwards. If `i + nums[i] >= goal`, `goal = i`. Return `goal == 0`).*

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
        }
        return true;
    }
}
```

---

## 03. Jump Game II

**In My Words:** You are at index 0. Return the MINIMUM number of jumps to reach the last index. (It is guaranteed you can reach it).

**The Bridge:** Instead of just tracking the absolute furthest we can reach, we want to jump in "phases" (like BFS). We make a jump, and it takes us to a range of indices `[left, right]`. We explore all those indices to find the absolute FURTHEST we can go on our *next* jump.

**Optimized Intuition:** `jumps = 0`, `currentJumpEnd = 0`, `farthest = 0`. Iterate `i` from 0 to `N - 2`. `farthest = max(farthest, i + nums[i])`. When `i == currentJumpEnd`, we are forced to make a jump to continue. So `jumps++`, and our new `currentJumpEnd = farthest`.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int jump(int[] nums) {
        int jumps = 0;
        int currentJumpEnd = 0;
        int farthest = 0;
        
        // We only go up to length - 2 because once we are at the last index,
        // we don't need to jump anymore.
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            
            // We've reached the end of the current jump's reach
            if (i == currentJumpEnd) {
                jumps++;
                currentJumpEnd = farthest;
            }
        }
        return jumps;
    }
}
```

---

## 04. Gas Station

**In My Words:** You have circular route with gas stations. `gas[i]` is gas you get, `cost[i]` is gas to travel to next. Return starting index if you can complete the circuit, else -1.

**The Bridge:** Two brilliant Greedy insights:
1. If the total gas is less than total cost, it's impossible. Return -1.
2. If it IS possible, there is a unique solution. If you start at $A$ and run out of gas at $B$, it is mathematically impossible to start at ANY station between $A$ and $B$ and reach $B$ (because $A$ gave you a non-negative headstart, and you still failed). You must test the next station after $B$ as your new start!

**Optimized Intuition:** `totalGas`, `totalCost`, `currentGas`, `startNode = 0`. Iterate. Accumulate `currentGas += gas[i] - cost[i]`. If `currentGas < 0`, the route from `startNode` to `i` failed. Reset `currentGas = 0`, and set `startNode = i + 1`.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        int totalCost = 0;
        int currentGas = 0;
        int startNode = 0;
        
        for (int i = 0; i < gas.length; i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            
            currentGas += gas[i] - cost[i];
            
            // If we run out of gas, this startNode is invalid.
            // Also, any node between startNode and i is also invalid!
            if (currentGas < 0) {
                startNode = i + 1; // Try the next node
                currentGas = 0;    // Reset tank
            }
        }
        
        return totalGas >= totalCost ? startNode : -1;
    }
}
```
