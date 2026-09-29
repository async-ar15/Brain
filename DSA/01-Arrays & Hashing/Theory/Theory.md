# Theory - Arrays & Hashing

Hashing is the ultimate time-space tradeoff. You sacrifice $O(N)$ extra memory to reduce nested loops (which take $O(N^2)$ time) into a single pass (which takes $O(N)$ time).

## Where is it commonly used?
1. **Finding pairs/complements**: When you need to find if two numbers satisfy a mathematical condition (like summing to a target).
2. **Frequency counting**: When you need to count how many times elements appear (e.g., Anagrams, majority elements).
3. **Duplicate detection**: Checking if an array contains duplicates.
4. **Caching/Memoization**: Storing previously computed results to avoid redundant work.

## Strong signals to look for (When to use Hashing)
- "Find a pair of elements..."
- "Check if there is a duplicate..."
- "Count the occurrences..."
- Time limit is strict (e.g. $N \le 10^5$ meaning $O(N^2)$ is not allowed), but the array is **NOT sorted**. (If it were sorted, you'd use Two Pointers).
- "O(N) time complexity is required."

## When NOT to use Hashing
- The array is sorted, and you just need to find a pair (Use Two Pointers, it saves $O(N)$ space).
- The problem explicitly states "O(1) extra space" (Hashing inherently requires $O(N)$ space).
- You need elements in a specific order (HashMaps/HashSets do not maintain insertion order or sorted order, though `LinkedHashMap` and `TreeMap` exist, they have different tradeoffs).

## Common Hashing Patterns

### 1. The Complement Pattern (Look Back)
Instead of looking forward for a match, you put elements you've seen so far into a HashMap. For each new element, you calculate what it *needs* (its complement) and check if that complement is already in the map.

**Think:**
- Two Sum

```java
public int[] complementTemplate(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>(); // value -> index
    
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[]{map.get(complement), i};
        }
        map.put(nums[i], i);
    }
    return new int[]{};
}
```

### 2. Frequency Counting / Histogram Pattern
Iterate through the data and count the occurrences of each element.

**Think:**
- Valid Anagram
- Majority Element

```java
public boolean frequencyTemplate(String s, String t) {
    if (s.length() != t.length()) return false;
    
    int[] count = new int[26]; // Often faster than HashMap for lowercase letters
    
    for (int i = 0; i < s.length(); i++) {
        count[s.charAt(i) - 'a']++; // Increment for string s
        count[t.charAt(i) - 'a']--; // Decrement for string t
    }
    
    for (int c : count) {
        if (c != 0) return false;
    }
    return true;
}
```

### 3. Grouping Pattern
You have a list of items and you want to group them by some shared property (a signature or key). 

**Think:**
- Group Anagrams

```java
public List<List<String>> groupingTemplate(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();
    
    for (String s : strs) {
        String key = generateKey(s); // Sort the string, or create a frequency string
        
        if (!map.containsKey(key)) {
            map.put(key, new ArrayList<>());
        }
        map.get(key).add(s);
    }
    
    return new ArrayList<>(map.values());
}
```

# Your interview cheat code

```text
1. Am I looking for pairs or complements?
                  ↓
2. Is the array unsorted?
                  ↓
3. Do I need to count frequencies?
                  ↓
4. Am I grouping items with a common trait?
                  ↓
           ARRAYS & HASHING (O(N) Time, O(N) Space)
```
