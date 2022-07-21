#!/usr/bin/env python3

import json
import random


class colors:
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"


with open("words.json", "r") as f:
    secret_word = random.choice(json.load(f)).upper()


def format_board(board):
    output = "\n _______ \n/       \\\n"
    for i in board:
        output += "| "
        for j in range(5):
            if i[j] == secret_word[j]:
                output += colors.GREEN + i[j] + colors.RESET
            elif i[j] in secret_word:
                output += colors.YELLOW + i[j] + colors.RESET
            else:
                output += i[j]
        output += " |\n"
    output += "\\_______/\n"
    return output


board = []

while True:
    word = input("Enter a word: ").upper()
    if len(word) != 5:
        print("Are you sure you entered the word right?")
        continue
    board.append(word)
    if len(board) > 6:
        print(f"You lose! The word was {secret_word}")
        break
    print(format_board(board))
    if word == secret_word:
        print("You solved it!")
        break