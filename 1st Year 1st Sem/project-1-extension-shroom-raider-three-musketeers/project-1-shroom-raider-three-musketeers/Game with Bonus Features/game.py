
import time

from asciimatics.screen import Screen

import config
import physics_logic
import physics_logic_2
from config import (
    translate,
    HAMMER,
    MUSHROOM,
    PAVED,
    ROCK,
    STREET,
    TREE,
    WATER,
    held_item,
    mush_count,
    paved_tiles,
    standing_on_item,
)
from lose import lose
from map_reader import count_mush, emojizer, find_player, map_maker
from sound_check import play_sound
from ui import (
    ctrl_print,
    draw_box,
    initial_ctrl_print,
    inventory_label,
    inventory_print,
    item_on_ground_print,
    mush_print,
    time_print,
)
from winner import winner


def setup_game(map_file: str) -> tuple:
    current_map = map_maker(map_file, main_file=False)
    player_coor = find_player(current_map)
    return current_map, player_coor


# =====MAIN GAME=====


def in_game(
    screen: Screen,
    current_map: list,
    player_coor: tuple,
    stage: str,
) -> tuple:
    # Initialize local variables from config
    mush_count = config.mush_count
    paved_tiles = config.paved_tiles
    standing_on_item = config.standing_on_item
    item_on_ground_prompt = config.item_on_ground_prompt
    held_item = config.held_item

    screen_h, screen_w = screen.dimensions

    def new_print(
        map_bg_color: int,
        map_line_color: int,
        map_data: list,
        screen_w: int,
    ) -> None:
        for row_num, row in enumerate(emojizer(map_data)):
            for col_num, tile in enumerate(row):
                screen.print_at(
                    tile,
                    col_num * 2 + (screen_w // 2) - 70,
                    row_num + 1 + (screen_h - 25) // 2 - 8,
                    bg=map_bg_color,
                    colour=map_line_color,
                )
        screen.refresh()

    # ===== [ UI SETUP ] =====

    # Map UI
    map_w = 70
    map_h = 30

    # side Padding for Bottom UIs
    side_padding = 2

    # Mushroom Counter UI
    mush_count_col = screen_w // 2 + 43
    mush_count_row = map_h + 3 + (screen_h - 25) // 2 - 8

    # Item on ground status UI
    iog_count_col = screen_w // 2 - 42
    iog_count_row = screen_h + 3 + (screen_h - 25) // 2 - 8

    # Controls UI
    ctrl_print_col = screen_w // 2 - map_w + side_padding
    ctrl_print_row = map_h + 3 + (screen_h - 25) // 2 - 8

    # Inventory UI
    inventory_col = iog_count_col + 75
    inventory_row = map_h + 3 + (screen_h - 25) // 2 - 8

    # ===== GAME PHYSICS =====
    # player is spawned in the map

    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        (screen_w // 2) - 72,
        (screen_h - 25) // 2 - 8,
        (map_w + 2) * 2,
        map_h + 2,
    )  # box for map
    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        (screen_w // 2) - 72,
        map_h + 2 + (screen_h - 25) // 2 - 8,
        (map_w) * 2 + 4,
        6,
    )  # box for bottom tabs
    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        (screen_w // 2) - 72,
        map_h + 2 + (screen_h - 25) // 2 - 8,
        28,
        6,
    )  # box for bottom left ui
    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        mush_count_col - 2,
        mush_count_row - 1,
        31,
        6,
    )  # box for bottom right ui
    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        (screen_w // 2) - 72 + 28,
        map_h + 2 + (screen_h - 25) // 2 - 8,
        22,
        6,
    )  # box for pick up
    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        (screen_w // 2) + 28,
        map_h + 2 + (screen_h - 25) // 2 - 8,
        13,
        6,
    )  # box for pick up
    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        iog_count_col,
        map_h + 2 + (screen_h - 25) // 2 - 8 + 2,
        6,
        3,
    )  # box for item
    draw_box(
        screen,
        config.line_color,
        config.bg_color,
        iog_count_col + 73,
        map_h + 2 + (screen_h - 25) // 2 - 8 + 2,
        6,
        3,
    )  # box for item

    mush_print(
        screen,
        config.line_color,
        config.bg_color,
        mush_count,
        mush_count_col,
        mush_count_row,
    )
    item_on_ground_print(
        screen,
        config.line_color,
        config.bg_color,
        item_on_ground_prompt,
        iog_count_col,
        map_h + 2 + (screen_h - 25) // 2 - 8 + 1,
    )
    inventory_print(
        screen,
        config.line_color,
        config.bg_color,
        held_item,
        inventory_col,
        inventory_row,
    )
    initial_ctrl_print(
        screen,
        config.line_color,
        config.bg_color,
        ctrl_print_col,
        ctrl_print_row,
    )
    new_print(
        config.map_bg_color,
        config.map_line_color,
        current_map,
        screen_w,
    )
    inventory_label(
        screen,
        config.line_color,
        config.bg_color,
        screen.width // 2 + 29,
        mush_count_row,
    )
    total_mush = count_mush(current_map)

    start_time = time.time()
    current_time = 0

    while True:
        movement = screen.get_key()
        screen_w = screen.width

        current_time = time.time() - start_time

        # Standby until a key is pressed
        if movement is None:
            continue

        # Quit if q, Q or esc key is pressed
        if movement in {ord("q"), ord("Q"), 27}:
            play_sound(config.menu_sound)
            held_item = ""
            return False

        if movement in {ord("!")}:
            current_map, player_coor = setup_game(stage)

        # Movement management
        row_pos, col_pos = player_coor
        row_upd, col_upd = physics_logic.read(movement)
        new_row, new_col = row_pos + row_upd, col_pos + col_upd

        # refresh screen shortcut for collisions that will skip the next lines
        def refresh_screen_shrtcut() -> None:
            new_print(
                config.map_bg_color,
                config.map_line_color,
                current_map,
                screen_w,
            )
            mush_print(
                screen,
                config.line_color,
                config.bg_color,
                mush_count,
                mush_count_col,
                mush_count_row,
            )
            item_on_ground_print(
                screen,
                config.line_color,
                config.bg_color,
                item_on_ground_prompt,
                iog_count_col,
                map_h + 2 + (screen_h - 25) // 2 - 8 + 1,
            )
            inventory_print(
                screen,
                config.line_color,
                config.bg_color,
                held_item,
                inventory_col,
                inventory_row + 2,
            )
            ctrl_print(
                screen,
                config.bg_color,
                config.line_color,
                movement,
                ctrl_print_col,
                ctrl_print_row,
            )
            time_print(
                screen,
                config.bg_color,
                config.line_color,
                current_time,
                mush_count_col,
                inventory_row + 3,
            )
            screen.refresh()

        if movement is None:
            refresh_screen_shrtcut()
            continue

        # Pickup-system

        if movement in {ord("P"), ord("p")}:
            if held_item != " ":
                continue
            standing_on_item, held_item, item_on_ground_prompt = physics_logic.pick_up(
                standing_on_item,
                held_item,
            )
            refresh_screen_shrtcut()
        # Tile Update part
        # this part updates the map based on the new row and column that the user would arrive into

        if (
            new_row < 0
            or new_col < 0
            or new_row >= len(current_map)
            or new_col >= len(current_map[0])
        ):
            continue
        if (
            current_map[new_row][new_col] == "."
            or current_map[new_row][new_col] == PAVED
            or current_map[new_row][new_col] == STREET
        ):
            current_map, player_coor, standing_on_item, item_on_ground_prompt = (
                physics_logic.space_interaction(
                    row_pos,
                    col_pos,
                    new_row,
                    new_col,
                    current_map,
                    player_coor,
                    paved_tiles,
                    standing_on_item,
                )

            )
            refresh_screen_shrtcut()
        elif current_map[new_row][new_col] == ROCK:
            rock_destination = new_row + row_upd, new_col + col_upd
            if held_item != HAMMER:
                current_map, player_coor, standing_on_item = (
                    physics_logic.rock_interaction(
                        (row_pos, col_pos),
                        (new_row, new_col),
                        rock_destination,
                        current_map,
                        player_coor,
                        standing_on_item,
                        paved_tiles,
                    )
                )
            else:
                current_map, held_item = physics_logic.break_rock_interaction(
                    (new_row, new_col),
                    current_map,
                    held_item,
                    screen,
                )
            refresh_screen_shrtcut()
        elif current_map[new_row][new_col] == TREE:
            current_map, held_item = physics_logic.tree_interaction(
                (new_row, new_col),
                current_map,
                held_item,
                screen,
            )
            refresh_screen_shrtcut()
        elif current_map[new_row][new_col] == MUSHROOM:
            current_map, player_coor, standing_on_item, item_on_ground_prompt = (
                physics_logic.space_interaction(
                    row_pos,
                    col_pos,
                    new_row,
                    new_col,
                    current_map,
                    player_coor,
                    paved_tiles,
                    standing_on_item,
                )
            )
            mush_count = physics_logic.mushroom_interaction(mush_count)
            refresh_screen_shrtcut()
        elif current_map[new_row][new_col] in {"A", "F", "H"}:  # list of items
            item_on_ground_prompt = physics_logic.item_interaction(
                standing_on_item,
            )
            item_on_ground_print(
                screen,
                config.line_color,
                config.bg_color,
                item_on_ground_prompt,
                iog_count_col,
                iog_count_row,
            )
            current_map, player_coor, standing_on_item, item_on_ground_prompt = (
                physics_logic.space_interaction(
                    row_pos,
                    col_pos,
                    new_row,
                    new_col,
                    current_map,
                    player_coor,
                    paved_tiles,
                    standing_on_item,
                )
            )
            item_on_ground_prompt = physics_logic.item_interaction(
                standing_on_item,
            )
            refresh_screen_shrtcut()
        elif current_map[new_row][new_col] in {WATER, '%'}:
            return lose()

        refresh_screen_shrtcut()

        if mush_count == total_mush:
            return True
        else:
            refresh_screen_shrtcut()
            continue



