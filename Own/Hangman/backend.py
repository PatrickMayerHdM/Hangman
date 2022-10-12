import random

Liste = ["Test", "Hallo", "Patrick"]


def word_generator():
    gen_word = random.choice(Liste)
    return gen_word.upper()

def letter_in_word_check(letter, word):
    if letter in word:
        return True
    else:
        return False

