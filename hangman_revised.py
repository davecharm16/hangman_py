# Hangman Game Implementation -- Midterm Project
# By: [Thessa Monica Abellana]
# ID Number: [210037]
# Date Completed: [March 13, 2023]

# Certification of Authorship:
# I certify that this project is my own work and I have not copied or shared my code with anyone.
# Name: [Monica Abellana]
# Signature: [Your Signature]

import random


# Function to display the hangman figure based on the number of incorrect guesses
def display_hangman(incorrect_guesses, display, unused_letters):
    print("Guess the word, " + str(6 - incorrect_guesses) + " guess(es) left: " + print_display(display))
    print("Unused letters: " + print_unused_letters(unused_letters))


# Function to check if the guessed letter is in the word and update the display accordingly
def check_guess(word, display, letter, used_letters):
    used_letter_count = 0
    for used_letter in used_letters:
        if used_letter == letter:
            used_letter_count += 1
    if used_letter_count > 0:
        print("You have already used that letter.")
        return False
    used_letters.append(letter)
    correct_guess = False
    for i in range(len(word)):
        if word[i] == letter:
            display[i] = letter
            correct_guess = True
    return correct_guess


# Function to play game
def play_game(word, num_guesses):
    display = ["-" for i in range(len(word))]
    unused_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    used_letters = []
    incorrect_guesses = 0
    while "-" in display and incorrect_guesses < num_guesses:
        display_hangman(incorrect_guesses, display, unused_letters)
        guess = input()[0]
        guess = make_upper(guess)
        valid_guess = False
        for i in range(len(unused_letters)):
            if unused_letters[i] == guess:
                valid_guess = True
                break
        if not valid_guess:
            valid_guess = False
            for i in range(len(used_letters)):
                if used_letters[i] == guess:
                    valid_guess = True
                    break
        if not valid_guess:
            print("Please choose a valid letter.")
            continue
        if not check_guess(word, display, guess, used_letters):
            if not in_unused_letter(guess, unused_letters):
                continue
            unused_letters = remove_item(unused_letters, guess)
            incorrect_guesses += 1
        else:
            unused_letters = remove_item(unused_letters, guess)
    display_hangman(incorrect_guesses, display, unused_letters)

    if not in_display("-", display):
        print("CONGRATULATIONS! YOU WIN!")
    else:
        print("GAME OVER. The word was " + word)


def in_display(char, display):
    for i in display:
        if char == i:
            return True
    return False


def in_unused_letter(guess, unused_letters):
    for i in unused_letters:
        if guess == i:
            return True
    return False


def remove_item(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            lst[i:i + 1] = []
            return lst


def make_upper(word):
    upperList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowerList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    output = [i for i in word]
    final_output = ''

    for i in range(len(word)):
        for j in range(len(lowerList)):
            if word[i] == lowerList[j]:
                output[i] = upperList[j]

    for i in output:
        final_output += i

    return final_output


def print_display(display):
    actual_display = ''
    for i in display:
        actual_display += i + " "
    return actual_display


def print_unused_letters(display):
    actual_display = ''
    for i in display:
        actual_display += i + ""
    return actual_display


# Main program
print("LET'S PLAY HANGMAN!")
user_choice = ''
play = True
while play:
    word = input("Please enter a word for the other player to guess: ")
    word = make_upper(word)
    # Convert the word to uppercase
    play_game(word, 6)

    while True:
        user_choice = input("Play Again? [Y] or [N]?")
        if (user_choice == "Y" or user_choice == "y") or (user_choice == "N" or user_choice == "n"):
            if user_choice == "N" or user_choice == "n":
                play = False
                print("Thank you for Playing!")
                break
            else:
                break
        else:
            print("Please Enter Valid Character")
