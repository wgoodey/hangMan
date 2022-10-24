import random
import hangman_art
import hangman_words

word_with_blanks = []
correct_guesses = []
incorrect_guesses = []
guesses_left = 6
guess = ' '
game_over = False


def get_string(list_to_print):
    return ''.join(list_to_print)


def print_list(list_to_print):
    return ", ".join(list_to_print)


def fill_blanks():
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            word_with_blanks[position] = chosen_word[position]
    print(get_string(word_with_blanks))


def print_noose():
    print(f"{hangman_art.stages[guesses_left]}\n")


def get_game_status():
    if "_" not in word_with_blanks:
        print("Congratulations, you guessed the word and avoided death!")
    elif guesses_left == 0:
        print("You ran out of guesses...")
    else:
        return False

    return True


print(hangman_art.logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)

# Fill word_with_blanks with the correct number of blanks
for index in chosen_word:
    word_with_blanks.append("_")
fill_blanks()

while not game_over:
    print(f"Correct guesses: {print_list(correct_guesses)}")
    print(f"Wrong guesses: {print_list(incorrect_guesses)}")

    while True:
        guess = ""
        while guess == "":
            guess = input("\nWhich letter would you like to guess? ").lower()

        guess = guess[0]
        
        if not guess.isalpha():
            print("Please enter a letter")
        elif guess not in correct_guesses or guess not in incorrect_guesses:
            break

    # Check if the letter the user guessed is one of the letters in the chosen_word.
    if guess in chosen_word:
        correct_guesses.append(guess)
        print()
    else:
        incorrect_guesses.append(guess)
        guesses_left -= 1

    print_noose()
    if guesses_left > 0:
        fill_blanks()
    # Check if the game is over
    game_over = get_game_status()
