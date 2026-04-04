import pygame as pg
class Piece:
    def __init__(self,position,color,image,type_piece,point):
        self.position = position
        self.color = color
        self.image = image
        self.type_piece = type_piece
        id=[0]
        if self.color == 0:
            self.color = pg.Color('white')
        if self.color == 1:
            self.color = (0, 0, 0)

    def isValidMove(newPosition, board):
        pass
    #Override bizarre
    def __str__(self):
        self.ide = id
        if self.type_piece == 'King':
            self.ide='K'
            return f'{self.ide}'
        elif self.type_piece == 'Queen':
            return str('Q')
        elif self.type_piece == 'Bishop':
            self.ide ='B'
            return str(self.ide)
        elif self.type_piece == 'Rook':
            return str('R')
        elif self.type_piece == 'Knight':
            return 'N'
        elif self.type_piece == 'Pawn':
            return 'P'
        else:
            return 'Pièce inconnue'


class King(Piece):
    def action(self):
        pass
    #def isValidMove(newPosition,board):

    pass
class Queen(Piece):
    def action(self):
       pass
class Bishop(Piece):
    def action(self):
       pass
class Knight(Piece):
    def action(self):
      pass
class Rook(Piece):
    def action(self):
       pass

class Pawn(Piece):
    def action(self):
      pass
if __name__ == "__main__":
    white_king = King((0, 0), 0, 1,'Bishop',0)
    #print(white_king.color)
    print(white_king.type_piece)
    print(white_king)
    black_king = King((0, 0), 1, 1, None,0)
    #print(black_king.color)