# ===== [ GAME FUNCTION CALL ] =====


def new_game(stage: str = "") -> Screen:
    current_map, player_coor = setup_game(stage)
    return Screen.wrapper(lambda scr: in_game(scr, current_map, player_coor, stage))


def simulate_game(total: int, moves: str, stage_num: int = 0, stage: str = "") -> tuple:
    global standing_on_item, mush_count, held_item
    current_map, player_coor = setup_game(stage_num)
    for movement in moves:
        if movement not in {"w", "a", "s", "d", "p", "W", "A", "S", "D", "P"}:
            return current_map, False

    for movement in moves:
        if mush_count == total:
            return current_map, True

        if ord(movement) in {ord("q"), ord("Q")}:
            break

        if ord(movement) in {ord("P"), ord("p")}:
            if held_item != " ":
                continue
            standing_on_item, held_item, item_on_ground_prompt = (
                physics_logic_2.pick_up(standing_on_item, held_item)
            )
            continue

        row_pos, col_pos = player_coor
        row_upd, col_upd = physics_logic_2.read(ord(movement))
        new_row, new_col = row_pos + row_upd, col_pos + col_upd

        if (
            new_row < 0
            or new_col < 0
            or new_row >= len(current_map)
            or new_col >= len(current_map[0])
        ):
            continue
        if (
            current_map[new_row][new_col] == "."
            or current_map[new_row][new_col] == PAVED
            or current_map[new_row][new_col] == STREET
        ):
            current_map, player_coor, standing_on_item, _ = (
                physics_logic_2.space_interaction(
                    row_pos,
                    col_pos,
                    new_row,
                    new_col,
                    current_map,
                    player_coor,
                    paved_tiles,
                    standing_on_item,
                )
            )
        elif current_map[new_row][new_col] == ROCK:
            rock_destination = new_row + row_upd, new_col + col_upd
            if held_item != HAMMER:
                current_map, player_coor, standing_on_item = (
                    physics_logic_2.rock_interaction(
                        (row_pos, col_pos),
                        (new_row, new_col),
                        rock_destination,
                        current_map,
                        player_coor,
                        standing_on_item,
                        paved_tiles,
                    )
                )
            else:
                current_map, held_item = physics_logic_2.break_rock_interaction(
                    (new_row, new_col),
                    current_map,
                    held_item,
                )
        elif current_map[new_row][new_col] == TREE:
            current_map, held_item = physics_logic_2.tree_interaction(
                (new_row, new_col),
                current_map,
                held_item,
            )
        elif current_map[new_row][new_col] == MUSHROOM:
            current_map, player_coor, standing_on_item, _ = (
                physics_logic_2.space_interaction(
                    row_pos,
                    col_pos,
                    new_row,
                    new_col,
                    current_map,
                    player_coor,
                    paved_tiles,
                    standing_on_item,
                )
            )
            mush_count = physics_logic_2.mushroom_interaction(mush_count)
        elif current_map[new_row][new_col] in {"A", "F", "H"}:  # list of items
            current_map, player_coor, standing_on_item, _ = (
                physics_logic_2.space_interaction(
                    row_pos,
                    col_pos,
                    new_row,
                    new_col,
                    current_map,
                    player_coor,
                    paved_tiles,
                    standing_on_item,
                )
            )
        else:
            current_map = physics_logic_2.death_logic(
                current_map,
                row_pos,
                col_pos,
                new_row,
                new_col,
                standing_on_item,
            )
            return current_map, False

    return current_map, False
