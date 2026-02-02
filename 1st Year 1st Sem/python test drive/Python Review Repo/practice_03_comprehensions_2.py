def bacteria_counts(b, n):
    return tuple(b*(2**x) for x in range(n))

#print(bacteria_counts(3, 4))

def jeepney_groups(passengers, p):
    return tuple(passengers[i:i+p] for i in range(0, len(passengers), p))

#print(jeepney_groups(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'), 3))

def house_locations(distances):
    recent = (0,)

    for x in distances:
        recent += (recent[-1] + x,)
    return recent

#print(house_locations((2, 7, 1, 8)))

def attendance(presents, klase):
    attended = tuple(stud for stud in klase if stud in presents)
    absent = tuple(stud for stud in klase if stud not in presents)
    return (attended, absent)


#print(attendance(('dennis', 'jeremiah', 'eugene'),('eugene', 'alfred', 'dennis', 'vincent'),))

def empty_sections(s, studs):
    sections = set(num%s for num in studs)
    return s - len(sections)

'''print(empty_sections(8, (
 200062361, 200000263, 200092785, 200000916, 200071571,
 200089503, 200035712, 200015911, 200070711, 200061120,
 200020828, 200098139, 200056057, 200075391, 200016588,
 200005853, 200090523, 200015692, 200006517, 200066676,
)))'''

def fitness_routine(seq):
    def helper(seq, n):
        if len(seq)