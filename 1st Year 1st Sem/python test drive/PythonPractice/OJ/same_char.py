#check if strings s and t are the same words/sets of letters, regardless of casing.
#makes use of .lower() or even .upper()

def same(s, t):
    return s.lower() == t.lower()

print(same("banana", "Banana"))