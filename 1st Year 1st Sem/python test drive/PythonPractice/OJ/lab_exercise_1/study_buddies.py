def min_to_pass(s):
    if yow_sum(s) == "not an int":
        return None

    elif (60*(len(s) + 1) - yow_sum(s)) <= 100:
        return 60*(len(s) + 1) - yow_sum(s)

    else:
        return None

def yow_sum(seq): 
    if len(seq) == 0:
        return 0
    elif type(seq[0]) != int:
        return "not an int"
    else:
        return seq[0] + yow_sum(seq[1:])

print(min_to_pass((60, 60, "yow")))

"""
100+n / 2 = 60
n = 60*2 - 100




"""