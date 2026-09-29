# Theory - Stack

Stacks are the ultimate tool for handling "nested" relationships or processes that require you to remember recent, unresolved states.

## Where is it commonly used?
1. **Validating Pairs:** Matching parentheses, brackets, tags.
2. **Reverse Polish Notation / Expression Evaluation:** Parsing math formulas.
3. **Tracking state in a path:** Directory paths, web browser history.
4. **Monotonic Stacks (Day 9):** Finding the Next Greater/Smaller element.
5. **Depth-First Search (DFS):** The underlying engine for recursive tree/graph traversal is the call stack.

## Strong signals to look for
- "Valid Parentheses" or matching opening/closing tags.
- Nested structures `[[[]]]`.
- "Evaluate this expression".
- The problem requires you to temporarily store items until a specific "resolving" condition is met.

## The Matching Pattern (Valid Parentheses)

Whenever you have pairs that must close in the correct order (like `(`, `[`, `{`), a stack perfectly models this.
1. When you see an "opener", push it to the stack (it's unresolved).
2. When you see a "closer", it MUST match the *most recent* unresolved opener (the top of the stack). 
3. If it matches, pop it. If it doesn't match (or stack is empty), it's invalid.

### Template: Bracket Matching

```java
public boolean isValidTemplate(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    
    for (char c : s.toCharArray()) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c); // Opener -> push to waitlist
        } else {
            // Closer -> check if waitlist is valid
            if (stack.isEmpty()) return false;
            
            char top = stack.pop();
            if (c == ')' && top != '(') return false;
            if (c == ']' && top != '[') return false;
            if (c == '}' && top != '{') return false;
        }
    }
    
    // If stack isn't empty, some openers never found a closer
    return stack.isEmpty(); 
}
```

# Your interview cheat code

```text
1. Are you parsing nested structures (parentheses, tags)?
                  ↓
2. Do you need to remember previous elements and resolve them later in reverse order?
                  ↓
3. Is it related to expression evaluation (Postfix/RPN)?
                  ↓
                 STACK (O(N) Time, O(N) Space)
```
