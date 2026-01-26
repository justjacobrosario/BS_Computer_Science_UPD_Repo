def snip(s):
    if ". " in s:
        if s.index(". ") < (len(s) - 1):
            return f"{s[: (s.index(". ") + 1)]} [...]".strip()
        else:
            return f"{s}".strip()
    else:
        return f"{s}".strip()

print(snip("hello. "))