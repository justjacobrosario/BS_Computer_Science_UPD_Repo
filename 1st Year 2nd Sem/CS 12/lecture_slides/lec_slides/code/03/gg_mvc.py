import random
from enum import StrEnum, auto


class Verdict(StrEnum):
    CORRECT = auto()
    TOO_HIGH = auto()
    TOO_LOW = auto()
    OUT_OF_BOUNDS = auto()
    GAME_IS_OVER = auto()


class GuessingGameModel:
    def __init__(self, answer: int, attempts_left: int, min_guess: int, max_guess: int):
        self._answer = answer
        self._attempts_left = attempts_left
        self._min_guess = min_guess
        self._max_guess = max_guess
        self._is_game_over = False
        self._did_player_win = False

    @property
    def did_player_win(self):
        return self._did_player_win

    @property
    def answer(self):
        return self._answer

    @property
    def max_guess(self):
        return self._max_guess

    @property
    def min_guess(self):
        return self._min_guess

    @property
    def is_game_over(self) -> bool:
        return self._is_game_over

    @property
    def attempts_left(self) -> int:
        return self._attempts_left

    def make_guess(self, guess: int) -> Verdict:
        verdict = self._check_guess(guess)

        match verdict:
            case Verdict.CORRECT:
                self._is_game_over = True
                self._did_player_win = True
                self._attempts_left -= 1

            case Verdict.TOO_LOW | Verdict.TOO_HIGH:
                self._attempts_left -= 1

            case _:
                pass

        if self._attempts_left == 0:
            self._is_game_over = True

        return verdict

    def _check_guess(self, guess: int) -> Verdict:
        if self._is_game_over:
            return Verdict.GAME_IS_OVER
        elif guess < self._min_guess or guess > self._max_guess:
            return Verdict.OUT_OF_BOUNDS
        elif guess == self._answer:
            return Verdict.CORRECT
        elif guess < self._answer:
            return Verdict.TOO_LOW
        else:
            return Verdict.TOO_HIGH


class GuessingGameView:
    def ask_for_guess(self, min_guess: int, max_guess: int) -> int:
        return int(input('Enter a guess'
                         f' [{min_guess}-{max_guess}] :'))

    def print_verdict(self, verdict: Verdict, min_guess: int, max_guess: int):
        match verdict:
            case Verdict.CORRECT:
                print('You win!')
            case Verdict.TOO_LOW:
                print('Too low')
            case Verdict.TOO_HIGH:
                print('Too high')
            case Verdict.OUT_OF_BOUNDS:
                print('Guess must be between'
                      f'{min_guess} and {max_guess} (inclusive)')
            case Verdict.GAME_IS_OVER:
                print('Game is over')

    def print_lose_message(self, answer: int):
        print(f'You lose; answer is {answer}')


class GuessingGameController:
    def __init__(self, model: GuessingGameModel, view: GuessingGameView):
        self._model = model
        self._view = view

    def start(self):
        model = self._model
        view = self._view

        while not model.is_game_over:
            guess = view.ask_for_guess(model.min_guess, model.max_guess)
            verdict = model.make_guess(guess)
            view.print_verdict(verdict, model.min_guess, model.max_guess)

        if not model.did_player_win:
            view.print_lose_message(model.answer)


if __name__ == '__main__':
    answer = random.randint(1, 100)
    model = GuessingGameModel(answer, 8, 1, 100)
    view = GuessingGameView()
    controller = GuessingGameController(model, view)
     
    controller.start()