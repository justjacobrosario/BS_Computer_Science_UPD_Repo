class PlayerFactory:
    """Instantiates a Player based on a StrategyKind."""
 
    @classmethod
    def make(cls, strategy_kind: StrategyKind) -> Player:
        match strategy_kind:
            case StrategyKind.ALWAYS_CHEAT:
                strategy = AlwaysCheatStrategy()
 
            case StrategyKind.ALWAYS_COOPERATE:
                strategy = AlwaysCooperateStrategy()
 
            case StrategyKind.COPYCAT:
                strategy = CopycatStrategy()
 
        return Player(strategy)

