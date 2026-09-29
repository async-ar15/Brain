# Theory - Monotonic Stack

A Monotonic Stack is an incredibly powerful variation of a regular stack that allows us to find the "Next Greater Element" or "Next Smaller Element" in an array in exactly $O(N)$ time.

## Where is it commonly used?
- Daily Temperatures / Stock Spans
- Largest Rectangle in Histogram / Maximal Rectangle
- Trapping Rain Water

## Strong signals to look for
- "Find the **Next Greater Element** (NGE)."
- "Find the **Next Smaller Element** (NSE)."
- "How many days until a warmer temperature?"
- Problems asking about boundaries (how far left/right can this bar extend before hitting a smaller bar?).

## Why is it $O(N)$?
It looks like $O(N^2)$ because there's a `while` loop inside a `for` loop. But look closer: every element is pushed onto the stack EXACTLY ONCE. Every element is popped off the stack AT MOST ONCE. 
$N$ pushes + $N$ pops = $2N$ operations. $O(N)$.

## The Standard Template

This template finds the Next Greater Element. (To find Next Smaller Element, just flip the `<` to `>`).
Usually, we push **indices** to the stack, not the values themselves, because we often need to calculate distances (`currentIndex - poppedIndex`).

```java
public int[] nextGreaterElementTemplate(int[] nums) {
    int[] result = new int[nums.length]; // Stores the answer for each index
    Arrays.fill(result, -1);             // Default if no greater element exists
    
    // The stack will store INDICES of elements looking for their Next Greater Element
    // We enforce a Monotonically Decreasing stack of values.
    Deque<Integer> stack = new ArrayDeque<>();
    
    for (int i = 0; i < nums.length; i++) {
        // While current element is GREATER than the element at stack.top()
        while (!stack.isEmpty() && nums[i] > nums[stack.peek()]) {
            int poppedIndex = stack.pop();
            
            // The current element (nums[i]) is the Next Greater Element for poppedIndex!
            result[poppedIndex] = nums[i]; 
            
            // If the problem asked for "Distance to next greater":
            // result[poppedIndex] = i - poppedIndex;
        }
        
        // Push the current index onto the stack to wait for its Next Greater Element
        stack.push(i);
    }
    
    return result;
}
```

# Your interview cheat code

```text
1. Are you looking forward (or backward) for a value strictly GREATER or SMALLER?
                  ↓
2. Do you need to do this for EVERY element in an array?
                  ↓
3. Is O(N^2) too slow?
                  ↓
           MONOTONIC STACK (O(N) Time, O(N) Space)
```
