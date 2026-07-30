"""Unit tests for Shroom Raider game functionality.

Tests cover movement, player tracking, mushroom counting, tool usage,
and tile interactions.
"""


from config import GameState, TileType
from map_reader import count_mushrooms, find_player
from physics_logic import (
    ItemHandler,
    MovementHandler,
    MushroomHandler,
    TileInteractionHandler,
    TreeHandler,
)


class TestMovementHandler:
    """Tests for MovementHandler class."""

    def test_move_up(self) -> None:
        """Test W key outputs upward movement."""
        handler = MovementHandler()
        assert handler.process_key(ord("W")) == (-1, 0)
        assert handler.process_key(ord("w")) == (-1, 0)

    def test_move_down(self) -> None:
        """Test S key outputs downward movement."""
        handler = MovementHandler()
        assert handler.process_key(ord("S")) == (1, 0)
        assert handler.process_key(ord("s")) == (1, 0)

    def test_move_left(self) -> None:
        """Test A key outputs leftward movement."""
        handler = MovementHandler()
        assert handler.process_key(ord("A")) == (0, -1)
        assert handler.process_key(ord("a")) == (0, -1)

    def test_move_right(self) -> None:
        """Test D key outputs rightward movement."""
        handler = MovementHandler()
        assert handler.process_key(ord("D")) == (0, 1)
        assert handler.process_key(ord("d")) == (0, 1)

    def test_invalid_key(self) -> None:
        """Test invalid keys output no movement."""
        handler = MovementHandler()
        assert handler.process_key(ord("X")) == (0, 0)
        assert handler.process_key(ord("1")) == (0, 0)


class TestMapReader:
    """Tests for map reading functions."""

    def test_find_player_present(self) -> None:
        """Test finding player when present in map."""
        game_map = [
            ["T", "T", "T"],
            ["T", "L", "T"],
            ["T", "T", "T"],
        ]
        assert find_player(game_map) == (1, 1)

    def test_find_player_absent(self) -> None:
        """Test finding player when not in map."""
        game_map = [
            ["T", "T", "T"],
            ["T", ".", "T"],
            ["T", "T", "T"],
        ]
        assert find_player(game_map) is None

    def test_count_mushrooms_multiple(self) -> None:
        """Test counting mushrooms when multiple present."""
        game_map = [
            ["T", "+", "T"],
            ["T", "L", "+"],
            ["+", "T", "T"],
        ]
        assert count_mushrooms(game_map) == 3

    def test_count_mushrooms_none(self) -> None:
        """Test counting mushrooms when none present."""
        game_map = [
            ["T", "T", "T"],
            ["T", "L", "T"],
            ["T", "T", "T"],
        ]
        assert count_mushrooms(game_map) == 0


class TestTreeHandler:
    """Tests for tree handling mechanics."""

    def test_chop_tree(self) -> None:
        """Test chopping a single tree."""
        game_map = [
            ["T", "T", "T"],
            ["T", "L", "T"],
            ["T", "T", "T"],
        ]
        handler = TreeHandler()
        handler.chop(game_map, (0, 0))
        assert game_map[0][0] == TileType.SPACE.value

    def test_burn_single_tree(self) -> None:
        """Test burning an isolated tree."""
        game_map = [
            ["T", ".", "."],
            [".", "L", "."],
            [".", ".", "."],
        ]
        handler = TreeHandler()
        handler.burn(game_map, (0, 0))
        assert game_map[0][0] == TileType.SPACE.value

    def test_burn_connected_trees(self) -> None:
        """Test burning multiple connected trees."""
        game_map = [
            ["T", "T", "T"],
            ["T", "L", "."],
            ["T", "T", "."],
        ]
        handler = TreeHandler()
        handler.burn(game_map, (0, 0))

        # All connected trees should be burned
        assert game_map[0][0] == TileType.SPACE.value
        assert game_map[0][1] == TileType.SPACE.value
        assert game_map[0][2] == TileType.SPACE.value
        assert game_map[1][0] == TileType.SPACE.value
        assert game_map[2][0] == TileType.SPACE.value
        assert game_map[2][1] == TileType.SPACE.value


