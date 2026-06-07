class Player(ABC):
    def __init__(self):
        self.payoff = 0  # `payoff` is to be inherited
 
    @abstractmethod
    def get_next_action(self) -> Action:
        raise NotImplementedError
 
    def notify_opponent_action(self, action: Action):
        pass
 
 
class AlwaysCheatPlayer(Player):
    def get_next_action(self) -> Action:
        return Action.CHEAT
 
 
class AlwaysCooperatePlayer(Player):
    def get_next_action(self) -> Action:
        return Action.COOPERATE
 
 
class CopycatPlayer(Player):
    # TODO: Implement this yourself as practice


class Action(StrEnum):
    CHEAT = auto()
    COOPERATE = auto()
 
def main():
    if __name__ == '__main__':
        sim = TrustGameSimulator(
          AlwaysCheatPlayer(),
          AlwaysCooperatePlayer(),
        )
        sim.simulate_rounds(5)
    
        print('P1:', sim.p1_payoff)
        print('P2:', sim.p2_payoff)
 
class TrustGameSimulator:
    def __init__(self, p1: Player, p2: Player):
        self._p1 = p1
        self._p2 = p2
        self._p1_payoff = 0
        self._p2_payoff = 0
 
    def simulate_rounds(self, rounds: int):
        for _ in range(rounds):
            a1 = self._p1.get_next_action()
            a2 = self._p1.get_next_action()
 
            pay1, pay2 = self.get_payoffs(a1, a2)
            self._p1.payoff += pay1
            self._p2.payoff += pay2
 
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
        return self._p1.payoff
 
    @property
    def p2_payoff(self):
        return self._p2.payoff

