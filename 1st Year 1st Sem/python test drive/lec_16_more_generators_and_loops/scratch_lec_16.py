"""
(1) while loops
 - performs the action while condition is still True
 - the loop only stops if:
   - the condition is False
   - it arrives to a break keyword (which ends the loop)

e.g. 


def count_down_from(n):
    while n != 0: #only stops if n becomes 0
        yield n
        n -= 1
    yield "Blastoff!"


or 

def count_down_from(n):
    while True:
        if n == 0: # only breaks if n becomes 0
            break # it's like a base case
        else:
            yield n
            n -= 1
    yield "Blastoff!"

print([*count_down_from(10)]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, "Blastoff"]


"""

def collatz_seq(n):
    yield n
    n = n
    while n > 1:
        if n % 2 == 0:
            n = n//2
            yield n
        else:
            n = 3*n + 1
            yield n

#print([*collatz_seq(7)])


