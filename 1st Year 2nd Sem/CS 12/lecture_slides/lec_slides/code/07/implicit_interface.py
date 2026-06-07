class Strategy(Protocol):
    def get_next_action(self) -> Action:
        ...
 
    def notify_opponent_action(self, action: Action):
        ...

# Implicit `AlwaysCheatStrategy <: Strategy`
class AlwaysCheatStrategy:
    def get_next_action(self) -> Action:
        return Action.CHEAT
 
    def notify_opponent_action(self, action: Action):
        pass
