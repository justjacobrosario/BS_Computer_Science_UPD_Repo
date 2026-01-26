# === [ fib with memoization ] === 

def fib(n): # wrapper
    cache = {}

    def fib_jr(n): # recursion func
        if n in cache: # if input in cache, return output
            return cache[n]
        else:
            # if not in cache, do recursion, add output to cache and return it
            if n == 0: # base cases
                cache[n] = 0
                return 0
            elif n == 1:
                cache[n] = 1
                return 1
            else: # recursive case
                recursion = fib_jr(n-1) + fib_jr(n-2)
                cache[n] = recursion
                return recursion
    return fib_jr(n)

#print(fib(6))

# === [ Climb Ways ] ===
# number of ways to climb in n steps = fibonnaci

def climb_ways(n):
    cache = {}

    def helper(n):
        if n in cache:
            return cache[n]

        else:

            if n <= 1:
                cache[n] = n
                return n

            else:
                recursive = helper(n-1) + helper(n-2)
                cache[n] = recursive
                return recursive
    return helper(n)

#print(climb_ways(6))


# === [ Downright Paths ] ===
''' in a grid from top leftmost cell, how many ways to go to down rightmost cell by only going down or right
'''

def downright_paths(rows, cols): # wrapper
    cache = {}

    def helper(r, c): # recursion func
        if (r, c) in cache: # return output if pair is in cache
            return cache[(r, c)]

        else:
            if r == rows - 1 or c == cols - 1: # base case
                cache[(r, c)] = 1
                return 1

            else:
                # two recursions, since may two choices
                kumanan = helper(r, c+1)
                bumaba = helper(r+1, c)

                recursions = kumanan + bumaba
                cache[(r, c)] = recursions
                return recursions

    return helper(0, 0)

#print(downright_paths(2, 2))

# === [ Change ] ===
''' in a list of coins (1 peso, 5 pesos, etc) how many ways can we use those to 
add up to a price
'''
def change_coins(coins, price):
    cache = {}

    def helper(indx, price):

        if (indx, price) in cache:
            return cache[(indx, price)]

        else:
            if indx >= len(coins) or price < 0:
                cache[(indx, price)] = 0
                return 0

            elif price == 0:
                cache[(indx, price)] = 1
                return 1

            else:

                used = helper(indx, price - coins[indx])
                skip = helper(indx + 1, price)

                recursions = used + skip
                cache[(indx, price)] = recursions
                return recursions

    return helper(0, price)

#print(change_coins([1, 5, 20], 50))


# === [ Subset Sum ] ===
'''
 check if there is a subset that has a sum of s
'''

def has_subset_with_sum_s(seq, s):
    cache = {}

    def helper(indx, s):
        if (indx, s) in cache:
            return cache[(indx, s)]

        else:

            if s == 0:
                cache[(indx, s)] = True
                return True

            elif indx >= len(seq) or s < 0:
                cache[(indx, s)] = False
                return False


            else:

                ginamit = helper(indx + 1, s - seq[indx])
                skinip = helper(indx + 1, s)

                recursions = ginamit or skinip
                cache[(indx, s)] = recursions
                return recursions

    return helper(0, s)


#print(has_subset_with_sum_s([3, 5, 7, 10], 15))

# === [ Knapsack ] ===
''' pick list of item with max sum
'''

def knapsack(weights, values, max_weight): # wrapper
    cache = {}

    def helper(indx, max_weight): # recursion
        if (indx, max_weight) in cache: # return output if pair in cache
            return cache[(indx, max_weight)]

        else: # if not in cache, perform recursion

            if max_weight < 0: # base case : if its too heavy make it so that it wont be chosen
                cache[(indx, max_weight)] = float("-inf")
                return float("-inf")
            if indx >= len(weights): # base case : if no more next item, just return 0 value
                cache[(indx, max_weight)] = 0
                return 0

            else: # since two option, get max between use and skip
                # sa use, i add mo yung currrent value ng inxth item
                use = values[indx] + helper(indx + 1, max_weight - weights[indx])
                skip = helper(indx + 1, max_weight)

                recursion = max(use, skip)
                cache[(indx, max_weight)] = recursion
                return recursion

    return helper(0, max_weight)

print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))





