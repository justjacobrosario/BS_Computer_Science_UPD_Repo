---
problem type: enumeration problem
data structure: array
---


```python

def k_combination(arr, k):
	res = []

	def helper(curr_comb, start):
		if len(curr_comb) == k:
			res.append(curr_comb[:])

		else:

			for i in range(start, len(arr)):
				curr_item = arr[i]

				curr_comb.append(curr_item)

				helper(curr_comb, start + 1)

				curr_comb.pop()

	helper([], 0)

	return res



arr = [1, 2, 3]

print(k_combination(arr, 2))

'''
[[1, 2], [1, 3], [2, 2], [2, 3], [3, 2], [3, 3]]
'''
```