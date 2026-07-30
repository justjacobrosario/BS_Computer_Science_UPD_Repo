"""Physics Logic and Game Mechanics.

This module defines the classes and functions the will be used in-game to handle movement keys,
interactions with tiles, and tool mechanics.
"""

from config import GameState, TileType


class MovementHandler:
    """Handles the player movement input and direction conversion."""

    def process_key(self, movement: int) -> tuple[int, int]:
        """Convert the typed key code into movement.

        Args:
            movement: Key code from input

        Returns:
            Tuple of (change in rows, change in cols) for movement direction

        """
        if movement in {119, 87}:  # W, w - walk up
            return -1, 0
        elif movement in {115, 83}:  # S, s - walk down
            return 1, 0
        elif movement in {97, 65}:  # A, a - walk left
            return 0, -1
        elif movement in {100, 68}:  # D, d - walk right
            return 0, 1
        else:
            return 0, 0


class TileInteractionHandler:
    """Handles interactions between the player to different kinds of tiles."""

    def handle_space_movement(
        self,
        state: GameState,
        old_pos: tuple[int, int],
        new_pos: tuple[int, int],
    ) -> str:
        """Handle the movement of a player to a space tile or a paved tile.

        Args:
            state: Current game state
            old_pos: Previous player position (row,col) tuple
            new_pos: New player position (row,col) tuple

        Returns:
            Item on ground prompt message

        """
        old_row, old_col = old_pos
        new_row, new_col = new_pos

        # Init the message
        item_on_ground_prompt = ""

        # Check if we're to leave a paved tile
        if old_pos in state.paved_tiles:
            state.set_tile_at(old_row, old_col, TileType.PAVED.value)
        else:
            if state.standing_on_item == TileType.MUSHROOM.value:
                restore_tile = TileType.SPACE.value
            else:
                restore_tile = state.standing_on_item
            state.set_tile_at(old_row, old_col, restore_tile)

        # Update the player states
        state.standing_on_item = state.get_tile_at(new_row, new_col)
        state.set_tile_at(new_row, new_col, TileType.PLAYER.value)
        state.player_position = new_pos

        if state.standing_on_item not in {TileType.FLAMETHROWER.value, TileType.AXE.value}:
            item_on_ground_prompt = "No item to pick up"

        return item_on_ground_prompt

    def handle_rock_interaction(
        self,
        state: GameState,
        old_pos: tuple[int, int],
        rock_pos: tuple[int, int],
        rock_dest: tuple[int, int],
    ) -> bool:
        """Handle player when pushing a rock.

        Args:
            state: Current game state
            old_pos: Previous player position
            rock_pos: Current rock position
            rock_dest: Destination position for rock

        Returns:
            True if rock was successfully moved, else False otherwise

        """
        # Check first if the destination is still inside the map
        if not state.is_valid_position(rock_dest[0], rock_dest[1]):
            return False

        dest_tile = state.get_tile_at(rock_dest[0], rock_dest[1])

        # When the rock passes through a space or paved tile
        if dest_tile in {TileType.SPACE.value, TileType.PAVED.value}:
            state.set_tile_at(rock_dest[0], rock_dest[1], TileType.ROCK.value)
            state.set_tile_at(rock_pos[0], rock_pos[1], TileType.PLAYER.value)

            if old_pos in state.paved_tiles:
                state.set_tile_at(old_pos[0], old_pos[1], TileType.PAVED.value)
            else:
                if state.standing_on_item == TileType.MUSHROOM.value:
                    restore_tile = TileType.SPACE.value
                else:
                    restore_tile = state.standing_on_item
                state.set_tile_at(old_pos[0], old_pos[1], restore_tile)

            state.standing_on_item = (TileType.PAVED.value if rock_pos in state.paved_tiles
                                     else TileType.SPACE.value)
            state.player_position = rock_pos
            return True

        # When the rock passes through water
        elif dest_tile == TileType.WATER.value:
            state.set_tile_at(rock_dest[0], rock_dest[1], TileType.PAVED.value)
            state.set_tile_at(rock_pos[0], rock_pos[1], TileType.PLAYER.value)

            if old_pos in state.paved_tiles:
                state.set_tile_at(old_pos[0], old_pos[1], TileType.PAVED.value)
            else:
                if state.standing_on_item == TileType.MUSHROOM.value:
                    restore_tile = TileType.SPACE.value
                else:
                    restore_tile = state.standing_on_item
                state.set_tile_at(old_pos[0], old_pos[1], restore_tile)

            state.paved_tiles[rock_dest] = None
            state.standing_on_item = (TileType.PAVED.value if rock_pos in state.paved_tiles
                                     else TileType.SPACE.value)
            state.player_position = rock_pos
            return True

        # If can't push rock there
        return False

    def handle_tree_interaction(self, state: GameState, tree_pos: tuple[int, int]) -> bool:
        """Handle player interaction with a tree using diff tools.

        Args:
            state: Current game state
            tree_pos: Position of the tree

        Returns:
            True if tree was removed, False otherwise

        """
        if state.held_item == " ":
            return False

        tree_handler = TreeHandler()
        # Check current tool
        if state.held_item == TileType.AXE.value:
            tree_handler.chop(state.current_map, tree_pos)
            state.held_item = " "
            return True
        elif state.held_item == TileType.FLAMETHROWER.value:
            tree_handler.burn(state.current_map, tree_pos)
            state.held_item = " "
            return True

        # not a tool
        return False


