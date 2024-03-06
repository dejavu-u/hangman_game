import random

with open('russian_nouns.txt', 'r', encoding="utf-8") as file:
    words = file.readlines()
    words = [s.strip("\n") for s in words]


def random_word():
    return random.choice(words)
