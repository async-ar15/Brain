# Theory - System Design

These problems test your ability to compose multiple basic data structures together to achieve complex time complexities.

## Where is it commonly used?
1. **LRU Cache:** The most famous design question. Combines a HashMap and a Doubly Linked List.
2. **Insert Delete GetRandom O(1):** Combines a HashMap and an ArrayList.
3. **Data Stream as Disjoint Intervals:** Combines a TreeMap with Interval Merging logic.

## The "HashMap + [X]" Pattern

HashMaps provide $O(1)$ lookups, which is essential for almost every design problem. But HashMaps lack order, and they can't efficiently provide random elements or neighbors. You almost always pair a HashMap with a secondary structure.

### 1. HashMap + Doubly Linked List (LRU Cache)
- **HashMap:** `Map<Key, Node>` gives $O(1)$ access to any node.
- **Doubly Linked List:** Gives $O(1)$ ability to move a node to the "front" (most recently used) and $O(1)$ ability to delete the "tail" (least recently used).

### 2. HashMap + ArrayList (Insert/Delete/GetRandom)
- **ArrayList:** Gives $O(1)$ access to a random element via `list.get(rand.nextInt(size))`.
- **HashMap:** `Map<Value, Index_in_List>`. When you need to delete a value in $O(1)$, you look up its index in the map. Then, you swap that value with the LAST value in the ArrayList, and delete the last value (which is $O(1)$ for arrays!).

### 3. TreeMap (Binary Search Tree)
When you need to constantly find the "closest" value to a given key, or need to maintain sorted order of a stream of data.
- `treeMap.lowerKey(K)`: Greatest key strictly less than K. ($O(\log N)$)
- `treeMap.floorKey(K)`: Greatest key less than or equal to K. ($O(\log N)$)
- `treeMap.ceilingKey(K)`: Least key greater than or equal to K. ($O(\log N)$)

# Your interview cheat code

```text
1. Are you designing a data structure with multiple constraints?
                  ↓
2. Identify the bottlenecks. Does get() need to be O(1)? Does add() need to be O(1)?
                  ↓
3. Pair a HashMap with a secondary structure (DLL, ArrayList, PriorityQueue) to cover the weaknesses.
```
