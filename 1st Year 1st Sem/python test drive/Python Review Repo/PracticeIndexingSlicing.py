def rotate_clockwise(m):
    row1, row2 = m
    return (row2[0], row1[0]), (row2[1], row1[1])

def every_other(t):
    return t[::2]

def identify_tag(tag):
    if tag[1] == '/':
        return tag[2:-1]
    else:
        return tag[1:-1]

def is_palindrome(s):
    return s == s[::-1]

def perfect_shuffle(t):
    left, right = (t[:len(t)//2], t[len(t)//2:])
    fl, fr = left[0], right[0]
    return (fl, fr, *left[1:], *right[1:])

    if not t:
        return 
print(perfect_shuffle((1, 2, 3, 4)))