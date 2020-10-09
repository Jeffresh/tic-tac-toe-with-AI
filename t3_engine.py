class Board:
    def generate_new_board(self, string_board):
        return [[string_board[x + i] for x in range(3)] for i in range(3)]

    def __init__(self, string_representation):
        self.board = self.generate_new_board(string_representation)

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
