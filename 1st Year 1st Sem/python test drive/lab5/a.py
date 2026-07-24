"""
n minutes
1 <= s <= e <= n

how many pairs (s, e) are there
where it is equal to v

"""

def movie_highlights(excite_values):
    dic = {}

    for i in range(len(excite_values)):
        for j in range(i, len(excite_values)):
            if i == j:
                if excite_values[i] not in dic:
                    dic[excite_values[i]] = 1
                else:
                    dic[excite_values[i]] += 1
            else:
                if sorted(excite_values[i:j+1], reverse = True)[0] not in dic:
                    dic[sorted(excite_values[i:j+1], reverse = True)[0]] = 1
                else:
                    dic[sorted(excite_values[i:j+1], reverse = True)[0]] += 1
    return dic


def movie_highlights(arr):
    n = len(arr)

    prev_greater = [-1] * n
    next_greater = [n] * n
    stack = []

    # previous greater (strictly greater to the left)
    for i in range(n):
        while stack != [] and arr[stack[-1]] < arr[i]:
            stack.pop()
        else:
            if stack != []:
                prev_greater[i] = stack[-1]
        stack.append(i)

    stack = []
    # next greater or equal (first index to the right which is > or ==)
    for i in range(n)[::-1]:
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        else:
            if stack != []:
                next_greater[i] = stack[-1]
        stack.append(i)

    result = {}
    for i in range(n):
        L = i - prev_greater[i]   # choices for start index
        R = next_greater[i] - i   # choices for end index
        if arr[i] in result:
            result[arr[i]] += (L * R)
        else:
            result[arr[i]] = L * R

    return result






print(movie_highlights([1, 1, 7, 1, 7, 8, 2, 1]))


