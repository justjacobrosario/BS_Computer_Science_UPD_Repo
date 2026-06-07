import random
 
 
class GuessingGame:
    def __init__(self, answer: int, attempts: int):
        self.answer = answer
        self.attempts = attempts
 
    def start(self):
        while self.attempts > 0:
            guess = self.prompt_guess()
 
            if guess < 1 or guess > 100:
                print('Guess must be between 1 and 100 (inclusive)')
                continue
 
            if guess == self.answer:
                break
 
            self.print_feedback(guess)
            self.attempts -= 1
 
        if self.attempts > 0:
            print('You win!')
        else:
            print(f'You lose; the answer is {self.answer}')
 
    def prompt_guess(self):
        return int(input('Enter your guess [1-100]'
                         f' ({self.attempts} attempts left): '))
 
    def print_feedback(self, guess: int):
        if guess < self.answer:
            print("Too low")
        else:
            print("Too high")
 
 
def main():
    answer = random.randint(1, 100)
    game = GuessingGame(answer, 8)
    game.start()
 
 
if __name__ == '__main__':
    main()
