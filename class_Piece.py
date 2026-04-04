import pygame as pg
class Piece:
    def __init__(self,position,color,image,type_piece):
        self.position = position
        self.color = color
        self.image = image
        self.type_piece = type_piece
        if self.color == 0:
            self.color = pg.Color('white')
        if self.color == 1:
            self.color = (0, 0, 0)
    def __str__(self):
        if self.type_piece == 'King':
            return str('K')
        elif self.type_piece == 'Queen':
            return str('Q')
        elif self.type_piece == 'Bishop':
            id ='B'
            return id
        elif self.type_piece == 'Rook':
            return str('R')
        elif self.type_piece == 'Knight':
            return 'N'
        elif self.type_piece == 'Pawn':
            return 'P'
        else:
            return 'Pièce inconnue'


class King(Piece):
    #def isValidMove(newPosition,board):

    pass
class Queen(Piece):
    pass
class Bishop(Piece):
    pass
class Knight(Piece):
    pass
class Rook(Piece):
    pass
class Pawn(Piece):
    pass
if __name__ == "__main__":
    white_king = King((0, 0), 0, 1,'Bishop')
    #print(white_king.color)
    print(white_king.type_piece)

    black_king = King((0, 0), 1, 1, None)
    #print(black_king.color)


