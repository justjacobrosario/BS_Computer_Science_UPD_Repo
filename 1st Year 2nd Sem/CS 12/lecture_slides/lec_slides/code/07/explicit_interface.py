from abc import ABC, abstractmethod  # ABC means "abstract


# base class"
class Strategy(ABC):
    @abstractmethod
    def get_next_action(self) -> Action: ...

    @abstractmethod
    def notify_opponent_action(self, action: Action): ...


# Explicit `AlwaysCheatStrategy <: Strategy`
class AlwaysCheatStrategy(Strategy):
    def get_next_action(self) -> Action:
        return Action.CHEAT

    def notify_opponent_action(self, action: Action):
        pass
