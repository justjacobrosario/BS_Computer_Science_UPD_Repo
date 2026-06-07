class TrustGameSimulator:
    def __init__(self, p1: Character, p2: Character):
        self._p1_char = p1
        self._p2_char = p2
        self._p1_payoff = 0
        self._p2_payoff = 0
 
    def simulate_rounds(self, rounds: int):
        for _ in range(rounds):
            a1 = self.get_action(self._p1_char)
            a2 = self.get_action(self._p2_char)
 
            p1, p2 = self.get_payoffs(a1, a2)
            self._p1_payoff += p1
            self._p2_payoff += p2
 
    def get_action(self, c: Character) -> Action:
        match c:
            case Character.ALWAYS_CHEAT:
                return Action.CHEAT
            case Character.ALWAYS_COOPERATE:
                return Action.COOPERATE
            case Character.RANDOM:  # Added code
                return random.choice(list(Action))
 
    def get_payoffs(self, a1: Action, a2: Action):
        match a1, a2:
            case Action.CHEAT, Action.CHEAT:
                return (+0, +0)
 
            case Action.COOPERATE, Action.CHEAT:
                return (-1, +3)
 
            case Action.CHEAT, Action.COOPERATE:
                return (+3, -1)
 
            case Action.COOPERATE, Action.COOPERATE:
                return (+2, +2)
 
    @property
    def p1_payoff(self):
        return self._p1_payoff
 
    @property
    def p2_payoff(self):
        return self._p2_payoff


import random
from enum import StrEnum, auto
 
class Action(StrEnum):
    CHEAT = auto()
    COOPERATE = auto()
 
class Character(StrEnum):
    ALWAYS_CHEAT = auto()
    ALWAYS_COOPERATE = auto()
    RANDOM = auto()  # Added code
 
if __name__ == '__main__':
    sim = TrustGameSimulator(
        Character.RANDOM, Character.RANDOM)
    sim.simulate_rounds(5)
 
    print('P1:', sim.p1_payoff)
    print('P2:', sim.p2_payoff)
