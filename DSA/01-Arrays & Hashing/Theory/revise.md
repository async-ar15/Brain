# Arrays & Hashing — Revision Sheet

---

## 01. Contains Duplicate

**In My Words:** Given an array, return true if any value appears at least twice.

**Constraint Whispers:**
- $n \le 10^5$ → $O(N^2)$ TLE
- Needs $O(N)$ or $O(N \log N)$

**Brute Force:** Compare every element with every other element using two nested loops. $O(N^2)$ time, $O(1)$ space.

**Why It Hurts:** Too slow for large arrays.

**The Bridge:** We just need to know if we've seen a number before. A HashSet is perfect for $O(1)$ lookups.

**Optimized Intuition:** Iterate through the array. If the number is already in the HashSet, return true. Otherwise, add it.
Alternatively, `Arrays.sort(nums)` and check if adjacent elements are equal ($O(N \log N)$ time, $O(1)$ space).

**Template:** HashSet tracking

**Time:** $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (!set.add(num)) return true; // set.add returns false if element already exists
        }
        return false;
    }
}
```

---

## 02. Valid Anagram

**In My Words:** Given two strings `s` and `t`, return true if `t` is an anagram of `s`.

**Constraint Whispers:**
- Strings consist of lowercase English letters → We can use a fixed-size array of 26 instead of a HashMap.

**Brute Force:** Sort both strings and compare them. $O(N \log N)$ time.

**Why It Hurts:** Sorting is slow when we just need character frequencies.

**The Bridge:** Anagrams must have the exact same count of characters. We can count frequencies in one pass.

**Optimized Intuition:** Create an array `count[26]`. Iterate through the strings: increment for chars in `s`, decrement for chars in `t`. If all values in `count` are 0 at the end, they are anagrams.

**Template:** Frequency Counting

**Time:** $O(N)$ | **Space:** $O(1)$ (since alphabet size is fixed to 26)

**Code Solution:**
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }
}
```

---

## 03. Two Sum

**In My Words:** Given an array and a target, find the indices of the two numbers that add up to the target.

**Constraint Whispers:**
- Exactly one valid answer exists.
- Array is unsorted.

**Brute Force:** Two nested loops. $O(N^2)$ time.

**Why It Hurts:** Checking elements we've already looked at is inefficient.

**The Bridge:** As we iterate, for any `num`, we are looking for `target - num`. If we store previously seen numbers in a map alongside their indices, we can look up `target - num` in $O(1)$ time.

**Optimized Intuition:** One pass. Check if `target - nums[i]` is in the map. If yes, return indices. If no, put `nums[i]` and `i` into the map.

**Template:** Complement Pattern

**Time:** $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

---

## 04. Group Anagrams

**In My Words:** Given an array of strings, group the anagrams together.

**Constraint Whispers:**
- Lowercase english letters.

**Brute Force:** Compare every string to every other string using the Valid Anagram function. Extremely slow.

**The Bridge:** We need a way to group them. Anagrams have the same "signature". What is the signature? Either the sorted version of the string, or a character frequency count.

**Optimized Intuition:** Create a HashMap mapping `Signature -> List of Strings`. For each string, generate its signature (e.g. sort it). Add the string to the corresponding list in the map.

**Template:** Grouping Pattern

**Time:** $O(N \cdot K \log K)$ where K is max length of string (if sorting signature) | **Space:** $O(N \cdot K)$

**Code Solution:**
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars); // The signature
            
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(s);
        }
        
        return new ArrayList<>(map.values());
    }
}
```

---

## 05. Product of Array Except Self

**In My Words:** Return an array where `answer[i]` is the product of all elements except `nums[i]`. MUST write in $O(N)$ and without using the division operation.

**Constraint Whispers:**
- You cannot use division.
- $O(1)$ extra space complexity follow-up (the output array doesn't count).

**Brute Force:** For each element, loop through the rest of the array to calculate the product. $O(N^2)$.

**Why It Hurts:** Recalculating overlapping products.

**The Bridge:** The product of array except `i` is actually: `(Product of everything to the left of i) * (Product of everything to the right of i)`.

**Optimized Intuition:** Create a `res` array. First pass (left to right): Store the running prefix product in `res`. Second pass (right to left): Keep a running suffix product in a variable, and multiply it with the value already in `res[i]`.

**Time:** $O(N)$ | **Space:** $O(1)$ auxiliary

**Code Solution:**
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        
        // 1. Prefix pass
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }
        
        // 2. Postfix pass
        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postfix;
            postfix *= nums[i];
        }
        
        return res;
    }
}
```

---

## 06. Longest Consecutive Sequence

**In My Words:** Given an unsorted array of integers, return the length of the longest consecutive elements sequence. MUST run in $O(N)$ time.

**Constraint Whispers:**
- $O(N)$ time requirement means sorting is strictly forbidden ($O(N \log N)$).

**Brute Force:** Sort the array, then iterate to find the longest streak. $O(N \log N)$.

**Why It Hurts:** The problem explicitly demands $O(N)$.

**The Bridge:** We need $O(1)$ lookups to find consecutive numbers. A HashSet provides this. But to keep it $O(N)$, we should only start counting a sequence if it's the *start* of a sequence. How do we know it's the start? If `num - 1` is NOT in the set!

**Optimized Intuition:** Add all nums to a HashSet. For each num, check if `num - 1` exists. If it DOES NOT exist, it's the start of a sequence. From there, while `num + length` exists in the set, increment the length. Keep track of the max length.

**Time:** $O(N)$ (each number is visited at most twice) | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        
        int longest = 0;
        
        for (int num : set) {
            // Check if this is the start of a sequence
            if (!set.contains(num - 1)) {
                int length = 1;
                
                // Count the sequence length
                while (set.contains(num + length)) {
                    length++;
                }
                
                longest = Math.max(longest, length);
            }
        }
        
        return longest;
    }
}
```
