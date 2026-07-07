

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
    

print(permutation([1, 2, 3]))