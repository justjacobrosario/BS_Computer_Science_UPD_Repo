

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


x = [1, 2, 3]

#print(combinations_comprehension_2(x))


'''
subsequences

if len(seq) <= 1, then return seq //edge case, no need to recurse//

else, //iterate every subsequence via recursion//
result = [] //subseqs container//

//recursive part : include or not include an element to the subseq//

def helper(idx, subseq) // idx : index of curr element (to include or not to the subseq)

    helper(idx + 1, subseq) // recursion 1 : not include curr element

    helper(idx + 1, subseq + [seq[idx]]) // recursion 2 : include curr element
    subseq.pop() // 


'''

def subsequences(seq):
    if len(seq) <= 1:
        return [seq]
    
    else:
        result = []

        def helper(idx, subseq):
            # base case: 
            if len(seq) == idx:
                result.append(subseq.copy())
                return

            # recursion 1: ignore current element
            helper(idx + 1, subseq)

            # recursion 2: add the current element, recurse, and pop it again to backtrack
            subseq.append(seq[idx])
            helper(idx+1, subseq)
            subseq.pop()

        helper(0, [])

        return result
    
print(subsequences(x))

