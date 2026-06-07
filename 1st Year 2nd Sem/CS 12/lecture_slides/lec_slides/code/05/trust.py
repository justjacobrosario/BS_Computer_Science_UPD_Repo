from __future__ import annotations
from pprint import pprint
from typing import Protocol
from collections.abc import Sequence
from enum import StrEnum, auto
from dataclasses import dataclass
 
 
class Action(StrEnum):
    COOPERATE = auto()
    CHEAT = auto()
 
 
class StrategyName(StrEnum):
    ALL_CHEAT = 'All Cheat'
    ALL_COOPERATE = 'All Cooperate'
    COPYCAT = 'Copycat'
    GRUDGER = 'Grudger'
    DETECTIVE = 'Detective'
 
    def __str__(self):
        return self.value
 
 
class GameStrategy(Protocol):
    @property
    def name(self) -> StrategyName:
        ...
 
    def get_next_action(self) -> Action:
        ...
 
    def notify_opponent_action(self, action: Action) -> None:
        ...
 
    def new_match(self) -> None:
        ...
 
 
class CopycatStrategy:
    def __init__(self):
        self.new_match()
 
    def new_match(self):
        self._last_opponent_action: Action | None = None
 
    @property
    def name(self) -> StrategyName:
        return StrategyName.COPYCAT
 
    def get_next_action(self) -> Action:
        return self._last_opponent_action if \
            self._last_opponent_action else Action.COOPERATE
 
    def notify_opponent_action(self, action: Action):
        self._last_opponent_action = action
 
 
class AlwaysCheatStrategy:
    def new_match(self):
        pass
 
    @property
    def name(self) -> StrategyName:
        return StrategyName.ALL_CHEAT
 
    def get_next_action(self) -> Action:
        return Action.CHEAT
 
    def notify_opponent_action(self, action: Action):
        pass
 
 
class AlwaysCooperateStrategy:
    def new_match(self):
        pass
 
    @property
    def name(self) -> StrategyName:
        return StrategyName.ALL_COOPERATE
 
    def get_next_action(self) -> Action:
        return Action.COOPERATE
 
    def notify_opponent_action(self, action: Action):
        pass
 
 
class GrudgerStrategy:
    def __init__(self):
        self.new_match()
 
    def new_match(self):
        self._was_ever_cheated_on = False
 
    @property
    def name(self) -> StrategyName:
        return StrategyName.GRUDGER
 
    def get_next_action(self) -> Action:
        return Action.CHEAT if self._was_ever_cheated_on \
            else Action.COOPERATE
 
    def notify_opponent_action(self, action: Action):
        self._was_ever_cheated_on |= action == Action.CHEAT
 
 
class DetectiveStrategy:
    def __init__(self):
        self.new_match()
 
    def new_match(self):
        self._last_opponent_action: Action = Action.CHEAT
        self._was_ever_cheated_on = False
        self._hardcoded_actions_left = [
            Action.COOPERATE,
            Action.CHEAT,
            Action.COOPERATE,
            Action.COOPERATE,
        ]
 
    @property
    def name(self) -> StrategyName:
        return StrategyName.DETECTIVE
 
    def get_next_action(self) -> Action:
        if self._hardcoded_actions_left:
            return self._hardcoded_actions_left.pop(0)
 
        return self._last_opponent_action \
            if self._was_ever_cheated_on \
            else Action.CHEAT
 
    def notify_opponent_action(self, action: Action):
        self._last_opponent_action = action
        self._was_ever_cheated_on |= action == Action.CHEAT
 
 
class Player:
    @classmethod
    def copycat(cls):
        return Player(CopycatStrategy())
 
    @classmethod
    def always_cheat(cls):
        return Player(AlwaysCheatStrategy())
 
    @classmethod
    def always_cooperate(cls):
        return Player(AlwaysCooperateStrategy())
 
    @classmethod
    def grudger(cls):
        return Player(GrudgerStrategy())
 
    @classmethod
    def detective(cls):
        return Player(DetectiveStrategy())
 
    def __init__(self, strategy: GameStrategy):
        self._strategy = strategy
        self._total_payoff = 0
 
    @property
    def strategy_name(self) -> StrategyName:
        return self._strategy.name
 
    @property
    def total_payoff(self) -> int:
        return self._total_payoff
 
    def add_payoff(self, value: int):
        self._total_payoff += value
 
    def get_next_action(self) -> Action:
        return self._strategy.get_next_action()
 
    def notify_opponent_action(self, action: Action) -> None:
        return self._strategy.notify_opponent_action(action)
 
    def new_match(self) -> None:
        return self._strategy.new_match()
 
 
@dataclass(frozen=True)
class RoundResult:
    round_number: int
    p1_action: Action
    p2_action: Action
    p1_payoff: int
    p2_payoff: int
 
 
