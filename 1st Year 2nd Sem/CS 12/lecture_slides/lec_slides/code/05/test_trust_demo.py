from trust_demo import *


def test_game():
    p1 = Player(AlwaysCoopStrategy())
    p2 = Player(DetectiveStrategy())

    m = Match(p1, p2)

    res = m.do_one_round()

    assert res[0] == Choice.COOPERATE
