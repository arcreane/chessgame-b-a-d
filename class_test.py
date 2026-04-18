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

    # Override : lettre = type de pièce
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
            return 'K'
        elif self.type_piece == 'Pawn':
            return 'P'
        else:
            return 'Pièce inconnue'


class Queen(Piece):
    def action(self):
        pass


if __name__ == "__main__":
    white_queen = Queen((0,0), 0, 'Queen', 9, None)
    black_queen = Queen((0,0), 1, 'Queen', 9, None)

    # Test couleur
    print(f"{white_queen.color} est la couleur")
    print(f"{black_queen.color} est la couleur")

    # Test override pièce = lettre
    print(white_queen.type_piece)
    print(white_queen.__str__())

    if white_queen.__str__() == 'Q':
        print('ok')
    else:
        print('not ok')
