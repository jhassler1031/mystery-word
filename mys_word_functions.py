
def display_state(miss_count, display_word):
    print("You have " + str(miss_count) + " misses remaining.")
    print(display_word)
    return

def mod_display(guess, display_word):
    display_list = list(display_word)
    count = 0
    return display_word


def is_in_word(guess, rand_word, display_word):
    if letter in rand_word:
        display_word = mod_display(guess, display_word)
        return display_word
    else:
        return display_word

def request_guess(correct_letters, incorrect_letters):
    guess = input("Please guess a letter: ")
    if guess in correct_letters or guess in incorrect_letters:
        print("You have already guessed that letter.")
        return request_guess(correct_letters, incorrect_letters)
    else:
        return guess




def player_turn(rand_word, display_word, correct_letters, incorrect_letters, miss_count):
    display_state(miss_count, display_word)
    guess = request_guess(correct_letters, incorrect_letters)
    if is_in_word(guess):
        print("Good guess, that letter is in the word.")
        correct_letters.append(guess)
        display_word = mod_display(guess, display_word)
        return display_word, correct_letters, incorrect_letters, miss_count
    else:
        print("Sorry, that letter is not in the word.")
        incorrect_letters.append(guess)
        miss_count -= 1
        return display_word, correct_letters, incorrect_letters, miss_count
