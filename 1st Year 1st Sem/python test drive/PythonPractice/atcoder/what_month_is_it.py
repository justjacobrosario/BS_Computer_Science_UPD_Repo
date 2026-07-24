def num_order(n):
    n = int(n)
    if ((n%10) == 1):
        return f"{n}st"
    elif ((n%10) == 2):
        return f"{n}nd"
    elif ((n%10) == 3):
        return f"{n}rd"
    else:
        return f"{n}th"

def month():
    x = int(input("current month: "))
    y = int(input(f"how many months after the {num_order(x)} month? "))
    # result = x + y
    if (x + y) <= 12:
        return f"{y} months after the {num_order(x)} month is the {num_order(x + y)} month."
    elif y < 12: # if (x + y) > 12 but y < 12, subtract 12, x, and y
        return f"{y} months after the {num_order(x)} month is the {num_order(abs(12 - x - y))} month."
    elif y >= 12: # if y >=12, since 12 months cycles back, then get y%12 and add to the current month
        return f"{y} months after the {num_order(x)} month is the {num_order((y % 12) + x)} month."
print(month())