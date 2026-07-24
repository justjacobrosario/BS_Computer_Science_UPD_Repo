def find(query_sn):
    for item in data:
        if item[0] == query_sn:
            return item[1]

def tup_pair_to_dict(seq):
    res = {}
    for tup_pair in seq:
        key, value = tup_pair
        res[key] = value
    return res

data = {
(200099911, "Juan Daw"),
(200099922, "Janine Daw"),
(200099955, "Pedro Daw"),
}

data = dict(data)

d = {1:2, 3:4}

"""print(d)
print(200099911 in data)"""
"""
print(tup_pair_to_dict(data))
print(dict(data))"""


map_1[row_pos][col_pos] = '🪓' if map_1[row_pos][col_pos] == "A" else AXE
    map_1[row_pos][col_pos] = '🔥' if map_1[row_pos][col_pos] == "F" else FLAMETHROWER


def classify_by_standing(y, students):
    freshmans = []
    sophomores = []
    juniors = []
    seniors = []
    immortals = []
    for stud, stud_id in students:
        sy = stud_id[:4]
        if sy == str(y):
            freshmans.append(stud)
        elif sy == str(y - 1):
            sophomores.append(stud)
        elif sy == str(y - 2):
            juniors.append(stud)
        elif sy == str(y - 3):
            seniors.append(stud)
        else:
            immortals.append(stud)
    dic = {
    "freshman": set(freshmans),
    "sophomore": set(sophomores),
    "junior": set(juniors),
    "senior": set(seniors),
    "immortal": set(immortals),
    }
    return dic

print(classify_by_standing(2025, (
    ("Alpha", "2022-99999"),
    ("Beta", "2021-11111"),
    ("Charlie", "2025-12345"),
    ("Delta", "2024-31415"),
    ("Echo", "2023-27182"),
    ("Foxtrot", "2000-00000"),
))
)
    