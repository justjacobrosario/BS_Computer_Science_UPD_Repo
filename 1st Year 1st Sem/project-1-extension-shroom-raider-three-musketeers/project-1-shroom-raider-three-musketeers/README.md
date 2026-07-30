# Shroom Raider

A terminal-based puzzle game where you play as Laro Craft (or Isko in the bonus version). You'll explore different locations to collect mushrooms while overcoming obstacles, pushing rocks, and using tools.

## Project Structure

This project has two main versions:

- **Base Game Folder**: Contains the basic implementation without extra features.
- **Game with Bonus Features Folder**: Improved version with bonus features (list of bonus features here [Bonus Features Summary](#bonus-features-summary)).

## Contents

- [Base Game](#base-game)
  - [Running the Base Game](#running-the-base-game)
  - [Base Game Controls](#base-game-controls)
  - [Base Game Elements](#base-game-elements)
  - [Base Game Features](#base-game-features)
- [Game with Bonus Features](#game-with-bonus-features)
  - [Running the Bonus Version](#running-the-bonus-version)
  - [Bonus Features Summary](#bonus-features-summary)
  - [Bonus Game Controls](#bonus-game-controls)
  - [Additional Bonus Elements](#additional-bonus-elements)
  - [Bonus Features Implemented](#bonus-features-implemented)
- [Code Organization](#code-organization)
- [Unit Tests](#unit-tests)
- [Stage File Format](#stage-file-format)
- [Credits](#credits)



### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository.
2. Navigate to the appropriate project directory (base game or bonus version).
3. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

**Note**: The base game needs only `pytest`, while the bonus version requires additional packages, including `asciimatics`, `pygame`, and `bcrypt`.

## Base Game

The base game offers the core Shroom Raider experience with all essential mechanics built into a simple terminal interface.

### Running the Base Game

**Interactive Mode (Play Normally)**:

```bash
python3 shroom_raider.py
```

Or with a specific stage file:

```bash
python3 shroom_raider.py -f <stage_file>
```

**Simulation Mode (Automated Testing)**:

```bash
python3 shroom_raider.py -f <stage_file> -m <moves> -o <output_file>
```

Example:
```bash
python3 shroom_raider.py -f default_stage.txt -m "ssspd" -o output.txt
```

Where:
- `-f` specifies the stage file.
- `-m` specifies a string of moves (e.g., "wasd" for up, left, down, right).
- `-o` specifies the output file name.

**Alternative Module Syntax**:

```bash
python3 -m shroom_raider
python3 -m shroom_raider -f <stage_file>
python3 -m shroom_raider -f <stage_file> -m <moves> -o <output_file>
```

### Base Game Controls

- **W** or **w**: Move up
- **A** or **a**: Move left
- **S** or **s**: Move down
- **D** or **d**: Move right
- **P** or **p**: Pick up item on current tile
- **!**: Reset the current stage

**Important Notes**:
- Controls are case-insensitive.
- You can enter multiple moves at once (e.g., `wwdds`).
- Only the first invalid character halts move execution.

### Base Game Elements

**Tiles**:

- **🧑 (L)** - Laro Craft: The player character.
- **　(.)** - Empty tile: Walkable space.
- **🌲 (T)** - Tree: Blocks movement unless using an axe or flamethrower.
- **🍄 (+)** - Mushroom: Collect these to win.
- **🪨 (R)** - Rock: Can be pushed.
- **🟦 (~)** - Water: Causes game over if entered.
- **⬜ (_)** - Paved tile: Created when a rock falls into water.

**Items**:

- **🪓 (x)** - Axe: Chops down one tree.
- **🔥 (*)** - Flamethrower: Burns all connected trees.

### Base Game Features

**Core Mechanics**:

- Grid-based movement in four directions.
- Push rocks into empty spaces, paved tiles, or water.
- Cannot push multiple rocks at once.
- Use the axe for single trees and the flamethrower for groups of connected trees.
- You can hold one item at a time and cannot drop items.
- Water creates paved tiles when rocks are pushed into it.
- Falling into water results in game over.

**Win Condition**: Collect all mushrooms in the level.

**Lose Condition**: Fall into water.

**Stage Reset**: Press `!` to restart the current stage.

## Game with Bonus Features

The enhanced version has a rich story mode, animated cutscenes, support for multiple languages, user accounts, leaderboards, and extensive customization options.

### Running the Bonus Version

**Main Menu Mode**:

```bash
python3 shroom_raider.py
```

Or:

```bash
python3 shroom_raider.py -p
```

**Direct Speedrun Mode**:

```bash
python3 shroom_raider.py -f <stage_number>
```

**Simulation Mode**:

```bash
python3 shroom_raider.py -f <stage_number> -m <moves> -o <output_file>
```

### Bonus Features Summary

Here is a clear list of bonus features added for grading consideration:

1. **Main Menu** - An animated menu with various options.
2. **Story Mode with Cutscenes** - A complete narrative with animated sequences.
3. **Multi-Language Support** - Supports English, Japanese, and Filipino with dynamic translations.
4. **User Account System** - Features sign-up, log-in, and deletion with secure password hashing.
5. **Global Leaderboard** - Lists the top 10 players with persistent storage.
6. **Local Records System** - Tracks personal top 10 times per user.
7. **Sound System** - Includes background music and sound effects with volume controls.
8. **Visual Customization** - Offers 10 character options and 64 color themes for the UI.
9. **Enhanced UI/UX** - Interface powered by asciimatics with animations and color.
10. **Settings Menu** - Comprehensive settings for language, accounts, sound, and general information.
11. **Ability to Exit/Quit** - Q key closes the game and returns to the menu smoothly.
12. **Multiple Stages (20+)** - Features UP Diliman-themed locations with unique challenges.
13. **Time Tracking** - A speedrun timer integrated with the leaderboard.
14. **Stage Loading Screens** - Animated transitions between stages.
15. **Animations** - Includes effects like rockets, jeeps, and typewriter text.
16. **Additional Items** - A hammer to break rocks.
17. **Additional Tiles** - Decorative building elements like Brick, Roof, Concrete, and Street.
18. **SQLite Database** - For storing user and leaderboard data persistently.
19. **Skip Cutscene Feature** - Allows users to control whether to view animations.
20. **Color-Coded UI Elements** - Offers visual feedback for controls and status.

All bonus features are fully functional and integrated into the overall game experience.

---

### Bonus Game Controls

Same as the base game with additional options:

- **Q** or **q**: Quit to main menu.
- **S** or **s**: Skip cutscenes/animations.
- **Any other key**: Skip text animation in cutscenes.

### Additional Bonus Elements

**New Tiles**:

- **🟥 (B)** - Brick: Decorative building tile.
- **🟫 (Y)** - Roof: Decorative building tile.
- **🟧 (C)** - Concrete: Decorative building tile.
- **🔲 (S)** - Street: Walkable paved road.

**New Item**:

- **🔨 (H)** - Hammer: Breaks rocks instantly.

### Bonus Features Implemented

#### 1. Story Mode with Cutscenes

**Introductory Cutscene**:
- Story about Isko, a cadet from planet Iskorion.
- Passes the UPCAT (Universal Placement and Cosmic Aptitude Test).
- Mission to observe human academic behavior at UP Diliman.
- Crash landing results in memory core corruption.
- Becomes stuck in an infinite loop around the UP campus.

**Stage-Specific Cutscenes**:
- Each game stage has unique introduction cutscenes.
- Stages themed after actual UP Diliman locations, including AECH (Tutorial stage) and others.

**Ending Cutscene**:
- Sequence showing Brain Core restoration.
- Resolution of the time loop.
- Animated victory celebration.

**Animation Features**:
- Rocket launch and landing animations.
- Malfunction effects with visual glitches.
- Jeep (UP Ikot) animations.
- ASCII art displays of UP landmarks.
- Typewriter text effects.
- Skip options for all cutscenes.

#### 2. Multi-Language Support

**Three Languages Available**:
- English
- Japanese (日本語)
- Filipino

**Language Features**:
- All UI text is translated dynamically.
- Menu options translate in real-time.
- In-game messages and prompts translate.
- Cutscene dialogue also translates.
- Can be changed anytime in settings.

#### 3. User Account System

**Account Management**:
- Sign up with a username and password.
- Secure password hashing using bcrypt.
- Log into existing accounts.
- Guest mode available.
- Account deletion functionality.
- Account data is stored in an SQLite database.

**User Profile**:
- Displays the current pilot (username).
- Tracks personal records.
- Individual leaderboard statistics.

#### 4. Leaderboard System

**Global Rankings**:
- Top ten players saved.
- Displays username, completion time, and mushrooms collected.
- Automatically sorted by fastest completion.
- Persistent across sessions.

**Local Records**:
- Personal top ten completion times.
- Shows your best performances.
- Tracked per user account.

#### 5. Sound System

**Audio Features**:
- Background music for different game states.
- Menu music.
- Sound effects for win/lose events.
- Sounds for rock pushing and mushroom collection.
- Sounds for tree chopping and burning.

**Volume Controls**:
- Main volume slider (0-10).
- Sound effects volume slider (0-10).
- Real-time volume adjustment.
- Settings accessible from the main menu.

#### 6. Visual Customization (Appearance Menu)

**Character Selection**:
- Ten different character emojis to choose from.

**UI Color Customization**:
- Background color: Eight options.
- UI visuals/borders color: Eight options.
- Real-time preview of selections.
- Persistent across sessions.

#### 7. Enhanced UI/UX

**Asciimatics-Powered Interface**:
- Animated starfield backgrounds.
- Stylized ASCII art titles.
- Box-drawn menus and game borders.
- Color-coded elements.
- Smooth frame-based rendering.

**HUD Elements**:
- Mushroom counter.
- Currently held item display.
- Item on ground indicator.
- Timer (for speedrun mode).
- Visual control guide with highlighting.

**Multiple UI Boxes**:
- Separate panels for map, inventory, and controls.
- Clear separation of game information.
- Professional-looking terminal interface.

#### 8. Main Menu

**Menu Options**:
- Speedrun Mode.
- Story Mode.
- Leaderboard access.
- Settings (Language, Account, Sound, About).
- Appearance customization.
- Quit option.

#### 9. Settings Menu

**Four Settings Categories**:

**Language Settings**:
- Switch between English, Japanese, and Filipino.
- Instant UI updates.
- Clear current language indicator.

**Account Settings**:
- Create a new account (Sign In).
- Log into existing account.
- Delete current account.
- View pilot ID and status.

**Sound Settings**:
- Main volume control with visual bar.
- Sound effects volume control.
- Interactive adjustment buttons.

**About Section**:
- Development team information.
- Member names.
- Course section.
- Version information.
- Inspiration credits.

#### 10. Ability to Exit

- Press Q from any game screen to return to the main menu.
- Graceful exit handling.
- State saved when quitting.

#### 11. Multiple Stages

**20+ Unique Stages** themed after UP Diliman locations:
- Tutorial stage (AECH).
- Academic buildings and dormitories.
- Campus landmarks and facilities.
- Food courts and parks.

#### 12. Time Tracking

- Timer displays during speedrun mode.
- Format: MM:SS:ms.
- Recorded to leaderboards for ranking comparisons. 

#### 13. Stage Loading Screens

- Animated loading sequence.
- UP Ikot jeep animation.
- Stage number display.
- ASCII art stage indicators.

## Code Organization

Both versions have a modular structure with clear separation of concerns.

### Base Game Architecture

**shroom_raider.py**:
- Main entry point.
- Argument parsing using `argparse`.
- Handles interactive and simulation modes.
- Routes to the appropriate game functions.

**game.py**:
- Core game loop.
- Game state initialization.
- Interactive and simulation mode handlers.
- Displays game state.
- Integrates all game subsystems.

**map_reader.py**:
- Stage file parsing.
- Player position detection.
- Mushroom counting.
- ASCII to emoji conversion.
- Map string formatting for output.

**physics_logic.py**:
- Movement direction conversion.
- Rock pushing mechanics.
- Tile movement.
- Tree interaction with tools.
- Item pickup logic.
- Mushroom collection and tool implementations.

**ui.py**:
- Screen clearing.
- Displays for mushroom count, item status, inventory, and controls.

**config.py**:
- Game constants and color constants for UI.
- Global state variables.

**test_game.py**:
- Unit tests for various game mechanics.

### Bonus Version Architecture

**Additional/Modified Modules**:

**menu.py**:
- Main menu frame class.
- Displays menu options.
- Routes mode selection.
- Manages Asciimatics scenes.

**animations.py**:
- Handles cutscene sequences and animations.
- Typewriter text effect.
- Skip mechanics for animations.

**sign_in.py**:
- User authentication frames.
- Manages settings and leaderboard displays.
- Language selection and account management.

**appearance.py**:
- Character selection interface.
- Color customization system with previews.

**winner.py** and **lose.py**:
- Animated victory and game over screens.
- Displays results and prompts.

**sound_check.py**:
- Manages sound playback and volume control.

**data.py**:
- Manages SQLite database for user accounts.
- Handles password hashing and leaderboard data.

**ASCII_GRAPHICS.py**:
- Pre-defined ASCII art assets and graphics.

**physics_logic_2.py**:
- Manages physics for simulation mode.

**Enhanced config.py**:
- Language system and additional features.

### Key Algorithms

**Connected Trees (Flamethrower)**:

Uses recursive depth-first search to find all connected trees:

1. Start at the target tree position.
2. Check all four adjacent cells (up, down, left, right).
3. If an adjacent cell has a tree and hasn’t been visited:
   - Add to visited set.
   - Recursively explore from that tree.
4. Return set of all connected tree positions.
5. Replace all positions with empty tiles.

**Implementation**:
- Uses a set to track visited positions.
- Recursive function handles traversal.
- Base cases include out of bounds or reaching a non-tree.

**Rock Pushing Logic**:

1. Calculate the destination position (one tile beyond the rock).
2. Check if the destination is valid:
   - It must be within bounds.
   - It must be empty, paved, or water.
3. If the destination is water:
   - Convert the water to a paved tile.
   - Add it to the paved tiles dictionary.
   - Move the rock to the water position.
4. If the destination is a valid floor:
   - Move the rock to the destination.
   - Move the player to the rock's old position.
5. Restore the previous tile state (either paved or item) at the player's old position.

**Paved Tile Tracking**:

- Keeps a dictionary of paved tile coordinates.
- Key: `(row, col)` tuple.
- Value: `None` (existence check only).
- Used when the player or rock moves away from a paved tile.
- Ensures proper restoration of tiles.

---

## Unit Tests

### Running Tests

From the base game directory:

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

To run a specific test file:

```bash
pytest test_game.py
```

### Test Coverage

**Movement Tests** (test_game.py):
- `test_read_up()`: Validates that pressing W/w produces upward movement (-1, 0).
- `test_read_down()`: Validates that pressing S/s produces downward movement (1, 0).
- `test_read_left()`: Validates that pressing A/a produces leftward movement (0, -1).
- `test_read_right()`: Validates that pressing D/d produces rightward movement (0, 1).
- `test_read_invalid()`: Validates that invalid keys produce no movement (0, 0).

**Player Detection Tests**:
- `test_find_player()`: Confirms correct detection of player coordinates.
- `test_find_player_not_found()`: Confirms None is returned when no player exists.

**Mushroom Counting Tests**:
- `test_count_mushrooms()`: Validates that the mushroom counting is accurate.
- `test_count_mushrooms_none()`: Confirms a count of zero with no mushrooms.

**Tool Mechanics Tests**:
- `test_chop_tree()`: Confirms the axe removes a single tree correctly.
- `test_burn_single_tree()`: Confirms the flamethrower burns an isolated tree.
- `test_burn_connected_trees()`: Validates that all connected trees can be burned.

**Item System Tests**:
- `test_pick_up_axe()`: Validates that picking up the axe updates the state correctly.
- `test_pick_up_flamethrower()`: Confirms the flamethrower pickup mechanics.

**Collection Tests**:
- `test_mushroom_collection()`: Validates that the mushroom counter increments properly.

### Test Thoroughness

The test suite is thorough because it:

- Tests all main mechanics: movement, tools, items, collection.
- Includes edge cases: missing player, zero mushrooms, and invalid input.
- Tests complex situations: connected trees versus single trees.
- Confirms state changes: ensures the game state updates properly.
- Uses precise assertions: checks expected outcomes accurately.
- Tests both simple and complex scenarios: single actions and combinations.

### Adding New Tests

To add to the test suite:

1. Create a function in `test_game.py` that starts with `test_`.
2. Import necessary modules.
3. Set up the test data (create the test map/state).
4. Execute the function being tested.
5. Assert the expected results.

Example:

```python
def test_new_feature():
    """Description of what this test validates."""
    # Setup
    test_map = [["T", "L", "."]]
    
    # Execute
    result = some_function(test_map)
    
    # Assert
    assert result == expected_value
```

The modular code structure makes it easy to test individual functions, following unit testing best practices.

---

## Stage File Format

### Base Game Format

Text files should have this structure:

```
<rows> <columns>
<ASCII_map_row_1>
<ASCII_map_row_2>
...
<ASCII_map_row_n>
```

Example:

```
5 9
TTTTTTTTT
T...+...T
T...L...T
T.......T
TTTTTTTTT
```

Where:
- First line: number of rows and columns (space-separated).
- Subsequent lines: ASCII representation using defined characters.
- Valid dimensions: 3 ≤ rows, cols ≤ 30.

### Bonus Version Format

**Multiple Maps File (MAPS.txt)**:

Maps are separated by backslashes (`\`):

```
\
<map_1_content>
\
<map_2_content>
\
...
```

**Stage File Organization**:
- Maps are stored in `MAPS.txt`.
- They can be accessed by index number.
- Each stage corresponds to a specific UP location.
- Custom decorative tiles (B, Y, C, S) provide visual variety.

---

## Tips and Strategies

**For Both Versions**:

- **Plan ahead**: Look at the entire map before making moves.
- **Use rocks wisely**: Strategically create bridges over water.
- **Item management**: Only pick up tools when necessary (they can't be dropped).
- **Flamethrower power**: Use it on large groups of trees for efficiency.
- **Water awareness**: Plan paths carefully, as there's no recovery from water.
- **Reset liberally**: Press `!` to practice different approaches.

**Bonus Version Specific**:

- **Speedrun mode**: Memorize the best paths and minimize moves.
- **Watch cutscenes once**: Skip them on repeat plays to save time.
- **Try different characters**: A variety in visuals keeps gameplay interesting.
- **Adjust volumes**: Balance music and sound effects to fit your preference.
- **Check leaderboards**: Compare your times to find ways to improve.
- **Create an account**: Track your progress and compete globally.

---

## Troubleshooting

### Base Game Issues

**Game won't start**:
- Check Python version (needs 3.12+): `python3 --version`.
- Install dependencies: `python3 -m pip install -r requirements.txt`.
- Verify file permissions.

**Stage file errors**:
- Ensure the file exists in the correct directory.
- Confirm the filename is spelled correctly.
- Check that the file format meets specifications.

**Tests failing**:
- Make sure pytest is installed: `python3 -m pip install pytest`.
- Ensure all source files are present.
- Check for any modifications to the files.

### Bonus Version Issues

**Import errors**:
- Install any missing dependencies: `python3 -m pip install -r requirements.txt`.
- Verify that asciimatics, pygame, and bcrypt are installed.
- Check that the Python version is compatible.

**Sound not playing**:
- Ensure pygame.mixer is initialized correctly.
- Check the sound file paths in config.py.
- Confirm that audio files exist in the directory.
- Test your system's audio output.

**Database errors**:
- Delete and recreate database.db if it's corrupted.
- Check write permissions in the directory.
- Ensure bcrypt is installed for password hashing.

**Animation lag**:
- Reduce terminal size if you're experiencing performance issues.
- Skip animations by using the S key.
- Close other resource-intensive applications.

**Display issues**:
- Verify that your terminal supports UTF-8 encoding.
- Confirm emoji rendering in the terminal.
- If characters don't display correctly, try different terminal emulators.
- Adjust terminal font size for the best view.

---



## Credits

**Development Team**: Three Musketeers

**Members**:
- Sarenas, Justin Clyde
- Domingo, Jan Benedict
- Rosario, Justin Jacob

**Course**: CS 11 FIJ/MUV2

**Institution**: Department of Computer Science, College of Engineering, University of the Philippines Diliman

**Version**: 1.0 "Infinite Loop"

**Inspiration**: The culture at UP Diliman and the iconic UP Ikot jeepney system.

**Special Note**: The Mushrooms of Memory are fictional, but the Lagoon is very real. Handle with care.

---

## Academic Integrity Notice

This project follows the course's AI policy. Any use of LLMs or similar technologies was limited to providing assistance, with full transcripts submitted as required. Most of the work represents original student efforts and creative design.

---

## License and Usage

This is an academic project created for CS 11 coursework. All rights are reserved by the development team and the University of the Philippines Diliman, Department of Computer Science.

---

Thank you for playing Shroom Raider! May your loops be short and your mushrooms plentiful.

"Persistence, Failure, and Resilience" - The essential qualities of every student, every cadet, every Isko.