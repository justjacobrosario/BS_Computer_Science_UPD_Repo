# -*- coding: utf-8 -*-
from asciimatics.screen import Screen
from config import translate
import config


def draw_box(
    screen: Screen,
    line_color: int,
    bg_color: int,
    ini_col: int,
    ini_row: int,
    width: int,
    height: int,
) -> None:
    # Top border
    screen.print_at(
        "┌",
        ini_col,
        ini_row,
        colour=line_color,
        bg=bg_color,
    )
    screen.print_at(
        "─" * (width - 2),
        ini_col + 1,
        ini_row,
        colour=line_color,
        bg=bg_color,
    )
    screen.print_at(
        "┐",
        ini_col + width - 1,
        ini_row,
        colour=line_color,
        bg=bg_color,
    )

    # Side border
    for row in range(height - 2):
        screen.print_at(
            f"│{' ' * (width - 2)}│",
            ini_col,
            ini_row + 1 + row,
            colour=line_color,
            bg=bg_color,
        )

    # Bottom border
    screen.print_at(
        "└",
        ini_col,
        ini_row + height - 1,
        colour=line_color,
        bg=bg_color,
    )
    screen.print_at(
        "─" * (width - 2),
        ini_col + 1,
        ini_row + height - 1,
        colour=line_color,
        bg=bg_color,
    )
    screen.print_at(
        "┘",
        ini_col + width - 1,
        ini_row + height - 1,
        colour=line_color,
        bg=bg_color,
    )
    screen.refresh()


def mush_print(
    screen: Screen,
    line_color: int,
    bg_color: int,
    count: int,
    mush_count_col: int,
    mush_count_row: int,
) -> None:
    # Get translation dynamically
    mush_count_label = translate("Mushroom Count: ", "キノコ数: ", "Bilang ng Kabute: ", config.chosen_lang)
    
    # Draws mushroom count
    screen.print_at(
        mush_count_label,
        mush_count_col,
        mush_count_row,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        count,
        mush_count_col,
        mush_count_row + 1,
        bg=bg_color,
        colour=line_color,
    )
    screen.refresh()


def item_on_ground_print(
    screen: Screen,
    line_color: int,
    bg_color: int,
    item_on_ground_prompt: str,
    iog_count_col: int,
    iog_count_row: int,
) -> None:
    # Get translations dynamically
    iog_message = translate("No item to pick up", "拾うアイテムがない", "Walang item", config.chosen_lang)
    pick_message = translate("[P] Pickup        ", "[P] 拾う", "[P] Pulutin", config.chosen_lang)
    
    # Draws if there is an item on the current tile
    if item_on_ground_prompt == "No item to pick up" or item_on_ground_prompt == " ":
        screen.print_at(
            iog_message,
            iog_count_col,
            iog_count_row,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            " ",
            iog_count_col + 2,
            iog_count_row + 2,
            bg=bg_color,
            colour=line_color,
        )
    else:
        screen.print_at(
            pick_message,
            iog_count_col,
            iog_count_row,
            bg=bg_color,
            colour=line_color,
            attr=Screen.A_BOLD,
        )
        screen.print_at(
            item_on_ground_prompt,
            iog_count_col + 2,
            iog_count_row + 2,
            bg=bg_color,
            colour=line_color,
        )
    screen.refresh()


def inventory_label(
    screen: Screen,
    line_color: int,
    bg_color: int,
    inventory_col: int,
    inventory_row: int,
) -> None:
    # Get translation dynamically
    inv_message = translate("Inventory:", "所持品:", "Imbentaryo:", config.chosen_lang)
    
    screen.print_at(
        inv_message,
        inventory_col,
        inventory_row,
        bg=bg_color,
        colour=line_color,
    )
    screen.refresh()


def inventory_print(
    screen: Screen,
    line_color: int,
    bg_color: int,
    held_item: str,
    inventory_col: int,
    inventory_row: int,
) -> None:
    # Draws currently equipped item
    def emo(item: str) -> str:
        dic = {"F": "🔥", "A": "🪓", "H": "🔨"}
        if item in dic:
            return dic[item]
        else:
            return " "

    screen.print_at(
        emo(held_item),
        inventory_col,
        inventory_row,
        bg=bg_color,
        colour=line_color,
    )
    screen.refresh()


def initial_ctrl_print(
    screen: Screen,
    line_color: int,
    bg_color: int,
    ctrl_print_col: int,
    ctrl_print_row: int,
) -> None:
    # Get translations dynamically
    quit_m = translate("[Q] Quit", "[Q] 終了", "[Q] Umalis", config.chosen_lang)
    up_m = translate("[W] Walk Up", "[W] 上へ進む", "[W] Pataas", config.chosen_lang)
    left_m = translate("[A] Walk Left", "[A] 左へ進む", "[A] Pakaliwa", config.chosen_lang)
    down_m = translate("[S] Walk Down", "[S] 下へ進む", "[S] Pababa", config.chosen_lang)
    right_m = translate("[D] Walk Right", "[D] 右へ進む", "[D] Pakanan", config.chosen_lang)
    
    screen.print_at(
        "🢁",
        ctrl_print_col + 1,
        ctrl_print_row,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        "🢀",
        ctrl_print_col - 1,
        ctrl_print_row + 1,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        "🢃",
        ctrl_print_col + 1,
        ctrl_print_row + 2,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        "🢂",
        ctrl_print_col + 3,
        ctrl_print_row + 1,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        quit_m,
        ctrl_print_col - 2,
        ctrl_print_row + 3,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        up_m,
        ctrl_print_col + 8,
        ctrl_print_row,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        left_m,
        ctrl_print_col + 8,
        ctrl_print_row + 1,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        down_m,
        ctrl_print_col + 8,
        ctrl_print_row + 2,
        bg=bg_color,
        colour=line_color,
    )
    screen.print_at(
        right_m,
        ctrl_print_col + 8,
        ctrl_print_row + 3,
        bg=bg_color,
        colour=line_color,
    )
    screen.refresh()


