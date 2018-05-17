
def display_state(miss_count, display_word):
    print("You have " + str(miss_count) + " misses remaining.")
    print(display_word)
    return

def mod_display(letter, display_word):
    display_list = list(display_word)
    count = 0


def is_in_word(letter, rand_word, display_word):
    if letter in rand_word:
        mod_display(letter, display_word)
        return True
    else:
        return False

def request_guess(correct_letters, incorrect_letters):
    guess = input("Please guess a letter: ")
    if guess in correct_letters or guess in incorrect_letters:
        print("You have already guessed that letter.")
        request_guess(correct_letters, incorrect_letters)
    else:
        return guess




def player_turn(rand_word, display_word, correct_letters, incorrect_letters, miss_count):
    display_state(miss_count, display_word)
    guess = request_guess(correct_letters, incorrect_letters)
    
