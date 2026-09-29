# 1. Arrays & Hashing - Pre-requisites

## 1. Arrays (Revisited)

An array is a collection of items stored at contiguous memory locations.

Key Characteristics:
- **Fixed Size (usually)**: In Java, arrays have a fixed size (`int[] arr = new int[5];`).
- **Dynamic Arrays**: `ArrayList` in Java handles resizing automatically behind the scenes (usually by doubling the size when full and copying elements).

| Operation | Time Complexity |
| :--- | :--- |
| **Access (Index)** | $O(1)$ |
| **Search (Value)** | $O(N)$ |
| **Insert/Delete (End)** | $O(1)$ (amortized for dynamic) |
| **Insert/Delete (Middle/Start)** | $O(N)$ |

## 2. Hashing (HashMaps & HashSets)

Hashing is a technique used to uniquely identify a specific object from a group of similar objects. In DSA, we use it to achieve $O(1)$ lookup times.

### How it works:
1. **Hash Function**: Takes a key (like a string or integer) and converts it into an integer (the hash code).
2. **Buckets**: An array where the actual data is stored. The hash code determines the index (bucket).
3. **Collisions**: When two different keys produce the same hash code, they are placed in the same bucket (usually handled via chaining/linked lists).

### HashSet vs HashMap

- **HashSet**: Stores unique elements. You only care *if* an element exists.
- **HashMap**: Stores Key-Value pairs. You want to look up a value *associated* with a key.

| Operation | Time Complexity (Average) | Time Complexity (Worst Case) |
| :--- | :--- | :--- |
| **Insert** | $O(1)$ | $O(N)$ (if many collisions) |
| **Delete** | $O(1)$ | $O(N)$ |
| **Search (Lookup)**| $O(1)$ | $O(N)$ |

## Code Snippets (Java)

```java
// --- HASHSET ---
import java.util.HashSet;
import java.util.Set;

Set<Integer> set = new HashSet<>();

// 1. Insert - O(1)
set.add(10);
set.add(20);
set.add(10); // Ignored, already exists

// 2. Search/Check Existence - O(1)
boolean hasTen = set.contains(10); // true
boolean hasFifty = set.contains(50); // false

// 3. Remove - O(1)
set.remove(20);

// --- HASHMAP ---
import java.util.HashMap;
import java.util.Map;

Map<String, Integer> map = new HashMap<>();

// 1. Insert - O(1)
map.put("Alice", 25);
map.put("Bob", 30);
map.put("Alice", 26); // Overwrites 25 with 26

// 2. Search/Lookup - O(1)
int aliceAge = map.get("Alice"); // 26
boolean hasBob = map.containsKey("Bob"); // true

// 3. Default Values (Very useful in counting!)
// If "Charlie" doesn't exist, return 0 instead of null
int charlieAge = map.getOrDefault("Charlie", 0); 

// 4. Frequency Counting Pattern
String s = "hello";
Map<Character, Integer> counts = new HashMap<>();
for (char c : s.toCharArray()) {
    counts.put(c, counts.getOrDefault(c, 0) + 1);
}
// counts will be: {'h':1, 'e':1, 'l':2, 'o':1}
```
