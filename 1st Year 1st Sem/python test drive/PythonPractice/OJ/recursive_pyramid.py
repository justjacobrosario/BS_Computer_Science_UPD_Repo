def recursive_pyramid(symbol, base):
    if base == 1:
        return f"{symbol}"

    else:
        return f"{symbol*base:^{base}}" + "\n" + recursive_pyramid(symbol, base-1)

print(recursive_pyramid("%", 6))


"""
n = "Hello"
m = "Theredsakas"
print(f"{n:^10}\n{m:^10}")
"""
"""
0000000
_00000_
__000__
___0___
"""
