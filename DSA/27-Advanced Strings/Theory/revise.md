# Advanced Strings — Revision Sheet

---

## 01. Find the Index of the First Occurrence in a String

**In My Words:** Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

**The Bridge:** This is the exact problem that KMP was designed to solve in $O(N + M)$ time. By precalculating the Longest Prefix Suffix (LPS) array for the `needle`, we can shift our search efficiently upon mismatches without ever moving the `haystack` pointer backwards.

**Optimized Intuition (KMP):**
1. Compute `lps` array for `needle` using the template.
2. Initialize pointers `i = 0` (for haystack) and `j = 0` (for needle).
3. Loop while `i < haystack.length()`:
   - If characters match, increment both `i` and `j`.
   - If `j == needle.length()`, we found a match! Return `i - j`.
   - If mismatch and `j == 0`, just increment `i`.
   - If mismatch and `j > 0`, DO NOT increment `i`. Instead, backtrack `j` to `lps[j - 1]`.

**Template:** KMP Pattern Matching

**Time:** $O(N + M)$ | **Space:** $O(M)$ for the LPS array

**Code Solution:**
```java
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        if (needle.length() > haystack.length()) return -1;
        
        int[] lps = computeLPS(needle);
        int i = 0; // Haystack pointer
        int j = 0; // Needle pointer
        
        while (i < haystack.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            }
            
            if (j == needle.length()) {
                return i - j; // Match found
            } else if (i < haystack.length() && haystack.charAt(i) != needle.charAt(j)) {
                if (j != 0) {
                    j = lps[j - 1]; // Shift needle using LPS
                } else {
                    i++; // No prefix matched, move haystack pointer
                }
            }
        }
        
        return -1;
    }
    
    private int[] computeLPS(String pattern) {
        int[] lps = new int[pattern.length()];
        int prevLPS = 0;
        int i = 1;
        
        while (i < pattern.length()) {
            if (pattern.charAt(i) == pattern.charAt(prevLPS)) {
                prevLPS++;
                lps[i] = prevLPS;
                i++;
            } else {
                if (prevLPS == 0) {
                    lps[i] = 0;
                    i++;
                } else {
                    prevLPS = lps[prevLPS - 1];
                }
            }
        }
        return lps;
    }
}
```

---

## 02. Repeated Substring Pattern

**In My Words:** Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

**The Bridge:** If a string `s` is composed of a repeated substring (e.g. `s = "ababab"`), then it has a specific property. If we concatenate `s + s` (`"abababababab"`), and remove the very first and very last character (`"bababababa"`), the original string `s` ("ababab") will STILL exist inside that modified string! If it wasn't made of repeating substrings, it wouldn't exist.

**Optimized Intuition:** 
Concatenate `s + s`. Remove the first and last characters (using `substring(1, doubleS.length() - 1)`). Use the `contains()` or `indexOf()` method (which uses KMP or similar under the hood) to check if `s` exists in the modified string.

*(Note: There is also an elegant solution using purely the KMP LPS array: If `lps[n-1] > 0` AND `n % (n - lps[n-1]) == 0`, it's true).*

**Time:** $O(N)$ (if `contains` uses KMP/Rabin-Karp) | **Space:** $O(N)$ for the concatenated string

**Code Solution:**
```java
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String doubled = s + s;
        String modified = doubled.substring(1, doubled.length() - 1);
        
        return modified.contains(s);
    }
}
```
