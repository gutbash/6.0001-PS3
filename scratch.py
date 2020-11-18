import math
import random
import string

# SCRABBLE_LETTER_VALUES = {
#     'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
# }

# print('a' in SCRABBLE_LETTER_VALUES)

# ran_letter = random.choice(string.ascii_lowercase)
# print(ran_letter)

# dic = {'a': 1, 'b': 3, 'c': 3}
# dic1 = {}

# for i in dic:
#     print(i)

# print(dic)

# word = 'Aabc*'

# def valid(dic, word):
#     for i in word:
#         if not i in dic:
#             return False
#         else:
#             continue
#     return True

# print(valid(dic, word))

# new_word = word.split('*')
# print(new_word)
# final_word = 'i'.join(new_word)
# print(final_word)
# print(len(final_word))

# total = 0
# for key in dic:
#     total += dic[key]

# print(total)

# print(len(dic1))

def substitute_hand(hand, letter):
    
    hand_new = {}
    ran_letter = random.choice(string.ascii_lowercase)
    
    while ran_letter in hand:
        ran_letter = random.choice(string.ascii_lowercase)

    if not letter in hand:
        return hand

    for i in hand:
        if i == letter:
            hand_new[ran_letter] = hand[i]
        else:
            hand_new[i] = hand[i]

    return hand_new

print(substitute_hand({'a': 1, 'b': 3, 'c': 3}, 'c'))