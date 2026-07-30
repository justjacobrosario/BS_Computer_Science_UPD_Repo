"""Main Game Loop of Shroom Raider.

This module handles the functions for ui, movements, and physics logic that are defined from
the modules that will be imported.
"""

from config import GameState, TileType
from map_reader import count_mush, emojizer, find_player, read_stage_file
from physics_logic import (
    ItemHandler,
    MovementHandler,
    MushroomHandler,
    TileInteractionHandler,
)
from ui import (
    clear_screen,
    ctrl_print,
    inventory_print,
    item_on_ground_print,
    mush_print,
)


def initialize_paved_tiles(current_map: list[list[str]]) -> dict[tuple[int, int], None]:
    """Make a dictionary of the coords of paved tiles that will be used in the future mechanics.

    When the player or a rock collides to a tile that is paved, this dictionary restores
     the paved tile when they pass through.

    Args:
        current_map: Ascii-based map that will be used in-game

    Returns:
        Dict with paved tile coordinates as keys

    """
    # Init the dict for the paved tiles
    paved_tiles: dict[tuple[int, int], None] = {}
    for i in range(len(current_map)):
        for j in range(len(current_map[0])):
            if current_map[i][j] == TileType.PAVED.value:
                paved_tiles[i, j] = None
    return paved_tiles


def setup_game(stage_file: str) -> tuple[list[list[str]], tuple[int, int] | None, dict[tuple[int, int], None]]:
    """Set up a new game by loading the map and finding initial positions.

    Args:
        stage_file: Path to the stage file we want to load

    Returns:
        Tuple with the map, player position, and paved tiles dict

    """
    current_map = read_stage_file(stage_file)
    player_coor = find_player(current_map)
    paved_tiles = initialize_paved_tiles(current_map)
    return current_map, player_coor, paved_tiles


def display_game_state(
    current_map: list[list[str]],
    mush_count: int,
    item_on_ground_prompt: str,
    held_item: str,
) -> None:
    """Show the current state of the game to the player.

    Args:
        current_map: The map we're displaying
        mush_count: How many mushrooms the player has collected
        item_on_ground_prompt: What item is on the ground, if there is any
        held_item: What item the player is currently holding

    """
    clear_screen()

    # Print the map
    for row in emojizer(current_map):
        print("".join(row))

    print()  # just for spacing
    mush_print(mush_count)
    item_on_ground_print(item_on_ground_prompt)
    inventory_print(held_item)
    ctrl_print()


