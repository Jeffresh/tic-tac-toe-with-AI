class Board:

    def __init__(self, dimensions=3, string_representation=None):
        self.dimensions = dimensions
        self.board = self.generate_new_board(string_representation)

    def generate_new_board(self, string_board=None):
        if string_board:
            return [[string_board[x + i] for x in range(self.dimensions)] for i in range(self.dimensions)]
        else:
            return [[' ', ' ', ' '] for _ in range(self.dimensions)]

    def update_board(self, first_value, second_value, player):
        coord_i, coord_j = second_value - 1, first_value - 1
        move_evaluation = self.check_coordinates(coord_i, coord_j)

        if move_evaluation:
            return False, move_evaluation
        else:
            self.board[second_value - 1][first_value - 1] = player
            return True, self.board

    def check_coordinates(self, coord_i, coord_j):
        if type(coord_i) != int or coord_j != int:
            return 'You should enter numbers!'
        elif coord_i >= len(self.board) or coord_j >= len(self.board[0]):
            return 'Coordinates should be from 1 to 3!'
        elif self.board[coord_j][coord_j] != '_' or self.board[coord_j][coord_j]:
            return 'This cell is occupied! Choose another one!'
        else:
            return None

    def __str__(self):
        print_board = '-' * 9 + '\n'
        for i in range(3):
            print_board += '| ' + ' '.join(self.board[i]) + ' |\n'
        print_board += '-' * 9

        return print_board


class T3Engine:
    def play(self):
        string_board = input('Enter cells: ')
        self.create_board(string_board)

    def create_board(self, string_representation):
        pass

    def evaluate_board(self):
        pass

    def do_move(self, player):
        pass

    def player_move(self):
        pass

    def cpu_move(self):
        pass

    def evaluate_move(self):
        pass


if __name__ == '__main__':
    new_board = Board('_OOXX____')
    print(new_board)
