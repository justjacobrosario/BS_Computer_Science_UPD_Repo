import time
from unittest.mock import NonCallableMagicMock
import config
import random
from winner import winner
from config import translate

from ASCII_GRAPHICS import (
    jeep,
    num_1,
    num_2,
    num_3,
    num_4,
    num_6,
    num_5,
    num_7,
    num_8,
    num_9,
    num_10,
    num_11,
    num_12,
    num_13,
    num_14,
    num_15,
    num_16,
    num_17,
    num_18,
    num_19,
    num_20,
    rocket,
    large_rocket,
    solar_system,
    upd,
    oble,
    upd_map,
    stage,
    bulb,
    broken_bulb
)

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import FigletText

import sound_check

# ===== [HELPER AND EFFECT FUNCTIONS ] =====


def skip_cutscene(screen: Screen) -> bool:
    """Return True if any key is pressed."""
    key = screen.get_key()
    return key in {ord("s"), ord("S")}, key


def skip_interval(screen: Screen, interval: int) -> None:
    start = time.time()
    while time.time() - start < interval:
        skip_all, key = skip_cutscene(screen)
        if skip_all:
            return
        elif key not in {None, ord("s"), ord("S")}:
            break
        time.sleep(0.05)


def typewrite_print_at(
    screen: Screen,
    text: str,
    x: int = 0,
    y: int = 0,
    delay: float = 0.03,
    skip_m: str = None,
):
    """
    Display text with a typewriter animation on the screen.

    Args:
        screen (Screen): The asciimatics Screen object.
        text (str): The text to display (can include newlines).
        x, y (int, int): Start oordinates of the first charac.
        delay (float): Time delay between each character.
        skip_m (str): Message to display at the bottom.

    Returns:
        bool: True if user wants to skip the whole cutscene, False if user wants to continue
    """

    if config.chosen_lang == "japanese":
        for i, line in enumerate(text.splitlines()):
            current_x = x
            current_y = y + i

            for charac in line:
                screen.print_at(charac, current_x, current_y)
                screen.refresh()
                current_x += 1
                time.sleep(delay)

                # Skip whole cutscene by pressing S, Skip the typewrite animation by pressing any other key
                key = screen.get_key()
                if key in [ord("s"), ord("S")]:
                    return True
                elif key not in [None, ord("s"), ord("S")]:
                    # Just display all text
                    screen.print_at(line[current_x - x :], current_x, current_y)
                    screen.refresh()
                    break
    else:
        for i, line in enumerate(text.splitlines()):
            sound_check.clicking_sound()
            current_x = (screen.width - len(line)) // 2
            current_y = y + i

            for charac in line:
                screen.print_at(charac, current_x, current_y)
                screen.refresh()
                current_x += 1
                time.sleep(delay)

                # Skip whole cutscene by pressing S, Skip the typewrite animation by pressing any other key
                key = screen.get_key()
                if key in [ord("s"), ord("S")]:
                    sound_check.clicking_sound(stop=True)
                    return True
                elif key not in [None, ord("s"), ord("S")]:
                    # Just display all text
                    screen.print_at(
                        line[current_x - (screen.width - len(line)) // 2 :],
                        current_x,
                        current_y,
                    )
                    screen.refresh()
                    break
        sound_check.clicking_sound(stop=True)

    return False


# ===== [ ANIMATION FUNCTIONS ] =====


def animate_rocket_up(
    screen: Screen,
    rocket: str,
    initial_col: int,
    initial_row: int,
    num_frames: int,
) -> None:
    """
    Animate a rocket ASCII art going upwards.

    Args:
        screen (Screen): The asciimatics Screen object
        rocket (str): The ASCII art to display
        initial_col (int): Starting column of the top left text
        initial_row (int): Starting row of the top left text
        num_frame (int): Number of frames the rocket will animate
    """

    rocket_list = rocket.split("\n")
    tmp_row = initial_row
    sound_check.emergency(config.take_off, False)
    for _ in range(num_frames):
        # Skipping Mechanics
        key = screen.get_key()
        # Skip the whole cutscene
        if key in [ord("S"), ord("s")]:
            sound_check.emergency(config.take_off, True)
            return
        # Skip the animation
        if key not in [None, ord("S"), ord("s")]:
            break

        for r in rocket_list:
            screen.print_at(
                text=r,
                x=initial_col,
                y=tmp_row,
            )
            tmp_row += 1
        screen.refresh()
        time.sleep(1 / 10)
        # clear previous rocket frame
        for r in rocket_list:
            screen.print_at(" " * len(r), initial_col, tmp_row - len(rocket_list))
            tmp_row += 1
        tmp_row = initial_row
        initial_row -= 1
    screen.clear()


def animate_rocket_to_earth(
    screen: Screen,
    solar_system: str,
    initial_col: int,
    initial_row: int,
) -> None:
    """
    Animate rocket emoji going to earth

    Args:
        screen (Screen): The asciimatics Screen object
        solar_system (str): The ASCII art to display
        initial_col (int): Starting column of the top left text
        initial_row (int): Starting row of the top left text
    """

    system_lst = solar_system.split("\n")
    tmp_row = initial_row
    for r in system_lst:
        screen.print_at(text=r, x=initial_col, y=tmp_row)
        tmp_row += 1
    screen.refresh()

    # Rocket going to Earth
    for i in range(10)[::-1]:
        # Skipping Mechanics
        key = screen.get_key()
        # Skip the whole cutscene
        if key in [ord("S"), ord("s")]:
            sound_check.emergency(config.take_off, True)
            return
        # Skip the animation
        if key not in [None, ord("S"), ord("s")]:
            break

        screen.print_at(text="🚀", x=initial_col, y=initial_row + 1 + i)
        screen.print_at(text=" ", x=initial_col, y=initial_row + 2 + i)
        screen.refresh()
        time.sleep(0.5)
    sound_check.emergency(config.take_off, True)


def animate_malfunction(
    screen: Screen,
    broken_bulb: str,
    initial_col: int,
    initial_row: int,
) -> None:
    """
    Animate malfunction going to earth

    Args:
        screen (Screen): The asciimatics Screen object
    """

    width, height = screen.width, screen.height
    emojis = ["🟥", "❌", "💫", "💥", "❗", "⚠", "🔴"]
    sound_check.emergency(config.wee_woo, False)
    start = time.time()
    while time.time() - start < 7:
        # Skipping Mechanics
        key = screen.get_key()
        # Skip the whole cutscene
        if key in [ord("S"), ord("s")]:
            sound_check.emergency(config.wee_woo, True)
            return
        # Skip the animation
        if key not in [None, ord("S"), ord("s")]:
            break

        chosen = random.choice(emojis)
        col = random.randint(0, width - 2)
        row = random.randint(0, height - 2)

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(chosen, x=col, y=row)
        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        title = FigletText("MEMORY CORE", font="cybermedium")
        title2 = FigletText("BROKEN", font="cybermedium")

        y2 = 0
        for y, line in enumerate(str(title).splitlines(), start=15):
            screen.print_at(line, (screen.width - title.max_width) // 2, y, colour=1)
            y2 += 1

        for y, line in enumerate(str(title2).splitlines(), start=15):
            screen.print_at(line, (screen.width - title2.max_width) // 2, y + y2, colour=1)

        broken_bulb_list = broken_bulb.split("\n")
        row_add = 0
        for r, row in enumerate(broken_bulb_list):
            for c, chrac in enumerate(row):
                screen.print_at(text=chrac, x=initial_col + c, y=initial_row + int(row_add), colour = 1)
            row_add += 1

        screen.refresh()

        screen.refresh()
        time.sleep(1 / 100)
    screen.clear()
    screen.refresh()
    sound_check.emergency(config.wee_woo, True)


def animate_rocket_drop(
    screen: Screen,
    rocket: str,
    initial_col: int,
    initial_row: int,
    num_frames: int,
) -> None:
    """
    Animate rocket emoji going down.

    Args:
        screen (Screen): The asciimatics Screen object
        rocket (str): The ASCII art to display
        initial_col (int): Starting column of the top left text
        initial_row (int): Starting row of the top left text
        num_frame (int): Number of frames the rocket will animate
    """

    rocket_list = rocket.split("\n")[::-1]
    tmp_row = initial_row
    for _ in range(num_frames):
        # Skipping Mechanics
        key = screen.get_key()
        # Skip the whole cutscene
        if key in [ord("S"), ord("s")]:
            return
        # Skip the animation
        if key not in [None, ord("S"), ord("s")]:
            break

        for r in rocket_list:
            screen.print_at(r, initial_col, tmp_row)
            tmp_row += 1
        screen.refresh()
        time.sleep(1 / 10)
        # clear previous rocket frame
        for r in rocket_list:
            screen.print_at("  " * len(r), initial_col, tmp_row - len(rocket_list))
            tmp_row += 1
        tmp_row = initial_row
        initial_row += 1
    time.sleep(3)
    screen.clear()


def animate_jeep(
    screen: Screen, jeep_art: str, col: int, row: int, frames: int
) -> bool:
    """
    Animate a jeep animation.

    Args:
        screen (Screen): Class that will be implemented in the terminal
        jeep_art (str): ASCII art to be displayed
        col (int): Initial top left column of the jeep
        row (int): Initial top left row of the jeep
        frames (int): Number of frames the jeep will propagate

    Returns:
        bool: True if user wants to skip the whole cutscene, False if user wants to continue

    """

    jeep_lines = jeep_art.split("\n")
    for _ in range(frames):
        # Skipping Mechanics
        key = screen.get_key()
        # Skip the whole cutscene
        if key in [ord("S"), ord("s")]:
            return
        # Skip the animation
        if key not in [None, ord("S"), ord("s")]:
            break

        # Draw jeep
        for i, line in enumerate(jeep_lines):
            screen.print_at(line, col, row + i)
        screen.refresh()
        time.sleep(0.05)

        # Clear previous frame
        for i, line in enumerate(jeep_lines):
            screen.print_at(" " * len(line), col, row + i)
        col += 2
    return False

def animate_jeep_pro_max(
    screen: Screen, jeep_art: str, frames: int
) -> bool:
    """
    Animate a jeep animation.

    Args:
        screen (Screen): Class that will be implemented in the terminal
        jeep_art (str): ASCII art to be displayed
        frames (int): Number of frames the jeep will propagate

    Returns:
        bool: True if user wants to skip the whole cutscene, False if user wants to continue

    """
    height, width = screen.height, screen.width


    for _ in range(3):


        jeep_lines = jeep_art.splitlines()
        jeep_lines1 = jeep_art.splitlines()[::-1]

        row = random.randint(len(jeep_lines), height - len(jeep_lines))
        col = 0

        row1 = random.randint(len(jeep_lines), height - len(jeep_lines))
        col1 = screen.width - 71

        sound_check.jeep_sound(False)

        for _ in range(frames):
            # Skipping Mechanics
            key = screen.get_key()
            # Skip the whole cutscene
            if key in [ord("S"), ord("s")]:
                sound_check.jeep_sound(True)
                return
            # Skip the animation
            if key not in [None, ord("S"), ord("s")]:
                break

            # Draw jeep
            for i, line in enumerate(jeep_lines):
                screen.print_at(line, col, row + i)
                screen.print_at(" ", col - 1, row + i)


            
            # Draw jeep
            for i, line in enumerate(jeep_lines1):
                screen.print_at(line[::-1], col1, row1 - i)
                screen.print_at(" ", col1 + len(line) + 1, row1 - i)

            col += 1
            col1 -= 1
            screen.refresh()
            time.sleep(0.01)
        
        sound_check.jeep_sound(True)

            
        


def animate_upd(
    screen: Screen,
    upd: str,
    initial_col: int,
    initial_row: int,
) -> None:
    """
    Display upd logo.

    Args:
        screen (Screen): The asciimatics Screen object
        upd (str): The ASCII art to display
        initial_col (int): Starting column of the top left text
        initial_row (int): Starting row of the top left text
    """

    upd_lst = upd.split("\n")
    row_add = 0
    for r, row in enumerate(upd_lst):
        for c, chrac in enumerate(row):
            if r % 2 != 0:  # to remove stretching
                screen.print_at(
                    text=chrac, x=initial_col + c, y=initial_row + int(row_add)
                )
        row_add += 0.5
    screen.refresh()
    time.sleep(3)


def animate_upd_map(
    screen: Screen,
    upd: str,
    initial_col: int,
    initial_row: int,
) -> None:
    """
    Display upd map.

    Args:
        screen (Screen): The asciimatics Screen object
        upd (str): The ASCII art to display
        initial_col (int): Starting column of the top left text
        initial_row (int): Starting row of the top left text
    """

    upd_lst = upd.split("\n")
    row_add = 0
    for r, row in enumerate(upd_lst):
        for c, chrac in enumerate(row):
            screen.print_at(text=chrac, x=initial_col + c, y=initial_row + int(row_add))
        row_add += 1
    screen.refresh()
    time.sleep(3)


def loading_screen(screen: Screen, frames: int, stage_num: int) -> None:
    initial_col = 1
    initial_row = screen.height * 3 // 4
    ind = 0
    num_ind = 0

    stages = [
        num_1,
        num_2,
        num_3,
        num_4,
        num_5,
        num_6,
        num_7,
        num_8,
        num_9,
        num_10,
        num_11,
        num_12,
        num_13,
        num_14,
        num_15,
        num_16,
        num_17,
        num_18,
        num_19,
        num_20
    ]

    sound_check.jeep_sound(stop=False)

    for _ in range(frames):
        tmp_row = initial_row
        key = screen.get_key()

        if key in {ord("s"), ord("S")}:
            sound_check.jeep_sound(stop=True)
            return True
        elif key is not None:
            sound_check.jeep_sound(stop=True)
            return

        for line in jeep.splitlines():
            screen.print_at(line, initial_col, tmp_row)
            screen.print_at(" ", initial_col - 1, tmp_row)
            tmp_row += 1
        for i, line in enumerate(stage.splitlines()):
            if ind >= len(line):
                break
            else:
                screen.print_at(
                    line[ind],
                    (screen.width - len(line)) // 2 + ind,
                    (screen.height - len(stage.splitlines())) // 3 + i,
                )
        for i, line in enumerate(stages[stage_num - 1].splitlines()):
            if ind < len(stage.splitlines()[0]):
                break
            elif num_ind >= len(line):
                break
            else:
                screen.print_at(
                    line[num_ind],
                    (screen.width - len(stage.splitlines()[0])) // 2
                    + len(stage.splitlines()[0])
                    + num_ind
                    + 2,
                    (screen.height - len(stage.splitlines())) // 3 + i,
                )
        num_ind += 1 if ind >= len(stage.splitlines()[0]) else 0
        screen.refresh()

        initial_col += 1
        ind += 1
        time.sleep(0.02)
    sound_check.jeep_sound(stop=True)

def animate_restored(
    screen: Screen,
    bulb: str,
    initial_col: int,
    initial_row: int,
) -> None:
    """
    Animate restored memory

    Args:
        screen (Screen): The asciimatics Screen object
    """

    width, height = screen.width, screen.height
    emojis = ["🌟","⭐","🤩","✨"]
    start = time.time()
    while time.time() - start < 5:
        # Skipping Mechanics
        key = screen.get_key()
        # Skip the whole cutscene
        if key in [ord("S"), ord("s")]:
            return True
        # Skip the animation
        if key not in [None, ord("S"), ord("s")]:
            break

        chosen = random.choice(emojis)
        col = random.randint(0, width - 2)
        row = random.randint(0, height - 2)

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(chosen, x=col, y=row)
        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        title = FigletText("MEMORY CORE", font="cybermedium")
        title2 = FigletText("RESTORED", font="cybermedium")

        y2 = 0
        for y, line in enumerate(str(title).splitlines(), start=15):
            screen.print_at(line, (screen.width - title.max_width) // 2, y, colour=3)
            y2 += 1

        for y, line in enumerate(str(title2).splitlines(), start=15):
            screen.print_at(line, (screen.width - title2.max_width) // 2, y + y2, colour=3)

        bulb_list = bulb.split("\n")
        row_add = 0
        for r, row in enumerate(bulb_list):
            for c, chrac in enumerate(row):
                screen.print_at(text=chrac, x=initial_col + c, y=initial_row + int(row_add), colour = 3)
            row_add += 1

        screen.refresh()

        screen.refresh()
        time.sleep(1 / 100)
    screen.clear()
    screen.refresh()
    return False

def animate_attributes(
    screen: Screen,
) -> None:
    """
    Animate attributes text

    Args:
        screen (Screen): The asciimatics Screen object
    """
    
    width, height = screen.width, screen.height
    start = time.time()
    while time.time() - start < 5:
        # Skipping Mechanics
        key = screen.get_key()
        # Skip the whole cutscene
        if key in [ord("S"), ord("s")]:
            return True
        # Skip the animation
        if key not in [None, ord("S"), ord("s")]:
            break

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."
        screen.print_at(text = skip_m, x = (screen.width - len(skip_m)) // 2, y = screen.height - 2)
        

        title = FigletText("Persistence, Failure,", font="cybermedium")
        title2 = FigletText("and Resilience", font="cybermedium")

        y2 = 0
        for y, line in enumerate(str(title).splitlines(), start=15):
            screen.print_at(line, (screen.width - title.max_width) // 2, y, colour=3)
            y2 += 1

        for y, line in enumerate(str(title2).splitlines(), start=15):
            screen.print_at(line, (screen.width - title2.max_width) // 2, y + y2, colour=3)

        screen.refresh()

        screen.refresh()
        time.sleep(1 / 100)
    screen.clear()
    screen.refresh()
    return False
    sound_check.jeep_sound(stop=True)

    skip_interval(screen, 1)


# ===== [ CUTSCENE FUNCTIONS ] =====


def intro_cutscene() -> None:
    """
    Execute introductory cutscene in Screen.wrapper()

    Returns:
    bool: True if user wants to skip the whole cutscene, False if user wants to continue
    """

    def run(screen: Screen):
        """
        Run the intro cutscene scenes inside a Screen Object

        Args:
        screen (Screen): The asciimatics Screen object.

        Returns:
        bool: True if user wants to skip the whole cutscene, False if user wants to continue
        """
        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        # Scene 0 - - - - - - - - - - - - - - - - - - - - -
        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_0 = translate(
            f"📱 Incoming Transmission...\n                         \n'Congratulations, Cadet {config.current_user}.\nYou passed the Universal Placement and Cosmic Aptitude Test — the UPCAT!'",
            f"📱 受信中の通信...\n                         \n「おめでとう、訓練生{config.current_user}。\nユニバーサル配置・宇宙適性試験、通称UPCATに合格した！」",
            f"📱 Paparating na transmisyon...\n                         \n'Binabati kita, Kadete {config.current_user}.\nNakapasa ka sa Universal Placement at Cosmic Aptitude Test — o mas kilala bilang UPCAT!'",
            config.chosen_lang,
        )
        if typewrite_print_at(screen, script_0, 5, 5, 0.03):
            return
        screen.refresh()

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 1 - - - - - - - - - - - - - - - - - - - - -
        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_1 = translate(
            f"Destination: Planet Earth — Sector 'UP Diliman'\n                    \nMission: Observe human academic behavior.\n                    \nDuration: Unknown.",
            f"目的地：地球 — セクター『UPディリマン』\n                    \n任務：人間の学問的行動を観察せよ。\n                    \n期間：不明。",
            f"Destinasyon: Planet Earth — Sektor 'UP Diliman'\n                    \nMisyon: Obserbahan ang asal-akademiko ng mga tao.\n                    \nTagal: Hindi matukoy.",
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_1,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 2 - - - - - - - - - - - - - - - - - - - - -
        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_2 = translate(
            f"Preparing launch sequence...\n                    \n3...\n                    \n2...\n                    \n1...\n                    \nLIFTOFF! 🚀",
            f"発射シーケンス準備中...\n                    \n3...\n                    \n2...\n                    \n1...\n                    \n発射！🚀",
            f"Ihahanda ang paglulunsad...\n                    \n3...\n                    \n2...\n                    \n1...\n                    \nLIPAD! 🚀",
            config.chosen_lang,
        )
        script_2_1 = translate(
            "                            \n                    \n    \n                    \n    \n                    \n    \n                    \n          ",
            "                                   \n                    \n                                   \n                    \n                                   \n                    \n                                   \n                    \n                                   ",
            "                                   \n                    \n                                   \n                    \n                                   \n                    \n                                   \n                    \n                                   ",
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_2,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        time.sleep(1)
        typewrite_print_at(
            screen,
            script_2_1,
            5,
            5,
            0,
        )
        screen.refresh

        animate_rocket_up(
            screen=screen,
            rocket=large_rocket,
            initial_col=(screen.width - 30) // 2,
            initial_row=15,
            num_frames=50,
        )

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 3 - - - - - - - - - - - - - - - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_3 = translate(
            f'Trajectory stable.\nDestination locked: "Sunken Garden"\nAtmosphere entry imminent.',
            f"軌道安定。\n目的地ロック：『サンケン・ガーデン』\n大気圏突入、まもなく。",
            f'Matatag ang trajectory.\nNakakandado ang destinasyon: "Sunken Garden"\nPapasok na sa atmospera.',
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_3,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        animate_rocket_to_earth(
            screen=screen,
            solar_system=solar_system,
            initial_col=(screen.width - 33) // 2,
            initial_row=(screen.height - len(solar_system.splitlines())) // 2,
        )

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 4 - - - - - - - - - - - - - - - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_4 = translate(
            f"⚠️ Warning: System malfunction detected!\nMemory Core destabilizing...\nNavigation error — coordinates looping!\nLooping...\nLooping...\nLooping...",
            f"⚠️ 警告：システム異常検出！\nメモリーコア不安定化中...\nナビゲーションエラー — 座標ループ中！\nループ...\nループ...\nループ...",
            f"⚠️ Babala: May aberya sa sistema!\nNasisira ang Memory Core...\nError sa nabigasyon — paikot-ikot ang mga koordinado!\nUlit...\nUlit...\nUlit...",
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_4,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        animate_malfunction(screen=screen, broken_bulb = broken_bulb, initial_col = (screen.width - 13)//2, initial_row= screen.height - 20)

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 5 - - - - - - - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_5 = translate(
            f"💥 Impact detected near Sunken Garden.\nBrain Core corrupted.\nMission route looping endlessly.\n📡 Connection lost.",
            f"💥 サンケン・ガーデン付近で衝突を検出。\nブレインコア破損。\n任務ルート、無限ループ中。\n📡 通信途絶。",
            f"💥 Naitala ang pagbangga malapit sa Sunken Garden.\nSira ang Brain Core.\nWalang tigil ang pag-ulit ng ruta.\n📡 Nawalan ng koneksyon.",
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_5,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 6 - - - - - - - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_6 = translate(
            f"*BEEP!* *HONK!* *IKOT! IKOT!*",
            f"＊ビーッ！＊ホーン！＊イクット！イクット！＊",
            f"*BEEP!* *HONK!* *IKOT! IKOT!*",
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_6,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        animate_jeep(
            screen=screen,
            jeep_art=jeep,
            col=0,
            row=(screen.height - len(jeep.splitlines())) // 2,
            frames=screen.width,
        )

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 7 - - - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)

        animate_upd(
            screen=screen,
            upd=oble,
            initial_col=(screen.width - 50) // 2,
            initial_row=screen.height - 31,
        )
        script_7 = translate(
            f'🧑 CHARACTER PROFILE\n\nName: {config.current_user}\nCodename: "Isko" (from Iskorion)\nMission: Study human persistence under repetitive academic stress\nGoal: Recover the Mushrooms of Memory to restore his Brain Core',
            f"🧑 キャラクタープロフィール\n\n名前：{config.current_user}\nコードネーム：「イスコ」（イスコリオン由来）\n任務：人間の学業的ストレス下での粘り強さを研究せよ\n目標：メモリーマッシュルームを回収し、ブレインコアを修復せよ",
            f'🧑 PROFILE NG KARAKTER\n\nPangalan: {config.current_user}\nCodename: "Isko" (mula sa Iskorion)\nMisyon: Pag-aralan ang tiyaga ng tao sa paulit-ulit na akademikong stress\nLayunin: Kolektahin ang Mushrooms of Memory para maibalik ang Brain Core',
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_7,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 8 - - - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_8 = translate(
            f"{config.current_user} blinks.\nThe air smells like isaw.\nHe sees a sign: *Welcome to UP Diliman.*",
            f"{config.current_user}が瞬きをする。\n空気はイサウの香り。\n看板にはこう書かれている：『UPディリマンへようこそ』。",
            f"Pumikit-dilat si {config.current_user}.\nAmoy isaw ang hangin.\nMay nakitang karatula: *Welcome to UP Diliman.*",
            config.chosen_lang,
        )
        if typewrite_print_at(
            screen,
            script_8,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        animate_upd(
            screen=screen,
            upd=upd,
            initial_col=((screen.width - 60) // 2),
            initial_row=screen.height - 32,
        )

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 9 - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_9 = translate(
            f'But the roads shift endlessly.\nThe UP Ikot jeep circles on repeat.\nAnd the world resets every turn.\n\n"Guess I\'m stuck in a loop… again."',
            f"だが道は終わりなくねじれ、\nUPイコット・ジープは永遠に回り続ける。\n世界は曲がるたびにリセットされる。\n\n「またループに閉じ込められたか…」",
            f'Pero paikot-ikot ang mga daan.\nUmiikot nang walang tigil ang UP Ikot jeep.\nAt muling nagre-reset ang mundo sa bawat liko.\n\n"Mukhang na-trap na naman ako sa loop…"',
            config.chosen_lang,
        )

        if typewrite_print_at(
            screen,
            script_9,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        animate_upd_map(
            screen=screen,
            upd=upd_map,
            initial_col=(screen.width - 51) // 2,
            initial_row=(screen.height - len(upd_map.splitlines()) + 5) // 2,
        )

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


# ==== [STAGES CUTSCENES] ====


def aech_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 1)
        screen.clear()

        time.sleep(0.5)

        introduction = "🏛️  AECH 🏛️"
        message = translate(
            "Where HOPES make you hopeless.\nTutorial stage. Learn how to move, push rocks, and start raiding mushrooms.\nObjective: Collect all 🍄 Mushrooms of Memory to restore your Brain Core.",
            "希望(HOPES)が絶望を生む場所。\nチュートリアルステージ。移動・岩押し・マッシュルーム収集を学べ。\n目的 ：すべての🍄メモリーマッシュルームを集め、ブレインコアを修復せよ。",
            "Kung saan ginagawang hopeless ang HOPES.\nTutorial stage. Matutong gumalaw, magtulak ng bato, at magsimulang mang-raid ng mushrooms.\nLayunin: Kolektahin lahat ng 🍄 para maibalik ang Brain Core.",
            config.chosen_lang,
        )
        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )
        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        skip_interval(screen, 5)

    Screen.wrapper(run)


def aech_end() -> None:
    def run(screen: Screen) -> None:
        screen.clear()

        introduction = "CONGRATULATONS"
        message = translate(
            "✅ Brain Core fragment secured.\n 🛰️ Route recalibrating...\nNext location: [Stage Name].",
            "✅ ブレインコア断片確保。\n 🛰️ ルート再計算中...\n次の地点:[ステージ名]。",
            "✅ Nakuhang muli ang piraso ng Brain Core.\n🛰️ Nire-recalibrate ang ruta...\nSusunod na lokasyon: [Stage Name].",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        typewrite_print_at(screen, message, 0, screen.height // 4 + 3)

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key is not None:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def eee_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 2)
        screen.clear()

        introduction = "⚡ EEEI ⚡"
        message = translate(
            "⚡ EEEI — Wired, tired, inspired.\nReroute the circuit paths. Keep your mind grounded.\nObjective: Collect all 🍄 while avoiding overload.",
            "⚡ EEEI — 電線だらけ、疲労だらけ、そしてひらめきだらけ。\n回路を再配線しろ。心をショートさせるな。\n目的：オーバーロードを避けつつ、すべての🍄を集めよ。",
            "⚡ EEEI — Wired, tired, inspired.\nAyusin ang mga circuit.\nLayunin: Kolektahin lahat ng 🍄 habang iniiwasan ang overload.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key is not None:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def msi_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 3)
        screen.clear()

        introduction = "🌊  MSI 🌊"
        message = translate(
            "Flooded with deadlines.\nUse rocks to bridge waters. Don’t test if your GPA floats.\nObjective: Build paths and collect all 🍄 safely.",
            "締切の洪水。\n岩で水を渡れ。GPAが浮くかは試すな。\n目的：安全に道を作り、すべての🍄を集めよ。",
            "Nilunod ng mga deadline.\nGamitin ang mga bato para tumawid. Huwag subukang palutangin ang GPA.\nLayunin: Gumawa ng daan at kolektahin lahat ng 🍄.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def palma_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 4)
        screen.clear()

        introduction = "🏫  Palma Hall 🏫"
        message = translate(
            "The Orientation.\nForests of trees. Professors everywhere.\nObjective: Burn or chop trees to clear your path.",
            "オリエンテーション。\n木々の森、教授だらけ。\n目的：木を燃やすか切って道を開け。",
            "Ang Orientation.\nPuno ng puno at propesor ang paligid.\nLayunin: Sunugin o putulin ang mga puno para makadaan.",
            config.chosen_lang,
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def dorms_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 5)
        screen.clear()

        introduction = "🌸  Kamia & Sampaguita 🌸"
        message = translate(
            "Where sleepless nights bloom.\nThe hallways twist like your circadian rhythm.\nObjective: Rest when you can, move when you must.",
            "不眠の夜が咲く場所。\n廊下は体内時計のようにねじれる。\n目的：休めるときに休み、動けるときに動け。",
            "Dito sumisibol ang mga gabing walang tulog.\nAng mga pasilyo’y paikot tulad ng orasan ng katawan.\nLayunin: Magpahinga kung kailan pwede, kumilos kung kinakailangan.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def upis_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 6)
        screen.clear()

        introduction = "🏫  UPIS 🏫"
        message = translate(
            "Smaller humans, bigger energy.\nDon’t get distracted by chaos. Stay on task, Isko.\nObjective: Collect all 🍄 and exit before recess.",
            "小さな人間、大きなエネルギー。\n混乱に惑わされるな、イスコ。\n目的：休み時間前にすべての🍄を集め、脱出せよ。",
            "Mas maliliit na tao, mas matataas na enerhiya.\nHuwag magpadala sa gulo. Mag-focus, Isko.\nLayunin: Kolektahin lahat ng 🍄 bago mag-recess.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def sunken_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 7)
        screen.clear()

        introduction = "🌿  Sunken Garden 🌿"
        message = translate(
            "The jungle of the loop.\nIt’s overgrown... and dangerous.\n💀 Warning: Hostile organism detected.\n🦂 Specimen: Scorpius Dilimanus\nStatus: Stationary, venomous.\n{config.current_user}: “So this planet fights back now?”\n> New hazard unlocked: Scorpion Block\nAvoid contact or the loop resets.\nObjective: Collect all 🍄 without touching the 🦂.",
            "サンケン・ガーデン — ループの密林。\n生い茂り…危険な場所。\n💀 警告：敵性生命体を検出。\n🦂 種：スコルピウス・ディリマナス\n状態：静止・毒性あり。\n{config.current_user}：「この惑星、今度は反撃か？」\n＞ 新たな危険：スコーピオンブロック\n触れるとループがリセットされる。\n目的：🦂に触れずにすべての🍄を集めよ。",
            "Ang gubat ng loop.\nMasukal… at delikado.\n💀 Babala: May nakitaang kalabang organismo.\n🦂 Espesimen: Scorpius Dilimanus\nKatayuan: Hindi gumagalaw, may lason.\n{config.current_user}: “So lumalaban na rin ang planetang ‘to?”\n> Bagong hazard: Scorpion Block\nIwasang mahawakan o mauulit ang loop.\nLayunin: Kolektahin lahat ng 🍄 nang hindi nahahawakan ang 🦂.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def econ_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 8)
        screen.clear()

        introduction = "📈  Econ 📈"
        message = translate(
            "Where demand is high, and supply is sleep.\nRocks are assets. Mushrooms are currency.\nObjective: Invest wisely. Collect every 🍄.",
            "需要は高く、供給は睡眠。\n岩は資産、マッシュルームは通貨。\n目的：賢く投資し、すべての🍄を集めよ。",
            "Mataas ang demand, kulang ang tulog.\nYaman ang bato. Pera ang 🍄.\nLayunin: Maging matalino sa galaw, kolektahin lahat ng 🍄.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def econ_end() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 8)
        screen.clear()
        message = translate(
            "📡 Fragment Recovered:\n“Report: Humans perform repetitive labor under pressure.”\n“Hypothesis: Persistence is built, not born.”",
            "📡 断片回収：\n「報告：人間はプレッシャー下で反復労働を行う。」\n「仮説：粘り強さは生まれつきではなく、培われるものだ。」",
            "📡 Fragmentong Narekober:\n“Ulat: Ang mga tao’y paulit-ulit sa trabaho sa ilalim ng pressure.”\n“Hipotesis: Ang tiyaga ay hinuhubog, hindi ipinapanganak.”",
            config.chosen_lang,
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def iirh_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 9)
        screen.clear()

        introduction = "🌺  Ilang-Ilang RH 🌺"
        message = translate(
            "Where gossip echoes louder than lectures.\nEvery wrong turn loops you back.\nObjective: Trace the right path, and collect every 🍄.",
            "噂が講義より響く場所。\n誤った道はすべてループに戻る。\n目的：正しい道を見つけ、すべての🍄を集めよ。",
            "Kung saan mas malakas ang tsismis kaysa leksyon.\nBawat maling liko, balik simula.\nLayunin: Hanapin ang tamang daan at kolektahin lahat ng 🍄.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def uhs_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 10)
        screen.clear()

        introduction = "🏥  UHS 🏥"
        message = translate(
            "Finally, health care... for free?\nYou’ll need it.\nObjective: Keep your balance, avoid traps, and collect all 🍄.",
            "ついに医療が無料に？\nすぐ必要になるぞ。\n目的：バランスを保ち、罠を避け、すべての🍄を集めよ。",
            "Sa wakas, libreng health care?\nKakailanganin mo ‘yan.\nLayunin: Panatilihin ang balanse, iwasan ang patibong, at kolektahin lahat ng 🍄.",
            config.chosen_lang,
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def acacia_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 11)
        screen.clear()

        introduction = "🌙  Acacia Dorm 🌙"
        message = translate(
            "Darkness level: Thesis week.\nVision low. Hope lower.\nObjective: Find all 🍄 in the dark corridors.",
            "暗さレベル：卒論週。\n視界ゼロ、希望ゼロ。\n目的：暗闇の廊下で🍄をすべて見つけよ。",
            "Antas ng dilim: Thesis week.\nMahina ang paningin. Mas mahina ang pag-asa.\nLayunin: Hanapin lahat ng 🍄 sa madidilim na pasilyo.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def a2_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 12)
        screen.clear()

        introduction = "🍢  Area 2 🍢"
        message = translate(
            "Food, friends, and feral cats.\nSmells good. Sounds dangerous.\nObjective: Collect every 🍄 while navigating tight streets.",
            "食、友情、野良猫。\n良い匂い、危険な音。\n目的：狭い路地を進みながらすべての🍄を集めよ。",
            "Pagkain, barkada, at mga pusang gala.\nMabango pero delikado.\nLayunin: Kolektahin lahat ng 🍄 habang umiikot sa masisikip na kalsada.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def melchor_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 13)
        screen.clear()

        introduction = "🧮  Melchor Hall 🧮"
        message = translate(
            "Where logic meets madness.\nEverything’s mechanical. Nothing makes sense.\nObjective: Solve the patterns and collect every 🍄.",
            "論理と狂気の交差点。\nすべてが機械的、何も意味をなさない。\n目的：パターンを解き、すべての🍄を集めよ。",
            "Kung saan nagtatagpo ang lohika at kabaliwan.\nLahat mekanikal. Wala nang may saysay.\nLayunin: Lutasin ang mga pattern at kolektahin lahat ng 🍄.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def melchor_end() -> None:
    def run(screen: Screen) -> None:
        screen.clear()
        message = translate(
            "📡 Fragment Recovered:\n“Observation nearing completion.”\n“Loop behavior: predictable, yet stubbornly hopeful.”",
            "📡 断片回収：\n「観察、完了に近づく。」\n「ループ行動：予測可能だが、しつこく希望を持つ。」",
            "📡 Fragmentong Narekober:\n“Malapit nang matapos ang obserbasyon.”\n“Gawi ng loop: paulit-ulit, ngunit matigas sa pag-asa.”",
            config.chosen_lang,
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def alumni_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 14)
        screen.clear()

        introduction = "🏠  Bahay ng Alumni 🏠"
        message = translate(
            "Home of Room TBA.\nEvery exit says ‘To Be Announced.’\nObjective: Find all 🍄 before the map confuses itself.",
            "ルームTBAの本拠地。\nすべての出口に『発表予定』と書かれている。\n目的：マップが自滅する前に🍄をすべて見つけよ。",
            "Bahay ng Room TBA.\nLahat ng labasan, ‘To Be Announced.’\nLayunin: Kolektahin lahat ng 🍄 bago malito ang mapa.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def chk_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 15)
        screen.clear()

        introduction = "🏃  CHK 🏃"
        message = translate(
            "Where PE dreams end.\nYou’ll slide more than you’ll move.\nObjective: Control your steps and get every 🍄.",
            "体育の夢が終わる場所。\n動くより滑る。\n目的：足元を制御し、すべての🍄を手に入れよ。",
            "Dito nagtatapos ang mga pangarap sa PE.\nMas madulas kaysa lakad.\nLayunin: Kontrolin ang bawat hakbang at kunin lahat ng 🍄.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def solair_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 16)
        screen.clear()

        introduction = "🗣️  SOLAIR 🗣️"
        message = translate(
            "Where debates never end.\nWalls argue back. Floors disagree.\nObjective: Stay focused and collect all 🍄.",
            "議論が終わらぬ場所。\n壁は反論し、床は意見する。\n目的：集中を保ち、すべての🍄を集めよ。",
            "Dito walang katapusang debate.\nMaging ang pader, nakikipagtalo.\nLayunin: Manatiling kalmado at kolektahin lahat ng 🍄.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def oblation_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 17)
        screen.clear()

        introduction = "🗿  Oblation Plaza 🗿"
        message = translate(
            "The center of all orbits.\nIt feels... peaceful. Too peaceful.\nObjective: Gather every 🍄 and prepare for the final stretch.",
            "すべての軌道の中心。\n静かだ…静かすぎる。\n目的：🍄をすべて集め、最後の道に備えよ。",
            "Ang sentro ng lahat ng paikot.\nTahimik... masyadong tahimik.\nLayunin: Kolektahin lahat ng 🍄 at maghanda sa huling yugto.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def gyudfood_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 18)
        screen.clear()

        introduction = "🍔  Gyudfood 🍔"
        message = translate(
            "Mission refuel: sisig and soul.\nNo enemies here, just calories.\nObjective: Collect the 🍄 and take a breather.",
            "任務補給：シシグと魂。\n敵なし、カロリーのみ。\n目的：🍄を集め、一息つけ。",
            "Mission refill: sisig at kaluluwa.\nWalang kalaban dito, puro kain.\nLayunin: Kolektahin ang 🍄 at magpahinga sandali.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def hda_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 19)
        screen.clear()

        introduction = "🌹  HDA 🌹"
        message = translate(
            "Silence... but not peace.\nMemories linger here.\nObjective: Gather the last memory fragments. 🍄",
            "静寂…だが平穏ではない。\nここには記憶が残る。\n目的：最後の記憶断片🍄を集めよ。",
            "Tahimik... pero hindi payapa.\nMay mga alaala pa ring naiwan dito.\nLayunin: Kolektahin ang huling mga piraso ng alaala. 🍄",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)


def knl_intro() -> None:
    def run(screen: Screen) -> None:
        loading_screen(screen, 100, 20)
        screen.clear()

        introduction = "🌌  Krus na Ligas Park 🌌"
        message = translate(
            " it all comes full circle.\nEvery road you took leads back here.\nObjective: Collect the final 🍄 and end the loop.",
            "すべてが円を描く場所。\n歩んだ道はすべてここに戻る。\n目的：最後の🍄を集め、ループを終わらせよ。",
            "Kung saan nagbabalik ang lahat.\nLahat ng daan, patungo rito.\nLayunin: Kolektahin ang huling 🍄 at tapusin ang loop.",
            config.chosen_lang,
        )

        screen.print_at(
            introduction, (screen.width - len(introduction)) // 2, screen.height // 4
        )

        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 5)

        screen.refresh()

        if typewrite_print_at(screen, message, 0, screen.height // 4 + 3):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1.5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in {None, ord("s"), ord("S")}:
                break
            time.sleep(0.05)

    Screen.wrapper(run)

def end_cutscene():
    """
    Execute ending cutscene in Screen.wrapper()

    Returns:
    bool: True if user wants to skip the whole cutscene, False if user wants to continue
    """

    def run(screen: Screen):
        """
        Run the end cutscene scenes inside a Screen Object

        Args:
        screen (Screen): The asciimatics Screen object.

        Returns:
        bool: True if user wants to skip the whole cutscene, False if user wants to continue
        """
        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        # Scene 0 - - - - - - - - - - - - - - - - - - - - -

        screen.clear()

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_0 = translate("Brain Core fully restored.\n                              \nLoop collapsing...\n                              \nSignal reconnecting...\n                              \n", "ブレインコア完全修復。\n                              \nループ崩壊中…\n                              \n信号再接続中…\n                              \n", "Kumpleto na ang Brain Core.\n                              \nNawawasak na ang loop...\n                              \nMuling kumokonekta ang signal...\n                              \n", config.chosen_lang)
        if typewrite_print_at(
            screen,
            script_0,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        if animate_restored(screen=screen, bulb = bulb, initial_col = (screen.width - 13)//2, initial_row= screen.height - 20):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 5:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)
        

        # Scene 1 - - - - - - - - - - - - - - - - - - - - -

        screen.clear()
        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_1 = translate(f"📡 Transmission from Iskorion:\n\"Cadet {config.current_user} — codename: Isko.\nObservation complete.\nYou have witnessed persistence, failure, and resilience.\"", f"📡 イスコリオンからの通信：\n「訓練生{config.current_user} — コードネーム：イスコ。\n観察完了。\n粘り、失敗、そして回復力を目撃したな。」", f"📡 Mensahe mula sa Iskorion:\n\"Kadete {config.current_user} — codename: Isko.\nTapos na ang obserbasyon.\nNakita mo ang pagtitiyaga, kabiguan, at muling pagtindig.\"", config.chosen_lang)
        if typewrite_print_at(
            screen,
            script_1,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        if animate_attributes(screen = screen):
            return

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        
        # Scene 2 - - - - - - - - - - - - - - - - - - - - -

        screen.clear()
        skip_m = "Press [S] to skip the whole cutscene. Press any key to skip text animation."

        screen.print_at(skip_m, (screen.width - len(skip_m)) // 2, screen.height - 2)
        script_2 = translate(f"{config.current_user} looks around.\n                   \nThe Ikot jeep circles one last time.\n                   \n*BEEP!* *HONK!* \"IKOT! IKOT!\"\n                   \n{config.current_user} smiles.\n                   \n\"Mission complete. Loop survived.\"\n                   \n\n— END OF SHROOM RAIDER —\n                   \n", f"{config.current_user}は周囲を見回す。\n                   \nイコット・ジープが最後の一周をする。\n                   \n＊ビーッ！＊ホーン！＊イクット！イクット！＊\n                   \n{config.current_user}は微笑む。\n                   \n「任務完了。ループ、生還。」\n                   \n\n— SHROOM RAIDER 終了 —\n                   \n", f"Tumingin sa paligid si {config.current_user}.\n                   \nUmiikot ang jeep sa huling pagkakataon.\n                   \n*BEEP!* *HONK!* \"IKOT! IKOT!\"\n                   \nNgumiti siya.\n                   \n\"Mission complete. Nakaligtas sa loop.\"\n                   \n\n— WAKAS NG SHROOM RAIDER —\n                   \n", config.chosen_lang)
        if typewrite_print_at(
            screen,
            script_2,
            5,
            5,
            0.03,
        ):
            return
        screen.refresh()

        animate_jeep_pro_max(screen = screen, jeep_art = jeep, frames = screen.width)

        # Skip whole cutscene by pressing S, Skip to next scene by pressing any other key
        start = time.time()
        while time.time() - start < 1:
            skip_all, key = skip_cutscene(screen)
            if skip_all:
                return
            elif key not in [None, ord("s"), ord("S")]:
                break
            time.sleep(0.05)

        # Scene 3 - - - - - - - - - - - - - - - - - - - - -

        winner()
        

        

    Screen.wrapper(run)

     
def try_lang():
    def run(screen: Screen):
        animate_jeep_pro_max(screen = screen, jeep_art=jeep, frames = screen.width)

    Screen.wrapper(run)

