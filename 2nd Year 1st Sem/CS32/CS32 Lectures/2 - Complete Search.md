## 2.1. Worker-Job Problem
: Let there be n workers and n jobs, in which every worker have specific salary demand for each job.

: Let there be a 2-d matrix cost, where `cost[i][j]` refers to the demanded profit of worker i at  job j.

: Goal : Find the list where the ith element is worker i,  and its value is the jth job, such that form a permutation of possible job assignments, it returns the list with the minimum salary demands.

e.g.


|          | Task 0 | Task 1 | task 2 |
| -------- | ------ | ------ | ------ |
| Worker 0 | **4**  | 6      | 2      |
| Worker 1 | 8      | **5**  | 7      |
| Worker 2 | 7      | 9      | **6**  |
in this setup, `[0, 1, 2]` is the most optimized setup

