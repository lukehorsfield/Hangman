import random


def hangman():
    word_list = ['Chocolate', 'Elephant', 'Sunshine', 'Butterfly', 'Mountain', 'Rainbow', 'Universe', 'Adventure',
                 'Baseball', 'Computer',
                 'Detective', 'Ecosystem', 'Fireworks', 'Happiness', 'Icecream', 'Jellyfish', 'Kangaroo', 'Lighthouse',
                 'Meditation', 'Nostalgia']

    answer = random.choice(word_list).upper()
    answer_statement = '_' * len(answer)
    guessed_letters = set()

    guesses = 6

    while guesses > 0 and answer_statement != answer:
        print('-- Current Word: ' + answer_statement)
        print(f'-- Guessed letters: {", ".join(guessed_letters)}')
        guess = input('Guess a letter: ').upper()
        print(' ')

        if guess in guessed_letters:
            print("You've already guessed this letter, try again.")
            continue

        elif len(guess) > 1:
            print("Sorry, you can only guess one letter at a time, try again.")
            continue

        else:
            guessed_letters.add(guess)

        if guess in answer:
            print('Correct guess!')
            for i in range(len(answer)):
                if answer[i] == guess:
                    answer_statement = answer_statement[:i] + guess + answer_statement[i + 1:]

        else:
            guesses -= 1
            print(f'Incorrect guess! You have {guesses} guesses left.')

    if answer_statement == answer:
        print(f'Congratulations! You guessed the word: {answer}')
    elif guesses == 0:
        print(f'Out of guesses. The word was: {answer}')


hangman()