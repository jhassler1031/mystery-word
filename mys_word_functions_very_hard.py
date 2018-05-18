
import random

def det_word_diff(word, one_point, two_point, three_point, four_point, five_point, eight_point, ten_point):
    word_diff = 0
    for letter in word:
        if letter in one_point:
            word_diff += 1
        elif letter in two_point:
            word_diff += 2
        elif letter in three_point:
            word_diff += 3
        elif letter in four_point:
            word_diff += 4
        elif letter in five_point:
            word_diff += 5
        elif letter in eight_point:
            word_diff += 8
        else:
            word_diff += 10
    return word_diff


def choose_difficulty(easy_list, normal_list, hard_list):
    difficulty = input("""Please choose a difficulty.
    Press 1 for easy,
    2 for normal,
    or 3 for hard: """)
    if difficulty == "1":
        return random.choice(easy_list).lower()
    elif difficulty == "2":
        return random.choice(normal_list).lower()
    elif difficulty == "3":
        return random.choice(hard_list).lower()
    else:
        print("Incorrect Entry.")
        return choose_difficulty(easy_list, normal_list, hard_list)


def display_word(correct_letters, rand_word):
    display_list = []
    for char in rand_word:
        if char in correct_letters:
            display_list.append(char)
        else:
            display_list.append("_")
    return "".join(display_list)

def request_guess(correct_letters, incorrect_letters):
    guess = input("Please guess a letter: ").lower()
    if guess in correct_letters or guess in incorrect_letters:
        print("You have already guessed that letter.")
        return request_guess(correct_letters, incorrect_letters)
    elif len(guess) > 1:
        print("Please only enter one letter at a time.")
        return request_guess(correct_letters, incorrect_letters)
    else:
        return guess

def player_turn(rand_word, correct_letters, incorrect_letters, miss_count):
    guess = request_guess(correct_letters, incorrect_letters)
    if guess in rand_word:
        print("Good guess, that letter is in the word.")
        correct_letters.append(guess)
        return correct_letters, incorrect_letters, miss_count
    else:
        print("Sorry, that letter is not in the word.")
        incorrect_letters.append(guess)
        miss_count -= 1
        return correct_letters, incorrect_letters, miss_count
