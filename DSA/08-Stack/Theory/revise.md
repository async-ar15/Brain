# Stack — Revision Sheet

---

## 01. Valid Parentheses

**In My Words:** Given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid (brackets must be closed in the correct order).

**The Bridge:** Open brackets are "unresolved". They must be closed in the exact reverse order they were opened (LIFO). This perfectly matches a stack.

**Optimized Intuition:** Loop through string. If opening bracket, push to stack. If closing bracket, pop from stack and check if it matches. If stack is empty when finding a closer, or if they don't match, return false. Finally, if stack is not empty at the end, return false (unclosed openers).

**Template:** Bracket Matching

**Time:** $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                
                char top = stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        
        return stack.isEmpty();
    }
}
```

---

## 02. Min Stack

**In My Words:** Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time $O(1)$.

**Constraint Whispers:**
- `getMin()` MUST be $O(1)$. You cannot search the stack for the minimum.

**The Bridge:** If we just keep a single `min` variable, what happens when we `pop` that minimum? We lose the previous minimum! So, we need to remember the "minimum AT THAT MOMENT" for EVERY element we push.

**Optimized Intuition:** We can use two stacks. 
1. `stack`: Stores the actual values.
2. `minStack`: Stores the minimum value seen *so far* up to the current height of the stack.
When pushing `x`, push `x` to `stack`. Push `Math.min(x, minStack.top())` to `minStack`. When popping, pop from both!

**Time:** $O(1)$ all operations | **Space:** $O(N)$ for the extra stack

**Code Solution:**
```java
class MinStack {
    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty()) {
            minStack.push(val);
        } else {
            minStack.push(Math.min(val, minStack.peek()));
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
```

---

## 03. Evaluate Reverse Polish Notation

**In My Words:** Evaluate the value of an arithmetic expression in RPN. (e.g. `["2","1","+","3","*"]` -> `((2 + 1) * 3) = 9`).

**The Bridge:** In RPN, operators strictly follow their two operands. When you see a number, you wait. When you see an operator, you immediately apply it to the two most recently seen numbers. "Most recent" = LIFO = Stack.

**Optimized Intuition:** Iterate through tokens. If token is a number, parse to int and push to stack. If token is an operator `(+, -, *, /)`, pop two numbers, apply the operator, and push the result back onto the stack. At the end, the stack contains exactly 1 element: the final answer.

**Gotcha:** Order matters for `-` and `/`. The FIRST popped number is the RIGHT operand. The SECOND popped number is the LEFT operand. (e.g. `[13, 5, /]` -> push 13, push 5. pop 5 (b), pop 13 (a). Result is `a / b = 13 / 5`).

**Time:** $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (String t : tokens) {
            if (t.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            } else if (t.equals("-")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a - b);
            } else if (t.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (t.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a / b);
            } else {
                stack.push(Integer.parseInt(t));
            }
        }
        
        return stack.pop();
    }
}
```

---

## 04. Generate Parentheses

**In My Words:** Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**The Bridge:** This is technically a Backtracking problem, but it strongly relates to Stacks conceptually because we must maintain "validity". We can't close a parenthesis unless an open one is "waiting" on the stack. Instead of a literal stack, we just keep counts of `openN` and `closedN`.

**Optimized Intuition:** 
Backtracking rules:
1. Base case: `openN == n` and `closedN == n`. Add string to result.
2. We can add an `(` if `openN < n`.
3. We can add a `)` if `closedN < openN` (this ensures validity).

**Time:** $O(4^N / \sqrt{N})$ (Catalan number) | **Space:** $O(N)$ (recursion stack)

**Code Solution:**
```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        backtrack(res, new StringBuilder(), 0, 0, n);
        return res;
    }
    
    private void backtrack(List<String> res, StringBuilder current, int open, int close, int max) {
        if (current.length() == max * 2) {
            res.add(current.toString());
            return;
        }
        
        if (open < max) {
            current.append("(");
            backtrack(res, current, open + 1, close, max);
            current.deleteCharAt(current.length() - 1);
        }
        if (close < open) {
            current.append(")");
            backtrack(res, current, open, close + 1, max);
            current.deleteCharAt(current.length() - 1);
        }
    }
}
```
