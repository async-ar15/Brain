# Union Find — Revision Sheet

---

## 01. Number of Provinces

**In My Words:** There are `n` cities. Some of them are connected. You are given an $n \times n$ matrix `isConnected` where `isConnected[i][j] = 1` if the $i^{th}$ city and the $j^{th}$ city are directly connected, and 0 otherwise. Return the total number of provinces (connected components).

**The Bridge:** This can be solved with standard DFS traversal. However, this is the textbook problem for Union-Find! Start with `count = n`. Every time you process an edge and successfully union two nodes, decrement `count`. At the end, `count` is your answer.

**Optimized Intuition:**
Initialize `UnionFind uf = new UnionFind(n)`.
Loop `i` from 0 to n. Loop `j` from `i + 1` to n (only top-right triangle needed).
If `isConnected[i][j] == 1`, `uf.union(i, j)`.
Return `uf.count`.

**Time:** $O(N^2)$ (to read the matrix) | **Space:** $O(N)$

**Code Solution:**
*(Refer to standard UnionFind template. Call `union(i, j)` and return `count`)*.

---

## 02. Redundant Connection

**In My Words:** You are given an array of `edges`. The graph started as a tree with `N` nodes, and one extra edge was added, creating a cycle. Return an edge that can be removed so that the resulting graph is a tree of `N` nodes.

**The Bridge:** A tree is a graph with exactly $N-1$ edges and no cycles. Adding one edge creates a cycle. The moment we try to `union` an edge where both nodes ALREADY share the same root, we know that edge caused the cycle!

**Optimized Intuition:**
Initialize `UnionFind uf = new UnionFind(n + 1)` (1-indexed).
Loop through `edges`.
`if (!uf.union(edge[0], edge[1])) return edge;`

**Template:** Union-Find Cycle Detection

**Time:** $O(N \cdot \alpha(N))$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    // (Insert standard UnionFind class with path compression here)
    
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        UnionFind uf = new UnionFind(n + 1); 
        
        for (int[] edge : edges) {
            if (!uf.union(edge[0], edge[1])) {
                return edge; // Cycle detected
            }
        }
        return new int[0];
    }
}
```

---

## 03. Accounts Merge

**In My Words:** Given a list of `accounts` where `accounts[i] = [name, email1, email2, ...]`. If two accounts have at least one common email, they belong to the same person. Merge the accounts and return them in sorted order.

**Constraint Whispers:**
- Connecting entities based on shared properties is exactly what Union-Find excels at.
- But Union-Find operates on integer IDs, not strings!

**The Bridge:** We need to map every unique email to an Integer ID so we can use Union-Find. Then, for every account, we union the ID of its first email with the IDs of all its other emails. Finally, we group the emails by their root ID.

**Optimized Intuition:**
1. Loop through all accounts. Assign a unique `Integer` ID to every unique email using a Map `emailToId`. Keep a Map `emailToName`.
2. Initialize `UnionFind uf = new UnionFind(emailToId.size())`.
3. Loop through accounts again. For each account, `union(emailToId.get(emails[1]), emailToId.get(emails[j]))`.
4. Create a Map `Map<Integer, List<String>> components` to group emails. Loop through all unique emails, find their root `uf.find(emailToId.get(email))`, and add the email to the root's list.
5. Format the result: Sort each email list, prepend the Name from `emailToName`, and add to final list.

**Time:** $O(E \log E)$ where E is total emails | **Space:** $O(E)$

**Code Solution:**
```java
class Solution {
    // (Assume standard UnionFind class is defined here)
    
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, Integer> emailToId = new HashMap<>();
        Map<String, String> emailToName = new HashMap<>();
        int id = 0;
        
        for (List<String> account : accounts) {
            String name = account.get(0);
            for (int i = 1; i < account.size(); i++) {
                String email = account.get(i);
                if (!emailToId.containsKey(email)) {
                    emailToId.put(email, id++);
                    emailToName.put(email, name);
                }
            }
        }
        
        UnionFind uf = new UnionFind(id);
        
        for (List<String> account : accounts) {
            int firstEmailId = emailToId.get(account.get(1));
            for (int i = 2; i < account.size(); i++) {
                uf.union(firstEmailId, emailToId.get(account.get(i)));
            }
        }
        
        Map<Integer, List<String>> components = new HashMap<>();
        for (String email : emailToId.keySet()) {
            int root = uf.find(emailToId.get(email));
            components.putIfAbsent(root, new ArrayList<>());
            components.get(root).add(email);
        }
        
        List<List<String>> res = new ArrayList<>();
        for (int root : components.keySet()) {
            List<String> emails = components.get(root);
            Collections.sort(emails);
            emails.add(0, emailToName.get(emails.get(0))); // Prepend name
            res.add(emails);
        }
        
        return res;
    }
}
```
