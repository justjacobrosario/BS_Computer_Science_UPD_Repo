from pathlib import Path

import config

# ==== MAP READER ====


def map_maker(file: str, *, main_file: bool = True) -> list:
    base_path = Path(__file__).parent
    file_path = base_path / file

    if main_file:
        with open(file_path) as maps:
            maps = (
                maps.read()
            )  # reads and stores the value of all of the line of the text file

            maps = Path(file_path).read_text()

            return [
                [list(line) for line in mapa[1:-1].split("\n")]
                for mapa in [one_map for one_map in maps[1:-1].split("\\")]
            ]
    else:
        with open(file_path) as maps:
            maps = maps.read()
            new = [list(line) for line in maps.splitlines()[1:]]
            return list(new)


def find_player(maps: list) -> tuple:
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "L":
                return (i, j)
    return 0,0


def count_mush(maps: list) -> int:
    total_mush = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == config.MUSHROOM:
                total_mush += 1

    return total_mush


def emojizer(lst: list) -> list:
    return [row_emojizer_helper(row) for row in lst]


def row_emojizer_helper(row: list) -> list:
    emojized_row = []
    dic = {
        "L": config.player_charac,
        "T": "🌲",
        "+": "🍄",
        "R": "🗿",
        "-": "⬜",
        "~": "🟦",
        "A": "🪓",
        "F": "🔥",
        "H": "🔨",
        "B": "🟥",
        "Y": "🟫",
        "C": "🟧",
        "S": "🔲",
        "%": "🦂",
    }
    for tile in row:
        if tile in dic:
            emojized_row.append(dic[tile])
        else:
            emojized_row.append("  ")

    return emojized_row


def restart(map_number: int = 0, map_file: str = "") -> list:
    return map_maker(map_file, main_file=False) if map_file else map_maker(map_number)