@dataclass(frozen=True)
class MatchResult:
    round_results: Sequence[RoundResult]
    p1_total_payoff: int
    p2_total_payoff: int
 
 
class Payoffs:
    @classmethod
    def default(cls) -> Payoffs:
        return Payoffs(
            (+0, +0),
            (+3, -1),
            (-1, +3),
            (+2, +2),
        )
 
    def __init__(self,
                 cheat_cheat: tuple[int, int],
                 cheat_cooperate: tuple[int, int],
                 cooperate_cheat: tuple[int, int],
                 cooperate_cooperate: tuple[int, int]):
        self._cheat_cheat = cheat_cheat
        self._cheat_cooperate = cheat_cooperate
        self._cooperate_cheat = cooperate_cheat
        self._cooperate_cooperate = cooperate_cooperate
 
    def get_payoffs(self, a1: Action, a2: Action) -> tuple[int, int]:
        match a1, a2:
            case Action.CHEAT, Action.CHEAT:
                return self._cheat_cheat
 
            case Action.CHEAT, Action.COOPERATE:
                return self._cheat_cooperate
 
            case Action.COOPERATE, Action.CHEAT:
                return self._cooperate_cheat
 
            case Action.COOPERATE, Action.COOPERATE:
                return self._cooperate_cooperate
 
 
class TrustGameMatch:
    def __init__(self, p1: Player, p2: Player,
                 total_rounds: int, payoffs: Payoffs):
        self._player1 = p1
        self._player2 = p2
        self._total_rounds = total_rounds
        self._payoffs = payoffs
 
        self._round_number = 1
 
    @property
    def round_number(self) -> int:
        return self._round_number
 
    @property
    def total_rounds(self) -> int:
        return self._total_rounds
 
    def play_remaining_rounds(self) -> list[RoundResult]:
        ret: list[RoundResult] = []
 
        while self.round_number <= self.total_rounds:
            if result := self.play_round():
                ret.append(result)
 
        return ret
 
    def play_round(self) -> RoundResult | None:
        if self.round_number == 1:
            self._player1.new_match()
            self._player2.new_match()
 
        return self._play_round(
            self._player1.get_next_action(),
            self._player2.get_next_action(),
        )
 
    def _play_round(self, a1: Action, a2: Action) -> RoundResult | None:
        if (round_number := self._round_number) > self.total_rounds:
            return None
 
        self._round_number += 1
 
        payoff1, payoff2 = self._payoffs.get_payoffs(a1, a2)
 
        self._player1.notify_opponent_action(a2)
        self._player2.notify_opponent_action(a1)
 
        self._player1.add_payoff(payoff1)
        self._player2.add_payoff(payoff2)
 
        return RoundResult(
            round_number=round_number,
            p1_action=a1,
            p2_action=a2,
            p1_payoff=payoff1,
            p2_payoff=payoff2,
        )
 
 
class TrustGameTournament:
    @classmethod
    def default(cls) -> TrustGameTournament:
        p1 = Player.copycat()
        p2 = Player.always_cheat()
        p3 = Player.always_cooperate()
        p4 = Player.grudger()
        p5 = Player.detective()
 
        players = [p1, p2, p3, p4, p5]
        payoffs = Payoffs.default()
 
        return TrustGameTournament(players, 10, payoffs)
 
    def __init__(self, players: list[Player], rounds_per_match: int,
                 payoffs: Payoffs):
        self._players = list(players)
        self._rounds_per_match = rounds_per_match
        self._payoffs = payoffs
 
    @property
    def players(self):
        return list(self._players)
 
    def play_matches(self) -> list[MatchResult]:
        ret: list[MatchResult] = []
 
        for i1, p1 in enumerate(self._players):
            for i2, p2 in enumerate(self._players):
                if i1 >= i2:
                    continue
 
                match_result = self._play_match(p1, p2)
                ret.append(match_result)
 
        return ret
 
    def _play_match(self, p1: Player, p2: Player) -> MatchResult:
        m = TrustGameMatch(p1, p2, self._rounds_per_match, self._payoffs)
        results = m.play_remaining_rounds()
 
        p1_total_payoff = sum(r.p1_payoff for r in results)
        p2_total_payoff = sum(r.p2_payoff for r in results)
 
        return MatchResult(
            round_results=results,
            p1_total_payoff=p1_total_payoff,
            p2_total_payoff=p2_total_payoff,
        )
 
 
class TrustGame:
    def start(self):
        tour = TrustGameTournament.default()
        res = tour.play_matches()
        pprint(res)
 
        for p in tour.players:
            print(p.strategy_name, p.total_payoff)
 
 
TrustGame().start()