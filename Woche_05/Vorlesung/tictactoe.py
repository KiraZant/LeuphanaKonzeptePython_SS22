class TicTacToe:
    """
    This class implements the game logic of Tic-Tac-Toe.
    Update method should be called whenever a player should make a turn
    Reset_field method should be called when the game is over and a re-match is wanted
    """
    def __init__(self):
        self.__field = {i: str(i) for i in range(1, 10)}

    def update(self, player):
        """
        Reads input from current player, updates the game field and checks whether game is over

        :param player: str: Identifier of current player ("X"/"O")
        """
        pos = int(input(f"Spieler {player} - Geben Sie die Nummer des Feldes an: "))
        if self.is_valid(pos):
            self.__field[pos] = player
            if self.is_over():
                print(f"Spieler {player} hat gewonnen!")
        else:
            self.update(player)

    def is_valid(self, position):
        """
        Checks whether chosen position is valid, i.e., not occupied yet

        :param position: int: Index of chosen position
        :return: bool: True if position is valid
        """
        return not self.__field[position] in ['X', 'O']

    def is_over(self):
        """
        Checks whether one of the players has won; is called in update method
        :return: bool: True, if a player has won the game
        """
        hor_ind = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ver_ind = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        diag_ind = [[1, 5, 9], [3, 5, 7]]
        hor = any([self.__field[i[0]] == self.__field[i[1]] == self.__field[i[2]] for i in hor_ind])
        ver = any([self.__field[i[0]] == self.__field[i[1]] == self.__field[i[2]] for i in ver_ind])
        diag = any([self.__field[i[0]] == self.__field[i[1]] == self.__field[i[2]] for i in diag_ind])
        return hor or ver or diag

    def reset_field(self):
        """
        Resets the game field to its initial position; called if a re-match is wanted
        """
        self.__field = {i: str(i) for i in range(1, 10)}

    def print_field(self):
        """
        Prints the current game field
        """
        for i in self.__field:
            print(self.__field[i], end='  ')
            if i % 3 == 0:
                print('')
