def night_shift(today, j, k):
    
    if today == "Sunday":
        today = 1 
    elif today == "Monday":
        today = 2
    elif today == "Tuesday":
        today = 3
    elif today == "Wednesday":
        today = 4
    elif today == "Thursday":
        today = 5
    elif today == "Friday":
        today = 6
    elif today == "Saturday":
        today = 7

    nth_day = today + (j**k)%7
    nth_day = nth_day%7

    if (nth_day == 1) or (nth_day == 4):
        return "Moe"
    elif (nth_day == 2) or (nth_day == 6):
        return "Miyako"
    elif (nth_day == 3) or (nth_day == 7):
        return "Saki"
    elif nth_day == 5:
        return "Miyu"

print(night_shift("Monday", 18, 19))

"""
    Moe = 1
    Miyako = 2
    Saki = 3
    Moe = 4
    Miyu = 5
    Miyako = 6
    Saki = 7
"""