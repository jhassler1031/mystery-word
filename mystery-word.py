
#The computer needs to choose a word at random

with open("/usr/share/dict/words") as infile:
    words_list = infile.read()

words_list = words_list.split()

import random

rand_word = random.choice(words_list).lower() #.lower to normalize

#Now we have a random word.  Need to create the display word

word_length = len(rand_word)
display_word = "_" * word_length

#Start user interface

print("Game Start:  The word is " + str(word_length) + " letters long.  Good luck!")
