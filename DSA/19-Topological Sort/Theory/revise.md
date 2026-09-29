# Topological Sort — Revision Sheet

---

## 01. Course Schedule

**In My Words:** There are `numCourses` labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates you must take course `b` first if you want to take course `a`. Return true if you can finish all courses.

**The Bridge:** This is the pure definition of cycle detection in a Directed Acyclic Graph (DAG). If there's a cycle, you can't finish.

**Optimized Intuition:** Kahn's Algorithm. Build `adjList` and `inDegree` array. (Note: `[a, b]` means edge is `b -> a`). Add all nodes with `inDegree == 0` to Queue. Process Queue: `count++`, decrement neighbors' in-degree, add to Queue if 0. At the end, return `count == numCourses`.

**Template:** Kahn's Algorithm

**Time:** $O(V + E)$ | **Space:** $O(V + E)$

**Code Solution:**
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        
        int[] inDegree = new int[numCourses];
        
        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]); // pre[1] -> pre[0]
            inDegree[pre[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) queue.offer(i);
        }
        
        int count = 0;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            count++;
            
            for (int neighbor : adj.get(curr)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        return count == numCourses;
    }
}
```

---

## 02. Course Schedule II

**In My Words:** Same as Course Schedule, but instead of returning true/false, return the ACTUAL ORDER you should take the courses in. If impossible, return an empty array.

**The Bridge:** Kahn's algorithm processes nodes in exactly the valid topological order! We just need to record the nodes as we pop them from the queue.

**Optimized Intuition:** Exactly the same code as Course Schedule, but maintain an `int[] order = new int[numCourses]`. Whenever you `poll()` from the queue, `order[index++] = curr`. If `index == numCourses` at the end, return `order`. Else return `new int[0]`.

**Template:** Kahn's Algorithm

**Time:** $O(V + E)$ | **Space:** $O(V + E)$

**Code Solution:**
```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        
        int[] inDegree = new int[numCourses];
        
        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) queue.offer(i);
        }
        
        int[] order = new int[numCourses];
        int index = 0;
        
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            order[index++] = curr;
            
            for (int neighbor : adj.get(curr)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        return index == numCourses ? order : new int[0];
    }
}
```

---

## 03. Alien Dictionary

**In My Words:** There is a new alien language that uses the English alphabet. However, the order of the letters is unknown. You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are **sorted lexicographically** by the rules of this new language. Return a string of the unique letters sorted in this new order.

**Constraint Whispers:**
- Hard problem. Building the graph is harder than the sort itself.

**The Bridge:** If `words` is sorted, then comparing adjacent words gives us order rules. E.g. `["wrt", "wrf"]`. The first difference is 't' and 'f'. Because it's sorted, 't' MUST come before 'f'. This gives us a directed edge `t -> f`. Once we build all these edges, we just run Topological Sort on the characters!

**Optimized Intuition:** 
1. Initialize Adjacency List `Map<Character, Set<Character>>` and `Map<Character, Integer> inDegree`. Add ALL unique characters from ALL words to both maps first (with inDegree 0).
2. Compare adjacent words `words[i]` and `words[i+1]`. 
3. Edge case: if `words[i]` is longer than `words[i+1]` and starts with `words[i+1]` (e.g. "abc", "ab"), it's invalid. Return "".
4. Find first differing character. Add edge `c1 -> c2`. Increment `inDegree[c2]`. `break` (we only get ONE rule per word pair).
5. Run Kahn's Algorithm on the Maps.
6. Check for cycles: if `result.length() != inDegree.size()`, return "".

**Time:** $O(C)$ where C is total length of all words | **Space:** $O(1)$ (Max 26 characters)

**Code Solution:**
```java
class Solution {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> adj = new HashMap<>();
        Map<Character, Integer> inDegree = new HashMap<>();
        
        // Initialize for all unique characters
        for (String w : words) {
            for (char c : w.toCharArray()) {
                adj.putIfAbsent(c, new HashSet<>());
                inDegree.putIfAbsent(c, 0);
            }
        }
        
        // Build graph
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            
            // Edge case: invalid sorted order (e.g. "abc", "ab")
            if (w1.length() > w2.length() && w1.startsWith(w2)) {
                return "";
            }
            
            // Find first difference
            for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
                char c1 = w1.charAt(j);
                char c2 = w2.charAt(j);
                if (c1 != c2) {
                    if (!adj.get(c1).contains(c2)) {
                        adj.get(c1).add(c2);
                        inDegree.put(c2, inDegree.get(c2) + 1);
                    }
                    break; // Only the FIRST difference matters!
                }
            }
        }
        
        // Kahn's BFS
        Queue<Character> queue = new LinkedList<>();
        for (char c : inDegree.keySet()) {
            if (inDegree.get(c) == 0) queue.offer(c);
        }
        
        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            char curr = queue.poll();
            sb.append(curr);
            for (char neighbor : adj.get(curr)) {
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        return sb.length() == inDegree.size() ? sb.toString() : "";
    }
}
```
