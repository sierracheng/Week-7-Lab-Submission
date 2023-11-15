from logic import get_winner,is_draw

# X win
test_board = [[None,"O","X"],["O",None,"X"],[None,None,"X"]]
winner = get_winner(test_board)
print(winner)

# O win
test_board = [["O","O","X"],["O",None,"X"],["O",None,"X"]]
winner = get_winner(test_board)
print(winner)

# Nobody win
test_board = [[None,"O","X"],["O",None,"X"],["O",None,"O"]]
winner = get_winner(test_board)
print(winner)


# O win
test_board = [["O","X","X"],["O","X",None],["O",None,None]]
winner = get_winner(test_board)
print(winner)

# X win
test_board = [["X","X",None],["O","O",None],["X","X","X"]]
winner = get_winner(test_board)
print(winner)

# is draw
test_board = [["X","X","O"],["O","O","X"],["X","O","O"]]
isDraw = is_draw(test_board)
print(isDraw)

# is not draw
test_board = [["O","X","O"],["X","O","X"],["X","O","O"]]
isDraw = is_draw(test_board)
print(isDraw)

