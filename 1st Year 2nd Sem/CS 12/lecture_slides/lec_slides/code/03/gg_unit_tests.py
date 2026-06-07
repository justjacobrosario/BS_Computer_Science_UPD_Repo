from gg_mvc import GuessingGameModel, Verdict
 
 
def test_make_guess_more_than_max():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100

    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(101)
 
    assert verdict == Verdict.OUT_OF_BOUNDS
    assert model.answer == answer
    assert model.attempts_left == attempts_left
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert not model.is_game_over
    assert not model.did_player_win
 
 
def test_make_guess_less_than_min():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
 
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(0)
 
    assert verdict == Verdict.OUT_OF_BOUNDS
    assert model.answer == answer
    assert model.attempts_left == attempts_left
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert not model.is_game_over
    assert not model.did_player_win
 
 
def test_make_guess_less_than_answer():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
 
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(5)
 
    assert verdict == Verdict.TOO_LOW
    assert model.answer == answer
    assert model.attempts_left == attempts_left - 1
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert not model.is_game_over
    assert not model.did_player_win
 
 
def test_make_guess_greater_than_answer():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
 
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(15)
 
    assert verdict == Verdict.TOO_HIGH
    assert model.answer == answer
    assert model.attempts_left == attempts_left - 1
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert not model.is_game_over
    assert not model.did_player_win
 
 
def test_make_guess_correct():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
 
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    verdict = model.make_guess(answer)
 
    assert verdict == Verdict.CORRECT
    assert model.answer == answer
    assert model.attempts_left == attempts_left - 1
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert model.is_game_over
    assert model.did_player_win
 
 
def test_make_guess_when_game_over():
    answer = 10
    attempts_left = 7
    min_guess = 1
    max_guess = 100
 
    model = GuessingGameModel(answer, attempts_left, min_guess, max_guess)
    for _ in range(attempts_left):
        model.make_guess(100)
 
    verdict = model.make_guess(100)
 
    assert verdict == Verdict.GAME_IS_OVER
    assert model.answer == answer
    assert model.attempts_left == 0
    assert model.min_guess == min_guess
    assert model.max_guess == max_guess
    assert model.is_game_over
    assert not model.did_player_win