class TestItemHandler:
    """Tests for item pickup mechanics."""

    def test_pick_up_axe(self) -> None:
        """Test picking up an axe."""
        standing_on = TileType.AXE.value
        held = " "
        handler = ItemHandler()
        new_standing, new_held, prompt = handler.pick_up_item(standing_on, held)

        assert new_standing == TileType.SPACE.value
        assert new_held == TileType.AXE.value
        assert prompt == "No item to pick up"

    def test_pick_up_flamethrower(self) -> None:
        """Test picking up a flamethrower."""
        standing_on = TileType.FLAMETHROWER.value
        held = " "
        handler = ItemHandler()
        new_standing, new_held, prompt = handler.pick_up_item(standing_on, held)

        assert new_standing == TileType.SPACE.value
        assert new_held == TileType.FLAMETHROWER.value
        assert prompt == "No item to pick up"

    def test_item_prompt_axe(self) -> None:
        """Test getting item prompt for axe."""
        handler = ItemHandler()
        assert handler.get_item_prompt(TileType.AXE.value) == "🪓"

    def test_item_prompt_flamethrower(self) -> None:
        """Test getting item prompt for flamethrower."""
        handler = ItemHandler()
        assert handler.get_item_prompt(TileType.FLAMETHROWER.value) == "🔥"


class TestMushroomHandler:
    """Tests for mushroom collection."""

    def test_collect_mushroom(self) -> None:
        """Test mushroom collection increments count."""
        handler = MushroomHandler()
        count = 0
        count = handler.collect_mushroom(count)
        assert count == 1

        count = handler.collect_mushroom(count)
        assert count == 2


class TestGameState:
    """Tests for GameState dataclass."""

    def test_game_state_initialization(self) -> None:
        """Test GameState initializes correctly."""
        game_map = [[".", ".", "."], [".", "L", "."], [".", ".", "."]]
        state = GameState(current_map=game_map, player_position=(1, 1))

        assert state.player_position == (1, 1)
        assert state.mushroom_count == 0
        assert state.held_item == " "

    def test_is_game_won(self) -> None:
        """Test game won detection."""
        game_map = [[".", ".", "."], [".", "L", "."], [".", ".", "."]]
        state = GameState(
            current_map=game_map,
            player_position=(1, 1),
            total_mushrooms=3,
        )

        assert not state.is_game_won()

        state.mushroom_count = 3
        assert state.is_game_won()

    def test_is_valid_position(self) -> None:
        """Test position validation."""
        game_map = [[".", ".", "."], [".", "L", "."], [".", ".", "."]]
        state = GameState(current_map=game_map, player_position=(1, 1))

        assert state.is_valid_position(0, 0)
        assert state.is_valid_position(2, 2)
        assert not state.is_valid_position(-1, 0)
        assert not state.is_valid_position(0, 3)
        assert not state.is_valid_position(3, 0)

    def test_get_set_tile(self) -> None:
        """Test getting and setting tiles."""
        game_map = [[".", ".", "."], [".", "L", "."], [".", ".", "."]]
        state = GameState(current_map=game_map, player_position=(1, 1))

        assert state.get_tile_at(1, 1) == "L"

        state.set_tile_at(0, 0, "T")
        assert state.get_tile_at(0, 0) == "T"


class TestTileInteractions:
    """Tests for tile interaction mechanics."""

    def test_space_movement(self) -> None:
        """Test movement to space tile."""
        game_map = [
            [".", ".", "."],
            [".", "L", "."],
            [".", ".", "."],
        ]
        state = GameState(current_map=game_map, player_position=(1, 1))

        handler = TileInteractionHandler()
        handler.handle_space_movement(state, (1, 1), (1, 2))

        assert state.player_position == (1, 2)
        assert state.get_tile_at(1, 2) == TileType.PLAYER.value
        assert state.get_tile_at(1, 1) == TileType.SPACE.value

    def test_tree_interaction_with_axe(self) -> None:
        """Test tree interaction with axe."""
        game_map = [
            [".", "T", "."],
            [".", "L", "."],
            [".", ".", "."],
        ]
        state = GameState(
            current_map=game_map,
            player_position=(1, 1),
            held_item=TileType.AXE.value,
        )

        handler = TileInteractionHandler()
        result = handler.handle_tree_interaction(state, (0, 1))

        assert result is True
        assert state.get_tile_at(0, 1) == TileType.SPACE.value
        assert state.held_item == " "

    def test_tree_interaction_without_tool(self) -> None:
        """Test tree interaction without any tool."""
        game_map = [
            [".", "T", "."],
            [".", "L", "."],
            [".", ".", "."],
        ]
        state = GameState(
            current_map=game_map,
            player_position=(1, 1),
            held_item=" ",
        )

        handler = TileInteractionHandler()
        result = handler.handle_tree_interaction(state, (0, 1))

        assert result is False
        assert state.get_tile_at(0, 1) == TileType.TREE.value
