from __future__ import annotations
from enum import Enum, auto
import pyxel 

# directions for the wasd directions of the bullet
class Dir(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    CURSOR = auto()

# Command messages for general instructions
class Msg(Enum):
    SHOOT = auto()
    SHIFTMODE = auto()
    CONTINUE = auto()
    QUIT = auto()
    SHOOT_UP = auto()
    SHOOT_DOWN = auto()
    SHOOT_LEFT = auto()
    SHOOT_RIGHT = auto()
    SHOOT_UP_2 = auto()
    SHOOT_DOWN_2 = auto()
    SHOOT_LEFT_2 = auto()
    SHOOT_RIGHT_2 = auto()

class Player:
    def __init__(self) -> None:
        # User key mapping
        self._keys_map: dict[Msg, int] = {
            Msg.SHOOT        : pyxel.MOUSE_BUTTON_LEFT,
            Msg.SHIFTMODE    : pyxel.KEY_SHIFT,
            Msg.CONTINUE     : pyxel.KEY_SPACE,
            Msg.QUIT         : pyxel.KEY_Q,
            Msg.SHOOT_UP     : pyxel.KEY_W,
            Msg.SHOOT_DOWN   : pyxel.KEY_S,
            Msg.SHOOT_LEFT   : pyxel.KEY_A,
            Msg.SHOOT_RIGHT  : pyxel.KEY_D,
            Msg.SHOOT_UP_2   : pyxel.KEY_UP,
            Msg.SHOOT_DOWN_2 : pyxel.KEY_DOWN,
            Msg.SHOOT_LEFT_2 : pyxel.KEY_LEFT,
            Msg.SHOOT_RIGHT_2: pyxel.KEY_RIGHT
        }

    @property
    def keys_map(self) -> dict[Msg, int]:
        return self._keys_map
    