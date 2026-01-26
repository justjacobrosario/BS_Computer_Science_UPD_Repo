'''
1. PREFIX SUMS USGE
'''
def prefix_sum(seq):
    res = [0]
    for item in seq:
        res.append(res[-1] + item)
    return res

def max_sum_of_subarrays(seq):
    res = []
    pre_sum = prefix_sum(seq)

    for i in range(len(seq)):a
        pre_sum_i = pre_sum[i]
        for j in range(i, len(seq)):
            res.append(pre_sum[j] - pre_sum_i)
            print(seq[i:j+1], pre_sum[j] - pre_sum_i)

    return max(res)

#print(max_sum_of_subarrays([1, 2, 3, 4, 5]))
 

'''
2. BINARY SEARCH
'''

def first_occurence_thanos(seq, x):
    l, r = 0, len(seq) - 1
    candidate = None

    while l <= r:
        m = (l + r) // 2
        if seq[m] == x:
            candidate = m
            r = m - 1
        else:
            if seq[m] > x:
                r = m - 1
            else:
                l = m + 1
    return candidate

#print(first_occurence_thanos([1, 1, 2, 2, 2, 3, 3, 5], 2))


def first_at_least_x(seq, x):
    l, r = 0, len(seq) - 1
    candidate = None

    while l <= r:
        m = (l + r) // 2
        if seq[m] >= x:
            candidate = m
            r = m -1
        else:
            l = m + 1

    return candidate

    #print(first_at_least_x([1, 3, 5, 7, 9], 6))








'''
3. MERGE SORT
'''

def merge_sort(seq):

    if len(seq) == 1:
        return seq

    else:
        m = len(seq) // 2
        l = seq[:m]
        r = seq[m:]

        l = merge_sort(l)
        r = merge_sort(r)

        return _merge(l, r)

def _merge(left, right):
    l, r = 0, 0
    res = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    for item in left[l:]:
        res.append(item)
    for item in right[r:]:
        res.append(item)

    return res

#print(merge_sort([3, 5, 7, 6, 9, 0, 1, 4, 8, 2]))


'''
4. MEMOIZATION
'''

def fib(n):
    cache = {}

    def helper(n):
        if n in cache:
            return cache[n]

        else:

            if n <= 1:
                cache[n] = n
                return n
            else:
                recursion = helper(n - 1) + helper(n - 2)
                cache[n] = recursion
                return recursion

    return helper(n)

#print(fib(6))


'''
5. MONOTONIC STACK
# counts subarrays with unique max val without enumerating subarrays
# previous greater (lists the max number from indx i leftwards from the seq)
# next greater (lists the max number from indx i rightwards from the seq)
'''

def movie_highlights(seq):
    n = len(seq)

    previous_greater = [-1]*n
    next_greater = [n]*n

    # previous greater processes

    stack = []

    for i in range(n):
        while stack != [] and seq[stack[-1]] < seq[i]:
            stack.pop()
        else:
            if stack != []:
                previous_greater[i] = stack[-1]
        stack.append(i)

    # next greater processes

    stack = []

    for i in range(n)[::-1]:
        while stack != [] and seq[stack[-1]] <= seq[i]:
            stack.pop()
        else:
            if stack != []:
                next_greater[i] = stack[-1]
        stack.append(i)

    # dict processes

    result = {}

    for i in range(n):
        L = i - previous_greater[i]
        R = next_greater[i] - i
        result[seq[i]] = result.get(seq[i], 0) + L*R

    return result


print(movie_highlights([1, 1, 7, 1, 7, 8, 2, 1]))

'''
6. SLIDING WINDOW
# accumulates last index
# acknowledge if operation is valid from frst to last
# else, if invalid, 1. remove first element and 2. incremenet first indx
# if the operation is now valid, acknowledge it

# number of valid arrays is (last - first + 1)
'''

def subarrays_atmost_p(seq, p):
    first = 0
    prod = 1
    count = 0

    for last in range(len(seq)):
        prod *= seq[last] # multiply next num

        # Negative Case ( if prod > p )
        while prod > p and first <= last:
            prod //= seq[first]
            first += 1

        # Positive Case ( if prod is <= p )
        count += (last - first) + 1

    return count


#print(subarrays_atmost_p((2, 1, 2), 3))




def count_subarrays_with_at_most_k_sum(seq, k):
    l = 0
    count = 0
    total = 0

    for r in range(len(seq)):
        total += seq[r]

        while total > k and l <= r:
            total -= seq[l]
            l += 1

        count += (r - l) + 1

    return count

    #print(count_subarrays_with_at_most_k_sum([1, 2, 3, 4], 1))


def len_of_longest_substring_with_atmost_k_characs(strng, k):
    l = 0
    listahan = {}
    distinct = 0
    best = 0

    for r in range(len(strng)):
        # update distinctiveness
        if strng[r] not in listahan or listahan[strng[r]] == 0:
            distinct += 1
            listahan[strng[r]] = 1
        else:
            listahan[strng[r]] += 1

        # negative case making it positive by pushing l
        while distinct > k and l <= r:
            listahan[strng[l]] -= 1
            if listahan[strng[l]] == 0:
                distinct -= 1
            l += 1

        best = max(best, (r-l + 1))
    return best


    # print(len_of_longest_substring_with_atmost_k_characs("eceba", 2))



