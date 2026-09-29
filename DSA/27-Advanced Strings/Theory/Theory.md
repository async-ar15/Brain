# Theory - Advanced Strings (KMP)

You will rarely be asked to write KMP from memory, but understanding its LPS table generation is a highly valued concept for Hard string problems.

## Where is it commonly used?
1. **Find the Index of the First Occurrence in a String:** Implement `strStr()`.
2. **Shortest Palindrome:** Finding the longest palindromic prefix of a string.
3. **Repeated Substring Pattern:** Checking if a string is composed of a smaller string repeated.

## The KMP Algorithm (Knuth-Morris-Pratt)

KMP operates in strictly $O(N + M)$ time by never moving the `haystack` pointer backward.

It is split into two phases:
1. **Build the LPS Array:** $O(M)$ time. `LPS[i]` stores the length of the Longest Proper Prefix that is also a Suffix for the substring `pattern[0...i]`.
2. **Search:** $O(N)$ time. Iterate through the `haystack`. When a mismatch occurs, use the LPS array to safely shift the `needle` pointer backwards without losing progress.

### Template: LPS Array Generation

```java
public int[] computeLPS(String pattern) {
    int[] lps = new int[pattern.length()];
    int prevLPS = 0; // Length of the previous longest prefix suffix
    int i = 1;
    
    // LPS[0] is always 0 because a proper prefix cannot be the whole string
    while (i < pattern.length()) {
        if (pattern.charAt(i) == pattern.charAt(prevLPS)) {
            // Characters match! Extend the prefix length
            prevLPS++;
            lps[i] = prevLPS;
            i++;
        } else {
            // Characters do not match
            if (prevLPS == 0) {
                // We are at the very beginning of the pattern. LPS is 0.
                lps[i] = 0;
                i++;
            } else {
                // TRICKY PART: We mismatch, but we might have a smaller prefix that matches.
                // We look up the LPS array to find the next longest prefix to try.
                // Notice we do NOT increment 'i' here.
                prevLPS = lps[prevLPS - 1];
            }
        }
    }
    return lps;
}
```

## Rabin-Karp Algorithm (Rolling Hash)

Another $O(N + M)$ pattern matching algorithm, often easier to understand than KMP.

Instead of matching characters one by one, it converts the `needle` into a unique integer hash. Then, it converts a sliding window of the `haystack` into an integer hash.
If the hashes match, the strings match!

**The Rolling Hash:**
Calculating a hash for every window takes $O(M)$ time, making it $O(N \cdot M)$ again.
The magic is the *Rolling Hash*. When the window slides, you can calculate the new hash in $O(1)$ time by mathematically subtracting the character that left the window and adding the character that entered the window.

# Your interview cheat code

```text
1. Are you searching for a specific substring within a massive string?
                  ↓
2. Do they explicitly ban O(N*M) brute force?
                  ↓
           USE KMP (LPS Array) OR RABIN-KARP (Rolling Hash)
```
