# 27. Advanced Strings - Pre-requisites

## Why are Strings "Advanced"?

Standard string algorithms (like Two Pointers or Sliding Window) operate in $O(N)$ time.
However, there is a class of string problems involving **Pattern Matching** (finding a substring within a massive string) that brute-force approaches solve in $O(N \cdot M)$ time.

Advanced String Algorithms exist to reduce pattern matching to $O(N + M)$ time.

## Substring Search (Needle in a Haystack)

If you have `haystack = "hello world"` and `needle = "world"`, you want to find the starting index.
In Java, you can just use `haystack.indexOf(needle)`. But in an interview, you may be asked to implement the logic behind `indexOf`.

**Brute Force Approach:**
For every character in `haystack`, try to match the entire `needle`. If a mismatch occurs, reset the pointer to the next character in `haystack` and start over.
- *Why it's slow:* If `haystack = "AAAAAAAAAAAAAB"` and `needle = "AAAB"`, you will successfully match 'AAA' over and over again, only to fail on the 'B', and then you have to restart the check from the very beginning of 'AAA'.

## The Concept of LPS (Longest Prefix Suffix)

The core insight to avoid restarting the search from scratch is realizing that **the characters you just successfully matched contain valuable information.**

If you are looking for `"ABABC"` and you matched `"ABAB"` but failed on the `'C'`, you don't need to go all the way back to the beginning. You *know* the last two characters you saw were `"AB"`. And `"AB"` happens to be the prefix of your needle! So you can just resume checking from the 3rd character.

This is the foundation of the KMP algorithm.
