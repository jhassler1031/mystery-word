
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
