import pygame as pg
import os

class Piece:
    def __init__(self, position, color, type_piece, point, imu):
        self.position = position
        self.color = color
        self.type_piece = type_piece
        self.point = point
        self.imu = imu

        # Gestion couleur comme ton code
        if self.color == 0:
            self.color = pg.Color('white')
        if self.color == 1:
            self.color = (0, 0, 0)

    def isValidMove(newPosition, board):
        pass

    def __str__(self):
        if self.type_piece == 'King':
            return 'K'
        elif self.type_piece == 'Queen':
            return 'Q'
        elif self.type_piece == 'Bishop':
            return 'B'
        elif self.type_piece == 'Rook':
            return 'R'
        elif self.type_piece == 'Knight':
            return 'N'
        elif self.type_piece == 'Pawn':
            return 'P'
        else:
            return 'Pièce inconnue'


class King(Piece):
    def action(self):
        pass


if __name__ == "__main__":
    # Test couleur
    white_king = King((0,0), 0, 'King', 1, None)
    black_king = King((0,0), 1, 'King', 1, None)

    print(f"{white_king.color} est la couleur du roi blanc")
    print(f"{black_king.color} est la couleur du roi noir")

    # Test override
    print(white_king.type_piece)
    print(white_king.__str__())

    if white_king.__str__() == 'K':
        print("ok")
    else:
        print("not ok")
