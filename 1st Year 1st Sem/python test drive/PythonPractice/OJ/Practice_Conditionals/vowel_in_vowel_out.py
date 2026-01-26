def is_pavivo(word):
    return (((word[0]).lower().strip() == (word[-1]).lower().strip()) and (word[0]).lower().strip() in "aeiou" and (len(word) >= 0))

print(is_pavivo(""))