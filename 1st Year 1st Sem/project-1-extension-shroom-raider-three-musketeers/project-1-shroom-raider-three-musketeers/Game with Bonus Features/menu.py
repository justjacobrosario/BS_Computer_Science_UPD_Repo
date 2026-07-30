# -*- coding: utf-8 -*-
import sys
from types import NoneType

from asciimatics.effects import Print, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout

from config import translate
import config
from appearance import appearance_menu
from game import new_game
from sign_in import sign_in, settings, leaderboard
from sound_check import play_sound
import game_modes

""" CONSTRUCTS A CLASS FOR THE FRAME OF BUTTONS THAT WILL BE ASSIGNED LATER"""


class MainMenuFrame(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = 20, 35

        # center the frame
        x, y = ((screen.width - width) // 2, 14)

        super().__init__(
            screen,
            height,
            width,
            data={},
            x=x,
            y=y,
            can_scroll=False,
            has_border=False,
            hover_focus=True,
        )

        # color palette
        self.palette = {
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "label": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
        }

        main_menu = Layout([4])
        bottom_menu = Layout(
            [
                1,
                0.5,
                1,
            ],
        )
        quit_menu = Layout([1])
        self.add_layout(main_menu)
        self.add_layout(bottom_menu)
        self.add_layout(quit_menu)

        # centered column
        main_menu.add_widget(Label("───────────────────────────────────"))
        main_menu.add_widget(
            Button(text = translate("         SPEEDRUN MODE         ", 
                                    "        Supiido Ran Moodo      ", 
                                    "         SPEEDRUN MODE         ", config.chosen_lang), on_click = self._speedrun_mode),
        )
        main_menu.add_widget(Label("───────────────────────────────────"))
        main_menu.add_widget(Label(""))
        main_menu.add_widget(Label("───────────────────────────────────"))
        main_menu.add_widget(
            Button(text = translate("          STORY MODE           ", 
                                    "         Sutoorii Moodo       ", 
                                    "          STORY MODE           ", config.chosen_lang), on_click =  self._story_mode),
        )
        main_menu.add_widget(Label("───────────────────────────────────"))
        main_menu.add_widget(Label(""))
        main_menu.add_widget(Label("───────────────────────────────────"))
        main_menu.add_widget(
            Button(text = translate("          LEADERBOARD          ", 
                                    "          Riidaaboodo          ", 
                                    "          LEADERBOARD          ", config.chosen_lang), on_click = self._leaderboard),
        )
        main_menu.add_widget(Label("───────────────────────────────────"))
        main_menu.add_widget(Label(""))
        main_menu.add_widget(Label(""))

        bottom_menu.add_widget(Label(label = translate("───Settings───", 
                                                       "────Settei────", 
                                                       "───Settings───", config.chosen_lang)), 0)
        bottom_menu.add_widget(Button("    ⚙     ", self._settings), 0)
        bottom_menu.add_widget(Label("──────────────"), 0)

        quit_menu.add_widget(Label(""))
        quit_menu.add_widget(Label(""))
        quit_menu.add_widget(Label(""))

        quit_menu.add_widget(Button(text = translate(" QUIT ", "Shuuryou", "UMALIS", config.chosen_lang), on_click = self._quit))

        bottom_menu.add_widget(Label(label = translate("───Customize──", 
                                                       "─ Kasutamaizu─", "───Customize──", config.chosen_lang)), 2)
        bottom_menu.add_widget(Button("    🖌     ", self._appearance), 2)
        bottom_menu.add_widget(Label("──────────────"), 2)

        # finalize main_menu setup
        self.fix()

    def _story_mode(self) -> None:
        # This is the function called when the story mode button is pressed
        play_sound("andromeda-space-adventure-403080.mp3", play=False)
        return game_modes.story_mode()

    def _speedrun_mode(self) -> None:
        # This is the function called when the speedrun mode button is pressed
        play_sound("andromeda-space-adventure-403080.mp3", play=False)
        return game_modes.speedrun_mode()

    def _quit(self) -> None:
        # This is the function called when the quit button is pressed
        sys.exit(0)

    def _sign_in(self) -> NoneType:
        return sign_in()

    def _settings(self) -> None:
        return settings()

    def _leaderboard(self) -> None:
        if config.current_user == "GUEST":
            return sign_in()
        return leaderboard()

    def _appearance(self) -> None:
        return appearance_menu()


def compile_display_main_menu(screen: Screen) -> None:
    """Compile the frames to be dispayed."""
    # === [ SHROOM RAIDER TITLE ] ===

    title = FigletText(text = translate("Shroom Raider", "Shurūmu Reidā", "Shroom Raider", config.chosen_lang), font="standard")
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 7
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg_effect = Stars(screen, count=200, pattern="..+..   ...x...  ...*...")

    # Put the frame inside a Scene (a collection of effects)
    scene = Scene(
        [
            bg_effect,
            title_banner,
            MainMenuFrame(screen),
        ],
        -1,
    )  # -1 = run indefinitely until exit

    # Play the scene
    screen.play([scene])


def main_menu() -> NoneType:
    play_sound(config.menu_sound)
    return Screen.wrapper(compile_display_main_menu)