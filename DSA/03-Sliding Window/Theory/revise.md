# Sliding Window — Revision Sheet

---

## 01. Best Time to Buy and Sell Stock

**In My Words:** Given an array of prices, choose one day to buy and a different day in the future to sell to maximize profit.

**Constraint Whispers:**
- You must buy BEFORE you sell. (Time flows in one direction).

**Brute Force:** Nested loops. For every day, check all future days and find the max profit. $O(N^2)$ time.

**The Bridge:** As we move through the array, the best profit we can make ending on day `i` is `prices[i] - min(prices seen so far)`. We only need to track the minimum price seen so far!

**Optimized Intuition:** This is a simplified sliding window (or two pointers). Left pointer is the "buy" day (the lowest price seen so far). Right pointer is the "sell" day. If `prices[right] < prices[left]`, we found a new lowest price, so `left = right`. Otherwise, calculate profit and update max.

**Time:** $O(N)$ | **Space:** $O(1)$

**Code Solution:**
```java
class Solution {
    public int maxProfit(int[] prices) {
        int left = 0; // buy
        int maxProfit = 0;
        
        for (int right = 1; right < prices.length; right++) {
            // Is this a profitable transaction?
            if (prices[left] < prices[right]) {
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            } else {
                // We found a new, lower price to buy at!
                left = right;
            }
        }
        return maxProfit;
    }
}
```

---

## 02. Longest Substring Without Repeating Characters

**In My Words:** Find the length of the longest substring without any duplicate characters.

**Constraint Whispers:**
- Substring = Contiguous = Sliding Window.

**The Bridge:** If our window has no duplicates, we can safely expand `right`. The moment `right` encounters a character that is already in our window, the window becomes invalid. We must shrink `left` until that duplicate character is removed from the window.

**Optimized Intuition:** Use a HashSet (or boolean array) to track characters in the window. `right` expands. If `s[right]` is in the set, a duplicate exists! Enter a `while` loop: remove `s[left]` from the set and `left++` until `s[right]` is no longer in the set. Then add `s[right]` and update max length.

**Template:** Variable Size Window

**Time:** $O(N)$ | **Space:** $O(min(N, M))$ where M is the charset size.

**Code Solution:**
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int left = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char curr = s.charAt(right);
            
            // While the window is invalid (contains a duplicate)
            while (set.contains(curr)) {
                set.remove(s.charAt(left));
                left++; // Shrink from the left
            }
            
            // Window is valid again, add current char
            set.add(curr);
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
```

---

## 03. Longest Repeating Character Replacement

**In My Words:** Given a string of uppercase letters, you can replace up to `k` characters. Return the length of the longest substring containing all repeating letters you can get.

**Constraint Whispers:**
- Contiguous substring = Sliding Window.
- We have a specific limit `k` on invalid elements.

**The Bridge:** A window is VALID if: `(Length of window) - (Count of most frequent character in window) <= k`. If the number of characters we have to replace exceeds `k`, the window is invalid and we must shrink `left`.

**Optimized Intuition:** Keep a frequency map (or `int[26]`) of characters in the window. Keep track of the `maxFreq` (count of the most frequent character). If `(right - left + 1) - maxFreq > k`, then `left++` and decrement the frequency of the char at `left`.

**Template:** Variable Size Window

**Gotcha:** We don't strictly need to update `maxFreq` when shrinking the window. Why? Because the maximum window size will only increase when we find a NEW historical maximum frequency. This is a subtle optimization that keeps the time complexity strictly $O(N)$.

**Time:** $O(N)$ | **Space:** $O(1)$ (array of 26)

**Code Solution:**
```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int left = 0;
        int maxFreq = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char curr = s.charAt(right);
            count[curr - 'A']++;
            maxFreq = Math.max(maxFreq, count[curr - 'A']);
            
            // Is the window invalid?
            // Window length - Most frequent char count > k
            while ((right - left + 1) - maxFreq > k) {
                char leftChar = s.charAt(left);
                count[leftChar - 'A']--;
                left++;
            }
            
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
```
