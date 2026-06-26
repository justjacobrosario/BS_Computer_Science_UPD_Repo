: Recall that to make an algorithm, we first use brute force to understand the steps of the problem.

: But aside from deeply understanding it, we also use brute force to utilize **complete search** (which will completely enumerate all possible outcomes).

: Complete search utilizes the high speed operation of computers.

## 2.1. Worker-Job Problem

### 2.1.1. Intro
: Let there be n workers and n jobs, in which every worker have specific salary demand for each job.

: Let there be a 2-d matrix cost, where `cost[i][j]` refers to the demanded profit of worker i at  job j.

: Goal : Find the list where the ith element is job j, assigned to worker i, such that has the minimum salary demands.

|          | Task 0 | Task 1 | task 2 |
| -------- | ------ | ------ | ------ |
| Worker 0 | **4**  | 6      | 2      |
| Worker 1 | 8      | 7      | **5**  |
| Worker 2 | 7      | **6**  | 9      |
in this setup, `[0, 2, 1]` is the most optimized setup

### 2.1.2. Conceptualization

: If we are to use brute force, we can list all possible permutations of lists in which the values represents the jth job indexed to the ith worker. then pick the list with the minimum sum of values (minimum combined salary demand)


### 2.1.3. Implementation

: we can first define a function for getting a permutation of n objects and slots.

: then define a function iterating every permuted list and mapping it to its combined cost, then get the minimum combined cost, then return the list/s mapped to that minimum combined cost

### A. My Sample Implementation

```python
def perm_generator(seq):
    if not seq:
        yield ()
    else:
        for idx in range(len(seq)):
            start = seq[idx]
            for next_objs in perm_generator(seq[:idx]+seq[idx+1:]):
                yield (start, *next_objs)

def permutations(seq):
    instances = []
    for instance in perm_generator(seq):
        instances.append(instance)

    return instances


def get_optimal_worker_job_setup(matrix):
    workers = len(matrix)
    cost_setups = {}

    possible_setups = permutations([*range(workers)])
    for setup in possible_setups:
        combined_cost = sum([matrix[worker][job] for worker, job in enumerate(setup)])

        if combined_cost in cost_setups:
            cost_setups[combined_cost].append(setup)
        else:
            cost_setups[combined_cost] = [setup]

    min_combined_cost = min(cost_setups.keys())

    if len(cost_setups[min_combined_cost]) == 1:
        return cost_setups[min_combined_cost][0]
    else:
        return cost_setups[min_combined_cost]


sample = [
    [4, 10, 1, 11],
    [10, 8, 15, 20],
    [10, 12, 10, 9],
    [8, 10, 3, 32]
    ]

print(get_optimal_worker_job_setup(sample))


```

#### B. Discussed Implementation
```c
def permutations(seq):
    if not seq:
        yield ()
    else:
        for i in range(len(seq)):
            # seq[i] will be the first
            for p in permutations([*seq[:i], *seq[i+1:]]):
                yield (seq[i], *p)


def best_assignment(cost):
    n = len(cost)

    def total_cost(p):
        # worker i is assigned task p[i]
        return sum(cost[i][p[i]] for i in range(n))

    return min(total_cost(p) for p in permutations(range(n)))


def main():
    for cas in range(int(input())):
        print(best_assignment([[*map(int, input().split())] for _ in range(int(input()))]))


if __name__ == "__main__":
    main()



```
