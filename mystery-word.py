
#connect to functions in separate file

from mys_word_functions import player_turn, display_word
#The computer needs to choose a word at random

with open("/usr/share/dict/words") as infile:
    words_list = infile.read()

words_list = words_list.split()

import random

rand_word = random.choice(words_list).lower() #.lower to normalize

#Now we have a random word.  Need to create the display word

word_length = len(rand_word)
miss_count = 8
correct_letters = []
incorrect_letters = []


#Start user interface

print("Game Start:  The word is " + str(word_length) + " letters long.  Good luck!")

while True:
    print("You have " + str(miss_count) + " misses remaining.")
    print(display_word(correct_letters, rand_word))
    correct_letters, incorrect_letters, miss_count = player_turn(rand_word, correct_letters, incorrect_letters, miss_count)

    if rand_word == display_word(correct_letters, rand_word):
        print("Congratulations!  You've won!")
        break
    elif miss_count == 0:
        print("I'm sorry, you've lost.")
        break
    else:
        print("Next turn.")