class TreeHandler:
    """Handles tree removal mechanics (the chopping and burning mechanics)."""

    def chop(self, game_map: list[list[str]], position: tuple[int, int]) -> None:
        """Chop a single tree at the given position.

        Args:
            game_map: The game map
            position: Position of tree to chop (row, col)

        """
        row, col = position
        game_map[row][col] = TileType.SPACE.value

    def burn(self, game_map: list[list[str]], position: tuple[int, int]) -> None:
        """Burn connected trees starting from the given position.

        Args:
            game_map: The game map
            position: Starting position for burning (row, col)

        """
        trees_to_burn = self._find_connected_trees(game_map, position)
        for row, col in trees_to_burn:
            game_map[row][col] = TileType.SPACE.value

    def _find_connected_trees(
        self,
        game_map: list[list[str]],
        position: tuple[int, int],
        visited: set[tuple[int, int]] | None = None,
    ) -> set[tuple[int, int]]:
        """Find all trees connected to the starting position using via DFS.

        Args:
            game_map: The game map
            position: Current position to check
            visited: Set of already visited positions

        Returns:
            Set of all connected tree positions

        """
        # Init visited set if not provided
        if visited is None:
            visited = set()

        row, col = position

        # Boundary checking
        if (row < 0 or col < 0 or
            row >= len(game_map) or col >= len(game_map[0])):
            return visited

        # Check if this is a tree and we haven't visited it yet
        if game_map[row][col] != TileType.TREE.value or position in visited:
            return visited

        visited.add(position)

        # Check all 4 directions
        self._find_connected_trees(game_map, (row + 1, col), visited)
        self._find_connected_trees(game_map, (row - 1, col), visited)
        self._find_connected_trees(game_map, (row, col + 1), visited)
        self._find_connected_trees(game_map, (row, col - 1), visited)

        return visited


class ItemHandler:
    """Handles item pickup mechanics."""

    def pick_up_item(self, standing_on: str, held: str) -> tuple[str, str, str]:
        """Pick up an item from the ground.

        Args:
            standing_on: Item that the player is standing
            held: Currently held item

        Returns:
            (new_standing_on, new_held, prompt) tuple

        """
        prompt = "No item to pick up"  # default prompt

        if standing_on == TileType.AXE.value:
            return TileType.SPACE.value, TileType.AXE.value, prompt
        elif standing_on == TileType.FLAMETHROWER.value:
            return TileType.SPACE.value, TileType.FLAMETHROWER.value, prompt

        return standing_on, held, prompt

    def get_item_prompt(self, item: str) -> str:
        """Get the display prompt for an item.

        Args:
            item: Item character

        Returns:
            the emoji representation of the item

        """
        if item == TileType.AXE.value:
            return "🪓"
        elif item == TileType.FLAMETHROWER.value:
            return "🔥"
        else:
            return ""


class MushroomHandler:
    """Handles mushroom collection mechanics."""

    def collect_mushroom(self, count: int) -> int:
        """Increment mushroom collection count.

        Args:
            count: Current mushroom count

        Returns:
            Updated mushroom count

        """
        return count + 1
