class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def is_inside(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def get_piece(self, x, y):
        if not self.is_inside(x, y):
            return None
        return self.grid[y][x]

    def place_piece(self, piece):
        if self.is_inside(piece.x, piece.y):
            self.grid[piece.y][piece.x] = piece

    def move_piece(self, piece, new_x, new_y):
        if not self.is_inside(new_x, new_y):
            return False

        if not piece.action(new_x, new_y, self.grid):
            return False

        self.grid[piece.y][piece.x] = None  
        piece.x = new_x
        piece.y = new_y
        self.grid[new_y][new_x] = piece     

        return True
