class Strategy(Protocol):
    def get_next_action(self) -> Action:
        ...
 
    def notify_opponent_action(self, action: Action):
        ...


# AlwaysCheatStrategy <: Strategy
class AlwaysCheatStrategy:
    def get_next_action(self) -> Action:
        return Action.CHEAT
 
    def notify_opponent_action(self, action: Action):
        pass


# Composed of `Strategy`
class Player:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
 
    def get_next_action(self) -> Action:
        return self._strategy.get_next_action()
 
    def notify_opponent_action(self, action: Action):
        self._strategy.notify_opponent_action(action)