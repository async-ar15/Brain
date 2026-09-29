# Intervals — Revision Sheet

---

## 01. Merge Intervals

**In My Words:** Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals.

**The Bridge:** If they aren't sorted, an interval at the end of the array might overlap with one at the beginning, forcing us to check everything against everything ($O(N^2)$). If sorted by start time, overlapping intervals MUST be adjacent!

**Optimized Intuition:** Sort by start time. Initialize `result` with the first interval. For each subsequent interval, if its start is $\le$ the end of the last interval in `result`, they overlap! Merge them by updating the end of the last interval to `max(last.end, current.end)`. Else, no overlap; just add the current interval to `result`.

**Template:** Merge Intervals

**Time:** $O(N \log N)$ | **Space:** $O(N)$ (for output)

**Code Solution:**
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;
        
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> res = new ArrayList<>();
        
        int[] current = intervals[0];
        res.add(current);
        
        for (int[] interval : intervals) {
            if (current[1] >= interval[0]) {
                current[1] = Math.max(current[1], interval[1]);
            } else {
                current = interval;
                res.add(current);
            }
        }
        
        return res.toArray(new int[res.size()][]);
    }
}
```

---

## 02. Insert Interval

**In My Words:** Given a set of non-overlapping, sorted intervals, insert a new interval into the intervals (merge if necessary).

**Constraint Whispers:**
- The given list is ALREADY sorted and non-overlapping.
- This means we can do it in $O(N)$ without the $O(N \log N)$ sorting step!

**The Bridge:** There are three distinct phases as we iterate through the existing intervals:
1. Intervals that end strictly BEFORE the new interval starts. (No overlap, just add them).
2. Intervals that OVERLAP with the new interval. (Merge them into the new interval by expanding its bounds).
3. Intervals that start strictly AFTER the new interval ends. (No overlap, just add them).

**Optimized Intuition:** Iterate through intervals. 
If `interval[1] < newInterval[0]`, add `interval` to result.
Else if `interval[0] > newInterval[1]`, add `newInterval` to result, then update `newInterval = interval` (this handles appending the rest cleanly).
Else (they overlap!), update `newInterval[0] = min(newInterval[0], interval[0])` and `newInterval[1] = max(newInterval[1], interval[1])`. Wait to add it until the overlap finishes.

**Time:** $O(N)$ | **Space:** $O(N)$ (for output)

**Code Solution:**
```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        
        for (int[] interval : intervals) {
            if (interval[1] < newInterval[0]) {
                res.add(interval);
            } else if (interval[0] > newInterval[1]) {
                res.add(newInterval);
                newInterval = interval; // The current interval becomes the new one to push later
            } else {
                newInterval[0] = Math.min(newInterval[0], interval[0]);
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            }
        }
        res.add(newInterval);
        
        return res.toArray(new int[res.size()][]);
    }
}
```

---

## 03. Non-overlapping Intervals

**In My Words:** Find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**The Bridge:** Removing the minimum number of intervals is mathematically identical to KEEPING the maximum number of non-overlapping intervals. How do we keep the most intervals? Always pick the one that ends the EARLIEST, because that leaves the maximum possible free time for future intervals!

**Optimized Intuition:** 
Sort the intervals by their END time. Keep track of the `end` of the last included interval. Iterate through. If the current interval's start is $<$ `end`, it overlaps, so we must remove it (`count++`). If it's $\ge$ `end`, we keep it and update `end = current interval's end`.

*(Note: You can also sort by start time, but if you do, when there's an overlap, you MUST greedily keep the one with the smaller end time to minimize future overlaps).*

**Time:** $O(N \log N)$ | **Space:** $O(1)$ auxiliary

**Code Solution:**
```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        // Sort by end time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        
        int count = 0;
        int end = intervals[0][1];
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < end) {
                // Overlap! We must remove one. We implicitly remove the one 
                // that ends later (which is the current one, since we sorted by end time)
                count++;
            } else {
                // No overlap. Update our end boundary.
                end = intervals[i][1];
            }
        }
        
        return count;
    }
}
```

---

## 04. Meeting Rooms II

**In My Words:** Given an array of meeting time intervals, return the minimum number of conference rooms required.

**The Bridge:** The number of rooms required is exactly the maximum number of overlapping meetings at any single point in time. If 3 meetings are happening at 2:00 PM, you need 3 rooms.

**Optimized Intuition:** Separate the start times and end times into two arrays and sort them both. This turns it into a timeline. Use two pointers, one for starts and one for ends. If `starts[s] < ends[e]`, a meeting started before the earliest ending meeting finished. We need a room! `count++`, `s++`. If `starts[s] >= ends[e]`, a meeting ended, freeing up a room. `count--`, `e++`. Track the `maxCount`.

**Template:** Line Sweep / Chronological

**Time:** $O(N \log N)$ | **Space:** $O(N)$

**Code Solution:**
```java
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int[] starts = new int[intervals.length];
        int[] ends = new int[intervals.length];
        
        for (int i = 0; i < intervals.length; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        
        Arrays.sort(starts);
        Arrays.sort(ends);
        
        int res = 0, count = 0;
        int s = 0, e = 0;
        
        while (s < intervals.length) {
            if (starts[s] < ends[e]) {
                count++;
                s++;
            } else {
                count--;
                e++;
            }
            res = Math.max(res, count);
        }
        
        return res;
    }
}
```
