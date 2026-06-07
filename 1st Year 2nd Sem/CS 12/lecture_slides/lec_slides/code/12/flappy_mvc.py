from __future__ import annotations
from collections import deque
from collections.abc import Sequence
from dataclasses import dataclass
from enum import StrEnum
from random import randint
from typing import Protocol

import pyxel

FPS = 60
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 140
GROUND_HEIGHT = 6


class ViewObserver(Protocol):
    def do_stuff(self):
        ...


@dataclass(frozen=True, slots=True)
class BirdInfo:
    x: float
    y: float
    radius: float
    color: int = 10


@dataclass(frozen=True, slots=True)
class PipeInfo:
    x: float
    y: float
    width: float
    height: float
    color: int = 11


@dataclass
class Bird:
    x: float
    y: float
    radius: float
    v_y: float
    a_y: float
    color: int = 10

    def is_colliding_with_pipe(self, pipe: Pipe) -> bool:
        tl = (pipe.x, pipe.y)
        tr = (pipe.x + pipe.width, pipe.y)
        bl = (pipe.x, pipe.y + pipe.height)
        br = (pipe.x + pipe.width, pipe.y + pipe.height)
        corners = (tl, tr, bl, br)

        for x, y in corners:
            dx2 = (self.x - x)**2
            dy2 = (self.y - y)**2
            if dx2 + dy2 <= self.radius**2:
                return True

        if self.x + self.radius >= pipe.x and self.x + self.radius <= pipe.x + pipe.width:
            if self.y + self.radius >= pipe.y and self.y - self.radius <= pipe.y + pipe.height:
                return True
        return False
    

@dataclass
class Pipe:
    x: float
    y: float
    width: float
    height: float
    done: bool = False
    color: int = 11
    v_x: float = 0.0


class FlappyState(StrEnum):
    PENDING = 'pending'
    ONGOING = 'ongoing'
    GAME_OVER = 'game over'


class FlappyModel:
    def __init__(self, bird_v_y, bird_a_y, pipe_v_x):
        self._bird_v_y = bird_v_y
        self._bird_a_y = bird_a_y
        self._pipe_v_x = pipe_v_x
        self._bird = None
        self._pipes = deque([])
        self._state = FlappyState.PENDING

    def reset(self):
        self._bird = Bird(
            SCREEN_WIDTH / 5, SCREEN_HEIGHT / 2, 6,
            self._bird_v_y, self._bird_a_y
        )
        self._score = 0
        self._pipes.clear()
        self._state = FlappyState.PENDING
        self._setup_pipes()

    def _setup_pipes(self):
        for i in range(5):
            offset = i * 60
            height = randint(SCREEN_HEIGHT // 8, 4 * SCREEN_HEIGHT // 7)
            gap = 40
            pipe_top = Pipe(3 * SCREEN_WIDTH / 4 + offset, 0, 16, height)
            pipe_top.v_x = self._pipe_v_x
            pipe_bot = Pipe(3 * SCREEN_WIDTH / 4 + offset, height + gap, 16, SCREEN_HEIGHT - height - gap - GROUND_HEIGHT)
            pipe_bot.v_x = self._pipe_v_x
            self._pipes.extend((pipe_top, pipe_bot))

    def _cycle_pipes(self):
        assert self._pipes
        pipe_top = self._pipes[0]
        pipe_bot = self._pipes[1]
        if not pipe_top.done and pipe_top.x + pipe_top.width < self._bird.x - self._bird.radius:
            self._score += 1
            pipe_top.done = True
            pipe_bot.done = True
        if pipe_top.x + pipe_top.width < 0:
            self._pipes.popleft()
            self._pipes.popleft()
            offset = 60
            height = randint(SCREEN_HEIGHT // 8, 4 * SCREEN_HEIGHT // 7)
            gap = 46
            pipe_top.done = pipe_bot.done = False
            pipe_top.x = self._pipes[-1].x + offset
            pipe_top.height = height
            pipe_bot.x = self._pipes[-1].x + offset
            pipe_bot.y = height + gap
            pipe_bot.height = SCREEN_HEIGHT - height - gap - GROUND_HEIGHT
            self._pipes.append(pipe_top)
            self._pipes.append(pipe_bot)

    def tick(self):
        match self._state:
            case FlappyState.PENDING:
                pass
            case FlappyState.ONGOING:
                self._bird.y += self._bird.v_y
                self._bird.v_y += self._bird.a_y
                for pipe in self._pipes:
                    pipe.x += pipe.v_x

                    if self._bird.is_colliding_with_pipe(pipe):
                        self._state = FlappyState.GAME_OVER

                if self._bird.y + self._bird.radius >= SCREEN_HEIGHT - GROUND_HEIGHT:
                    self._state = FlappyState.GAME_OVER

                self._cycle_pipes()
            case FlappyState.GAME_OVER:
                pass

    def press_space(self):
        match self._state:
            case FlappyState.PENDING | FlappyState.ONGOING:
                self._state = FlappyState.ONGOING
                self._bird.v_y = self._bird_v_y
            case FlappyState.GAME_OVER:
                pass

    def press_r(self):
        self.reset()

    @property
    def score(self):
        return self._score

    @property
    def bird_info(self):
        bird = self._bird
        return BirdInfo(bird.x, bird.y, bird.radius, bird.color)

    @property
    def pipes_info(self):
        return tuple(
            PipeInfo(pipe.x, pipe.y, pipe.width, pipe.height, pipe.color)
            for pipe in self._pipes
        )

    @classmethod
    def default(cls):
        model = cls(-2.1, 0.14, -30 / FPS)
        model.reset()
        return model


class FlappyView:
    def draw(self, bird_info: BirdInfo, pipes_info: Sequence[PipeInfo], score: int):
        pyxel.cls(6)
        
        pyxel.rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT, 4)
        for pipe in pipes_info:
            pyxel.rect(pipe.x, pipe.y, pipe.width, pipe.height, pipe.color)

        pyxel.circ(bird_info.x, bird_info.y, bird_info.radius, bird_info.color)

        pyxel.text(5, 5, str(score), 7)
        pyxel.text(SCREEN_WIDTH - 45, 5, 'Restart: R', 7)

    def is_space_pressed(self):
        return pyxel.btnp(pyxel.KEY_SPACE)

    def is_r_pressed(self):
        return pyxel.btnp(pyxel.KEY_R)


class FlappyController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def update(self):
        model = self._model

        if self._view.is_space_pressed():
            model.press_space()

        if self._view.is_r_pressed():
            model.press_r()

        model.tick()

    def draw(self):
        model = self._model
        self._view.draw(model.bird_info, model.pipes_info, model.score)

    def start(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=FPS)
        pyxel.run(self.update, self.draw)


if __name__ == '__main__':
    model = FlappyModel.default()
    view = FlappyView()
    controller = FlappyController(model, view)
    controller.start()