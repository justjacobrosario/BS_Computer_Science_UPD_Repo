def convert(d0, d1, d2, b):
    return d0*(b**0) + d1*(b**1) + d2*(b**2)

def total_legs(h, w, p):
    return h*2 + w*4 + p*4

def num_subsquares(n, k):
    return (n - k + 1)**2

def pow_digits(a, b):
    return f"{(pow(a, b, 10**11)):011d}"

from fractions import Fraction

def substitute(a, b):
    return Fraction(1, a+1) + Fraction(1, b+1) + Fraction((a*b)-1, (a+1)*(b+1))


def number_tail(n):
    return ((n-(n%10))//10,n%10) if (n-(n%10)) != 0 else (None,n%10)

a, b = ({'x' : 1}, {'z' : 3})

c = a | {'y' : 2} | b

print(c)