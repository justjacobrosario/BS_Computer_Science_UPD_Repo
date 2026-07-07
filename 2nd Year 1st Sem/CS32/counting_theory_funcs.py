

def permutation(seq):
    if len(seq) <= 1:
        return [seq]
    else:
        
        #  recursive block
        result = []
        for i in range(len(seq)): # set a first element (current)
            current = seq[i]
            remaining = seq[:i]  + seq[i+1:]

            for perm in permutation(remaining): # recursively do that to the remaining things
                result.append([current] + perm)
        

        return result
    

def combinations_comprehension_2(tup):
    n = len(tup)
    return tuple((tup[x], tup[y], tup[z])
        for x in range(n)
        for y in range(x+1, n)
        for z in range(y+1, n)) # add another for loop to increase element number per combi


x = [1, 2, 3, 4, 5]

print(combinations_comprehension_2(x))

    
print(permutation(x))