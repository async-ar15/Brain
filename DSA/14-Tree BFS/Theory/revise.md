# Tree BFS — Revision Sheet

---

## 01. Binary Tree Level Order Traversal

**In My Words:** Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**The Bridge:** This is the literal definition of the BFS template.

**Optimized Intuition:** Use a Queue. Enqueue root. While queue is not empty: take `size`. Loop `size` times: dequeue node, add to level list, enqueue left child, enqueue right child. Add level list to final result.

**Template:** Level Order BFS

**Time:** $O(N)$ | **Space:** $O(N)$ (Queue can hold at most $N/2$ nodes at the widest level)

**Code Solution:**
```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = queue.poll();
                level.add(curr.val);
                
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            res.add(level);
        }
        
        return res;
    }
}
```

---

## 02. Binary Tree Right Side View

**In My Words:** Imagine you are standing on the right side of the tree. Return the values of the nodes you can see, ordered from top to bottom.

**The Bridge:** What does "right side view" actually mean? It means returning the LAST node of every level! Since BFS processes levels perfectly, we just need to grab the last element processed in each level's `for` loop.

**Optimized Intuition:** Run standard BFS. Inside the `size` loop, if `i == size - 1`, we are at the last node of the current level. Add its value to our result list.

**Time:** $O(N)$ | **Space:** $O(N)$ (Queue)

**Code Solution:**
```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            for (int i = 0; i < size; i++) {
                TreeNode curr = queue.poll();
                
                // If it's the last element in the level, it's visible from the right
                if (i == size - 1) {
                    res.add(curr.val);
                }
                
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
        }
        
        return res;
    }
}
```

---

## 03. Average of Levels in Binary Tree

**In My Words:** Given the root, return the average value of the nodes on each level.

**The Bridge:** This is just Level Order Traversal where, instead of adding values to a list, we add them to a running sum for that level, and then divide by the `levelSize`.

**Optimized Intuition:** Run standard BFS. Track a `double currentSum = 0` before the inner loop. Inside the loop, `currentSum += curr.val`. After the loop, `res.add(currentSum / size)`.

**Time:** $O(N)$ | **Space:** $O(N)$ (Queue)

**Code Solution:**
```java
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<>();
        if (root == null) return res;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            double sum = 0;
            
            for (int i = 0; i < size; i++) {
                TreeNode curr = queue.poll();
                sum += curr.val;
                
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            
            res.add(sum / size);
        }
        
        return res;
    }
}
```
