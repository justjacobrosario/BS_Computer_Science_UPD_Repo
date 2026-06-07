import random
 
 
def main():
    answer = random.randint(1, 100)
    attempts = 8
 
    while attempts > 0:
        guess = int(input('Enter your guess [1-100]'
                          f' ({attempts} attempts left): '))
 
        if guess < 1 or guess > 100:
            print('Guess must be between 1 and 100 (inclusive)')
            continue
 
        if guess == answer:
            break
 
        if guess < answer:
            print("Too low")
        else:
            print("Too high")
 
        attempts -= 1
 
    if attempts > 0:
        print('You win!')
    else:
        print(f'You lose; the answer is {answer}')
 
 
if __name__ == '__main__':
    main()
