def weekly_budg(mon_budg, tue_budg, wed_budg, thu_budg, fri_budg, target_budg):
    commute = mon_budg[0] + tue_budg[0] + wed_budg[0] + thu_budg[0] + fri_budg[0]
    breakf = mon_budg[1] + tue_budg[1] + wed_budg[1] + thu_budg[1] + fri_budg[1]
    lunch = mon_budg[2] + tue_budg[2] + wed_budg[2] + thu_budg[2] + fri_budg[2]
    dinn = mon_budg[3] + tue_budg[3] + wed_budg[3] + thu_budg[3] + fri_budg[3]
    misc = mon_budg[4] + tue_budg[4] + wed_budg[4] + thu_budg[4] + fri_budg[4]

    save = target_budg - (commute + breakf + lunch + dinn + misc)

    return save

def display_budg(mon_budg, tue_budg, wed_budg, thu_budg, fri_budg):
    mon_budg = get_mon_budg()

    commute = mon_budg[0] + tue_budg[0] + wed_budg[0] + thu_budg[0] + fri_budg[0]
    breakf = mon_budg[1] + tue_budg[1] + wed_budg[1] + thu_budg[1] + fri_budg[1]
    lunch = mon_budg[2] + tue_budg[2] + wed_budg[2] + thu_budg[2] + fri_budg[2]
    dinn = mon_budg[3] + tue_budg[3] + wed_budg[3] + thu_budg[3] + fri_budg[3]
    misc = mon_budg[4] + tue_budg[4] + wed_budg[4] + thu_budg[4] + fri_budg[4]

    data = (
        ("---", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "TOTAL")
        ("Commute", mon_budg[0], tue_budg[0], wed_budg[0], thu_budg[0], fri_budg[0], commute),
        ("Breakfast", mon_budg[1], tue_budg[1], wed_budg[1], thu_budg[1], fri_budg[1], breakf),
        ("Lunch", mon_budg[2], tue_budg[2], wed_budg[2], thu_budg[2], fri_budg[2], lunch),
        ("Dinner", mon_budg[3], tue_budg[3], wed_budg[3], thu_budg[3], fri_budg[3], dinn),
        ("Miscellaneous", mon_budg[4], tue_budg[4], wed_budg[4], thu_budg[4], fri_budg[4], misc),
        )

    for row in data:
        return ("{:<15} {:<15} {:<15}".format(*row))

def get_mon_budg(commute, breakf, lunch, dinn, misc):
    return (commute, breakf, lunch, dinn, misc)

def get_tue_budg(commute, breakf, lunch, dinn, misc):
    return (commute, breakf, lunch, dinn, misc)

def get_wed_budg(commute, breakf, lunch, dinn, misc):
    return (commute, breakf, lunch, dinn, misc)

def get_thu_budg(commute, breakf, lunch, dinn, misc):
    return (commute, breakf, lunch, dinn, misc)

def get_fri_budg(commute, breakf, lunch, dinn, misc):
    return (commute, breakf, lunch, dinn, misc)

# Input here:
#day_budg(commute, breakf, lunch, dinn, misc)

mon_budg(22, 100, 100, 100, 50)
tue_budg(22, 100, 100, 100, 50)
wed_budg(22, 100, 100, 100, 50)
thu_budg(22, 100, 100, 100, 50)
fri_budg(22, 100, 100, 100, 50)

print(display_budg(mon_budg, tue_budg, wed_budg, thu_budg, fri_budg))