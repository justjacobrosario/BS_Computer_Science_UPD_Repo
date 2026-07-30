"""Initial file for Shroom Raider Core Basic Game.

This module handles the prompting in the terminal.
For interactive mode, type: python3 shroom_raider.py
For interactive mode with a specific stage to play on, type: python3 shroom_raider.py -f <stage file>
For simulation mode with a specific stage, sequence of moves, and output file,
type: python3 shroom_raider.py -f <stage file> -m <moves (e.g. WASDAS)> -o <output file>
"""

import argparse
import pathlib
import sys

from game import new_game, simulate_game
from map_reader import map_to_string


def main() -> None:
    """Run the function for the main game."""
    parser = argparse.ArgumentParser()

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

    args = parser.parse_args()

    # Determine stage file
    stage_file = args.file or "default_stage.txt"

    # Check whether file exists or not
    if not pathlib.Path(stage_file).exists():
        print(f"Error: Stage file '{stage_file}' not found!", file=sys.stderr)
        sys.exit(1)

    # If moves are provided, run simulation mode
    if args.moves:
        if not args.output:
            print("Error: -o/--output is required when using -m/--moves", file=sys.stderr)
            sys.exit(1)

        # Simulate the game
        new_map, is_cleared = simulate_game(args.moves, stage_file)

        # Write output to the output file
        status = "CLEAR" if is_cleared else "NO CLEAR"
        r = len(new_map)
        c = len(new_map[0])
        output_content = status + "\n" + f"{r} {c}" + "\n" + map_to_string(new_map)

        try:
            pathlib.Path(args.output).write_text(output_content, encoding="utf-8")
        except OSError as e:
            print(f"Error writing output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Interactive play mode if there is no moves provided
        new_game(stage_file)


if __name__ == "__main__":
    main()
