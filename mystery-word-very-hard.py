
#connect to functions in separate file

from mys_word_functions_hard import player_turn, display_word, choose_difficulty

#The computer needs to choose a word at random after player chooses difficulty

with open("/usr/share/dict/words") as infile:
    words_list = infile.read()

words_list = words_list.split()

#Create letter scoring - based off of scrabble

one_point = ["e", "a", "i", "o", "n", "r", "t", "l", "s", "u"]
two_point = ["d", "g"]
three_point = ["b", "c", "m", "p"]
four_point = ["f", "h", "v", "w", "y"]
five_point = ["k"]
eight_point = ["j", "x"]
ten_point = ["q", "z"]

#Create different list per difficulty

easy_list = []
normal_list = []
hard_list = []
"""
for item in words_list:
    if len(item) >= 4 and len(item) <= 6:
        easy_list.append(item)
    elif len(item) > 6 and len(item) <= 10:
        normal_list.append(item)
    elif len(item) > 10:
        hard_list.append(item)
"""
rand_word = choose_difficulty(easy_list, normal_list, hard_list)

#Now we have a random word.  Need to create the display word

word_length = len(rand_word)
miss_count = 8
correct_letters = []
incorrect_letters = []
wants_to_play = True


#Start user interface

print("Game Start:  The word is " + str(word_length) + " letters long.  Good luck!")

while wants_to_play:
    while True:
        print("You have " + str(miss_count) + " misses remaining.")
        print(display_word(correct_letters, rand_word))
        correct_letters, incorrect_letters, miss_count = player_turn(rand_word, correct_letters, incorrect_letters, miss_count)

        if rand_word == display_word(correct_letters, rand_word):
            print("Congratulations!  You've won!")
            break
        elif miss_count <= 0:
            print("I'm sorry, you've lost.")
            print("The word was " + rand_word + ".")
            break
        else:
            print("Next turn.")
    answer = input("Would you like to play again? Y or N: ")
    if answer.lower() == "y":
        correct_letters = []
        incorrect_letters = []
        rand_word = choose_difficulty(easy_list, normal_list, hard_list)
    else:
        wants_to_play = False
