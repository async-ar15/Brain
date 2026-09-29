# Theory - Prefix Sum

Prefix Sum is a technique where we precalculate cumulative sums of an array. It transforms $O(N)$ subarray sum calculations into $O(1)$ lookups.

## Where is it commonly used?
- Any problem asking for the **sum of a subarray/range**.
- Problems asking for the **count of subarrays** that sum to a specific target (especially when negative numbers are present).
- Finding equilibrium/pivot indexes.

## Strong signals to look for
- "Sum of elements between indices L and R."
- "Number of continuous subarrays that sum to K."
- The array contains **negative numbers** and asks for subarray sums (Sliding window fails here because expanding the window might *decrease* the sum).

## The "Running Sum + HashMap" Pattern

This is one of the most important concepts in modern interview questions (e.g., *Subarray Sum Equals K*). 

If you want to find if there is a subarray that sums to `K` ending at current index `i`, you don't need to check all subarrays. You just maintain a `runningSum`. 
If `runningSum - K` exists as a prefix sum earlier in the array, then a subarray summing to `K` MUST exist between that earlier point and `i`!

**Math Proof:**
If `Prefix_Current - Prefix_Old = K`, then `Prefix_Current - K = Prefix_Old`.

### Template: Subarray Sum with HashMap

```java
public int subarraySumTemplate(int[] nums, int k) {
    // Map stores: <Prefix Sum, Frequency>
    Map<Integer, Integer> map = new HashMap<>();
    
    // Base case: A prefix sum of 0 has occurred exactly once (before any elements)
    map.put(0, 1); 
    
    int runningSum = 0;
    int count = 0;
    
    for (int num : nums) {
        runningSum += num; // Calculate current prefix sum
        
        // Does runningSum - k exist in our map?
        int remove = runningSum - k;
        if (map.containsKey(remove)) {
            // We found valid subarrays! Add their frequency to our count.
            count += map.get(remove);
        }
        
        // Add the current running sum to the map
        map.put(runningSum, map.getOrDefault(runningSum, 0) + 1);
    }
    
    return count;
}
```

# Your interview cheat code

```text
1. Does the problem involve subarrays?
                  ↓
2. Does it involve SUMS of those subarrays?
                  ↓
3. Are there multiple queries OR does the array contain negative numbers?
                  ↓
           PREFIX SUM (Often combined with HashMap)
```
