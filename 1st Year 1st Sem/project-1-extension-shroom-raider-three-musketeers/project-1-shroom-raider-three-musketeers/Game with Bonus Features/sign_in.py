# -*- coding: utf-8 -*-
from ast import Global
from asciimatics.effects import Print, Stars
from asciimatics.exceptions import StopApplication
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Label, Layout, Text, layout
import data
import menu
from config import translate
import config
import sound_check
import random


class Settings(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (30, 90)
        x, y = ((screen.width - width) // 2, 11)

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

        # Color palette
        self.palette = {
            # Backgrounds
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            # Labels and buttons
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            # Text input
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            # Scrollbars, disabled widgets
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        settings = Layout([1])
        self.add_layout(settings)

        settings.add_widget(Label(""))
        settings.add_widget(
            Label(
                label=translate(
                    "Switch to different available languages.",
                    "Riyō kanōna gengo ni kirikaeru",
                    "Palitan ang wikang ginagamit",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        settings.add_widget(
            Label(
                label=translate(
                    "Interface text updates instantly.",
                    "Moji ga sugu kōshin",
                    "Agaran na mapapalitan ang mga texto",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(
            Button(
                text=translate(
                    "         LANGUAGE         ",
                    "          GENGO           ",
                    "           WIKA           ",
                    config.chosen_lang,
                ),
                on_click=self._language,
            ),
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(Label(""))

        settings.add_widget(
            Label(
                label=translate(
                    "Sign up, log in or delete your pilot profile.",
                    "Pairotto purofairu o tōroku, roguin, sakujo shimasu.",
                    "Magrehistro, mag-log in o tanggalin ang iyong pilot profile.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        settings.add_widget(
            Label(
                label=translate(
                    "Manage Isko's mission data.",
                    "Isuko no misshondēta o kanri.",
                    "Pamahalaan ang mission data ni Isko.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(
            Button(
                text=translate(
                    "         ACCOUNT          ",
                    "         AKAUNTO          ",
                    "         ACCOUNT          ",
                    config.chosen_lang,
                ),
                on_click=self._account,
            ),
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(Label(""))

        settings.add_widget(
            Label(
                label=translate(
                    "Fine tune how loud your sound trip gets.",
                    "Saundo no onryō o chōsei shimasu.",
                    "Ayusin ang lakas ng iyong sound trip.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(
            Button(
                text=translate(
                    "          SOUND           ",
                    "          SAUNDO          ",
                    "          TUNOG           ",
                    config.chosen_lang,
                ),
                on_click=self._sound,
            ),
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(Label(""))

        settings.add_widget(
            Label(
                label=translate(
                    "Learn more about the team behind the game.",
                    "Kaihatsu-sha no jōhō o miru.",
                    "Alamin ang mga Lumikha sa Likod ng Laro.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(
            Button(
                text=translate(
                    "          ABOUT           ",
                    "        NI TSUITE         ",
                    "          ABOUT           ",
                    config.chosen_lang,
                ),
                on_click=self._about,
            ),
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(Label(""))
        settings.add_widget(Label(""))
        settings.add_widget(Label("──────────────────────────────", align="^"))
        settings.add_widget(
            Button(
                text=translate(
                    "    BACK TO MAIN MENU     ",
                    "   MEIN MENYŪ NI MODORU   ",
                    "   BUMALIK SA MAIN MENU   ",
                    config.chosen_lang,
                ),
                on_click=self._back,
            ),
        )
        settings.add_widget(Label("──────────────────────────────", align="^"))

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _language(self) -> None:
        Screen.wrapper(compile_language)

    def _account(self) -> None:
        Screen.wrapper(compile_accounts)

    def _sound(self) -> None:
        Screen.wrapper(compile_sounds)

    def _about(self) -> None:
        Screen.wrapper(compile_about)

    def _back(self) -> None:
        menu.main_menu()


class Leaderboard(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (20, 65)
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

        # Color palette
        self.palette = {
            # Backgrounds
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            # Labels and buttons
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            # Text input
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            # Scrollbars, disabled widgets
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        leaderboard = Layout([1])
        self.add_layout(leaderboard)

        leaderboard.add_widget(
            Label(
                label=translate(
                    "See how your loops compare with other cadets across the system.",
                    "Shisutemu-nai no hoka no kunren-sei to, kimi no seiseki o hikaku seyo.",
                    "Paghambingin ang iyong pagganap sa iba pang kadete.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        leaderboard.add_widget(Label("───────────────────────────────", align="^"))
        leaderboard.add_widget(
            Button(
                text=translate(
                    "    🌐 GLOBAL RANKINGS    ",
                    "   🌐 GURŌBARU RANKINGU   ",
                    " 🌐 PANGKALAHATANG RANGGO ",
                    config.chosen_lang,
                ),
                on_click=self._global,
            ),
        )
        leaderboard.add_widget(Label("───────────────────────────────", align="^"))
        leaderboard.add_widget(Label(""))

        leaderboard.add_widget(Label(""))
        leaderboard.add_widget(
            Label(
                label=translate(
                    "View your mission loops saved on this device.",
                    "Kono debaisu ni hozon sa reta misshonrūpu o hyōji.",
                    "Tingnan ang iyong naka-save na mission loops sa device na ito.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        leaderboard.add_widget(Label("───────────────────────────────", align="^"))
        leaderboard.add_widget(
            Button(
                text=translate(
                    "     💾 LOCAL RECORDS     ",
                    "     💾 RŌKARU KIROKU     ",
                    "      💾 LOKAL NA TALA    ",
                    config.chosen_lang,
                ),
                on_click=self._local,
            ),
        )
        leaderboard.add_widget(Label("───────────────────────────────", align="^"))
        leaderboard.add_widget(Label(""))

        leaderboard.add_widget(Label(""))
        leaderboard.add_widget(Label(""))
        leaderboard.add_widget(
            Button(
                text=translate(" BACK ", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            ),
        )

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _global(self) -> None:
        Screen.wrapper(compile_global)

    def _local(self) -> None:
        Screen.wrapper(compile_local)

    def _back(self) -> None:
        menu.main_menu()


class GlobalRankings(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (30, 120)
        x, y = ((screen.width - width) // 2, 11)

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

        # Color palette
        self.palette = {
            # Backgrounds
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            # Labels and buttons
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            # Text input
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            # Scrollbars, disabled widgets
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        leaderboard = Layout([1, 25, 1, 25, 1, 25, 1])
        bottom = Layout([1])
        self.add_layout(leaderboard)
        self.add_layout(bottom)

        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))

        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)

        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)
        leaderboard.add_widget(Label("|", align="^"), 4)

        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)
        leaderboard.add_widget(Label("|", align="^"), 6)

        top_ten = data.global_ten("database.db")
        top_ten.extend([("", "", "")] * (10 - len(top_ten)))

        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 1
        )
        leaderboard.add_widget(
            Label(
                label=translate("NAME", "NAMAE", "PANGALAN", config.chosen_lang),
                align="^",
            ),
            1,
        )
        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 1
        )

        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[0][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[1][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[2][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[3][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[4][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[5][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[6][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[7][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[8][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{top_ten[9][0]}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 1
        )

        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 3
        )
        leaderboard.add_widget(
            Label(
                label=translate(
                    "MUSHROOMS", "KINOKO", "MGA KABUTE", config.chosen_lang
                ),
                align="^",
            ),
            3,
        )
        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 3
        )

        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[0][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[1][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[2][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[3][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[4][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[5][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[6][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[7][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[8][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{top_ten[9][2]}", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 3
        )

        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 5
        )
        leaderboard.add_widget(
            Label(
                label=translate(
                    "TIME FINISHED",
                    "KANRYŌ JIKAN",
                    "ORAS NA NATAPOS",
                    config.chosen_lang,
                ),
                align="^",
            ),
            5,
        )
        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 5
        )

        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[0][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[1][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[2][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[3][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[4][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[5][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[6][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[7][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[8][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(Label(f"{top_ten[9][1]}", align="^"), 5)
        leaderboard.add_widget(Label("", align="^"), 5)
        leaderboard.add_widget(
            Label("─────────────────────────────────────", align="^"), 5
        )

        bottom.add_widget(Label(""))
        bottom.add_widget(Label(""))
        bottom.add_widget(Label(""))
        bottom.add_widget(
            Button(
                text=translate(" BACK ", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            )
        )

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _back(self) -> None:
        raise StopApplication("User exited")


class LocalRecords(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (30, 120)
        x, y = ((screen.width - width) // 2, 11)

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

        # Color palette
        self.palette = {
            # Backgrounds
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            # Labels and buttons
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            # Text input
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            # Scrollbars, disabled widgets
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        leaderboard = Layout([1, 25, 1, 25, 1])
        bottom = Layout([1])
        self.add_layout(leaderboard)
        self.add_layout(bottom)

        self.top_ten = data.top_ten_times(config.current_user, "database.db")
        self.top_ten.extend([""] * (10 - len(self.top_ten)))

        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))
        leaderboard.add_widget(Label("|", align="^"))

        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)
        leaderboard.add_widget(Label("|", align="^"), 2)

        for i in range(25):
            leaderboard.add_widget(Label("|", align="^"), 4)

        leaderboard.add_widget(
            Label(
                "────────────────────────────────────────────────────────",
                align="^",
            ),
            1,
        )
        leaderboard.add_widget(
            Label(
                label=translate("NAME", "NAMAE", "PANGALAN", config.chosen_lang),
                align="^",
            ),
            1,
        )
        leaderboard.add_widget(
            Label(
                "────────────────────────────────────────────────────────",
                align="^",
            ),
            1,
        )

        self.user = Label(f"{config.current_user}", align="^")

        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)
        leaderboard.add_widget(Label(f"{config.current_user}", align="^"), 1)
        leaderboard.add_widget(Label("", align="^"), 1)

        leaderboard.add_widget(
            Label(
                "────────────────────────────────────────────────────────",
                align="^",
            ),
            1,
        )

        leaderboard.add_widget(
            Label(
                "────────────────────────────────────────────────────────",
                align="^",
            ),
            3,
        )
        leaderboard.add_widget(
            Label(
                label=translate(
                    "⏱️ TIME FINISHED ⏱️",
                    "⏱️ KANRYŌ JIKAN ⏱️",
                    "⏱️ ORAS NA NATAPOS ⏱️",
                    config.chosen_lang,
                ),
                align="^",
            ),
            3,
        )
        leaderboard.add_widget(
            Label(
                "────────────────────────────────────────────────────────",
                align="^",
            ),
            3,
        )

        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[0]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[1]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[2]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[3]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[4]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[5]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[6]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[7]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[8]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)
        leaderboard.add_widget(Label(f"{self.top_ten[9]} seconds", align="^"), 3)
        leaderboard.add_widget(Label("", align="^"), 3)

        leaderboard.add_widget(
            Label(
                "────────────────────────────────────────────────────────",
                align="^",
            ),
            3,
        )

        bottom.add_widget(Label(""))
        bottom.add_widget(Label(""))
        bottom.add_widget(Label(""))
        bottom.add_widget(
            Button(
                text=translate(" BACK ", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            )
        )

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _back(self) -> None:
        raise StopApplication("User exited")


class Language(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (12, 49)
        x, y = ((screen.width - width) // 2, (screen.height - height) // 2)

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

        # === Color palette ===
        self.palette = {
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        top = Layout([1, 0.5, 1, 0.5, 1])
        middle = Layout([1])
        bottom = Layout([1])
        self.add_layout(top)
        self.add_layout(middle)
        self.add_layout(bottom)

        # --- Language buttons ---
        top.add_widget(Label("─────────────────"), 0)
        top.add_widget(Button("   ENGLISH   ", self._set_language_english), 0)
        top.add_widget(Label("─────────────────"), 0)

        top.add_widget(Label("─────────────────"), 2)
        top.add_widget(Button("  JAPANESE   ", self._set_language_japanese), 2)
        top.add_widget(Label("─────────────────"), 2)

        top.add_widget(Label("─────────────────"), 4)
        top.add_widget(Button("  FILIPINO   ", self._set_language_filipino), 4)
        top.add_widget(Label("─────────────────"), 4)

        # --- Message area ---
        middle.add_widget(Label(""))
        self.message_label = Label(
            label=translate(
                "CURRENT LANGUAGE: ENGLISH",
                "CURRENT LANGUAGE: JAPANESE",
                "CURRENT LANGUAGE: FILIPINO",
                config.chosen_lang,
            ),
            align="^",
        )
        middle.add_widget(self.message_label)
        middle.add_widget(Label(""))

        # --- Back button ---
        bottom.add_widget(
            Button(
                text=translate("  BACK  ", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            ),
            0,
        )

        self.fix()
        self.screen.force_update()

    def _set_language_english(self):
        self.current_lang = "ENGLISH"
        config.chosen_lang = "english"
        self.message_label.text = f"CURRENT LANGUAGE: {'ENGLISH'}"
        self.screen.force_update()  # tell Asciimatics to redraw frame

    def _set_language_japanese(self):
        self.current_lang = "JAPANESE"
        config.chosen_lang = "japanese"
        self.message_label.text = f"CURRENT LANGUAGE: {'JAPANESE'}"
        self.screen.force_update()  # tell Asciimatics to redraw frame

    def _set_language_filipino(self):
        self.current_lang = "FILIPINO"
        config.chosen_lang = "filipino"
        self.message_label.text = f"CURRENT LANGUAGE: {'FILIPINO'}"
        self.screen.force_update()  # tell Asciimatics to redraw frame

    def _back(self):
        settings()


class Account(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (30, 50)
        x, y = ((screen.width - width) // 2, (screen.height - height) // 2 + 6)

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

        # === Color palette ===
        self.palette = {
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        layout = Layout([1])
        self.add_layout(layout)

        layout.add_widget(Label(""))
        layout.add_widget(
            Label(
                label=translate(
                    "Create a new pilot profile.",
                    "Atarashī pairotto purofairu o sakusei",
                    "Gumawa ng bagong pilot profile.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label("───────────────────────────", align="^"))
        layout.add_widget(
            Button(
                text=translate(
                    "       SIGN IN         ",
                    "        SAIN'IN        ",
                    "      MAGREHISTRO      ",
                    config.chosen_lang,
                ),
                on_click=self._sign_in,
            )
        )
        layout.add_widget(Label("───────────────────────────", align="^"))
        layout.add_widget(Label(""))

        layout.add_widget(Label(""))
        layout.add_widget(
            Label(
                label=translate(
                    "Access your saved missions.",
                    "Hozon sa reta misshon ni akusesu.",
                    "I-access ang iyong naka-save na missions.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label("───────────────────────────", align="^"))
        layout.add_widget(
            Button(
                text=translate(
                    "        LOG IN         ",
                    "         ROGUIN        ",
                    "       MAG-LOG IN      ",
                    config.chosen_lang,
                ),
                on_click=self._log_in,
            )
        )
        layout.add_widget(Label("───────────────────────────", align="^"))

        layout.add_widget(Label(""))

        layout.add_widget(Label(""))
        layout.add_widget(
            Label(
                label=translate(
                    "Delete the account currently signed in.",
                    "Genzai roguin shite iru akaunto o sakujo.",
                    "Tanggalin ang account na kasalukuyang naka-log in.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "All local data for this pilot will be erased.",
                    "Kono pairotto no subete no rōkaru dēta ga shōkyo sa remasu.",
                    "Lahat ng lokal na data para sa pilot na ito ay mabubura.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label("───────────────────────────", align="^"))
        layout.add_widget(
            Button(
                text=translate(
                    "     DELETE ACCOUNT    ",
                    "     AKAUNTO SAKUJO    ",
                    " TANGGALIN ANG ACCOUNT ",
                    config.chosen_lang,
                ),
                on_click=self._delete_account,
            )
        )
        layout.add_widget(Label("───────────────────────────", align="^"))

        layout.add_widget(Label(""))

        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))

        layout.add_widget(
            Label("=============================================", align="^")
        )
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("Pilot ID: ISKO 01", align="^"))
        layout.add_widget(Label("Status: Active", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Label("=============================================", align="^")
        )
        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Button(
                text=translate(" BACK ", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            )
        )

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _sign_in(self) -> None:
        sign_in()

    def _log_in(self) -> None:
        Screen.wrapper(compile_log_in)

    def _delete_account(self) -> None:
        if config.current_user == "GUEST":
            return
        data.delete_account(config.current_user, "database.db")
        config.current_user = "GUEST"

    def _back(self):
        settings()


class SignIn(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (16, 49)
        x, y = ((screen.width - width) // 2, (screen.height - height) // 2)

        super().__init__(
            screen,
            height,
            width,
            data={},
            x=x,
            y=y,
            can_scroll=False,
            has_border=False,
        )

        # Color palette
        self.palette = {
            # Backgrounds
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            # Labels and buttons
            "label": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            # Text input
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            # Scrollbars, disabled widgets
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        layout = Layout([1])
        bottom = Layout([1, 1, 1])
        self.add_layout(layout)
        self.add_layout(bottom)

        layout.add_widget(Label(" -                                             - "))
        layout.add_widget(
            Label(
                label=translate(
                    "   🢃   FILL-UP TO REGISTER ATTEMPT   🢃   ",
                    "   🢃          TOUROKU SURU           🢃   ",
                    "   🢃     PUNAN UPANG MAGREHISTRO     🢃   ",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label(" -                                             - "))
        layout.add_widget(Label(""))

        # Input fields
        layout.add_widget(Label(" -                                             - "))
        self.username = Text(
            label=translate(
                "    Username :", "     YŪZĀ-MEI:", "    Username :", config.chosen_lang
            ),
            name="username",
        )
        self.password = Text(
            label=translate(
                "    Password :", "     PASUWĀDO:", "    Password :", config.chosen_lang
            ),
            name="password",
            hide_char="*",
        )
        self.confirmed = Text(
            label=translate(
                "     Confirm :", "      KAKUNIN:", "   I-confirm :", config.chosen_lang
            ),
            name="confirmed",
            hide_char="*",
        )

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.confirmed)

        layout.add_widget(Label(" -                                             - "))

        layout.add_widget(Label(""))

        bottom.add_widget(
            Button(
                text=translate("Submit", "SŌSHIN", "Isumite", config.chosen_lang),
                on_click=self._submit,
            ),
            1,
        )

        bottom.add_widget(Label(""), 1)
        bottom.add_widget(Label(""), 1)

        bottom.add_widget(
            Button(
                text=translate("Quit", "SHŪRYŌ", "Umalis", config.chosen_lang),
                on_click=self._quit,
            ),
            1,
        )

        bottom.add_widget(Label(""), 1)

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _submit(self) -> None:
        self.screen.clear()

        """Print or handle submitted data."""
        # saves data
        self.save()
        # assigns the typed data to corresponding text boxes
        username = self.data.get("username", "")
        password = self.data.get("password", "")
        confirmed = self.data.get("confirmed", "")

        if len(username) < 3:
            message = f"Username must be at least 3 characters long."
            self.screen.print_at(
                message,
                y=self.screen.height - 5,
                x=self.screen.width // 2 - len(message),
            )
        elif len(password) < 8:
            message = f"Please use a stronger password."
            self.screen.print_at(
                message,
                y=self.screen.height - 5,
                x=self.screen.width // 2 - len(message),
            )
        elif password != confirmed:
            message = f"Password confirmaton doesn't match the password."
            self.screen.print_at(
                message,
                y=self.screen.height - 5,
                x=self.screen.width // 2 - len(message),
            )
        elif config.current_user != "GUEST":
            message = f"Already Logged In."
            self.screen.print_at(
                message,
                y=self.screen.height - 5,
                x=self.screen.width // 2 - len(message),
            )
        else:
            data.create_db("database.db")
            if data.is_new(username, "database.db"):
                data.sign_in(username, password, "database.db")
                message = f"Submitted: {username}, {'*' * len(password)}"
                self.screen.print_at(
                    message,
                    y=self.screen.height - 5,
                    x=self.screen.width // 2 - len(message),
                )

                config.current_user = "username"
            else:
                message = "User with this username already exists"
                self.screen.print_at(
                    message,
                    y=self.screen.height - 5,
                    x=self.screen.width // 2 - len(message),
                )
        self.screen.refresh()

    def _quit(self) -> None:
        raise StopApplication("User exited")


class LogIn(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (16, 49)
        x, y = ((screen.width - width) // 2, (screen.height - height) // 2)

        super().__init__(
            screen,
            height,
            width,
            data={},
            x=x,
            y=y,
            can_scroll=False,
            has_border=False,
        )

        # Color palette
        self.palette = {
            # Backgrounds
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            # Labels and buttons
            "label": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            # Text input
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            # Scrollbars, disabled widgets
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        layout = Layout([1])
        bottom = Layout([1, 3, 1])
        self.add_layout(layout)
        self.add_layout(bottom)

        layout.add_widget(Label(" -                                             - "))
        layout.add_widget(
            Label(
                label=translate(
                    "   🢃   ACCESS YOUR PILOT PROFILE   🢃   ",
                    "   🢃 PAIROTTO PUROFAIRU NI AKUSESU 🢃   ",
                    "  🢃 I-ACCESS ANG IYONG PILOT PROFILE 🢃 ",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label(" -                                             - "))
        layout.add_widget(Label(""))

        # Input fields
        layout.add_widget(Label(" -                                             - "))
        self.username = Text(
            label=translate(
                "    Username :", "     YŪZĀ-MEI:", "    Username :", config.chosen_lang
            ),
            name="username",
        )
        self.password = Text(
            label=translate(
                "    Password :", "     PASUWĀDO:", "    Password :", config.chosen_lang
            ),
            name="password",
            hide_char="*",
        )

        layout.add_widget(self.username)
        layout.add_widget(self.password)

        layout.add_widget(Label(" -                                             - "))

        layout.add_widget(Label(""))

        bottom.add_widget(
            Button(
                text=translate("Log in", "Roguin", "Mag-log in", config.chosen_lang),
                on_click=self._login,
            ),
            1,
        )

        bottom.add_widget(Label(""), 1)
        bottom.add_widget(Label(""), 1)

        bottom.add_widget(
            Button(
                text=translate(
                    "Continue as Guest",
                    "Gesuto Toshite Zokkō",
                    "Ituloy bilang Guest",
                    config.chosen_lang,
                ),
                on_click=self._guest,
            ),
            1,
        )

        bottom.add_widget(Label(""), 1)

        bottom.add_widget(
            Button(
                text=translate("BACK", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            ),
            1,
        )

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _login(self) -> None:
        self.screen.clear()
        # saves data
        self.save()
        # assigns the typed data to corresponding text boxes
        username = self.data.get("username", "")
        password = self.data.get("password", "")

        if config.current_user != "GUEST":
            return

        data.create_db("database.db")
        if data.log_in(username, password, "database.db"):
            config.current_user = username
            message = f"Welcome Back {config.current_user}!"
            self.screen.print_at(
                message,
                y=self.screen.height - 5,
                x=self.screen.width // 2 - len(message) // 2,
            )
            message = f"CURRENT PILOT: {config.current_user}"
            self.screen.print_at(
                message,
                y=2,
                x=5,
            )
        else:
            message = "Log In Failed"
            self.screen.print_at(
                message,
                y=self.screen.height - 5,
                x=self.screen.width // 2 - len(message),
            )

    def _guest(self) -> None:
        config.current_user = "GUEST"
        raise StopApplication("User exited")

    def _back(self) -> None:
        raise StopApplication("User exited")


class Sound(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (30, 80)
        x, y = ((screen.width - width) // 2, (screen.height - height) // 2 + 7)

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

        # === Color palette ===
        self.palette = {
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        layout = Layout([7.5, 0.3, 2.5, 14, 2.5])
        bottom = Layout([1])
        self.add_layout(layout)
        self.add_layout(bottom)

        layout.add_widget(Label("", align="<"))
        layout.add_widget(Label("─────────────────", align="<"))
        layout.add_widget(
            Label(
                label=translate(
                    "|  MAIN VOLUME  |",
                    "|  MEIN ONRYŌ   |",
                    "|  MAIN VOLUME  |",
                    config.chosen_lang,
                ),
                align="<",
            )
        )
        layout.add_widget(Label("─────────────────", align="<"))

        layout.add_widget(Label("", align="<"))

        layout.add_widget(Label("─────────────────", align="<"))
        layout.add_widget(
            Label(
                label=translate(
                    "| SOUND EFFECTS |",
                    "|     KŌKAON    |",
                    "|MGA SOUND EFFECTS|",
                    config.chosen_lang,
                ),
                align="<",
            )
        )
        layout.add_widget(Label("─────────────────", align="<"))

        layout.add_widget(Label("", align="<"), 2)
        layout.add_widget(Label("─────", align="^"), 2)
        layout.add_widget(Button("-", self._dec_main_vol), 2)
        layout.add_widget(Label("─────", align="^"), 2)

        with_bar = "|■■■" * config.main_volume
        without_bar = "|   " * (10 - config.main_volume)

        self.main_vol = Label(with_bar + without_bar + "|", align="^")

        layout.add_widget(Label("", align="<"), 3)
        layout.add_widget(
            Label("─────────────────────────────────────────", align="^"), 3
        )
        layout.add_widget(self.main_vol, 3)
        layout.add_widget(
            Label("─────────────────────────────────────────", align="^"), 3
        )

        layout.add_widget(Label("", align="<"), 4)
        layout.add_widget(Label("─────", align="^"), 4)
        layout.add_widget(Button("+", self._inc_main_vol), 4)
        layout.add_widget(Label("─────", align="^"), 4)

        layout.add_widget(Label("", align="<"), 2)
        layout.add_widget(Label("─────", align="^"), 2)
        layout.add_widget(Button("-", self._dec_snd_fx), 2)
        layout.add_widget(Label("─────", align="^"), 2)

        layout.add_widget(Label("", align="<"), 3)
        layout.add_widget(
            Label("─────────────────────────────────────────", align="^"), 3
        )

        with_bars = "|■■■" * config.sound_fx
        without_bars = "|   " * (10 - config.sound_fx)

        self.sound_fx = Label(with_bars + without_bars + "|", align="^")
        layout.add_widget(self.sound_fx, 3)
        layout.add_widget(
            Label("─────────────────────────────────────────", align="^"), 3
        )

        layout.add_widget(Label("", align="<"), 4)
        layout.add_widget(Label("─────", align="^"), 4)
        layout.add_widget(Button("+", self._inc_snd_fx), 4)
        layout.add_widget(Label("─────", align="^"), 4)

        bottom.add_widget(Label("", align="^"))
        bottom.add_widget(Label("", align="^"))
        bottom.add_widget(Label("", align="^"))

        bottom.add_widget(
            Label("===================================================", align="^")
        )
        bottom.add_widget(Label("", align="^"))
        bottom.add_widget(
            Label(
                label=translate(
                    "Tip: The Louder the orbit, the stronger the vibe.",
                    "Hinto: Kidō ga ōkī hodo, fun'iki ga tsuyoku narimasu",
                    "Tip: Mas malakas ang orbit, mas malakas ang vibe.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        bottom.add_widget(Label("", align="^"))
        bottom.add_widget(
            Label("===================================================", align="^")
        )

        bottom.add_widget(Label("", align="^"))
        bottom.add_widget(Label("", align="^"))

        bottom.add_widget(
            Button(
                text=translate("BACK", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            )
        )

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _inc_main_vol(self) -> None:
        if config.main_volume == 10:
            return

        config.main_volume += 1

        with_bars = "|■■■" * config.main_volume
        without_bars = "|   " * (10 - config.main_volume)

        self.main_vol.text = with_bars + without_bars + "|"

        sound_check.change_main_vol(config.main_volume)

        self.screen.force_update()

    def _dec_main_vol(self) -> None:
        if config.main_volume == 0:
            return

        config.main_volume -= 1

        with_bars = "|■■■" * config.main_volume
        without_bars = "|   " * (10 - config.main_volume)

        self.main_vol.text = with_bars + without_bars + "|"

        sound_check.change_main_vol(config.main_volume)

        self.screen.force_update()

    def _inc_snd_fx(self) -> None:
        if config.sound_fx == 10:
            return

        config.sound_fx += 1

        with_bars = "|■■■" * config.sound_fx
        without_bars = "|   " * (10 - config.sound_fx)

        self.sound_fx.text = with_bars + without_bars + "|"

        sound_check.change_sound_fx_vol(config.sound_fx)
        self.screen.force_update()

    def _dec_snd_fx(self) -> None:
        if config.sound_fx == 0:
            return

        config.sound_fx -= 1

        with_bars = "|■■■" * config.sound_fx
        without_bars = "|   " * (10 - config.sound_fx)

        self.sound_fx.text = with_bars + without_bars + "|"

        sound_check.change_sound_fx_vol(config.sound_fx)
        self.screen.force_update()

    def _back(self) -> None:
        settings()


class About(Frame):
    def __init__(self, screen: Screen) -> None:
        height, width = (30, 90)
        x, y = ((screen.width - width) // 2, (screen.height - height) // 2 + 6)

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

        # === Color palette ===
        self.palette = {
            "background": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "label": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "button": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_button": (
                Screen.COLOUR_WHITE,
                Screen.A_NORMAL,
                Screen.COLOUR_YELLOW,
            ),
            "edit_text": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE),
            "focus_edit_text": (
                Screen.COLOUR_WHITE,
                Screen.A_BOLD,
                Screen.COLOUR_YELLOW,
            ),
            "field": (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK),
            "focus_field": (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_YELLOW),
            "disabled": (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK),
        }

        # === Layout setup ===
        layout = Layout([1])
        bottom = Layout([1, 1, 1])
        self.add_layout(layout)
        self.add_layout(bottom)

        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Label(
                label=translate(
                    "Organization: Three Musketeers",
                    "Soshiki: Sanjūshi",
                    "Organisasyon: Three Musketeers",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "Section: CS11 FIJ/MUV2",
                    "Sekushon: CS11 FIJ/MUV2",
                    "Seksyon: CS11 FIJ/MUV2",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Label(
                label=translate("Members:", "Menbā:", "Menbā:", config.chosen_lang),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "- Sarenas, Justin Clyde",
                    "- Sarenas, Justin Clyde",
                    "- Sarenas, Justin Clyde",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "- Domingo, Jan Benedict",
                    "- Domingo, Jan Benedict",
                    "- Domingo, Jan Benedict",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "- Rosario, Justin Jacob",
                    "- Rosario, Justin Jacob",
                    "- Rosario, Justin Jacob",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Label(
                label=translate(
                    'Version 1.0 "Infinite Loop"',
                    "Bājon 1.0 'Mugen Rūpu'",
                    "Bersyon 1.0 'Infinite Loop'",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "A student-made project inspired by",
                    "Gakusei ga sakusei shita purojekuto, insupaia sa reta:",
                    "Isang proyektong gawa ng mga mag-aaral na inspired ng:",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "UP Diliman's culture and UP ikot",
                    "UP Diriman no bunka to UP ikotto",
                    "kultura ng UP Diliman at UP ikot",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label("", align="^"))
        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Label("===========================================", align="^")
        )
        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Label(
                label=translate(
                    "Tip: Mushrooms of Memory are fictional.",
                    "Hinto: Kioku no kinoko wa kakū no mono desu.",
                    "Tip: Ang mga Mushrooms of Memory ay kathang-isip lamang.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(
            Label(
                label=translate(
                    "But the Lagoon is very real.",
                    "Shikashi, ragūn wa honmono desu.",
                    "Pero ang Lagoon ay totoo.",
                    config.chosen_lang,
                ),
                align="^",
            )
        )
        layout.add_widget(Label("", align="^"))
        layout.add_widget(
            Label("===========================================", align="^")
        )
        layout.add_widget(Label("", align="^"))

        bottom.add_widget(Label("────────────────", align="^"), 1)

        bottom.add_widget(
            Button(
                text=translate("   BACK   ", "MODORU", "BUMALIK", config.chosen_lang),
                on_click=self._back,
            ),
            1,
        )

        bottom.add_widget(Label("────────────────", align="^"), 1)

        self.auto_date = False  # toggle flag
        self.fix()

        # Refresh the widget data and force redraw
        self.fix()
        self.screen.force_update()

    def _back(self):
        settings()


def compile_sign_in(screen: Screen) -> None:
    title = FigletText(
        text=translate(
            "User Portal",
            "Yūzā Pōtaru",
            "Portal ng User",
            config.chosen_lang,
        ),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, SignIn(screen)], -1)
    screen.play([scene])


def compile_leaderboard(screen: Screen) -> None:
    title = FigletText(
        text=translate("LEADERBOARD", "RĪDĀBŌDO", "LEADERBOARD", config.chosen_lang),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, Leaderboard(screen)], -1)
    screen.play([scene])


def compile_log_in(screen: Screen) -> None:
    title = FigletText(
        text=translate(
            "User Portal", "YŪZĀ PŌTARU", "Portal ng User", config.chosen_lang
        ),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, LogIn(screen)], -1)
    screen.play([scene])


def compile_sounds(screen: Screen) -> None:
    title = FigletText(
        text=translate("SOUND", "SAUNDO", "TUNOG", config.chosen_lang), font="standard"
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, Sound(screen)], -1)
    screen.play([scene])


def compile_accounts(screen: Screen) -> None:
    title = FigletText(
        text=translate("ACCOUNTS", "AKAUNTO", "MGA ACCOUNT", config.chosen_lang),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, Account(screen)], -1)
    screen.play([scene])


def compile_global(screen: Screen) -> None:
    title = FigletText(
        text=translate(
            "GLOBAL RANKINGS",
            "GURŌBARU RANKINGU",
            "PANDAIGDIGANG RANGGO",
            config.chosen_lang,
        ),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, GlobalRankings(screen)], -1)
    screen.play([scene])


def compile_local(screen: Screen) -> None:
    title = FigletText(
        text=translate(
            "LOCAL RECORDS", "RŌKARU REKŌDO", "LOKAL NA REKORD", config.chosen_lang
        ),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, LocalRecords(screen)], -1)
    screen.play([scene])


def compile_language(screen: Screen) -> None:
    title = FigletText(
        text=translate("LANGUAGE", "GENGO", "WIKA", config.chosen_lang), font="standard"
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, Language(screen)], -1)
    screen.play([scene])


def compile_about(screen: Screen) -> None:
    title = FigletText(
        text=translate("ABOUT", "NI TSUITE", "ABOUT", config.chosen_lang),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, About(screen)], -1)
    screen.play([scene])


def compile_settings(screen: Screen) -> None:
    title = FigletText(
        text=translate("SETTINGS", "SETTEI", "SETTINGS", config.chosen_lang),
        font="standard",
    )
    title_x = (screen.width - len(str(title).splitlines()[2])) // 2
    title_y = 5
    title_banner = Print(
        screen,
        title,
        title_y,
        title_x,
        colour=Screen.COLOUR_YELLOW,
        speed=0,
    )

    bg = Stars(screen, count=150, pattern="..+..   ...x...  ...*...")

    scene = Scene([bg, title_banner, Settings(screen)], -1)
    screen.play([scene])


def settings() -> None:
    Screen.wrapper(compile_settings)


def sign_in() -> None:
    Screen.wrapper(compile_sign_in)


def leaderboard() -> None:
    Screen.wrapper(compile_leaderboard)
