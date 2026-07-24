from enum import Enum
from random import randint

''' Game Cases:
-Start ask input
- Too big, wrong
- Too small, wrong
- Correct, break
- No more attempts, break
'''

# since not bool, we made a triadic decision system
class Judge(Enum):
    TooBig = 0
    TooSmall = 1
    Correct = 2

# external funcs
def get_ran_num_up_to(n):
    return randint(1, n)

# Model
class gg_model:
    answer: int
    guess: int
    attempts: int

    def __init__(self, answer: int = 0, guess: int = 0, attempts: int = 0) -> None:
        self.answer = answer
        self.guess = guess
        self.attempts = attempts

    # states
    def check_guess(self) -> Judge:
        if self.guess > self.answer:
            return Judge.TooBig
        elif self.guess < self.answer:
            return Judge.TooSmall
        else:
            return Judge.Correct

    def use_attempt(self) -> None:
        self.attempts -= 1

    def no_more_attempts(self) -> bool:
        return self.attempts <= 0

class gg_view:
    model: gg_model 

    def __init__(self, model: gg_model  ) -> None:
        self.model = model

    def start(self) -> None:
        return input(f"Welcome to Guessing Game! From 1-100, guess the number in {self.model.attempts} attempts:")

    def is_correct(self, judge: Judge) -> bool:
        if self.model.attempts <= 0:
            print(f"X﹏X You Lose! No more attempts left.")
        else:
            if judge == Judge.TooBig:
                print(f"❌ {self.model.guess} is too big! {self.model.attempts} left:")
            elif judge == Judge.TooSmall:
                print(f"❌ {self.model.guess} is too small! {self.model.attempts} left:")
            elif judge == Judge.Correct:
                print(f"✅ You win! The correct answer is {self.model.answer}.")
                return True
        return False


class gg_controller:
    model: gg_model
    view: gg_view

    def __init__(self, model: gg_model, view: gg_view) -> None:
        self.model = model
        self.view = view


    def run(self) -> None:
        answer = int(get_ran_num_up_to(100))
        attempts = int(10)
        self.model.answer = answer
        self.model.attempts = attempts
        correctness: bool = False

        while self.model.no_more_attempts() == False and correctness == False:
            guess_input: int = int(self.view.start())
            self.model.guess = guess_input
            self.model.use_attempt()
            attempts_left: int = self.model.attempts
            self.model.attempts = attempts_left
            judge = self.model.check_guess()
            correctness = self.view.is_correct(judge)
            if correctness:
                break



model = gg_model()
view = gg_view(model)
controller = gg_controller(model, view)
controller.run()