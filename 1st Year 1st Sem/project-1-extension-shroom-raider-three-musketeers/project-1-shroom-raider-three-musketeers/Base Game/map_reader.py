"""ASCII-Representation to UI-Representation Map Reader.

This module translates ascii-represented map into its ui display.
This module also defines functions that returns the player coordinates, and mushroom count.
"""

from config import TileType


def read_stage_file(filename: str) -> list[list[str]]:
    """Read stage file and return the map as a 2D list.

    Args:
        filename: The selected stage file

    Returns:
        A 2D list representing the game map

    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    # First line contains dimensions
    dimensions = lines[0].strip().split()
    rows = int(dimensions[0])
    cols = int(dimensions[1])

    # Read the map (skip first line with dimensions)
    game_map: list[list[str]] = []
    for i in range(1, rows + 1):
        if i < len(lines):
            row = list(lines[i].rstrip("\n"))
            # Pad or trim to correct column count
            if len(row) < cols:
                row.extend(["."] * (cols - len(row)))
            elif len(row) > cols:
                row = row[:cols]
            game_map.append(row)
        else:
            # If file has fewer lines than expected, add empty rows
            game_map.append(["."] * cols)

    return game_map


def find_player(maps: list[list[str]]) -> tuple[int, int] | None:
    """Find player coordinates.

    Args:
        maps: ASCII-representation of the map

    Returns:
        Player coordinates as (row, col) tuple, or None if not found

    """
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == TileType.PLAYER.value:
                return (i, j)
    return None


def count_mush(maps: list[list[str]]) -> int:
    """Count total mushrooms in the map.

    Args:
        maps: ASCII-representation of the map

    Returns:
        Total number of mushrooms

    """
    total_mush = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == TileType.MUSHROOM.value:
                total_mush += 1
    return total_mush


def count_mushrooms(maps: list[list[str]]) -> int:
    """Count total mushrooms in the map (alias for count_mush).

    Args:
        maps: ASCII-representation of the map

    Returns:
        Total number of mushrooms

    """
    return count_mush(maps)


def emojizer(lst: list[list[str]]) -> list[list[str]]:
    """Translate ASCII-representation into UI-representation of the map.

    Args:
        lst: List of ASCII-representation of map

    Returns:
        List of UI-representation of the map

    """
    return [row_emojizer_helper(row) for row in lst]


def row_emojizer_helper(row: list[str]) -> list[str]:
    """Translate ASCII-representation into UI-representation of the map for each row.

    Args:
        row: List of ASCII-representation of a row of map

    Returns:
        List of UI-representation of a row of the map

    """
    emojized_row: list[str] = []
    dic = {
        "L": "🧑",
        "T": "🌲",
        "+": "🍄",
        "R": "🪨",
        "_": "⬜",
        "~": "🟦",
        "x": "🪓",
        "*": "🔥",
        ".": "　",
    }
    for tile in row:
        if tile in dic:
            emojized_row.append(dic[tile])
        else:
            emojized_row.append("　")
    return emojized_row


def map_to_string(game_map: list[list[str]]) -> str:
    """Convert map to string format for output.

    Args:
        game_map: List type of the UI-representation of the map

    Returns:
        String representation of the game map

    """
    return "\n".join(["".join(row) for row in game_map])
