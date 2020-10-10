class Board:

    def __init__(self, dimensions=3, string_representation=None):
        self.dimensions = dimensions
        self.board = self.generate_new_board(string_representation)

    def get_board_data(self):
        return self.board

    def generate_new_board(self, string_board=None):
        if string_board:
            return [[string_board[x + (3 * i)] for x in range(self.dimensions)] for i in range(self.dimensions)]
        else:
            return [[' ' for _ in range(self.dimensions)] for _ in range(self.dimensions)]

    def update_board(self, user_input, player):
        move_evaluation = self.check_coordinates(user_input)

        if move_evaluation:
            return {'updated': False, 'action': move_evaluation}
        else:
            first_value, second_value = map(int, user_input.split())
            coord_i, coord_j = 3 - int(second_value), int(first_value) - 1
            self.board[coord_i][coord_j] = player
            return {'updated': True, 'action': self.board}

    def check_coordinates(self, user_input):
        try:
            coord_j, coord_i = map(int, user_input.split())
        except (UnboundLocalError, ValueError):
            return 'You should enter numbers!'
        if coord_i > len(self.board) or coord_j > len(self.board[0]):
            return 'Coordinates should be from 1 to 3!'
        elif self.board[3 - coord_i][coord_j - 1] != '_' and self.board[3 - coord_i][coord_j - 1] != ' ':
            print(3-coord_i, coord_j - 1)
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
