# -*- coding: utf-8 -*-
import sys
from types import NoneType

from asciimatics.effects import Print, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout
from asciimatics.exceptions import StopApplication

from config import translate
import config
import map_reader
from sound_check import play_sound

""" CONSTRUCTS A CLASS FOR THE FRAME OF BUTTONS THAT WILL BE ASSIGNED LATER"""


class AppearanceFrame(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = 22, 60

        # center the frame
        x, y = ((screen.width - width) // 2, 13)

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
            "button": (Screen.COLOUR_YELLOW, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_button": (
                Screen.COLOUR_BLACK,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
        }

        # Create layouts with proper spacing
        character_label = Layout([1])
        character_row1 = Layout([1, 1, 1, 1, 1])
        character_row2 = Layout([1, 1, 1, 1, 1])
        controller_bg_label = Layout([1])
        controller_bg_row = Layout([1, 1, 1, 1, 1, 1, 1, 1])
        controller_visuals_label = Layout([1])
        controller_visuals_row = Layout([1, 1, 1, 1, 1, 1, 1, 1])
        back_layout = Layout([1])

        self.add_layout(character_label)
        self.add_layout(character_row1)
        self.add_layout(character_row2)
        self.add_layout(controller_bg_label)
        self.add_layout(controller_bg_row)
        self.add_layout(controller_visuals_label)
        self.add_layout(controller_visuals_row)
        self.add_layout(back_layout)

        # Character selection
        character_label.add_widget(Label(""))
        character_label.add_widget(Label("-" * 50, align="^"))
        character_label.add_widget(
            Label(
                label=translate(
                    "Choose your Character",
                    "Kyarakutaa o Sentaku",
                    "Piliin ang Iyong Karakter",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        character_label.add_widget(Label("-" * 50, align="^"))
        character_label.add_widget(Label(""))

        # Row 1
        character_row1.add_widget(Button("  1  ", self.player0), 0)
        character_row1.add_widget(Button("  2  ", self.player1), 1)
        character_row1.add_widget(Button("  3  ", self.player2), 2)
        character_row1.add_widget(Button("  4  ", self.player3), 3)
        character_row1.add_widget(Button("  5  ", self.player4), 4)

        # Row 2
        character_row2.add_widget(Button("  6  ", self.player5), 0)
        character_row2.add_widget(Button("  7  ", self.player6), 1)
        character_row2.add_widget(Button("  8  ", self.player7), 2)
        character_row2.add_widget(Button("  9  ", self.player8), 3)
        character_row2.add_widget(Button(" 10  ", self.player9), 4)

        # Controller BG Color
        controller_bg_label.add_widget(Label(""))
        controller_bg_label.add_widget(Label("-" * 50, align="^"))
        controller_bg_label.add_widget(
            Label(
                label=translate(
                    "Choose UI Background Color",
                    "Haikei Karaa o Sentaku",
                    "Piliin ang Kulay ng Background ng UI",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        controller_bg_label.add_widget(Label("-" * 50, align="^"))
        controller_bg_label.add_widget(Label(""))

        controller_bg_row.add_widget(Button(" BLK ", self.bg0), 0)
        controller_bg_row.add_widget(Button(" RED ", self.bg1), 1)
        controller_bg_row.add_widget(Button(" GRN ", self.bg2), 2)
        controller_bg_row.add_widget(Button(" YEL ", self.bg3), 3)
        controller_bg_row.add_widget(Button(" BLU ", self.bg4), 4)
        controller_bg_row.add_widget(Button(" MAG ", self.bg5), 5)
        controller_bg_row.add_widget(Button(" CYN ", self.bg6), 6)
        controller_bg_row.add_widget(Button(" WHT ", self.bg7), 7)

        # Controller Visuals Color
        controller_visuals_label.add_widget(Label(""))
        controller_visuals_label.add_widget(Label("-" * 50, align="^"))
        controller_visuals_label.add_widget(
            Label(
                label=translate(
                    "Choose UI Visuals Color",
                    "Bijuaru Karaa o Sentaku",
                    "Piliin ang Kulay ng UI Visuals",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        controller_visuals_label.add_widget(Label("-" * 50, align="^"))
        controller_visuals_label.add_widget(Label(""))

        controller_visuals_row.add_widget(Button(" BLK ", self.visuals0), 0)
        controller_visuals_row.add_widget(Button(" RED ", self.visuals1), 1)
        controller_visuals_row.add_widget(Button(" GRN ", self.visuals2), 2)
        controller_visuals_row.add_widget(Button(" YEL ", self.visuals3), 3)
        controller_visuals_row.add_widget(Button(" BLU ", self.visuals4), 4)
        controller_visuals_row.add_widget(Button(" MAG ", self.visuals5), 5)
        controller_visuals_row.add_widget(Button(" CYN ", self.visuals6), 6)
        controller_visuals_row.add_widget(Button(" WHT ", self.visuals7), 7)

        # Back button
        back_layout.add_widget(Label(""))
        back_layout.add_widget(Label(""))
        back_layout.add_widget(
            Button(
                text=translate(
                    "BACK TO MAIN MENU",
                    "Mein Menyuu ni Modoru",
                    "Bumalik sa Menu",
                    config.chosen_lang,
                ),
                on_click=self.back_to_main_menu,
            ),
            0,
        )

        # finalize setup
        self.fix()

    def print_selected(self, display):
        dic = {0: "⚫", 1: "🔴", 2: "🟢", 3: "🟡", 4: "🔵", 5: "🟣", 6: "💠", 7: "⚪"}
        item = ""
        if type(display) == int:
            item = "  " + dic[display] + "  "
        else:
            item = "  " + display + "  "

        margin = "      "

        self.screen.print_at(
            margin, x=(self.screen.width - len(margin)) // 2, y=3, bg=7
        )
        self.screen.print_at(item, x=(self.screen.width - len(item)) // 2, y=4, bg=7)
        self.screen.print_at(
            margin, x=(self.screen.width - len(margin)) // 2, y=5, bg=7
        )

    # Character selection methods - store the actual emoji
    def player0(self):
        charac = "🧑"
        config.player_charac = charac
        self.print_selected(charac)

    def player1(self):
        charac = "👨"
        config.player_charac = charac
        self.print_selected(charac)

    def player2(self):
        charac = "🤴"
        config.player_charac = charac
        self.print_selected(charac)

    def player3(self):
        charac = "👨‍🦱"
        config.player_charac = charac
        self.print_selected(charac)

    def player4(self):
        charac = "👧"
        config.player_charac = charac
        self.print_selected(charac)

    def player5(self):
        charac = "👩"
        config.player_charac = charac
        self.print_selected(charac)

    def player6(self):
        charac = "👸"
        config.player_charac = charac
        self.print_selected(charac)

    def player7(self):
        charac = "👩‍🦱"
        config.player_charac = charac
        self.print_selected(charac)

    def player8(self):
        charac = "👾"
        config.player_charac = charac
        self.print_selected(charac)

    def player9(self):
        charac = "🤖"
        config.player_charac = charac
        self.print_selected(charac)

    # Background color methods
    def bg0(self):
        charac = 0
        config.bg_color = charac
        self.print_selected(charac)

    def bg1(self):
        charac = 1
        config.bg_color = charac
        self.print_selected(charac)

    def bg2(self):
        charac = 2
        config.bg_color = charac
        self.print_selected(charac)

    def bg3(self):
        charac = 3
        config.bg_color = charac
        self.print_selected(charac)

    def bg4(self):
        charac = 4
        config.bg_color = charac
        self.print_selected(charac)

    def bg5(self):
        charac = 5
        config.bg_color = charac
        self.print_selected(charac)

    def bg6(self):
        charac = 6
        config.bg_color = charac
        self.print_selected(charac)

    def bg7(self):
        charac = 7
        config.bg_color = charac
        self.print_selected(charac)

    # Visuals color methods
    def visuals0(self):
        charac = 0
        config.line_color = charac
        self.print_selected(charac)

    def visuals1(self):
        charac = 1
        config.line_color = charac
        self.print_selected(charac)

    def visuals2(self):
        charac = 2
        config.line_color = charac
        self.print_selected(charac)

    def visuals3(self):
        charac = 3
        config.line_color = charac
        self.print_selected(charac)

    def visuals4(self):
        charac = 4
        config.line_color = charac
        self.print_selected(charac)

    def visuals5(self):
        charac = 5
        config.line_color = charac
        self.print_selected(charac)

    def visuals6(self):
        charac = 6
        config.line_color = charac
        self.print_selected(charac)

    def visuals7(self):
        charac = 7
        config.line_color = charac
        self.print_selected(charac)

    def back_to_main_menu(self):
        raise StopApplication("Return to main menu")


def compile_display_appearance(screen: Screen) -> None:
    """Compile the frames to be displayed."""
    # === [ APPEARANCE TITLE ] ===

    title = FigletText(
        text=translate("Appearance", "Gaiken", "Anyo", config.chosen_lang),
        font="standard",
    )
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

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    # Put the frame inside a Scene (a collection of effects)
    scene = Scene(
        [
            bg,
            title_banner,
            AppearanceFrame(screen),
        ],
        -1,
    )  # -1 = run indefinitely until exit

    # Play the scene
    screen.play([scene])


def appearance_menu() -> NoneType:
    play_sound(config.menu_sound)
    try:
        Screen.wrapper(compile_display_appearance)
    except StopApplication:
        from menu import main_menu

        main_menu()
