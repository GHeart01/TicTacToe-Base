# game.py
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        # Initialize the board with empty spaces
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # Print the current state of the board (no numbers, just X, O, or blank spaces)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Print the numbers 1-9 on the board (shown only at the beginning)
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Return all available moves as a list of integers (where the board still shows a blank space)
        return [i + 1 for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Check if there are any empty squares left (i.e., squares with a blank space)
        return ' ' in self.board
    
    def num_empty_squares(self):
        # Count how many empty squares (blank spaces) remain
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # Subtract 1 from the square to map to 0-8 (because the user enters 1-9)
        if self.board[square - 1] == ' ':
            self.board[square - 1] = letter
            if self.winner(square - 1, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check the diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
        
def play(game, x_player, o_player, print_game=True):
    # Show the board with numbers at the start of the game
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                # Show the board during the game (no numbers)
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # Switch turns
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)