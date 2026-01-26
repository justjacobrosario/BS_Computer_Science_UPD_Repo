def consists_of(word, alphabet):
    print(f"checking:\n{frozenset(word)}\n{alphabet}\n")
    return frozenset(word) == alphabet

print(consists_of("abaca", frozenset('abc')))