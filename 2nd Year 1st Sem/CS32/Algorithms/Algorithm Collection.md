: One axis, two-part code: what KIND of answer does the problem want, and what structure does it operate on?
: Code format is [Problem Type].[Data Structure] — e.g. C.A = Counting problem, on an Array. Read down to the matching problem type section, then match the structural signal inside it.
: Pipeline behind this file: Problem Type -> Structural Pattern in the input -> Data Structure -> Paradigm. The code captures the first and third of these; the "structural pattern" column captures the second.

---

# New heading letter system

**First letter — problem type** (what kind of answer is wanted):

| Letter | Problem type | The question being asked |
|---|---|---|
| **D** | Decision | "Is it possible / does X exist?" |
| **C** | Counting | "How many ways / how many X?" |
| **O** | Optimization | "What's the min/max/best?" |
| **E** | Enumeration / Search | "List all X" or "find any one X / any one path." |
| **F** | Function / Construction | "Compute this value" or "build/transform into this exact object." |

**Second letter — data structure** (what it operates on):

| Letter | Structure |
|---|---|
| **A** | Array |
| **L** | Linked List |
| **G** | Grid |
| **T** | Tree |
| **R** | Graph (Relations) |
| **S** | Stack / Queue |
| **H** | Hash Table |
| **N** | Numeric / scalar (no structure — number theory) |
| **P** | Paradigm-general (structure-agnostic technique: DP, Greedy, Backtracking used in the abstract, before being pinned to one structure) |

So a note's full code reads left to right the same way you'd say it out loud: "Counting problem, on an Array" = **C.A**. New notes going forward get named with this code, e.g. `D.A Two Pointers Existence Check`, `O.R Dijkstra's Algorithm`. Existing files keep their current names — the tables below still link to your current filenames; only rename a file if you're touching it anyway.

---

# I. Decision (D.) — does it exist / is it possible

[[- DECISION PROBLEMS]]

# II. Counting (C.) — how many ways / how many X

[[- COUNTING PROBLEMS]]

# III. Optimization (O.) — min / max / best

[[- OPTIMIZATION PROBLEMS]]

# IV. Enumeration / Search (E.) — list all / find any / explore

[[- ENUMERATION PROBLEMS]]

# V. Function / Construction (F.) — compute or build directly

[[- FUNCTION PROBLEMS]]

# Chameleon algorithms — same technique, different code by framing

A handful of techniques shift BOTH letters depending on how they're used. Rule stays the same as before: **one primary code where the technique lives (its unmodified, stand-alone form), every other use gets a row here instead of a duplicate note.**

| Technique | Primary code | Also appears as | What changes |
|---|---|---|---|
| Binary Search | **D.A** (does x exist in array) | **O.N** (binary search the answer) | Same halving logic, but instead of searching an array index you search a numeric answer range, checking feasibility at each midpoint |
| BFS | **E.R** (explore level by level) | **O.R** (shortest path), **D.R** (reachability) | Unweighted BFS naturally returns shortest path once you track distance; stopping at first hit turns it into a decision |
| DFS | **E.R** (explore all paths) | **D.R** (reachability), paired with backtracking for **O.P** | Plain DFS just visits; an early return on "found it" makes it D., a running-best makes it part of an O. search |
| Prefix Sum | **F.A** (compute a range sum) | **D.A** (does a subarray sum to >= k), **C.A** (count subarrays summing to k) | The prefix array itself is a pure function; what you DO with it — threshold check vs. hash-map count — is what shifts the first letter |
| Dynamic Programming | **O.P** (min/max) | **C.P** (counting DP), **D.A/D.G** (boolean/reachability DP) | The recurrence structure is identical; only what you store at each state changes — a number to optimize, a number to sum, or a boolean |
| Union Find | **D.R** (same group?) | **C.R** (count connected components), inside **E.R** (Kruskal's MST construction) | The structure always answers "same set?" — counting components and building an MST both sit on top of that same primitive |
| Greedy | **O.P** (best choice) | **E.P** (construction problems using greedy for a valid, not optimal, output) | Only counts as Optimization if the local choice is provably globally safe; otherwise it's a fast Construction heuristic |

**Rule of thumb**: if a technique needs a third row here, it's a sign the note itself is a *mechanism* (works on whatever you point it at) rather than a technique bound to one problem type — Prefix Sum, BFS, and DFS are the clearest examples. That's fine; the table is doing the categorization work a single fixed code can't.
