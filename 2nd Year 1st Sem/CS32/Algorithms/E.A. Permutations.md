---
problem type: enumeration problem
data structure: array
---


```python

def permutations(arr):
	if len(arr) == 0:
		return [[]]

	else:
		res = []

		for i in range(len(arr)):
			curr = arr[i]
			rest = arr[:i] + arr[i+1:]

			for perm in permutations(rest):
				res.append([curr] + perm)


		return res
		
arr = [1, 2, 3]

print(permutations(arr))

'''
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''


```


```python



def k_permutations(arr, k):
	res = []


	def helper(curr_perm, rem_items):
		if len(curr_perm) == k:
			res.append(curr_perm[:])
			return

		else:

			for i in range(len(rem_items)):
				curr_item = rem_items[i]

				curr_perm.append(curr_item)

				new_remaining = rem_items[:i] + rem_items[i+1:]

				helper(curr_perm, new_remaining)

				curr_perm.pop()

	helper([], arr)
	return res






arr = [1, 2, 3]

print(k_permutations(arr, 2))

'''
[[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
'''

```