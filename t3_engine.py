import random as rd


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
            return 'This cell is occupied! Choose another one!'
        else:
            return None

    def __str__(self):
        print_board = '-' * (self.dimensions ** 2) + '\n'
        for i in range(3):
            print_board += '| ' + ' '.join(self.board[i]) + ' |\n'
        print_board += '-' * (self.dimensions ** 2)

        return print_board


class T3Engine:

    def __init__(self):
        self.board = None

    def start(self):
        self.create_board()
        print(self.board)
        player = 1
        game_state = {'not_finished': True, 'game_result': None}

        while game_state['not_finished']:

            allowed_move = self.do_move(player)
            while not allowed_move['updated']:
                print(allowed_move['action'])
                allowed_move = self.do_move(player)

            game_state = self.evaluate_board(player)
            print(self.board)
            player = player % 2 + 1
            print(game_state['game_result'])

    def create_board(self, dimensions=3, string_board=None):
        self.board = Board(dimensions, string_representation=string_board)

    def won(self, player, rows):
        return (any(all([True if rows[i][j] == player else False for j in range(3)]) for i in range(3))
                or any(all([True if rows[j][i] == player else False for j in range(3)]) for i in range(3))
                or all(True if rows[i][i] == player else False for i in range(3))
                or all(True if rows[2 - i][i] == player else False for i in range(3)))

    def evaluate_board(self, player):
        rows = self.board.get_board_data()
        player = 'X' if player == 1 else 'O'

        x_number = sum(l.count('X') for l in rows)
        o_number = sum(l.count('O') for l in rows)
        game_state = {}

        if self.won(player, rows):
            game_state['not_finished'] = False
            game_state['game_result'] = '{} wins'.format(player)
        elif x_number + o_number != 9:
            game_state['not_finished'] = True
            game_state['game_result'] = 'Game not finished'
        else:
            game_state['not_finished'] = False
            game_state['game_result'] = 'Draw'

        return game_state

    def do_move(self, player):
        user_input = input('Enter the coordinates: ')
        player_symbol = 'X' if player == 1 else 'O'
        if player_symbol == 'X':
            user_input = input('Enter the coordinates: ')
            return self.player_move(user_input, player_symbol)
        elif player_symbol == 'O':
            return self.cpu_move('easy', player_symbol)

    def player_move(self, user_input, player_symbol):
        move_result = self.board.update_board(user_input, player_symbol)
        return move_result

    def cpu_move(self, mode, player_symbol):
        if mode == 'easy':
            print('Making move level "{}"'.format(mode))
            return self.run_easy_mode(player_symbol)

    def run_easy_mode(self, player_symbol):
        board_data = self.board.get_board_data()
        free_row = []
        free_column = []

        for index, row in enumerate(board_data):
            if ' ' or '_' in row[index]:
                free_row.append(index)
        random_row = free_row[rd.randint(0, len(free_row) - 1)]

        for index, column in enumerate(board_data[random_row]):
            if ' ' or '_' == column:
                free_column.append(index)

        random_column = free_column[rd.randint(0, len(free_column) - 1)]
        self.board.board[random_row][random_column] = player_symbol

        return {'updated': True, 'action': self.board}


if __name__ == '__main__':
    new_game = T3Engine()
    new_game.start()
