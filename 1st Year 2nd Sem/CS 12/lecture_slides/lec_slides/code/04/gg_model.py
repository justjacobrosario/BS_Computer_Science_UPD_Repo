from dataclasses import dataclass
from enum import Enum, auto
 
 
class Feedback(Enum):
    TOO_HIGH = auto()
    TOO_LOW = auto()
    CORRECT = auto()
    INVALID = auto()
 
 
@dataclass(frozen=True)
class State:
    attempts_left: int
    feedback: Feedback | None
    has_guessed_correctly: bool
 
 
class GuessingGameModel:
    def __init__(self, min_guess: int, max_guess: int, max_attempts: int, answer: int):
        if min_guess > max_guess:
            raise ValueError(
                f'min_guess ({min_guess}) should be less than or equal to max_guess ({max_guess})')
 
        if max_attempts <= 0:
            raise ValueError(
                f'max_attempts ({max_attempts}) should be positive')
 
        self.min_guess = min_guess
        self.max_guess = max_guess
        self.answer = answer
        self.attempts_left: int = max_attempts
        self.feedback: Feedback | None = None
        self.has_guessed_correctly: bool = False
 
    def make_guess(self, guess: int):
        if self.attempts_left == 0:
            self.feedback = Feedback.INVALID
            return
 
        if self.feedback == Feedback.CORRECT:
            self.feedback = Feedback.INVALID
            return
 
        if not (self.min_guess <= guess <= self.max_guess):
            self.feedback = Feedback.INVALID
            return
 
        self.attempts_left -= 1
        if guess == self.answer:
            self.feedback = Feedback.CORRECT
            self.has_guessed_correctly = True
        elif guess > self.answer:
            self.feedback = Feedback.TOO_HIGH
        else:
            self.feedback = Feedback.TOO_LOW
 
    def get_state(self) -> State:
        return State(
            self.attempts_left,
            self.feedback,
            self.has_guessed_correctly,
        )