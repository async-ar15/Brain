# Tries — Revision Sheet

---

## 01. Implement Trie (Prefix Tree)

**In My Words:** Design a Trie class with `insert`, `search`, and `startsWith` methods.

**The Bridge:** This is the foundational template.

**Optimized Intuition:** 
Create a `TrieNode` class with `TrieNode[] children = new TrieNode[26]` and `boolean isWord`.
For `insert`, walk down the tree, creating nodes if they don't exist, and mark the last node as `isWord = true`.
For `search`, walk down. If a node doesn't exist, return false. At the end, return `isWord`.
For `startsWith`, same as search, but just return true at the end.

**Time:** $O(L)$ for all ops where $L$ is word length | **Space:** $O(N \cdot L)$ for all inserted words

**Code Solution:**
*(Refer to the standard template in Theory.md)*

---

## 02. Design Add and Search Words Data Structure

**In My Words:** Design a data structure that supports adding words and searching words, where the search word can contain the `.` character which matches ANY letter.

**Constraint Whispers:**
- The `.` character means we have to branch out and check multiple paths!

**The Bridge:** It's exactly a Trie, but the `search` method becomes a recursive DFS. When we encounter a `.`, we don't know which child path to take, so we must try ALL non-null children. If ANY of those paths return true, we found a match.

**Optimized Intuition:** 
`addWord` is standard Trie insert.
`search(word)` calls a helper `dfs(word, index, node)`.
If `index == word.length`, return `node.isWord`.
If `word[index]` is a normal letter, go down that path recursively.
If `word[index]` is `.`, loop through all 26 children. If `child != null`, recursively call `dfs`. If it returns true, return true.

**Time:** $O(L)$ for add, $O(26^L)$ worst case for search with all dots | **Space:** $O(N \cdot L)$

**Code Solution:**
```java
class WordDictionary {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord = false;
    }
    
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
        }
        curr.isWord = true;
    }
    
    public boolean search(String word) {
        return dfs(word, 0, root);
    }
    
    private boolean dfs(String word, int index, TrieNode node) {
        if (index == word.length()) {
            return node.isWord;
        }
        
        char c = word.charAt(index);
        
        if (c == '.') {
            for (TrieNode child : node.children) {
                if (child != null && dfs(word, index + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            if (node.children[c - 'a'] == null) {
                return false;
            }
            return dfs(word, index + 1, node.children[c - 'a']);
        }
    }
}
```

---

## 03. Word Search II

**In My Words:** Given an $m \times n$ board of characters and a list of `words`, return all words on the board. (Simultaneous multi-word search).

**Constraint Whispers:**
- Running standard DFS Word Search for every single word in the dictionary will TLE because the dictionary is huge.

**The Bridge:** Instead of searching the board for words, we can search the Trie for board paths! We put all dictionary words into a Trie. Then, we start a DFS from every cell on the board. As we move on the board, we ALSO move down the Trie. If we ever hit a null node in the Trie, we immediately stop the DFS (pruning). If we hit `isWord`, we found a word!

**Optimized Intuition:** 
1. Build a Trie from the `words` array.
2. DFS from every cell `(r, c)`. Pass the current `TrieNode` into the DFS.
3. If `TrieNode.children[board[r][c]] == null`, return.
4. Move `TrieNode` to that child. If it's a word, add it to result (and set `isWord = false` so we don't add it twice).
5. Mark cell visited, recursively DFS 4 directions, backtrack cell.

**Time:** $O(M \cdot N \cdot 4^L)$ but heavily pruned by Trie | **Space:** $O(\text{Total letters in dictionary})$

**Code Solution:**
```java
class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word = null; // Store the actual word at the end node to avoid passing stringbuilder
    }
    
    public List<String> findWords(char[][] board, String[] words) {
        // Build Trie
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode curr = root;
            for (char c : w.toCharArray()) {
                if (curr.children[c - 'a'] == null) curr.children[c - 'a'] = new TrieNode();
                curr = curr.children[c - 'a'];
            }
            curr.word = w; // Mark end with the word itself
        }
        
        List<String> res = new ArrayList<>();
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                dfs(board, r, c, root, res);
            }
        }
        return res;
    }
    
    private void dfs(char[][] board, int r, int c, TrieNode node, List<String> res) {
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] == '#') return;
        
        char letter = board[r][c];
        TrieNode nextNode = node.children[letter - 'a'];
        if (nextNode == null) return; // Prune!
        
        if (nextNode.word != null) {
            res.add(nextNode.word);
            nextNode.word = null; // Prevent duplicate additions
        }
        
        board[r][c] = '#'; // Visited
        dfs(board, r + 1, c, nextNode, res);
        dfs(board, r - 1, c, nextNode, res);
        dfs(board, r, c + 1, nextNode, res);
        dfs(board, r, c - 1, nextNode, res);
        board[r][c] = letter; // Backtrack
    }
}
```
