# Theory - Intervals

Interval problems are a highly specialized subset of array problems. They often deal with scheduling (meetings, flights) or merging overlapping geometric ranges.

## Where is it commonly used?
1. **Merging:** Given a list of intervals, merge all overlapping ones.
2. **Inserting:** Given a list of non-overlapping intervals, insert a new one and merge if necessary.
3. **Scheduling / Meeting Rooms:** Find if a person can attend all meetings, or find the minimum number of meeting rooms required.

## The Merge Pattern

Once intervals are sorted by start time, you maintain a "current active interval". You compare the next interval to this active one.

If they overlap, you **MERGE** them. How? The new start time is already smaller (due to sorting). The new end time is simply the `max(currentEnd, nextEnd)`.
If they do NOT overlap, the "current active interval" is finished. You add it to your result, and the next interval becomes the new active interval.

### Template: Merging Intervals

```java
public int[][] mergeTemplate(int[][] intervals) {
    if (intervals.length <= 1) return intervals;
    
    // 1. Sort by start time
    Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
    
    List<int[]> result = new ArrayList<>();
    
    // 2. Initialize the first interval as the "active" interval
    int[] currentInterval = intervals[0];
    result.add(currentInterval); // Add reference to result, we will modify it in place!
    
    for (int[] interval : intervals) {
        int currentEnd = currentInterval[1];
        int nextStart = interval[0];
        int nextEnd = interval[1];
        
        if (currentEnd >= nextStart) { 
            // OVERLAP: Merge by extending the end time of the active interval
            currentInterval[1] = Math.max(currentEnd, nextEnd);
        } else { 
            // NO OVERLAP: Update active interval and add to result
            currentInterval = interval;
            result.add(currentInterval);
        }
    }
    
    return result.toArray(new int[result.size()][]);
}
```

## The "Line Sweep" or "Chronological" Pattern (Meeting Rooms II)

When the problem asks for the maximum number of overlapping intervals at any given point (e.g., how many meeting rooms do we need?), a brilliant trick is to separate the `start` times and `end` times into two different sorted arrays.

You iterate through time. If you see a start time, a meeting started (rooms required ++). If you see an end time, a meeting ended (rooms required --).

```java
public int meetingRooms(int[][] intervals) {
    int[] starts = new int[intervals.length];
    int[] ends = new int[intervals.length];
    
    for (int i = 0; i < intervals.length; i++) {
        starts[i] = intervals[i][0];
        ends[i] = intervals[i][1];
    }
    
    Arrays.sort(starts);
    Arrays.sort(ends);
    
    int count = 0, maxRooms = 0;
    int s = 0, e = 0;
    
    while (s < intervals.length) {
        if (starts[s] < ends[e]) {
            // A meeting started before the earliest ending meeting finished
            count++;
            s++;
        } else {
            // A meeting ended
            count--;
            e++;
        }
        maxRooms = Math.max(maxRooms, count);
    }
    return maxRooms;
}
```

# Your interview cheat code

```text
1. Does the problem involve ranges [start, end]?
                  ↓
2. ALWAYS SORT BY START TIME FIRST.
                  ↓
3. Does it ask to merge? (Use Merge Pattern)
4. Does it ask for max simultaneous overlap? (Use Line Sweep / Chronological Pattern)
```
