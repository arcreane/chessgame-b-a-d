from class_Piece import Piece
class King(Piece):
    def action(self, board, x, y):
        moves = []

        directions = [
            (1, 0),    
            (-1, 0),   
            (0, 1),     
            (0, -1),    
            (1, 1),     
            (1, -1),    
            (-1, 1),   
            (-1, -1)    
        ]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if board.is_inside(nx, ny):
                piece = board.get_piece(nx, ny)
              
                if piece is None:
                    moves.append((nx, ny))

                elif piece.color != self.color:
                    moves.append((nx, ny))

                else:
                    continue

        return moves
