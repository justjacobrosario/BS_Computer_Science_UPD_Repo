import time
from turtle import Screen

import config
from config import (
    AXE,
    FLAMETHROWER,
    HAMMER,
    MUSHROOM,
    PAVED,
    PLAYER,
    ROCK,
    STREET,
    WATER,
)
from map_reader import emojizer
from sound_check import play_sound

# ===== FUNCTIONS FOR IN GAME PHYSICS =====


def read(movement: int) -> tuple:
    # Converts a key to movement direction
    if movement in {119, 87}:  # walk up
        return -1, 0
    elif movement in {115, 83}:  # walk down
        return 1, 0
    elif movement in {97, 65}:  # walk left
        return 0, -1
    elif movement in {100, 68}:  # walk right
        return 0, 1
    return 0, 0


def is_valid_move(m: list, new_coords: int) -> bool:
    return (
        new_coords[0] < 0
        or new_coords[1] < 0
        or new_coords[0] >= len(m)
        or new_coords[1] >= len(m[0])
    )


def new_print(
    map_bg_color: int,
    map_line_color: int,
    map_data: list,
    screen_w: int,
    screen: Screen,
) -> None:
    # Draws the current map on the terminal
    for row_num, row in enumerate(emojizer(map_data)):
        for col_num, tile in enumerate(row):
            screen.print_at(
                tile,
                col_num * 2 + (screen_w // 2) - 70,
                row_num + 1 + (screen.height - 25) // 2 - 8,
                bg=map_bg_color,
                colour=map_line_color,
            )
    screen.refresh()


def rock_interaction(
    old_coords: tuple,
    new_coords: tuple,
    rock_destination: tuple,
    map_1: list,
    player_coor: tuple,
    standing_on_item: str,
    paved_tiles: dict,
) -> tuple:
    if (
        rock_destination[0] < 0
        or rock_destination[1] < 0
        or rock_destination[0] >= len(map_1)
        or rock_destination[1] >= len(map_1[0])
    ):
        return map_1, player_coor, standing_on_item
    if (
        map_1[rock_destination[0]][rock_destination[1]] == "."
        or map_1[rock_destination[0]][rock_destination[1]] == PAVED
    ):  # when the new destination of a rock is going to be a space or paved the player can move the rock
        play_sound(config.rock_push_sound, duration=200)
        map_1[rock_destination[0]][rock_destination[1]] = ROCK
        map_1[new_coords[0]][new_coords[1]] = PLAYER
        map_1[old_coords[0]][old_coords[1]] = (
            standing_on_item if standing_on_item != MUSHROOM else "."
        )
        standing_on_item = "." if new_coords not in paved_tiles else PAVED
        player_coor = new_coords
        return map_1, player_coor, standing_on_item
    elif (
        map_1[rock_destination[0]][rock_destination[1]] == WATER
    ):  # if the next destination is water then the rock falls into water and the water turns paved
        play_sound(config.rock_push_water_sound)
        map_1[rock_destination[0]][rock_destination[1]] = PAVED
        map_1[new_coords[0]][new_coords[1]] = PLAYER
        map_1[old_coords[0]][old_coords[1]] = (
            standing_on_item if standing_on_item != MUSHROOM else "."
        )
        paved_tiles[rock_destination[0], rock_destination[1]] = None
        standing_on_item = "." if new_coords not in paved_tiles else PAVED
        player_coor = new_coords
        return map_1, player_coor, standing_on_item
    else:
        return (
            map_1,
            player_coor,
            standing_on_item,
        )  # if no condition is satisfied then nothing would happen


def space_interaction(
    row_pos: int,
    col_pos: int,
    new_row: int,
    new_col: int,
    map_1: list,
    player_coor: tuple,
    paved_tiles: dict,
    standing_on_item: str,
) -> tuple:
    item_on_ground_prompt = ""  # Default value

    if (row_pos, col_pos) in paved_tiles:
        map_1[row_pos][col_pos] = PAVED
    elif map_1[row_pos][col_pos] == STREET:
        map_1[row_pos][col_pos] = STREET
    else:
        map_1[row_pos][col_pos] = (
            standing_on_item if standing_on_item != MUSHROOM else "."
        )

    standing_on_item = map_1[new_row][new_col]
    map_1[new_row][new_col] = PLAYER
    player_coor = new_row, new_col

    if standing_on_item not in {FLAMETHROWER, AXE, HAMMER}:
        item_on_ground_prompt = "No item to pick up"

    return map_1, player_coor, standing_on_item, item_on_ground_prompt


def tree_interaction(
    new_coor: tuple,
    map_1: list,
    held_item: str,
    screen: Screen,
) -> tuple:
    if held_item == " ":
        return map_1, held_item
    if held_item == AXE:
        map_1 = chop(map_1, new_coor)
        held_item = " "
        print(held_item)
    elif held_item == FLAMETHROWER:
        map_1 = burn(map_1, new_coor, screen)
        held_item = " "
        print(held_item)

    return map_1, held_item


def break_rock_interaction(
    new_coor: tuple,
    map_1: list,
    held_item: str,
) -> tuple:
    if held_item == " ":
        return map_1, held_item
    if held_item == HAMMER:
        map_1 = _break(map_1, new_coor)
        held_item = " "
        print(held_item)

    return map_1, held_item


def item_interaction(free_item: str) -> str:
    item_on_ground_prompt = ""

    if free_item == "A":
        item_on_ground_prompt = "🪓"
    elif free_item == "F":
        item_on_ground_prompt = "🔥"
    elif free_item == "H":
        item_on_ground_prompt = "🔨"
    else:
        item_on_ground_prompt = ""
    return item_on_ground_prompt


def pick_up(standing_on_item: str, held_item: str) -> tuple:
    item_on_ground_prompt = "No item to pick up"
    if standing_on_item == AXE:
        standing_on_item = "."
        held_item = AXE
        item_on_ground_prompt = "No item to pick up"
    if standing_on_item == FLAMETHROWER:
        standing_on_item = "."
        held_item = FLAMETHROWER
        item_on_ground_prompt = "No item to pick up"
    if standing_on_item == HAMMER:
        standing_on_item = "."
        held_item = HAMMER
        item_on_ground_prompt = "No item to pick up"

    return standing_on_item, held_item, item_on_ground_prompt


def mushroom_interaction(mush_count: int) -> int:
    play_sound(config.mushroom_collect_sound, stop_current=False)
    mush_count += 1
    return mush_count


# ===== FUNCTIONS FOR BASIC INVENTORY UTILITIES =====


# FLAMETHROWER


def burn(
    m: list,
    current: tuple,
    screen: Screen,
) -> list:
    possible_locs = _burn(
        m,
        current,
    )  # stores all of the locations of trees connected to the original tree
    play_sound(config.burning_sound, duration=len(possible_locs) * 10)
    for (
        i,
        j,
    ) in (
        possible_locs
    ):  # loops thru all of the locations and turns them into empty spaces
        m[i][j] = "F"
        new_print(config.map_bg_color, config.map_line_color, m, screen.width, screen)
        screen.refresh()
        time.sleep(0.000001)
        m[i][j] = "."
        new_print(config.map_bg_color, config.map_line_color, m, screen.width, screen)
        screen.refresh()
    return m


def _burn(
    m: list,
    current: tuple,
    path: set = set(),
) -> set:
    if (
        current[0] < 0
        or current[1] < 0
        or current[0] >= len(m)
        or current[1] >= len(m[0])
    ):
        return path  # bounds check
    elif m[current[0]][current[1]] != "T":
        return path  # check whether the current position is a tree or not
    elif current in path:
        return path  # check whether already visited the current path
    else:
        # moves the current path down left up right to get all possible values
        new_path = path | {current}
        down = _burn(m, (current[0] + 1, current[1]), new_path)
        left = _burn(m, (current[0], current[1] - 1), new_path)
        up = _burn(m, (current[0] - 1, current[1]), new_path)
        right = _burn(m, (current[0], current[1] + 1), new_path)

        return down | left | up | right


# AXE


def can_chop(m: list, current: tuple) -> bool:
    i, j = current
    if i < 0 or j < 0 or i > len(m) or j > len(m[0]):
        return False

    return m[i][j] == "T"


def chop(m: list, current: tuple) -> list:
    play_sound(config.chop_sound, duration=200)
    i, j = current
    m[i][j] = "."

    return m


# HAMMER


def can_break(m: list, current: tuple) -> bool:
    i, j = current
    if i < 0 or j < 0 or i > len(m) or j > len(m[0]):
        return False
    if m[i][j] == "T":
        return True
    return False


def _break(m: list, current: tuple) -> list:
    i, j = current
    m[i][j] = "."

    return m
