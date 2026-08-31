---
problem type: function problem
---



| Signal                                     | Structural pattern                   | Code    | Technique                  | Note                                       |
| ------------------------------------------ | ------------------------------------ | ------- | -------------------------- | ------------------------------------------ |
| "Largest number dividing both a and b"     | —                                    | **F.N** | Euclidean algorithm        | [[F.N. Greatest Common Divisor (GCD)]]     |
| "a^b mod m, huge b"                        | —                                    | **F.N** | Modular exponentiation     | [[M. Modular Exponentiation]]              |
| "Many range-sum queries on the same array" | Sorted/fixed input, repeated queries | **F.A** | Prefix sum                 | [[F.A. Prefix Sum]]                        |
| "Many range-update queries"                | Repeated updates, not queries        | **F.A** | Difference array           | [[S.A. Difference Array]]                  |
| "Many range-sum queries on a grid"         | Sorted/fixed 2D input                | **F.G** | Prefix sum grid            | [[F.G. Prefix Sum Grid]]                   |
| "Reverse the list / a sublist"             | Linked, no index access              | **F.L** | Iterative pointer reversal | [[F.L. Reverse Linked Lists]]              |
| "Remove nodes with value X"                | Linked, no index access              | **F.L** | Dummy head + skip          | [[F.L. Remove Nodes based on value]]       |
| "Remove duplicate values"                  | Linked, no index access              | **F.L** | Seen-set + skip            | [[F.L. Remove Duplicates in Linked Lists]] |
| "Merge two sorted lists"                   | Linked, already sorted               | **F.L** | Dummy head + two pointers  | [[S.L. Merge Two Sorted Lists]]            |
| "Produce a fully sorted array"             | Random/unstructured                  | **F.A** | Merge sort / Quick sort    | [[SO. Merge Sort]]                         |
| "Sort values in a small known range"       | Bounded value range                  | **F.A** | Counting sort              | [[SO. Counting Sort]]                      |
| "Matching brackets/parentheses"            | Contiguous, must-match-in-order      | **F.S** | Stack push/pop             | [[S.SQ. Valid Parentheses]]                |