def count_subarrays_with_atmost_k_prod(seq, p):
    l = 0
    prod = 1
    count = 0

    for r in range(len(seq)):
        prod *= seq[r]

        while prod > p and l <= r:
            prod //= seq[l]
            l += 1

        count += (r - l + 1)

    return count

    #print(count_subarrays_with_atmost_k_prod([2, 1, 2], 3))


'''
7. BFS (Bredth first Search)
# explore all neighbors of a node before moving deeper
'''


def shortest_path(adj, s, t):
    # return min num of edges needed to go from s to t. 
    # if t is unreachable return -1

    queue = [(s,0)]
    visited = {s}
    while queue: # loop until no more to visit in queue
        current = queue.pop(0)
        (curr_indx, curr_dist) = current


        if curr_indx == t: # positive case
            return curr_dist

        else: # negative case, queues next items until reach positive case else -1
            for neighbor in adj[curr_indx]:
                if neighbor not in visited:
                    queue.append((neighbor, curr_dist + 1))
                    visited.add(neighbor)
    return -1


print(shortest_path([[1, 2], [0, 3], [0, 3], [1, 2]], 0, 3))



def simple_flight_safety(islands, s, e, d):

    n = len(islands)
    queue = [(s, islands[s][1])]
    visited = {s:islands[s][1]}
    min_max_risk = float('inf') # infinity para hindi makuha sa min()

    while queue:
        curr_i, curr_max_risk = queue.pop(0) # dequeue first
        curr_pos, _ = islands[curr_i]

        if curr_i == e: # positive case : if reach nayung target, updte minmaxrisk
            min_max_risk = min(curr_max_risk, min_max_risk)

        # negative case : if di pa nag aarrive sa target
        for nxt_i in range(n):
            if nxt_i != curr_i: # exclude yung curr_i
                nxt_pos, nxt_risk = islands[nxt_i]

                if abs(nxt_pos - curr_pos) <= d: # if kaya puntahan
                    nxt_max_risk = max(nxt_risk, curr_max_risk)

                    # if di pa navisit OR navisit pero mas maliit yung risk
                    if (nxt_i not in visited) or (nxt_max_risk < visited[nxt_i]):
                        queue.append((nxt_i, nxt_max_risk))
                        visited[nxt_i] = nxt_max_risk


    return min_max_risk if min_max_risk != float('inf') else None

islands = [
    (0, 2),  # island 0, position 0, risk 2
    (3, 4),  # island 1, position 3, risk 4
    (5, 3),  # island 2, position 5, risk 3
    (7, 5)   # island 3, position 7, risk 5
]
s = 0
e = 3
d = 4

print(simple_flight_safety(islands, s, e, d))


def can_reach(islands, s, e, d, max_risk):
    queue = [s]
    visited = {s}

    while queue:
        curr_i = queue.pop(0)
        curr_pos, curr_risk  = islands[curr_i]

        if curr_i == e:
            return True

        else:

            for nxt_i in range(len(islands)):
                if nxt_i != curr_i:
                    nxt_pos, nxt_risk = islands[nxt_i]

                    if (nxt_i not in visited) and abs(nxt_pos - curr_pos) <= d and nxt_risk <= max_risk:
                        visited.add(nxt_i)
                        queue.append(nxt_i)

    return False



def flight_safety(islands, s, e, d):
    risks = sorted([r for _, r in islands])
    l, r = 0, len(risks) - 1
    candidate = None

    while l <= r:
        m = (l + r) // 2
        if can_reach(islands, s, e, d, risks[m]):
            candidate = risks[m]
            r = m - 1
        else:
            l = m + 1
    return candidate

islands = [
    (0, 2),  # island 0
    (3, 4),  # island 1
    (5, 3),  # island 2
    (7, 5)   # island 3
]

    #print(flight_safety(islands, 0, 3, 4))  # Output: 5
    #print(flight_safety(islands, 0, 3, 2))  # Output: None


'''
8. Pair Counting ( Binary Search 2.0 )
# has boundaries and two SORTED lists, but only loop one of it
# identify restriction
# for divisions in restriction, lower_bound must be CEILING DIVISION
# valid_pairs_count = higher_exc_bound_i - lower_inc_bound_i
# use binary searche"S" to get indx of higher_exc_bound_i and lower_inc_bound_i
'''

def sum_in_range(A, B, L, R):
    # return (a, b) pairs where L <= a + b <= R
    total_count = 0
    for a in A:
        # based on L <= a + b <= R
        lowest_b = L - a
        highest_b = R - a
        
        lower_inc_bound_i = first_ge_i(B, lowest_b)
        higher_exc_bound_i = first_gt_i(B, highest_b)

        valid_pairs_count = higher_exc_bound_i - lower_inc_bound_i
        total_count += valid_pairs_count
    return total_count


