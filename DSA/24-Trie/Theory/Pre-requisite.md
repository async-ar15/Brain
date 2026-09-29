# 17. Tries - Pre-requisites

## What is a Trie?

A Trie (pronounced "Try") or Prefix Tree is a special type of tree used to efficiently store and retrieve keys in a dataset of strings.

Imagine you have a dictionary of words: `["cat", "car", "cart", "dog"]`.
Instead of storing them in a List or a HashSet, a Trie stores them character by character in a tree structure.
- The root represents an empty string.
- It has branches for 'c' and 'd'.
- The 'c' node has a branch for 'a'.
- The 'a' node has branches for 't' and 'r'.

## Why use a Trie over a HashSet?

If you have a `HashSet<String>`, checking if a word exists takes $O(L)$ time, where $L$ is the length of the word (because of hashing and equals()). A Trie also takes $O(L)$ time.

**So why use a Trie?**
Because HashSets are terrible at **PREFIX** matching!
If you want to know "Are there any words that START WITH 'ca'?", a HashSet would require iterating through every single word.
A Trie answers this in $O(L)$ time. You just walk down the 'c' -> 'a' path. If the path exists, the prefix exists!

## The TrieNode Definition

Unlike a Binary Tree with just `left` and `right`, a TrieNode can have up to 26 children (for lowercase English letters).
It also needs a boolean flag to mark the end of a valid word. (Otherwise, in the example above, we wouldn't know if "ca" was a real word or just a prefix for "cat").

```java
class TrieNode {
    TrieNode[] children;
    boolean isEndOfWord;
    
    public TrieNode() {
        // Array of size 26 for 'a' to 'z'
        children = new TrieNode[26]; 
        isEndOfWord = false;
    }
}
```
