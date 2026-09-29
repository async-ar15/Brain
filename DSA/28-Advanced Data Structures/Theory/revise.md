# System Design — Revision Sheet

---

## 01. LRU Cache

**In My Words:** Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. `get` and `put` must be $O(1)$ time complexity. When the cache reaches its capacity, it should invalidate and remove the least recently used key before inserting a new item.

**The Bridge:** $O(1)$ access means we need a HashMap. But HashMaps have no concept of "recent". We need an ordered structure where we can move elements to the "front" in $O(1)$ time. An Array takes $O(N)$ to shift elements. A Doubly Linked List can remove and insert nodes in $O(1)$ time!

**Optimized Intuition:** 
1. Build a `Node` class with `key, value, prev, next`. (We store `key` inside the node so we can remove it from the HashMap when evicting).
2. Create `HashMap<Integer, Node> cache`.
3. Create Dummy `head` and `tail` nodes, connected to each other.
4. `put(k, v)`: If exists, remove old node. Create new node. Add to map. Insert right after `head` (most recent). If `cache.size() > capacity`, remove node right before `tail` (LRU) and remove its key from map.
5. `get(k)`: If not in map, return -1. Get node. Remove it from its current position. Insert it right after `head`. Return value.

**Time:** $O(1)$ for all | **Space:** $O(C)$ where C is capacity

**Code Solution:**
```java
class LRUCache {
    class Node {
        int key, val;
        Node prev, next;
        Node(int k, int v) { key = k; val = v; }
    }
    
    private int capacity;
    private Map<Integer, Node> cache;
    private Node head, tail; // Dummy nodes

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        Node node = cache.get(key);
        remove(node);
        insert(node); // Move to front
        return node.val;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            remove(cache.get(key));
        }
        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insert(newNode);
        
        if (cache.size() > capacity) {
            Node lru = tail.prev;
            remove(lru);
            cache.remove(lru.key);
        }
    }
    
    // Helper to remove node from DLL
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    // Helper to insert node right after head
    private void insert(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
}
```

---

## 02. Insert Delete GetRandom O(1)

**In My Words:** Design a class that supports `insert`, `remove`, and `getRandom` operations in $O(1)$ average time. `getRandom` must return a random element with equal probability.

**The Bridge:** $O(1)$ `getRandom` requires a contiguous array/list where we can pick a random index. $O(1)$ `insert` and `remove` usually requires a HashSet/HashMap. How do we remove from an ArrayList in $O(1)$? We swap the element we want to delete with the LAST element in the list, and then remove the last element! We use a HashMap to track the *index* of each value in the ArrayList so we know what to swap.

**Optimized Intuition:**
`List<Integer> list` and `Map<Integer, Integer> map` (value -> index).
- `insert(val)`: If exists, return false. Add to map `(val, list.size())`. Add to list.
- `remove(val)`: If not exists, return false. Get `index` of `val` from map. Get `lastVal` from end of list. Put `lastVal` into `list` at `index`. Update map for `lastVal` to `index`. Remove last element from list. Remove `val` from map.
- `getRandom()`: `list.get(random.nextInt(list.size()))`.

**Time:** $O(1)$ average | **Space:** $O(N)$

**Code Solution:**
```java
class RandomizedSet {
    private List<Integer> list;
    private Map<Integer, Integer> map;
    private java.util.Random rand;

    public RandomizedSet() {
        list = new ArrayList<>();
        map = new HashMap<>();
        rand = new java.util.Random();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) return false;
        
        map.put(val, list.size());
        list.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) return false;
        
        int index = map.get(val);
        int lastVal = list.get(list.size() - 1);
        
        // Swap the value to delete with the last value
        list.set(index, lastVal);
        map.put(lastVal, index);
        
        // Remove the last value
        list.remove(list.size() - 1);
        map.remove(val);
        
        return true;
    }
    
    public int getRandom() {
        return list.get(rand.nextInt(list.size()));
    }
}
```

---

## 03. Implement Trie (Prefix Tree)

*(Covered entirely in Day 17 - Tries)*

---

## 04. Design Twitter

**In My Words:** Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the 10 most recent tweets in the user's news feed.

**Constraint Whispers:**
- Finding the 10 most recent tweets among potentially thousands of followed users is exactly the "Top K Elements" problem. We need a Priority Queue (Max-Heap)!

**The Bridge:** 
- A user needs a Set of people they follow. (Every user should implicitly follow themselves).
- A user needs a List of their own tweets. (We can store tweets as `[time, tweetId]`).
- When generating the feed, we take the lists of tweets from ALL people the user follows, and merge them using a Max-Heap based on `time`. This is exactly "Merge K Sorted Lists".

**Optimized Intuition:**
Global `timestamp` counter. Map `followerMap` (userId -> Set of followeeIds). Map `tweetMap` (userId -> List of Tweet objects).
`postTweet`: Add to `tweetMap` with `timestamp++`.
`getNewsFeed`: Create Max-Heap of tweets. Add ALL tweets from ALL followed users into the heap. Poll 10 times. (Optimization: Only add the most recent 10 tweets from each user to the heap).
`follow`/`unfollow`: Update `followerMap`.

**Time:** $O(F \cdot T \log(F \cdot T))$ where F is followees, T is max tweets per user | **Space:** $O(U + T_{total})$

**Code Solution:**
```java
class Twitter {
    private int timestamp = 0;
    private Map<Integer, Set<Integer>> followers;
    private Map<Integer, List<int[]>> tweets; // [time, tweetId]

    public Twitter() {
        followers = new HashMap<>();
        tweets = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        tweets.putIfAbsent(userId, new ArrayList<>());
        tweets.get(userId).add(new int[]{timestamp++, tweetId});
    }
    
    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        
        // Add own tweets
        if (tweets.containsKey(userId)) {
            for (int[] tweet : tweets.get(userId)) maxHeap.offer(tweet);
        }
        
        // Add followees' tweets
        if (followers.containsKey(userId)) {
            for (int followeeId : followers.get(userId)) {
                if (tweets.containsKey(followeeId)) {
                    for (int[] tweet : tweets.get(followeeId)) maxHeap.offer(tweet);
                }
            }
        }
        
        List<Integer> feed = new ArrayList<>();
        while (!maxHeap.isEmpty() && feed.size() < 10) {
            feed.add(maxHeap.poll()[1]);
        }
        return feed;
    }
    
    public void follow(int followerId, int followeeId) {
        followers.putIfAbsent(followerId, new HashSet<>());
        followers.get(followerId).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if (followers.containsKey(followerId)) {
            followers.get(followerId).remove(followeeId);
        }
    }
}
```
