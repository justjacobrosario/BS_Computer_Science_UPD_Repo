---
problem type: enumeration problem
---


| Signal                                            | Structural pattern                              | Code    | Technique             | Note                              |
| ------------------------------------------------- | ----------------------------------------------- | ------- | --------------------- | --------------------------------- |
| "Generate all subsets/permutations/combinations"  | Combinatorial state space                       | **E.P** | Backtracking          | [[P. Recursion and Backtracking]] |
| "Find any path / does a path exist (explore all)" | Cyclic/connected                                | **E.R** | DFS                   | [[S.GR. Depth First Search]]      |
| "Visit level by level"                            | Cyclic/connected                                | **E.R** | BFS                   | [[S.GR. Breadth First Search]]    |
| "Order tasks given dependencies"                  | Cyclic/connected, ordering constraint           | **E.R** | Topological sort      | [[S.GR. Topological Sort]]        |
| "List all primes up to n"                         | Random/unstructured range                       | **E.N** | Sieve of Eratosthenes | [[E.N. Prime Count by Erasthotenes]]   |
| "Next greater/smaller element for every index"    | Contiguous, need to search backward efficiently | **E.A** | Monotonic stack       | [[S.SQ. Monotonic Stack]]         |
