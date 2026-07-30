# -*- coding: utf-8 -*-
import sys
from random import choice, randint

from asciimatics.effects import Print, Stars
from asciimatics.exceptions import ResizeScreenError
from asciimatics.particles import SerpentFirework, StarFirework
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from config import translate
import config
import sound_check


def compile_winner(screen: Screen) -> None:
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(
            screen,
            SpeechBubble(text = translate("[Q] Quit to Menu \n [R] Restart Stage", "[Q] Menyuu ni Modoru \n [R] Suteeji Saichousen", "[Q] Bumalik sa Menu \n [R] I-restart ang Stage", config.chosen_lang)),
            y=screen.height - 14,
            start_frame=5,
            colour=3,
        ),
    ]
    for _ in range(20):
        fireworks = [
            (SerpentFirework, 120, 150),
            (StarFirework, 120, 150),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(
                screen,
                randint(0, screen.width),
                randint(screen.height // 8, screen.height * 3 // 4),
                randint(start, stop),
                start_frame=randint(0, 250),
            ),
        )

    effects.append(
        Print(
            screen,
            FigletText(text = translate("G A M E", "G E E M U", "T A G U M P A Y", config.chosen_lang), font="colossal"),
            screen.height // 2 - 15,
            speed=1,
            start_frame=0,
            colour=3,
        ),
    )
    effects.append(
        Print(
            screen,
            FigletText(text = translate("C O M P L E T E D !", "K A N R Y O U !", "A N G  L A R O", config.chosen_lang), font="colossal"),
            screen.height // 2 - 5,
            speed=1,
            start_frame=3,
            colour=3,
        ),
    )
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)


def winner() -> None:
    sound_check.play_sound(config.win_sound)
    while True:
        try:
            Screen.wrapper(compile_winner)
            sys.exit(0)
        except ResizeScreenError:
            pass