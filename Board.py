class Board:

    WIDTH = 3
    HEIGHT = 3
    EMPTY_CELL = '-'

    def __init__(self):
        self.board = self._get_board()

    def __repr__(self):
        board = ''
        for row in self.board:
            board += str(row) + '\n'
        return board

    def set_cell(self, x, y, sign):
        self.board[y][x] = sign

    def get_cell(self, x, y):
        return self.board[y][x]

    def player_won(self):
        # Check if a row has 3 in a row
        for y in range(Board.HEIGHT):
            if self.board[y][0] != Board.EMPTY_CELL and self.board[y][0] == self.board[y][1] and self.board[y][0] == self.board[y][2]:
                return True
        # Check if a column has 3 in a row
        for x in range(Board.WIDTH):
            if self.board[0][x] != Board.EMPTY_CELL and self.board[0][x] == self.board[1][x] and self.board[0][x] == self.board[2][x]:
                return True
        # Checking main diagonal
        if self.board[0][0] != Board.EMPTY_CELL and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return True
        # Checking secondary diagonal
        if self.board[2][0] != Board.EMPTY_CELL and self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2]:
            return True
        return False

    def _get_board(self):
        board = []
        for x in range(Board.WIDTH):
            board.append([])
            for y in range(Board.HEIGHT):
                board[x].append(Board.EMPTY_CELL)
        return board


