---
problem type: optimization problem
---


| Signal                                          | Structural pattern                | Code    | Technique               | Note                                      |
| ----------------------------------------------- | --------------------------------- | ------- | ----------------------- | ----------------------------------------- |
| "Maximum subarray sum"                          | Random array, no sortedness       | **O.A** | Running-best (Kadane's) | [[O.A. Kadane's Algorithm]]               |
| "Max/min sum of a fixed-size window"            | Contiguous, fixed length          | **O.A** | Fixed sliding window    | [[O.A. Fixed Sliding Window]]             |
| "Shortest subarray with sum >= target"          | Contiguous, variable length       | **O.A** | Variable sliding window | [[O.A. Sliding Window of Varying Length]] |
| "Max/min in every sliding window"               | Contiguous, need running extremum | **O.A** | Monotonic deque         | [[S.SQ. Monotonic Deque]]                 |
| "Shortest path, unweighted graph"               | Cyclic/connected, equal edge cost | **O.R** | BFS                     | [[S.GR. Breadth First Search]]            |
| "Minimum coins / minimum edits / min-cost path" | Overlapping subproblems           | **O.P** | Dynamic programming     | [[P. Dynamic Programming]]                |
| "Locally optimal choice never gets revisited"   | Sorted or priority-ordered input  | **O.P** | Greedy                  | [[P. Greedy Algorithms]]                  |
