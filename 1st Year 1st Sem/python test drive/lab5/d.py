"""
delightful if 
1.each 0123456789 appears <= d times in its decimal rep
2.number is divisible by S

Goal: How many delightful positive integers are there?
return answer%(10**8)


"""

def delightful_number_count(d, S):
    subsqncs = list(subsequence([*range(10)]*d))
    count = 0

    for num in subsqncs:
        if int(num) % S == 0:
            count += 1

    return count



def subsequence(seq):
    res = [""]

    for item in seq:
        new = []
        for natapos in res:
            new.append(natapos + str(item))
            new.append((natapos + str(item))[::-1])
        res += new
    return set(res) - {""}
#print(subsequence([*range(3)]*2))

print(delightful_number_count(1, 7))