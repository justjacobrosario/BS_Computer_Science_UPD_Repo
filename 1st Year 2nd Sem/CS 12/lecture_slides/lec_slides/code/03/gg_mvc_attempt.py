from enum import Enum, auto


class Verdict(Enum):
    TOO_HIGH = auto()
    TOO_LOW = auto()
    OK = auto()


# LOGIC
class GuessingGameModel:
    def __init__(self, answer: int, attempts: int):
        self.answer = answer
        self.attempts = attempts

    def check_guess(self, guess: int) -> Verdict:
        if guess > self.answer:
            return Verdict.TOO_HIGH
        elif guess < self.answer:
            return Verdict.TOO_LOW
        else:
            return Verdict.OK

    def is_game_done(self) -> bool:
        return self.attempts == 0

    def use_attempt(self):
        self.attempts -= 1

    def is_guess_valid(self, guess: int) -> bool:
        return 1 <= guess <= 100


# I/O
class GuessingGameView:
    def show_final_message(self, attempts: int, answer: int):
        if attempts > 0:
            print("You win!")
        else:
            print(f"You lose; the answer is {answer}")

    def show_verdict(self, verdict: Verdict):
        if verdict == Verdict.TOO_HIGH:
            print("Too high")
        else:
            print("Too low")

    def get_guess(self, attempts: int) -> int:
        guess = int(input("Enter your guess [1-100]" f" ({attempts} attempts left): "))

        return guess

    def show_invalid(self):
        print("Guess must be between 1 and 100 (inclusive)")


# glue
class GuessingGameController:
    def __init__(self, model: GuessingGameModel, view: GuessingGameView):
        self.model = model
        self.view = view

    def run(self):
        while not self.model.is_game_done():
            guess = self.view.get_guess(self.model.attempts)
            verdict = self.model.check_guess(guess)

            if verdict == Verdict.OK:
                break

            self.view.show_verdict(verdict)
            self.model.use_attempt()

        self.view.show_final_message(self.model.attempts, self.model.answer)


# model = GuessingGameModel(64, 8)
# view = GuessingGameView()
# controller = GuessingGameController(model, view)
#
# controller.run()


# OddRandomAnswerGenerator
# EvenRandomAnswerGenerator


# class GuessingGameModel:
#     def __init__(
#         self,
#         min_guess: int,
#         max_guess: int,
#         max_attempts: int,
#         random_answer_generator: RandomAnswerGenerator | OddRandomAnswerGenerator | EvenRandomAnswerGenerator | SquareAnswerGenerator | NegativeAnswerGenerator | ...
# ,
#     ): ...


# if S <: T, then 𝑆 values can be used where 𝑇 values are needed

# then 𝑆 values can be used where S values are needed

# bool <: int

# then bool values can be used where int values are needed


# def f(x: int) -> int:
#     return x + 1
#
#
# print(f(True))


def f(x: object):
    print(x)


f(67)
f("67")
f([1, 2])
f(True)
f(...)


# OddRandomAnswerGenerator <: RandomAnswerGenerator

from typing import Protocol


class A(Protocol):  # A implementors must have body for f and g
    def f(self, x: int) -> int:  # f has no method body in A (only signature)
        ...

    # Same goes for g
    def g(self): ...


class B:  # B <: A
    def f(self, x: int) -> int:
        return x + 1

    def g(self): ...


def f(a: A): ...


b = B()
f(b)