def ctrl_print(
    screen: Screen,
    bg_color: int,
    line_color: int,
    movement: int,
    ctrl_print_col: int,
    ctrl_print_row: int,
) -> None:
    # Get translations dynamically
    quit_m = translate("[Q] Quit", "[Q] 終了", "[Q] Umalis", config.chosen_lang)
    up_m = translate("[W] Walk Up", "[W] 上へ進む", "[W] Pataas", config.chosen_lang)
    left_m = translate("[A] Walk Left", "[A] 左へ進む", "[A] Pakaliwa", config.chosen_lang)
    down_m = translate("[S] Walk Down", "[S] 下へ進む", "[S] Pababa", config.chosen_lang)
    right_m = translate("[D] Walk Right", "[D] 右へ進む", "[D] Pakanan", config.chosen_lang)
    
    if movement in {ord("w"), ord("W")}:
        screen.print_at(
            "🢁",
            ctrl_print_col + 1,
            ctrl_print_row,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.print_at(
            "🢀",
            ctrl_print_col - 1,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢃",
            ctrl_print_col + 1,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢂",
            ctrl_print_col + 3,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            quit_m,
            ctrl_print_col - 2,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            up_m,
            ctrl_print_col + 8,
            ctrl_print_row,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.print_at(
            left_m,
            ctrl_print_col + 8,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            down_m,
            ctrl_print_col + 8,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            right_m,
            ctrl_print_col + 8,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=line_color,
        )
        screen.refresh()
    if movement in {ord("a"), ord("A")}:
        screen.print_at(
            "🢁",
            ctrl_print_col + 1,
            ctrl_print_row,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢀",
            ctrl_print_col - 1,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.print_at(
            "🢃",
            ctrl_print_col + 1,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢂",
            ctrl_print_col + 3,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            quit_m,
            ctrl_print_col - 2,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            up_m,
            ctrl_print_col + 8,
            ctrl_print_row,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            left_m,
            ctrl_print_col + 8,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.print_at(
            down_m,
            ctrl_print_col + 8,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            right_m,
            ctrl_print_col + 8,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=line_color,
        )
        screen.refresh()
    if movement in {ord("s"), ord("S")}:
        screen.print_at(
            "🢁",
            ctrl_print_col + 1,
            ctrl_print_row,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢀",
            ctrl_print_col - 1,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢃",
            ctrl_print_col + 1,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.print_at(
            "🢂",
            ctrl_print_col + 3,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            quit_m,
            ctrl_print_col - 2,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            up_m,
            ctrl_print_col + 8,
            ctrl_print_row,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            left_m,
            ctrl_print_col + 8,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            down_m,
            ctrl_print_col + 8,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.print_at(
            right_m,
            ctrl_print_col + 8,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=line_color,
        )
        screen.refresh()
    if movement in {ord("d"), ord("D")}:
        screen.print_at(
            "🢁",
            ctrl_print_col + 1,
            ctrl_print_row,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢀",
            ctrl_print_col - 1,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢃",
            ctrl_print_col + 1,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            "🢂",
            ctrl_print_col + 3,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.print_at(
            quit_m,
            ctrl_print_col - 2,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            up_m,
            ctrl_print_col + 8,
            ctrl_print_row,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            left_m,
            ctrl_print_col + 8,
            ctrl_print_row + 1,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            down_m,
            ctrl_print_col + 8,
            ctrl_print_row + 2,
            bg=bg_color,
            colour=line_color,
        )
        screen.print_at(
            right_m,
            ctrl_print_col + 8,
            ctrl_print_row + 3,
            bg=bg_color,
            colour=Screen.COLOUR_YELLOW,
        )
        screen.refresh()


def time_print(
    screen: Screen,
    bg_color: int,
    line_color: int,
    current: float,
    time_col: int,
    time_row: int,
) -> None:
    # Get translation dynamically
    time_label = translate("Time: ", "時間: ", "Oras: ", config.chosen_lang)
    
    minutes = f"{(int(round(current, 2) // 60)):02d}"
    seconds = f"{(int(round(current, 2) % 60)):02d}"
    milliseconds = str(round(current, 2))[-2:]

    times = f"{minutes}:{seconds}:{milliseconds}"
    screen.print_at(
        time_label + " " + times,
        time_col,
        time_row,
        bg=bg_color,
        colour=line_color,
    )