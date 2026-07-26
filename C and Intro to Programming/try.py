n = int(input())

arr = input()


A = arr.split(" ")
int_arr = []
for x in A:
    int_arr.append(int(x))

def f(n, A):
    if n <= 2:
        return 0
    else:
        res = 0
        for i in range(n-2):
            if A[i] < A[i+1] > A[i+2]:
                res += 1
        return res

print(f(n, int_arr))