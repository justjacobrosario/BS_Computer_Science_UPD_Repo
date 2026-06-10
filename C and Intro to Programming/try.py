"1010"


def binary_to_decimal():
    b = input("binary: ")
    l = len(b)
    res = 0
    for i, val in enumerate(b):
        idx = l - i - 1
        res += int(val)*(2**idx)
        print(f"{val}*({idx}^{2})")

    print(res)
    
binary_to_decimal()