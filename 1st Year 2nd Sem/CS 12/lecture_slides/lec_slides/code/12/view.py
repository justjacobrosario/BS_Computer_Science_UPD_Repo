from collections.abc import Sequence
from typing import Protocol
import pyxel
from types import *


class UpdateHandler(Protocol):
    def update(self): ...


class DrawHandler(Protocol):
    def draw(self): ...


# Controller <: UpdateHandler
# Controller <: DrawHandler


class View:
    def draw_bird(self, bird) -> None:
        pyxel.circ(bird.x, bird.y, bird.r, pyxel.COLOR_YELLOW)

    def start_game(self, update_handler: UpdateHandler, draw_handler: DrawHandler):
        pyxel.init(250, 250, fps=30)
        pyxel.run(update_handler.update, draw_handler.draw)

    def draw_pipes(self, pipes) -> None:
        for pipe_pair in pipes:
            # first pipe
            pyxel.rect(
                pipe_pair.x, pipe_pair.y, pipe_pair.w, pipe_pair.h, pyxel.COLOR_GREEN
            )
            # second pipe
            pyxel.rect(
                pipe_pair.x,
                pyxel.height - pipe_pair.h,
                pipe_pair.w,
                pipe_pair.h,
                pyxel.COLOR_GREEN,
            )

    def draw_score(self, score: int) -> None:
        pyxel.text(
            pyxel.width // 2,
            pyxel.height // 2 - pyxel.height // 10,
            str(score),
            pyxel.COLOR_WHITE,
        )

    def reset_screen(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)
