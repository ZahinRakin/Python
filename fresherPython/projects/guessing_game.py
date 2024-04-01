import random

shrouded = random.randint(1, 10)
guess_count = 1
guess_limit = 5

while guess_count <= guess_limit:
    guess = int(input('Enter number between 1 and 10: '))
    if guess == shrouded:
        print(f'Congratulations! You have guessed it in your {guess_count} th try.')
        break
    guess_count += 1
else:
    print(f'sorry! You loose. the number was: {shrouded}')
