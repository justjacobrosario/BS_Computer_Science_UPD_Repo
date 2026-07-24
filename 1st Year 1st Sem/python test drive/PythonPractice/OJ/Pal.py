def is_palindromic(n):
    if len(str(n)) == 1:
        return True
    elif len(str(n)) == 2:
        if (n // 10) == (n % 10):
            return True
        else:
            return  False

    else:
        idx = len(str(n))
        if (n // (10**(idx - 1))) != (n % (10)):
            return False
        else:
            return True
            is_palindromic((n % 10**(idx-1)) // 10)

def is_palindromic(n):
    return str(n) == str(n)[::-1]

print(is_palindromic(12))