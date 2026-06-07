from abc import ABC, abstractmethod
 
class Player(ABC):
    def __init__(self):
        self._payoff = 0
 
    def add_payoff(self, value: int):
        self._payoff += value
 
    @abstractmethod
    def get_next_action(self) -> Action:
        ...
 
    @abstractmethod
    def notify_opponent_action(self, action: Action):
        ...
 
 
class AlwaysCheatPlayer(Player):
    def get_next_action(self) -> Action:
        return Action.CHEAT
 
    def notify_opponent_action(self, action: Action):
        pass
 
 
class CopycatPlayer(Player):
    def __init__(self):
        super().__init__(self)  # Don't forget this!
        self._last_opponent_action: Action | None = None
 
    def get_next_action(self) -> Action:
        if self._last_opponent_action is None:
            return Action.COOPERATE
 
        return self._last_opponent_action
 
    def notify_opponent_action(self, action: Action):
        self._last_opponent_action = action