def first_ge_i(seq, target):
    l, r = 0, len(seq) - 1
    candidate = None

    while l <= r:
        m = (l + r) // 2
        if seq[m] >= target:
            candidate = m
            r = m - 1
        else:
            l = m + 1
    return candidate

def first_gt_i(seq, target):
    l, r = 0, len(seq) - 1
    candidate = None

    while l <= r:
        m = (l + r) // 2
        if seq[m] > target:
            candidate = m

        else:
            l = m + 1
    return candidate


def count_pairs_leq(A, B, X):
    # return the number of valid (a, b) pairs
    total_count = 0
    for a in A:
        # b <= X - a, only the highest has boundary
        highest_b = X - a
        higher_exc_bound_i = first_gt_i(B, highest_b)
        print(a, highest_b, higher_exc_bound_i)
        valid_pairs_count = higher_exc_bound_i
        total_count += valid_pairs_count
    return total_count


def first_gt_i(seq, target):
    l, r = 0, len(seq) - 1
    candidate = len(seq)

    while l <= r:
        m = (l + r) // 2
        if seq[m] > target:
            candidate = m
            r = m - 1
        else:
            l = m + 1
    return candidate


#print(count_pairs_leq([1, 2, 3], [2, 3, 4], 5))


def movie_count(movies, actors, b1, b2):
    total_count = 0
    movies = sorted([m*60 for m in movies])
    actors = sorted(actors)

    for m in movies:
        # b1 <= m*a <= b2

        highest_a = b2 // m
        lowest_a = b1 // m + 1 if b1%m > 0 else b1 // m

        highest_exc_i = first_gt_i(actors, highest_a)
        lowest_inc_i =  first_ge_i(actors, lowest_a)

        valid_projects_count = highest_exc_i - lowest_inc_i
        total_count += valid_projects_count

    return total_count

def first_gt_i(seq, target):
    l, r = 0, len(seq) - 1
    candidate = len(seq)

    while l <= r:
        m = (l+r) // 2
        if seq[m] > target:
            candidate = m
            r = m - 1

        else:
            l = m + 1

    return candidate

def first_ge_i(seq, target):
    l, r = 0, len(seq) - 1
    candidate = len(seq)

    while l <= r:
        m = (l+r) // 2
        if seq[m] >= target:
            candidate = m
            r = m - 1

        else:
            l = m + 1

    return candidate

print(movie_count(
    [90, 63, 120, 70, 150],
    (3, 1, 4, 9, 6),
    5_000,
    15_000
)
)



'''
9. Dynamic Programming
'''

'''def dp_on_sequence(values_for_option_0, values_for_option_1, ..., values_for_option_k):
    # keep best totals ending with each option
    state0 = state1 = ... = statek = 0
    for i in range(n):
        # compute next states using allowed previous states
        nxt0 = f0(state0, state1, ..., statek, values_for_option_0[i])
        nxt1 = f1(...)
        ...
        state0, state1, ..., statek = nxt0, nxt1, ..., nxtk
    return max(state0, state1, ..., statek)
'''



def max_happiness(a, b, c):
    '''
    return max possible hapiness while we cant choose friends twice a row
    
    pseudo:
    1. make a placeholder
        it contains possible vals if we choose either study, friends, chores

    2. for every attempt:
        update each val of placeholder to the max happiness of yesterday + the chosen action's hapiness
    
    3. once every attempt is exhausted
        return the max value of the latest updated placeholder
    '''

    # 0:study, 1:chore, 2:friends
    dp = [0, 0, 0]

    for i in range(len(a)):
        prev_dp = dp[:]

        # if picked study
        dp[0] = max(prev_dp[0], prev_dp[1], prev_dp[2]) + a[i]

        # if picked chore
        # no 2 consecutive friends
        dp[1] = max(prev_dp[0], prev_dp[1], prev_dp[2]) + b[i]

        # if picked friends
        dp[2] = max(prev_dp[0], prev_dp[1]) + c[i]

    return max(dp)


print(max_happiness([1, 1, 1, 11], [10, 10, 10, 11], [100, 100, 100, 11]))




'''print(movie_count(
    [90, 63, 120, 70, 150],
    (3, 1, 4, 9, 6),
    5_000,
    15_000
)
)'''



'''
10. Prefix Frequency
'''

def zero_sum_counts(seq):
    prefix = 0
    freq = {0 : 1}
    count = 0


    for index, item in enumerate(seq):
        prefix += item

        count += freq.get(prefix, 0)

        freq[prefix] = freq.get(prefix, 0) + 1

        yield count

def target_sum_counts(seq, target):
    prefix = 0
    freq = {0 : 1}
    count = 0


    for index, item in enumerate(seq):
        prefix += item

        count += freq.get(prefix - target, 0)

        freq[prefix] = freq.get(prefix, 0) + 1

        yield count
