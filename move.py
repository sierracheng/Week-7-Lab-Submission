# This file is where player gives a move.
# Player could be a human or a bot.

import random
from utility import logging

def get_move(isBot, board):
    x = -1
    y = -1
    while True:
        if isBot is True:
            print("Getting a move of a bot")
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        else:
            print("TODO: take a turn!")

            # TODO: Input a move from the player.
            x, y = input("Enter the position of (x,y), split with comma: ").split(",")
            logging.info("Next move is (" + x + "," + y + ")")
            x = int(x)
            y = int(y)
        if is_valid_move(x,y,board):
            return x,y

def is_valid_move(x,y,board):
    if x < 0 or x > 2:
        print("Error: index must be in [0,2], but x is ", x)
        return False
    if y < 0 or y > 2:
        print("Error: index must be in [0,2], but y is ", y)
        return False
    if board[x][y] == "X" or board[x][y] == "O":
        print("Error: spot has been occupied")
        return False
    return True

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
        return "O"
    elif player == "O":
        return "X"
    
def isBot(hasBot, player):
    """Given the character for a player, returns the other player."""
    return hasBot and player == "O"