def in_game(
    current_map: list[list[str]],
    player_coor: tuple[int, int] | None,
    stage_file: str,
) -> tuple[list[list[str]], tuple[int, int] | None]:
    """Handle player input and updates game state.

    Processes moves, handles collisions, and updates the display.

    Args:
        current_map: The currently used map
        player_coor: Where the player is located
        stage_file: The selected stage file path

    Returns:
        Tuple of updated current_map and player_coor after all the interactions

    """
    # Init handlers
    movement_handler = MovementHandler()
    tile_handler = TileInteractionHandler()
    item_handler = ItemHandler()
    mushroom_handler = MushroomHandler()

    # Init local variables
    mush_count = 0
    paved_tiles = initialize_paved_tiles(current_map)
    standing_on_item = "."
    item_on_ground_prompt = " "
    held_item = " "

    total_mush = count_mush(current_map)

    display_game_state(current_map, mush_count, item_on_ground_prompt, held_item)

    while True:
        movement_input = input("\nEnter move(s): ").strip()

        if not movement_input:  # skip empty inputs
            continue

        for movement_char in movement_input:
            movement = ord(movement_char)

            # Quit if q, Q is pressed
            if movement in {ord("q"), ord("Q")}:
                held_item = ""
                return current_map, player_coor

            # Restart if ! is pressed
            if movement == ord("!"):
                current_map, player_coor, paved_tiles_new = setup_game(stage_file)
                paved_tiles = paved_tiles_new
                mush_count = 0
                held_item = " "
                standing_on_item = "."
                item_on_ground_prompt = " "
                total_mush = count_mush(current_map)
                display_game_state(current_map, mush_count, item_on_ground_prompt, held_item)
                continue

            # Movement management
            if player_coor is None:
                continue

            row_pos, col_pos = player_coor
            row_upd, col_upd = movement_handler.process_key(movement)
            new_row, new_col = row_pos + row_upd, col_pos + col_upd

            # Pickup-system
            if movement in {ord("P"), ord("p")}:
                if held_item != " ":
                    continue
                standing_on_item, held_item, item_on_ground_prompt = item_handler.pick_up_item(
                    standing_on_item,
                    held_item,
                )
                display_game_state(current_map, mush_count, item_on_ground_prompt, held_item)
                continue

            # Tile Update part
            if new_row < 0 or new_col < 0 or new_row >= len(current_map) or new_col >= len(current_map[0]):
                continue

            if (current_map[new_row][new_col] == TileType.SPACE.value
                    or current_map[new_row][new_col] == TileType.PAVED.value):
                state = GameState(
                    current_map=current_map,
                    player_position=player_coor,
                    standing_on_item=standing_on_item,
                )
                state.paved_tiles = paved_tiles
                item_on_ground_prompt = tile_handler.handle_space_movement(
                    state, (row_pos, col_pos), (new_row, new_col),
                )
                current_map = state.current_map
                player_coor = state.player_position
                standing_on_item = state.standing_on_item

            elif current_map[new_row][new_col] == TileType.ROCK.value:
                rock_destination = new_row + row_upd, new_col + col_upd
                state = GameState(
                    current_map=current_map,
                    player_position=player_coor,
                    standing_on_item=standing_on_item,
                )
                state.paved_tiles = paved_tiles
                tile_handler.handle_rock_interaction(
                    state, (row_pos, col_pos), (new_row, new_col), rock_destination,
                )
                current_map = state.current_map
                player_coor = state.player_position
                standing_on_item = state.standing_on_item

            elif current_map[new_row][new_col] == TileType.TREE.value:
                state = GameState(
                    current_map=current_map,
                    player_position=player_coor,
                    held_item=held_item,
                )
                tile_handler.handle_tree_interaction(state, (new_row, new_col))
                current_map = state.current_map
                held_item = state.held_item

            elif current_map[new_row][new_col] == TileType.MUSHROOM.value:
                state = GameState(
                    current_map=current_map,
                    player_position=player_coor,
                    standing_on_item=standing_on_item,
                )
                state.paved_tiles = paved_tiles
                item_on_ground_prompt = tile_handler.handle_space_movement(
                    state, (row_pos, col_pos), (new_row, new_col),
                )
                current_map = state.current_map
                player_coor = state.player_position
                standing_on_item = state.standing_on_item
                mush_count = mushroom_handler.collect_mushroom(mush_count)

            elif current_map[new_row][new_col] in {TileType.AXE.value, TileType.FLAMETHROWER.value}:
                item_on_ground_prompt = item_handler.get_item_prompt(standing_on_item)
                state = GameState(
                    current_map=current_map,
                    player_position=player_coor,
                    standing_on_item=standing_on_item,
                )
                state.paved_tiles = paved_tiles
                item_on_ground_prompt = tile_handler.handle_space_movement(
                    state, (row_pos, col_pos), (new_row, new_col),
                )
                current_map = state.current_map
                player_coor = state.player_position
                standing_on_item = state.standing_on_item
                item_on_ground_prompt = item_handler.get_item_prompt(standing_on_item)

            elif current_map[new_row][new_col] == TileType.WATER.value:
                # Game over - fell into water
                display_game_state(current_map, mush_count, item_on_ground_prompt, held_item)
                print("\nGame over! You fell into water!")
                return current_map, player_coor

            display_game_state(current_map, mush_count, item_on_ground_prompt, held_item)

            if mush_count == total_mush:
                # Winner!
                print("\nYou win! All mushrooms collected!")
                return current_map, player_coor

    return current_map, player_coor


