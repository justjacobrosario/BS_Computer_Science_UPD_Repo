# -*- coding: utf-8 -*-
import sys

from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import FigletText, Fire, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from config import translate
import config
import sound_check


def compile_lose(screen: Screen) -> None:
    """Set up the lose screen."""
    scenes = []
    effects = [
        Print(
            screen,
            Fire(
                screen.height,
                80,
                "*" * 70,
                0.8,
                60,
                screen.colours,
                bg=screen.colours >= 256,
            ),
            y=0,
            x=-40,
            speed=1,
            transparent=False,
        ),
        Print(
            screen,
            Fire(
                screen.height,
                80,
                "*" * 70,
                0.8,
                60,
                screen.colours,
                bg=screen.colours >= 256,
            ),
            y=0,
            x=screen.width - 40,
            speed=1,
            transparent=False,
        ),
        Print(
            screen,
            SpeechBubble(
                text=translate(
                    "[Q] Quit to Menu \n [!] Restart Stage",
                    "[Q] Menyuu ni Modoru \n [!] Suteeji Saichousen",
                    "[Q] Bumalik sa Menu \n [!] I-restart ang Stage",
                    config.chosen_lang,
                )
            ),
            y=screen.height - 15,
            start_frame=0,
            colour=3,
        ),
    ]

    effects.append(
        Print(
            screen,
            FigletText(
                text=translate(
                    "Y O U", "K I M I  W A", "N A M A T A Y", config.chosen_lang
                ),
                font="colossal",
            ),
            screen.height // 2 - 15,
            speed=1,
            start_frame=0,
            colour=1,
        ),
    )

    effects.append(
        Print(
            screen,
            FigletText(
                text=translate(
                    " D I E D !", "S H I N D A !", "K A !", config.chosen_lang
                ),
                font="colossal",
            ),
            screen.height // 2 - 5,
            speed=1,
            start_frame=3,
            colour=1,
        ),
    )

    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)


def lose() -> None:
    """Run the lose screen."""
    sound_check.play_sound(config.lose_sound)
    while True:
        try:
            Screen.wrapper(compile_lose)
            sys.exit(0)
        except ResizeScreenError:
            pass
