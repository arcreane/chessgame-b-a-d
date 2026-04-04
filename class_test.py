import pygame as pg
import os
class Piece:
    def __init__(self,position,color,type_piece,point,imu):
        self.position = position
        self.color = color

        self.type_piece = type_piece
        self.point = point
        self.im = imu
        id=[0]
        if self.color == 0:
            self.color = pg.Color('white')

        if self.color == 1:
            self.color = (0, 0, 0)

    def isValidMove(newPosition, board):
        pass
    #Override:lettre = type de pièce
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
    #def image(self):
        #if self.color == 0:
        #    self.imu =pg.image.load(os.path.join('Kings','Kw.png')).convert()
        #    return self.imu
        #elif self.color == 1:
        #    self.imu =pg.image.load(os.path.join('Kings','Kb.png')).convert()
        #    return self.imu

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

      pass
if __name__ == "__main__":
    white_pika=King((0,0),0,'Pawn',1,None)
    print(white_pika.color)
    print(white_pika.type_piece)
   # print(white_king.imu)



    #black_king = King((0, 0), 1, None,0)
    #print(black_king.color)


