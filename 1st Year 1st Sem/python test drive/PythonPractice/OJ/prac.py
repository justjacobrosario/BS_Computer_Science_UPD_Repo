def number_tail(n):
    return (None if n < 10 else n//10, n%10)

print(number_tail(321345))