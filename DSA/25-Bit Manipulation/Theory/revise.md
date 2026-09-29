# Bit Manipulation — Revision Sheet

---

## 01. Single Number

**In My Words:** Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

**The Bridge:** Constant extra space rules out HashMaps. Linear runtime rules out sorting. We need a math trick. The trick is XOR (`^`). Any number XORed with itself is 0 (`A ^ A = 0`). Any number XORed with 0 is itself (`A ^ 0 = A`).

**Optimized Intuition:** Initialize `res = 0`. Iterate through the array. `res ^= num`. At the end, all duplicates will have cancelled each other out to 0. The only thing left in `res` will be the single number.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int num : nums) {
            res ^= num;
        }
        return res;
    }
}
```

---

## 02. Number of 1 Bits

**In My Words:** Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**The Bridge:** We can check the last bit using `n & 1`. If it's 1, increment count. Then we logically shift right `n >>> 1` (zero-fill right shift in Java to ignore the sign bit). We do this 32 times. OR, we can use Brian Kernighan's Algorithm to skip the zeros!

**Optimized Intuition (Kernighan's):** 
`n & (n - 1)` drops the lowest set bit. 
Loop while `n != 0`. Inside loop: `n = n & (n - 1)`, `count++`.
This runs exactly as many times as there are '1' bits, rather than 32 times.

**Time:** $O(1)$ (At most 32 operations) | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1); // Drop lowest set bit
            count++;
        }
        return count;
    }
}
```

---

## 03. Counting Bits

**In My Words:** Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` ($0 \le i \le n$), `ans[i]` is the number of `1`'s in the binary representation of `i`.

**Constraint Whispers:**
- You could just run the previous function $n$ times for an $O(N \log N)$ solution, but can you do it in $O(N)$?

**The Bridge:** This is actually a Dynamic Programming problem disguised as a Bit Manipulation problem. The number of 1s in `i` is related to the number of 1s in a smaller number we already calculated.
Specifically, `i >> 1` (which is `i / 2`) has exactly the same number of 1s as `i`, EXCEPT if `i` is odd, it has one extra 1 at the end!

**Optimized Intuition:** `dp[0] = 0`. Loop `i` from 1 to `n`. 
`dp[i] = dp[i >> 1] + (i & 1)`.
*(Explanation: The 1s in `i` equals the 1s in `i / 2`, plus 1 if `i` is odd).*

**Time:** $O(N)$ | **Space:** $O(N)$ (for output array)

**Code Solution:**
```java
class Solution {
    public int[] countBits(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i >> 1] + (i & 1);
        }
        
        return dp;
    }
}
```

---

## 04. Reverse Bits

**In My Words:** Reverse the bits of a given 32 bits unsigned integer.

**The Bridge:** We need to extract bits from the right side of `n`, and append them to the right side of a new `result` integer (which pushes the previously appended bits to the left).

**Optimized Intuition:**
Initialize `result = 0`.
Loop 32 times:
1. Extract rightmost bit of `n`: `int bit = n & 1`.
2. Shift `result` to the left to make room: `result = result << 1`.
3. Add the extracted bit to `result`: `result = result | bit`. (Or `result += bit`).
4. Shift `n` to the right to process the next bit: `n = n >>> 1`. (MUST use `>>>` to zero-fill, otherwise negative numbers will infinite loop 1s).

**Time:** $O(1)$ (Exactly 32 operations) | **Space:** $O(1)$

**Code Solution:**
```java
public class Solution {
    public int reverseBits(int n) {
        int res = 0;
        
        for (int i = 0; i < 32; i++) {
            int bit = n & 1;          // Extract bit
            res = (res << 1) | bit;   // Shift res left and add bit
            n >>>= 1;                 // Logical right shift n
        }
        
        return res;
    }
}
```
