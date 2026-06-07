from enum import StrEnum, auto
from typing import Protocol


class Choice(StrEnum):
    CHEAT = auto()
    COOPERATE = auto()


class Kind(StrEnum):
    ALWAYS_COOP = auto()
    ALWAYS_CHEAT = auto()
    COPYCAT = auto()
    GRUDGER = auto()
    RANDOM = auto()
    DETECTIVE = auto()


# OCP
# Open-Closed Principle
# Open to addition
# Closed to modification

# kind -> strategy


# if the implementation of the methods are what differ
# use a protocol
class Strategy(Protocol):
    @property
    def kind(self) -> Kind: ...

    def make_choice(self, turn: int) -> Choice: ...

    def get_notified(self, choice: Choice): ...


class AlwaysCheatStrategy(Strategy):
    @property
    def kind(self):
        return Kind.ALWAYS_CHEAT

    def make_choice(self, turn: int) -> Choice:
        return Choice.CHEAT

    def get_notified(self, choice: Choice):
        pass


class CopycatStrategy(Strategy):
    def __init__(self):
        self._opponent_prev_choice = None

    @property
    def kind(self):
        return Kind.COPYCAT

    def make_choice(self, turn: int) -> Choice:
        if turn == 0:
            return Choice.COOPERATE
        else:
            assert self._opponent_prev_choice is not None
            return self._opponent_prev_choice

    def get_notified(self, choice: Choice):
        self._opponent_prev_choice = choice


class AlwaysCoopStrategy(Strategy):
    @property
    def kind(self):
        return Kind.ALWAYS_COOP

    def make_choice(self, turn: int) -> Choice:
        return Choice.COOPERATE

    def get_notified(self, choice: Choice):
        pass


class DetectiveStrategy(Strategy):
    def __init__(self):
        self._turns_so_far = 0
        self._betrayed = False

    @property
    def kind(self) -> Kind:
        return Kind.DETECTIVE

    def make_choice(self, turn: int) -> Choice:
        if turn in (0, 2, 3):
            return Choice.COOPERATE
        elif turn == 1:
            return Choice.CHEAT
        else:
            return Choice.COOPERATE if not self._betrayed else Choice.CHEAT

    def get_notified(self, choice: Choice):
        if self._turns_so_far < 4 and choice == Choice.CHEAT:
            self._betrayed = True
        self._turns_so_far += 1


class GrudgerStrategy(Strategy):
    def __init__(self):
        self._betrayed = False

    @property
    def kind(self):
        return Kind.GRUDGER

    def make_choice(self, turn: int) -> Choice:
        if not self._betrayed:
            return Choice.COOPERATE
        else:
            return Choice.CHEAT

    def get_notified(self, choice: Choice):
        if choice == Choice.CHEAT:
            self._betrayed = True


import random


class RandomStrategy(Strategy):
    @property
    def kind(self):
        return Kind.RANDOM

    def make_choice(self, turn: int) -> Choice:
        return random.choice((Choice.CHEAT, Choice.COOPERATE))

    def get_notified(self, choice: Choice):
        pass


class Player:
    def __init__(self, strategy: Strategy):
        self._tokens = 0
        self._strategy = strategy

    @property
    def tokens(self):
        return self._tokens

    def add_tokens(self, num_tokens: int):
        self._tokens += num_tokens

        if self._tokens < 0:  # avoids negative # of tokens
            self._tokens = 0

    def get_notified(self, choice: Choice):
        self._strategy.get_notified(choice)

    def make_choice(self, turn: int) -> Choice:
        return self._strategy.make_choice(turn)


class Match:
    def __init__(self, p1: Player, p2: Player):
        self._p1 = p1
        self._p2 = p2

        self.turn = 0
        self.rounds_left = 10

    def do_entire_match(self):
        while not self.is_game_over:
            print(self.do_one_round())

    @property
    def is_game_over(self):
        return self.rounds_left == 0

    def do_one_round(self):
        c1 = self._p1.make_choice(self.turn)
        c2 = self._p2.make_choice(self.turn)

        match c1, c2:
            case Choice.CHEAT, Choice.CHEAT:
                self._p1.add_tokens(0)
                self._p2.add_tokens(0)
            case Choice.CHEAT, Choice.COOPERATE:
                self._p1.add_tokens(3)
                self._p2.add_tokens(-1)
            case Choice.COOPERATE, Choice.CHEAT:
                self._p1.add_tokens(-1)
                self._p2.add_tokens(3)
            case Choice.COOPERATE, Choice.COOPERATE:
                self._p1.add_tokens(2)
                self._p2.add_tokens(2)

        self._p1.get_notified(c2)
        self._p2.get_notified(c1)

        self.turn += 1
        self.rounds_left -= 1

        return c1.value, c2.value, self._p1.tokens, self._p2.tokens
