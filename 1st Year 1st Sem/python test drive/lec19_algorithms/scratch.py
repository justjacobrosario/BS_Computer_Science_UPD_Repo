
def count_product_subarrays(seq, p):
    # prod <= p

    prod = 1
    f = 0
    count = 0

    for l in range(len(seq)):
        prod *= seq[l]

        while prod > p and f <= l:
            prod //= seq[f]
            f += 1

        count += l - f + 1
    return count

#print(count_product_subarrays([1, 2, 3, 4], 10))


def zero_sum_tracker(seq):
    seq = iter(seq)
    prefix = 0
    lista = {0:1}
    count = 0

    for item in seq:
        prefix += item # iterative case

        count += lista.get(prefix, 0) # increment

        lista[prefix] = lista.get(prefix, 0) + 1 # update the lista

        yield count

#print([*zero_sum_tracker([3, -1, -2, 5])])

def range_sum_queries(seq, queries):
    res = []
    prefix = prefix_sum(seq)

    for i, j in queries:
        res.append(prefix[j+1] - prefix[i])
    return res

def prefix_sum(seq):
    res = [0]

    for item in seq:
        res.append(res[-1] + item)

    return res

#print(range_sum_queries([5, -3, 2, 8], [(0, 3), (1, 2), (0, 0)]))


def count_budget_pairs(projects, contractors, b1, b2):
    projects = sorted(projects)
    contractors = sorted(contractors)
    count = 0

    for p in projects:
        # b1 <= p*c <= b2
        lowest_c = b1 // p + 1 if b1 % p != 0 else b1 // p
        largest_c = b2 //p

        lowest_c_i = get_inc_ge(contractors, lowest_c)
        largest_c_i = get_exc_gt(contractors, largest_c)

        count += largest_c_i - lowest_c_i
    return count

def get_inc_ge(seq, x):
    l, r = 0, len(seq) - 1
    candidate = len(seq)

    while l<=r:
        m = (l+r) // 2
        if seq[m] >= x:
            candidate = m
            r = m - 1
        else:
            l = m + 1
    return candidate

def get_exc_gt(seq, x):
    l, r = 0, len(seq) - 1
    candidate = len(seq)

    while l<=r:
        m = (l+r) // 2
        if seq[m] > x:
            candidate = m
            r = m - 1
        else:
            l = m + 1
    return candidate


#print(count_budget_pairs([10, 20, 30], [2, 3, 4], 40, 100))


def max_activity_happiness(G, S, R):

    # _init_
    states = [0, 0, 0]

    for day in range(len(G)):
        upd = [0, 0, 0]
        upd[0] = max(states[1], states[2]) + G[day]
        upd[1] = max(states) + S[day]
        upd[2] = max(states) + R[day]

        states = upd
    return max(states)

#print(max_activity_happiness([100, 50], [40, 50], [20, 10]))


def equal_parity_counter(seq):
    lista = {0:1}
    prefix = 0
    evens = 0
    odds = 0
    count = 0

    for item in seq:
        if item % 2 == 0:
            evens += 1
        else:
            odds += 1

        prefix = (evens - odds)

        count += lista.get(prefix, 0)

        lista[prefix] = lista.get(prefix, 0) + 1

        yield count


#print([*equal_parity_counter([2, 4, 6])])


def longest_divisor_chain(seq):
    seq = sorted(seq)

    dp = [1] * len(seq)

    for i in range(len(seq)):
        if i > 0:
            if seq[i] % seq[i-1] == 0:
                dp[i] = max(dp[i], dp[i-1] + 1)
    return max(dp)

#print(longest_divisor_chain([3, 6, 12, 24, 2]))


class Stage:
    def __init__(self):
        self.seq = []
    def insert_right(self, s):
        self.seq.append(s)
    def insert_left(self, s):
        self.seq = [s] + self.seq
    def get(self, i):
        if 0 <= i < len(self.seq):
            return self.seq[i] 
        else:
            raise ValueError



#from oj_strs import StrData

def get_string_data(seq):
    res = {}

    for item in seq:
        val = StrData(set(), set())

        for sub_item in seq:
            if item in sub_item:
                val.superstrings.add(sub_item)
            if sub_item in item:
                val.substrings.add(sub_item)

        res[item] = val

    return res


#print(get_string_data(('a', 'banana', 'anna', 'ann', 'an', 'hannah', 'an')))

from dataclasses import dataclass
@dataclass
class Account:
    account_id : str
    balance : int

    def withdraw(self, pera):
        if 0 > pera  or pera > self.balance:
            raise ValueError
        else:
            self.balance -= pera

    def deposit(self, pera):
        if 0 > pera:
            raise ValueError
        else:
            self.balance += pera


def test_Account():
    account = Account(account_id="JJV", balance=0)

    account.deposit(11)
    assert account.balance == 11
    account.withdraw(10)
    assert account.balance == 1

    try:
        account.withdraw(-2)
    except ValueError:
        print("This should be printed out")

    try:
        account.withdraw(2)
    except ValueError:
        print("This should also be printed out")


def window_shopping(seq, k):
    res = set()

    def prefix_sum(seq):
        ans = [0]
        for item in seq:
            ans.append(ans[-1] + item)
        return ans

    prefix = prefix_sum(seq)

    for i in range(len(seq) - k + 1):
        j = i + k - 1
        res.add(prefix[j + 1] - prefix[i])

    res = sorted(list(res), reverse = True)

    def get_nth(n):
        return res[n-1]

    return get_nth

def decorate(border = "#"):

    def decorate_helper(func):
        def wrapper(*args, **kwargs):

            message = str(func(*args, **kwargs))

            message_layer = f"{border} {message} {border}"
            pad_layer = border + " "*(len(message_layer)-2) + border
            edge_layer = border*len(message_layer)
            return edge_layer + '\n' + pad_layer + '\n' + message_layer + '\n' + pad_layer + '\n' + edge_layer
        return wrapper
    return decorate_helper


'''
hope3 = 135 + 140 + 250 + 190 + 250
hope2 = 230 + 230 + 200
hope1 = 375

reg3, bon3 = (60+170+55 + 170 + 80), (135 + 80+80 + 135)
print(reg3, bon3)

reg2, bon2 = (140 + 140 + 120), (90 + 90 + 80)
print(reg2, bon2)
reg1, bon1 = (100 + 100 + 100), (25 + 25 + 25)
print(reg1, bon1)
ey = sum((hope3, hope2, hope1)) // 3'''

'''x = 'abcd'

for letter in 'qwertyuiopasdfghjklzxcvbnm':
    if ord(letter) > ord(letter.upper()):
        print('small')
    elif ord(letter) < ord(letter.upper()):
        print('big')
    else:
        print('same')'''

x = repr("5")
#print(repr(x), type(x))

a = (1, 2)
b = (2, 0)


lines = []

'''while True:
    text = input('here: ')
    if text != '`':
        if text not in {'\n', '', ' '}:
            lines.append(text)
    else:
        break

edited = ''

for line in lines:
    edited += '        ' + line + '\n'

print(edited)'''

with open('formatted.txt', 'r', encoding='utf-8') as file:
    lines = (file.read()).split('\n')

edited = ''

for line in lines:
    if line not in {'\n', '', ' '}:

        edited += '        ' + line + '\n'

with open('formatted.txt', 'w', encoding='utf-8') as file:
    file.write(edited)