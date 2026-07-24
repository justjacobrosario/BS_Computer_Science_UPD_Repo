from enum import Enum





'''
wordle
ask input
right letters
correct arrangements
attempts left
lose, no more attempt
win, correct word
'''

class Verdict(Enum):
    Wrong = 0
    Some_Correct = 1
    Correct = 2
    NoAttempts = 3

class w_model:
    answer: str
    guess: str
    correct_words: set
    attempts: int
    verdict: str

    def __init__(self, answer: str, attempts: int = 10) -> None:
        self._answer = answer.upper()
        self._guess = ""
        self._correct_words = set()
        self._attempts = attempts
        self._verdict = Verdict.WRONG
        self._game_over = False

    @property
    def answer(self):
        return self._answer

    @property
    def guess(self):
        return self._guess

    @property
    def correct_words(self):
        return self._correct_words

    @property
    def attempts(self):
        return self._attempts

    @property
    def verdict(self):
        return self._verdict

    @property
    def is_game_over(self):
        return self._game_over

    def use_attempt(self):
        self._attempts -= 1

    def judge(self, guess) -> Verdict:
        if self._game_over:
            return Verdict.NoAttempts
        else:
            self._guess = guess.upper()
            self.use_attempt()
            self._correct_words = set()

            if self._guess == self._answer:
                self._verdict = Verdict.Correct
                self._game_over = True
                return self._verdict
            else:
                for letter in self._guess:
                    if letter in self._answer:
                        self._correct_words.add(letter)

                if self._correct_words:
                    self.verdict = Verdict.Some_Correct

                


class w_view:

    def ask(self, attempts: int) -> str:
        return input("Welcome to Wordle! For {attempts} left, guess the 5-letter word: ")
    def prompt_check(self, verdict: Verdict, correct_words: set(), guess: str):
        if verdict == Verdict.Wrong:
            print(f"❗ You didn't get any correct letter")
        elif verdict == Verdict.Some_Correct:
            print(f"📃 {correct_words} are in the correct word. Keep it up!")
        elif verdict == Verdict.Correct:
            print(f"✅ You win! {guess} is the correct answer!")
        elif verdict == Verdict.NoAttempts:
            print(f"❌ You lost! There are no more attepts left!")


class w_controller:
    model: w_model
    view: w_view

    def __init__(self, model: w_model, view: w_view):
        self._model: model
        self._view: view

    def start(self):
        model = self._model
        view = self._view

        while model.result() != Verdict.NoAttempts:
            guess = view.ask(model.attempts)
            model.guess = guess
            verdict = model.result()
            model.verdict = verdict
            view.prompt_check(model.verdict, model.correct_words, model.guess)
            model.use_attempt()

        view.prompt_check(model.verdict, model.correct_words, model.guess)

model = w_model(answer = "USERS")
view = w_view
controller = w_controller(model, view)
controller.start()

