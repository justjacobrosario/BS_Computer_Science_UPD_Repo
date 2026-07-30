"""User Interface for the In-game part.

This module defines the functions used in the interface in-game that display the borders,
map, and texts.
"""

import os


def clear_screen() -> None:
    """Clear the whole terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mush_print(count: int) -> None:
    """Display the mushroom count in the terminal.

    Args:
        count: Number of mushrooms collected

    """
    print(f"Mushrooms collected: {count}")


def item_on_ground_print(item_on_ground_prompt: str) -> None:
    """Display the item on ground prompt within the terminal.

    Args:
        item_on_ground_prompt: Prompt message to display

    """
    if item_on_ground_prompt in {"No item to pick up", " "}:
        print("No item to pick up")
    else:
        print(f"[P] Pickup {item_on_ground_prompt}")


def inventory_print(held_item: str) -> None:
    """Display the item in inventory within the terminal .

    Args:
        held_item: The item that is currently held

    """
    def ascii_to_emoji(item: str) -> str:
        """Translate the ASCII text to emoji version of tools.

        Args:
            item: The character of the item

        Returns:
            Emoji representation of the item

        """
        dic = {"*": "🔥", "x": "🪓"}
        if item in dic:
            return dic[item]
        else:
            return " "

    print(f"Inventory: {ascii_to_emoji(held_item)}")


def ctrl_print() -> None:
    """Display the game controls."""
    print("\nControls:")
    print("[W] Walk Up    [A] Walk Left")
    print("[S] Walk Down  [D] Walk Right")
    print("[P] Pickup     [!] Reset")
    print("[Q] Quit")
