import argparse
import os
import sys
import game_modes


os.environ["TERM"] = "xterm-256color"


import pathlib

from game import new_game, setup_game, simulate_game
from map_reader import count_mush
from menu import main_menu

# ===== MAIN GAME =====


def main() -> None:
    """Run the function for the main game."""
    parser = argparse.ArgumentParser()  # initialize the argument parse

    parser.add_argument(
        "-m",
        "--moves",
        help="string of moves that the user will play",
    )
    parser.add_argument(
        "-f",
        "--file",
        help="stage file",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file after reading the string of moves",
    )
    parser.add_argument(
        "-p",
        "--play",
        help="teleports the player to the main game",
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--speedrun",
        help="make the user play only the speedrun mode of the game without signing in",
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--storymode",
        help="make the user play only the story mode of the game without signing in",
        action="store_true",
    )
    parser.add_argument(
        "-u",
        "--username",
        help="play with account already signed in if in database",
    )
    parser.add_argument(
        "-w",
        "--password",
        help="play with account already signed in if in database",
    )

    args: argparse.Namespace = parser.parse_args()

    if args.play:
        main_menu()
    elif args.speedrun or args.storymode:
        if args.speedrun and args.storymode:
            sys.exit(0)
        elif args.speedrun:
            game_modes.speedrun_mode()
        else:
            game_modes.story_mode()

    if args.file is not None:
        if args.moves == None or args.moves is None:
            new_game(stage_num=int(args.file))
        else:
            new_map = simulate_game(
                count_mush(setup_game(int(args.file))[0]),
                args.moves,
                stage_num=int(args.file),
            )
            is_cleared = "CLEARED" if new_map[1] else "NOT CLEARED"
            new_map = (
                is_cleared + "\n" + "\n".join(["".join(row) for row in new_map[0]])
            )
            pathlib.Path(args.output).write_text(new_map)


main()
