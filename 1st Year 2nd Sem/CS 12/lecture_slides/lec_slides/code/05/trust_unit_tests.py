from main import Payoffs, Action, CopycatStrategy
 
 
def test_get_payoffs():
    p = Payoffs()
    assert p.get_payoffs(Action.CHEAT, Action.CHEAT) == (0, 0)
    assert p.get_payoffs(Action.CHEAT, Action.COOPERATE) == (+3, -1)
    assert p.get_payoffs(Action.COOPERATE, Action.CHEAT) == (-1, +3)
    assert p.get_payoffs(Action.COOPERATE, Action.COOPERATE) == (+2, +2)
 
 
def test_copycat():
    copycat = CopycatStrategy()
    assert copycat.get_next_action() == Action.COOPERATE
 
    copycat.notify_opponent_action(Action.CHEAT)
    assert copycat.get_next_action() == Action.CHEAT
 
    copycat.notify_opponent_action(Action.CHEAT)
    assert copycat.get_next_action() == Action.CHEAT
 
    copycat.notify_opponent_action(Action.COOPERATE)
    assert copycat.get_next_action() == Action.COOPERATE
