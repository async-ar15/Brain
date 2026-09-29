# Theory - Tries

Tries are specialized data structures that are almost exclusively used for string manipulation, autocomplete systems, and spell checkers.

## Where is it commonly used?
1. **Autocomplete Systems:** Finding all words that share a prefix.
2. **Spell Check / Word Search II:** Efficiently searching a 2D grid for a massive list of dictionary words.
3. **Bitwise XOR problems:** A specialized binary trie where edges are `0` or `1` can be used to find maximum XOR pairs.

## Strong signals to look for
- "Design a data structure that supports insert and search of words."
- "Find words that **start with** a given prefix."
- You have a dictionary of words and need to search a grid (Word Search II).

## The Standard Trie Implementation

Building a Trie is straightforward pointer manipulation.
- To map a character like `'c'` to an array index `[0-25]`, we use ASCII math: `char - 'a'`. So `'c' - 'a' = 2`.

### Template: Insert and Search

```java
class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    // Time: O(L) where L is length of word
    public void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (curr.children[index] == null) {
                curr.children[index] = new TrieNode();
            }
            curr = curr.children[index]; // Move down the tree
        }
        curr.isEndOfWord = true; // Mark the end of the full word
    }
    
    // Time: O(L)
    public boolean search(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (curr.children[index] == null) {
                return false; // The path doesn't exist
            }
            curr = curr.children[index];
        }
        return curr.isEndOfWord; // Must be a complete word, not just a prefix
    }
    
    // Time: O(L)
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for (char c : prefix.toCharArray()) {
            int index = c - 'a';
            if (curr.children[index] == null) {
                return false;
            }
            curr = curr.children[index];
        }
        return true; // We found the prefix path! Doesn't matter if it's a full word.
    }
}
```

# Your interview cheat code

```text
1. Are you storing strings and matching PREFIXES?
                  ↓
2. Is it a Word Search game with a dictionary of words?
                  ↓
           TRIE (Prefix Tree)
```
