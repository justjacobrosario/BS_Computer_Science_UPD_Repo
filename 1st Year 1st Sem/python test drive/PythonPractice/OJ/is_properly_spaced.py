#return True if no leading, trailing, and two consecutive spaces

def is_properly_spaced(s):
    print(f"stripped: {len(s.strip())}\nsplit: {len(s.split("  ")[0])}\norig: {len(s)}")
    return (len(s.strip()) == len(s)) and (len(s.split("  ")[0]) == len(s))

print(is_properly_spaced("b a n a n a"))