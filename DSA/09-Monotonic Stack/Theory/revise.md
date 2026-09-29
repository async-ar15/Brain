# Monotonic Stack — Revision Sheet

---

## 01. Daily Temperatures

**In My Words:** Given an array of temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the $i^{th}$ day to get a warmer temperature.

**Constraint Whispers:**
- $O(N)$ time preferred. $N \le 10^5$.

**The Bridge:** "Number of days until a warmer temperature" = "Distance to the Next Greater Element". This is the textbook definition of a Monotonically Decreasing Stack. 

**Optimized Intuition:** 
Maintain a decreasing stack of *indices*. Iterate through temps. If the current temp is greater than `temps[stack.peek()]`, we found a warmer day for the index at the top of the stack! Pop that index off, and its answer is `current_day - popped_day`. Keep popping until the current temp is no longer greater, then push the current day.

**Template:** Monotonic Decreasing Stack

**Time:** $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int prevDay = stack.pop();
                result[prevDay] = i - prevDay; // The distance
            }
            stack.push(i);
        }
        
        return result;
    }
}
```

---

## 02. Largest Rectangle in Histogram

**In My Words:** Given an array of integer heights representing a histogram, return the area of the largest rectangle.

**Constraint Whispers:**
- Hard problem. $N \le 10^5$. $O(N)$ time required.

**The Bridge:** A rectangle's height is determined by the *shortest* bar in its span. For any given bar `i`, what is the widest rectangle that can be formed using `heights[i]` as the *full height*? It extends left until it hits a shorter bar, and extends right until it hits a shorter bar. 
Therefore, for every bar, we need its **Next Smaller Element on the left** and **Next Smaller Element on the right**. A Monotonic Increasing stack gives us exactly this.

**Optimized Intuition:**
Maintain an increasing stack of indices. If `heights[i] < heights[stack.peek()]`, then `heights[i]` is the Right-Side NSE for the popped bar. What about the Left-Side NSE? It is the NEW top of the stack after popping! 
Area = `heights[popped] * (Right_NSE_Index - Left_NSE_Index - 1)`.

**Template:** Monotonic Increasing Stack

**Gotcha:** We need to process any bars left in the stack at the end. An easy trick is to append a `0` height bar at the end of the array to force the stack to pop everything.

**Time:** $O(N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        
        // We use an index going up to heights.length to act as the trailing 0
        for (int i = 0; i <= heights.length; i++) {
            int currHeight = (i == heights.length) ? 0 : heights[i];
            
            while (!stack.isEmpty() && currHeight < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                
                // Left limit is the new top of the stack. 
                // If stack is empty, it means this bar extends all the way to index 0.
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }
        
        return maxArea;
    }
}
```

---

## 03. Car Fleet

**In My Words:** There are `n` cars on a single-lane road going to a destination. Slower cars block faster cars, forming a "fleet" that travels at the slower car's speed. How many fleets arrive at the destination?

**The Bridge:** Calculate the time it takes for each car to reach the destination: `(target - position) / speed`. If a car starts BEHIND another car, but takes LESS time to reach the target, it will catch up and form a fleet. We must process cars starting from the closest to the destination (sort by position descending).

**Optimized Intuition:** 
Sort cars by position descending. Iterate through. Calculate time to arrive. Maintain a monotonic decreasing stack of *arrival times*. If a car takes LESS or EQUAL time than the car in front of it (stack peek), it catches up and merges (do NOT push it to stack). If it takes MORE time, it forms a new fleet (push to stack). The answer is the size of the stack.

**Gotcha:** Time is a `double`! Avoid integer division truncation.

**Time:** $O(N \log N)$ (sorting) | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        double[][] cars = new double[n][2];
        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = (double)(target - position[i]) / speed[i]; // Time to target
        }
        
        // Sort descending by position
        Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0]));
        
        Deque<Double> stack = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            double time = cars[i][1];
            // If stack is empty, or this car takes LONGER than the fleet in front of it
            if (stack.isEmpty() || time > stack.peek()) {
                stack.push(time);
            }
            // Else, it catches up to the fleet in front (do nothing, it merges)
        }
        
        return stack.size();
    }
}
```