def new_game(stage_file: str = "default_stage.txt") -> None:
    """Start a new interactive game session.

    Args:
        stage_file: Which stage to load (defaults to default_stage.txt)

    """
    current_map, player_coor, _ = setup_game(stage_file)
    in_game(current_map, player_coor, stage_file)


def simulate_game(moves: str, stage_file: str = "default_stage.txt") -> tuple[list[list[str]], bool]:
    """Run a game simulation with predetermined moves.

    Args:
        moves: String containing all the moves to execute
        stage_file: Which stage file to use (default_stage.txt if none selected)

    Returns:
        Tuple containing final map state and whether player won

    """
    current_map, player_coor, paved_tiles = setup_game(stage_file)

    # Initialize handlers
    movement_handler = MovementHandler()
    tile_handler = TileInteractionHandler()
    item_handler = ItemHandler()
    mushroom_handler = MushroomHandler()

    mush_count = 0
    held_item = " "
    standing_on_item = "."
    total_mush = count_mush(current_map)

    for movement in moves:
        if mush_count == total_mush:
            return current_map, True

        if movement.upper() == "Q":
            break

        if movement.upper() == "P":
            if held_item != " ":
                continue
            standing_on_item, held_item, _ = item_handler.pick_up_item(
                standing_on_item,
                held_item,
            )
            continue

        if player_coor is None:
            break

        row_pos, col_pos = player_coor
        row_upd, col_upd = movement_handler.process_key(ord(movement))
        new_row, new_col = row_pos + row_upd, col_pos + col_upd

        if movement not in {"w", "a", "s", "d", "p", "W", "A", "S", "D", "P"}:
            break

        if new_row < 0 or new_col < 0 or new_row >= len(current_map) or new_col >= len(current_map[0]):
            continue

        if (current_map[new_row][new_col] == TileType.SPACE.value
                or current_map[new_row][new_col] == TileType.PAVED.value):
            state = GameState(
                current_map=current_map,
                player_position=player_coor,
                standing_on_item=standing_on_item,
            )
            state.paved_tiles = paved_tiles
            tile_handler.handle_space_movement(state, (row_pos, col_pos), (new_row, new_col))
            current_map = state.current_map
            player_coor = state.player_position
            standing_on_item = state.standing_on_item

        elif current_map[new_row][new_col] == TileType.ROCK.value:
            rock_destination = new_row + row_upd, new_col + col_upd
            state = GameState(
                current_map=current_map,
                player_position=player_coor,
                standing_on_item=standing_on_item,
            )
            state.paved_tiles = paved_tiles
            tile_handler.handle_rock_interaction(
                state, (row_pos, col_pos), (new_row, new_col), rock_destination,
            )
            current_map = state.current_map
            player_coor = state.player_position
            standing_on_item = state.standing_on_item

        elif current_map[new_row][new_col] == TileType.TREE.value:
            state = GameState(
                current_map=current_map,
                player_position=player_coor,
                held_item=held_item,
            )
            tile_handler.handle_tree_interaction(state, (new_row, new_col))
            current_map = state.current_map
            held_item = state.held_item

        elif current_map[new_row][new_col] == TileType.MUSHROOM.value:
            state = GameState(
                current_map=current_map,
                player_position=player_coor,
                standing_on_item=standing_on_item,
            )
            state.paved_tiles = paved_tiles
            tile_handler.handle_space_movement(state, (row_pos, col_pos), (new_row, new_col))
            current_map = state.current_map
            player_coor = state.player_position
            standing_on_item = state.standing_on_item
            mush_count = mushroom_handler.collect_mushroom(mush_count)

        elif current_map[new_row][new_col] in {TileType.AXE.value, TileType.FLAMETHROWER.value}:
            state = GameState(
                current_map=current_map,
                player_position=player_coor,
                standing_on_item=standing_on_item,
            )
            state.paved_tiles = paved_tiles
            tile_handler.handle_space_movement(state, (row_pos, col_pos), (new_row, new_col))
            current_map = state.current_map
            player_coor = state.player_position
            standing_on_item = state.standing_on_item

        elif current_map[new_row][new_col] == TileType.WATER.value:
            return current_map, False

    return current_map, mush_count == total_mush
