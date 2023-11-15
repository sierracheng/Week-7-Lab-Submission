1# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import os
import logging
from datetime import datetime
from logic import make_empty_board, get_winner, is_draw
from move import get_move,other_player,isBot
from utility import logging

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging settings
#log_filename = datetime.now().strftime("logs/game_%Y%m%d_%H%M%S.log")
log_filename = "logs/0.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)
# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = "X"    
    is_one_player = int(input("Enter the number of players (1 or 2): ")) == 1

    while True:
        x,y = get_move(isBot(is_one_player, player), board)
        # TODO: Update the boarother_playerd.
        board[int(x)][int(y)] = player
        print("Current board is: ", board)

        winner = get_winner(board)

        # TODO: Update who's turn it is.
        if not winner:
            player = other_player(player)

        if winner != None:
            logging.info(board)
            print("winner is " + winner)
            break
            
        if is_draw(board):
            logging.info(board)
            print("Game result is draw. No winner.")
            break