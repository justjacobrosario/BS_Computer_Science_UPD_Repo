
"""
(1) - generator is a one-time-use sequence
- only purpose: get the next generator object using next()

e.g. mechanism of next()

_gen = x for x in range(5)
print(gen) <= raises a generator object
print(next(gen)) <= prints the 0th indx of range(5)
print(next(gen)) <= prints the 1th indx of range(5)
...
* print(next(gen)) <= prints the next indx of range(5)
until it approaches the StopIteration error, (means that theres no more next val)

we can use for-loops to loop the generator
e.g.
gen = (x for x in range(5))

for n in range(5):
    print(next(gen))

(2) yield keyword:
 - yield keyword is like return for functions,
   but instead of exiting the function after giving 
   the value, it will only pause the function
   and proceed to the next yield keyword if called again

e.g. 
    def vowels(): #returns the first yield val then to the next yields
        yield "a"
        yield "e"
        yield "i"
        yield "o"
        yield "u"

(3) Independence property of functions with yield:
 - once a function with yield is called or printed
 multiple times, you are technically calling the 
 original unupdated function, so it will always return
 the first yield val

e.g.
    print(next(vowels())) <-- prints "a"
    print(next(vowels())) <-- still prints "a"

 - to proceed to the next yield, assign the function
 to a specific variable then call that variable

e.g. 
    v1 = vowels()
    v2 = vowels() #different vars are independent from each

    print(next(v1)) <-- prints "a"
    print(next(v1)) <-- prints "e"
    print(next(v2)) <-- prints "a", independent from v1
    print(next(v1)) <-- prints "i"

(4) Identity Property of functions with yield/s
 - functions with yields is identified as a generator
 - u will only return a generator object using yield keyword
 - u will call the yield value using next()

(5) One-Time-Usage Property of generator objects
 - if generator objects are translated as an iterable 
   (a list, tuple, set, frozenset, splat), it an only be called ONCE

e.g.
    g = vowels()
    print(list(g)) <-- ["a", "e", "i", "o", "u"]
    print(list(g)) <-- []

(6) iter()
 - translates an iterable as a generator object
e.g.
    x = [1, 2, 3]
    g = iter(x)
    print(next(g)) <-- 1
    print(next(g)) <-- 2

(7) Use of generators in for-loops
 - generator functions can be the sequence of a for-loop
 - NOTE: once all generator objects are used, it will not be reused since its one-time
 e.g.
    for letter in vowels():
        print("letter:", letter) <-- prints the yield values step by step

(8) yield from
 - you can do wishful thinking by making a separate generator function and 
   get the yield value from it

e.g.

def nonempty_substrings(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            yield seq[i:j]

or u can do this       

def nonempty_substrings(seq):
    for i in range(len(seq)):
        yield from nonempty_substrings_from(i, seq) # you can yield from other generator funcs

def nonempty_substrings_from(i, seq):
    for j in range(i + 1, len(seq) + 1):
        yield seq[i:j]

for sub in nonempty_substrings('aba'):
    print(sub)



(9) generator exercises samples

e.g. duplicate every element of a seq
# do the operations in the generator func
def dupli(seq):
    for n in seq:
        yield n
        yield n
        
# do the printing of items in a seq in a separate for-loop
for v in dupli([3, 1, 4]):
    print(v)

e.g. enumerate indx and value

def members():
    yield "Momoi"
    yield "Midori"
    yield "Aris"
    yield "Yuzu"

def enumerate_from(gen, start):
    for name in gen:
        yield start, name
        start += 1
        
for (i, val) in enumerate_from(members(), 0):
    print(i, val)

returns ;
0 Momoi
1 Midori
2 Aris
3 Yuzu

e.g. partial sum
def partial_sums(seq):
    s = 0
    yield s
    for n in range(len(seq)):
        s += seq[n]
        yield s

for s in partial_sums((3, 1, 4)):
    print(s)

e.g. cartesian products
def cartesian_product(a, b):
    tmp_b = list(b) # since generator b is one_time, make it as a list
    for i in a:
        for j in tmp_b:
            yield (i, j)

for (x, y) in cartesian_product((1, 2), members()):
    print(x, y)



"""

def vowels():
    yield "a"
    yield "e"
    yield "i"
    yield "o"
    yield "u"

g = (vowels())


def members():
    yield "Momoi"
    yield "Midori"
    yield "Aris"
    yield "Yuzu"

def cartesian_product(a, b):
    tmp_b = list(b)
    for i in a:
        for j in tmp_b:
            yield (i, j)

"""for (x, y) in cartesian_product((1, 2), members()):
    print(x, y)
"""

def nonempty_substrings(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq) + 1):
            yield seq[i:j]

"""for sub in nonempty_substrings("abcd"):
    print(sub)"""

def count_from(start):
    while True:
        yield start
        start += 1

def take(n, seq):
    seq = iter(seq)
    for i in range(n):
        yield next(seq)

def nonempty_substrings(strng):
    def nonempty_substrings_start_from(i, strng):
        yield from (strng[i:j] for j in range(i + 1, len(strng) + 1))
            

    for i in range(len(strng)):
        yield from nonempty_substrings_start_from(i, strng)


"""for sub in nonempty_substrings("abcd"):
    print(sub)"""

#2, 3, 5, 7, 11, 13
def smallest_prime_factor(n):
    return next(
        p 
        for p in range(2, n + 1) 
        if n % p == 0)

#print(smallest_prime_factor(69))

x = "abcde"

print(x[0:3])

    

