class AnswerGenerator:
    def generate(self) -> int:
        ...
 
class RandomAnswerGenerator:
    def generate(self) -> int:
        # ...
 
class OddRandomAnswerGenerator:
    def generate(self) -> int:
        # ...
 
class NumberGuessingGameModel:
    def __init__(self, min_guess: int, max_guess: int, max_attempts: int,
                 answer_generator: AnswerGenerator):
        # ...
        self.answer_generator = answer_generator
        self.answer = answer_generator.generate()
 
        # ...
 
    def restart_game(self):
        # ...
        self.answer = self.answer_generator.generate()
