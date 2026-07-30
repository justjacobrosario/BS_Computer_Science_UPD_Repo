"""Configuration constants and enums that will going to be used in the game.

This module defines tile types, UI colors, and other game configurations.
"""

from enum import Enum


class TileType(Enum):
    """Different tile types in the game."""

    TREE = "T"
    PLAYER = "L"
    ROCK = "R"
    WATER = "~"
    MUSHROOM = "+"
    PAVED = "_"
    AXE = "x"
    FLAMETHROWER = "*"
    SPACE = "."


class UIColor(Enum):
    """In-game UI color constants."""

    LINE = 7  # White
    BACKGROUND = 0  # Black
    MAP_BACKGROUND = 0
    MAP_LINE = LINE


class GameState:
    """States that will be updated during in-game.

    States:
        current_map: list that represents the game map
        player_position: (row, col) tuple that tells the player location
        mushroom_count: Current number of mushrooms collected
        total_mushrooms: Total mushrooms in the map stage
        held_item: Currently held item (string " " if there is no held item)
        standing_on_item: The tile type that the player is standing
        paved_tiles: Dictionary tracking paved tile positions within the map stage
    """

    def __init__(
        self,
        current_map: list[list[str]],
        player_position: tuple[int, int],
        mushroom_count: int = 0,
        total_mushrooms: int = 0,
        held_item: str = " ",
        standing_on_item: str = ".",
    ) -> None:
        """Initialize GameState.

        Args:
            current_map: list that represents the game map
            player_position: (row, col) tuple that tells the player location
            mushroom_count: Current number of mushrooms collected
            total_mushrooms: Total mushrooms in the map stage
            held_item: Currently held item (string " " if there is no held item)
            standing_on_item: The tile type that the player is standing

        """
        self.current_map = current_map
        self.player_position = player_position
        self.mushroom_count = mushroom_count
        self.total_mushrooms = total_mushrooms
        self.held_item = held_item
        self.standing_on_item = standing_on_item
        self.paved_tiles: dict[tuple[int, int], None] = {}

    def is_game_won(self) -> bool:
        """Check if the player won in the game.

        Returns:
            True if all mushrooms have been collected, else it returns False.

        """
        return self.mushroom_count == self.total_mushrooms

    def is_valid_position(self, row: int, col: int) -> bool:
        """Check if a position is still inside the map.

        Args:
            row: Row coordinate
            col: Column coordinate

        Returns:
            True if position is valid, else it returns False.

        """
        return (0 <= row < len(self.current_map) and
                0 <= col < len(self.current_map[0]))

    def get_tile_at(self, row: int, col: int) -> str:
        """Get the tile coords at a particular position.

        Args:
            row: Row coordinate
            col: Column coordinate

        Returns:
            The tile character at the mentioned coords

        """
        return self.current_map[row][col]

    def set_tile_at(self, row: int, col: int, tile: str) -> None:
        """Set the tile at a particular position.

        Args:
            row: Row coordinate
            col: Column coordinate
            tile: Tile type to set

        """
        self.current_map[row][col] = tile
