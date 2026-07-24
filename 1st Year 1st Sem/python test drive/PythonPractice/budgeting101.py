def weekly_budget(week, target_allowance):
    commute_sum = get_nth_val(week, 1)
    breakfast_sum = get_nth_val(week, 2)
    lunch_sum = get_nth_val(week, 3)
    dinner_sum = get_nth_val(week, 4)
    misc_sum = get_nth_val(week, 5)

    saved = target_allowance - (commute_sum + breakfast_sum + lunch_sum + dinner_sum + misc_sum)
    #return display_stat(week)    

    data = (
        ("---", "Value in Php"),
        ("Commute", commute_sum),
        ("Breakfast", breakfast_sum),
        ("Lunch", lunch_sum),
        ("Dinner", dinner_sum),
        ("Miscellaneous", misc_sum),
        ("",""),
        ("Allowance", target_allowance),
        ("Expenses", (commute_sum + breakfast_sum + lunch_sum + dinner_sum + misc_sum)),
        ("Remaining", saved)
        )
    return "\n".join("{:<15} {:<15}".format(*row) for row in data)

def get_nth_val(week, n):
    if len(week) == 1:
        return week[0][n-1]
    else:
        return week[0][n-1] + get_nth_val(week[1:], n)

"""def display_stat(week):

    commute_sum = get_nth_val(week, 1)
    breakfast_sum = get_nth_val(week, 2)
    lunch_sum = get_nth_val(week, 3)
    dinner_sum = get_nth_val(week, 4)
    misc_sum = get_nth_val(week, 5)

    data = (
        ("---", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "TOTAL")
        ("Commute", week[0][0], week[1][0], week[2][0], week[3][0], week[4][0], commute_sum),
        ("Breakfast", week[0][1], week[1][1], week[2][1], week[3][1], week[4][1], breakfast_sum),
        ("Lunch", week[0][2], week[1][2], week[2][2], week[3][2], week[4][2], lunch_sum),
        ("Dinner", week[0][3], week[1][3], week[2][3], week[3][3], week[4][3], dinner_sum),
        ("Miscellaneous", week[0][4], week[1][4], week[2][4], week[3][4], week[4][4], misc_sum),
        )

    for row in data:
        return ("{:<15} {:<15} {:<15}".format(*row))"""



#day_bud = (commute, breakfast, lunch, dinner, misc)
weekly_allowance = 1000
"""
#less hustle
mon_bud = (22, 0.0, 0, 0, 0)
tue_bud = (44, 0, 60, 70, 0)
wed_bud = (22, 0, 60, 70, 0)
thu_bud = (44, 0, 60, 70, 0)
fri_bud = (11, 0, 60, 70, 0.0)
"""
"""
#mid hustle (lalakad pauwi)
mon_bud = (11, 0.0, 60, 70, 100)
tue_bud = (33, 0, 60, 0, 0)
wed_bud = (11, 0, 60, 70, 0)
thu_bud = (11, 0, 60, 0, 0)
fri_bud = (70, 0, 60, 0, 0.0)
"""
#ultra hustle (lalakad pauwi, delata lagi)
mon_bud = (11, 0.0, 60, 0, 100)
tue_bud = (33, 0, 60, 0, 0)
wed_bud = (11, 0, 60, 0, 0)
thu_bud = (11, 0, 60, 0, 0)
fri_bud = (70, 0, 60, 0, 0.0)


week = (mon_bud, tue_bud, wed_bud, thu_bud, fri_bud)

print(weekly_budget(week, weekly_allowance))