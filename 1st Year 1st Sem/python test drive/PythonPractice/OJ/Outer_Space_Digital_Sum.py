def digital_sum(n):
    if n < 10:
        return n
    elif n >= 10:
        return n%10 + digital_sum(n//10)


print(digital_sum(12345))