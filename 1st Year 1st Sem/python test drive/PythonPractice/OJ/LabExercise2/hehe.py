def right_half_pyramid(base):
    return "\n".join(tuple(("O" * (x + 1)) for x in range(base)))

def inverted_right_half_pyramid(base):
    return "\n".join(tuple(("O" * (base - x)) for x in range(base)))

print(inverted_right_half_pyramid(5))

OIII
OOII
OOOI
OOOO