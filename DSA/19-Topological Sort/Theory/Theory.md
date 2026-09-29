# Theory - Topological Sort (Kahn's Algorithm)

There are two ways to do Topological Sort (DFS and Kahn's BFS Algorithm). We heavily recommend Kahn's BFS Algorithm because it naturally detects cycles and is much more intuitive to write without complex visited arrays.

## Where is it commonly used?
1. **Scheduling:** Course Schedule, Task scheduling with dependencies.
2. **Build Systems:** Compiling files in the correct order (e.g., Makefiles, NPM dependencies).
3. **Alien Dictionary:** Determining the alphabetical order of characters in a foreign language.

## Strong signals to look for
- "Course prerequisites"
- "Task A must be completed before Task B"
- "Given a list of dependencies..."
- The problem asks for a valid ordering or asks if it's possible to complete all tasks (cycle detection).

## Kahn's Algorithm (BFS)

The logic is beautifully simple:
1. Find all courses that have NO prerequisites (`in-degree == 0`) and put them in a Queue.
2. While the Queue is not empty:
   - Pop a course. This course is now "completed". Add it to your result list.
   - Look at all the advanced courses this course unlocks (its neighbors).
   - Since you just completed a prerequisite for them, decrement their `in-degree` by 1.
   - If any neighbor's `in-degree` becomes 0, it means ALL its prerequisites are now completed! Add it to the Queue.
3. Once the Queue is empty, check the result list. If its size == total number of courses, you successfully completed everything! If it's less, there was a cycle (a deadlock) and you couldn't finish.

### Template: Kahn's Algorithm

```java
public int[] topoSort(int numCourses, int[][] prerequisites) {
    // 1. Build Adjacency List and In-Degree array
    List<List<Integer>> adjList = new ArrayList<>();
    for (int i = 0; i < numCourses; i++) adjList.add(new ArrayList<>());
    
    int[] inDegree = new int[numCourses];
    
    for (int[] pre : prerequisites) {
        int course = pre[0];
        int prereq = pre[1];
        
        // Edge is: prereq -> course
        adjList.get(prereq).add(course);
        inDegree[course]++; // course requires prereq
    }
    
    // 2. Initialize Queue with all In-Degree 0 nodes
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) {
            queue.offer(i);
        }
    }
    
    // 3. Process BFS
    int[] order = new int[numCourses];
    int index = 0;
    
    while (!queue.isEmpty()) {
        int curr = queue.poll();
        order[index++] = curr; // Record completion
        
        // Unlock neighbors
        for (int neighbor : adjList.get(curr)) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                queue.offer(neighbor);
            }
        }
    }
    
    // 4. Check for cycle
    if (index == numCourses) {
        return order; // Success
    } else {
        return new int[0]; // Cycle detected, impossible
    }
}
```

# Your interview cheat code

```text
1. Are there dependencies / prerequisites (A before B)?
                  ↓
2. USE KAHN'S ALGORITHM (BFS)
   a. Build Adjacency List and In-Degree Array
   b. Add In-Degree 0 to Queue
   c. Pop -> decrement neighbors' in-degree -> Add to Queue if 0.
```
