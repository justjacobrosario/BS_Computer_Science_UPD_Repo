def same(s, t):
    return s.lower() == t.lower()

''' 1. Alignments'''
def center_align(s, w):
    return f'{s:^{w}}'

''' 2. Replace Chars'''
def coolspeakify(w):
    return w.replace('L', '1').replace('I', '1').replace('E', '3').replace('O', '0').replace('A', '4').replace('T', '7')

''' 3. Split Strings'''
def seconds_since_midnight(t):
    hr, mins, secs = t.split(':')
    return int(secs) + int(mins)*60 + int(hr)*3600

def append_ellipsis(s):
    if s[-1] == '.':
        return s
    else:
        return s + '...'

''' 4. Count char occurences '''
def line_count(s):
    return s.count('\n')

def is_properly_spaced(s):
    if '  ' in s:
        return False
    elif ' ' == s[0] or ' ' == s[-1]:
        return False
    else:
        return True

def len_side_comment(s):
    l_parenthesis = s.index('(')
    r_parenthesis = s.index(')')
    return r_parenthesis - l_parenthesis - 1

# unsolved
def is_valid_student_number(s):
    ...

def is_valid_identifier(s):
    LOWER = 'abcdefghijklmnopqrstuvwxyz'
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s[0] in LOWER or s[0] in UPPER

print(is_valid_identifier("__banana__"))