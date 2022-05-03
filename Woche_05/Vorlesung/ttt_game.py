"""
This file uses the TicTacToe class and launches the Command Line game
"""
import tictactoe

feld = tictactoe.TicTacToe()
counter = 0

while True:
    feld.print_field()
    if counter % 2 == 0:
        feld.update('X')
    else:
        feld.update('O')
    if feld.is_over():
        answer = input("Möchten Sie eine Revanche? [y/n] ")
        if answer == 'y':
            feld.reset_field()
            counter = 0
            continue
        else:
            break
    counter += 1
