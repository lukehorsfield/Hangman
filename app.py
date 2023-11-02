import random


def hangman():
    word_list = ['Apple, Boring, Carrot, Delta, Elephant']

    answer = random.choice(word_list).upper()
    answer_statement = '_' * len(answer)

    guesses = 6

    while guesses > 0 and answer_statement != answer:
        print('Current Word: ' + answer_statement)
        guess = input('Guess a letter: ').upper()
        if guess in answer:
            print('Correct guess!')
            # Update answer_statement with the correctly guessed letter
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