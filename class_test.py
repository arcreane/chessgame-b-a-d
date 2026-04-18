import pygame as pg
import os
class Piece:
    def __init__(self,position,color,type_piece,point,imu):
        self.position = position
        self.color = color
        self.type_piece = type_piece
        self.point = point
        self.imu = imu
        if self.color == 0:
            self.color = pg.Color('white')

        if self.color == 1:
            self.color = (0, 0, 0)

    def isValidMove(newPosition, board):
        pass
    #Override:lettre = type de pièce
    def __str__(self):
        if self.type_piece == 'King':
            ide = 'K'
            return ide
        elif self.type_piece == 'Queen':
            ide = 'Q'
            return ide
        elif self.type_piece == 'Bishop':
            ide = 'B'
            return ide
        elif self.type_piece == 'Rook':
            ide = 'R'
            return ide
        elif self.type_piece == 'Knight':
            ide = 'K'
            return ide
        elif self.type_piece == 'Pawn':
            ide ='P'
            return ide
        else:
            return 'Pièce inconnue'

class Pawn(Piece):
    def action(self):
        pass


    #def isValidMove(newPosition,board):
    pass


if __name__ == "__main__":
    white_pika=Pawn((0,0),0,'Pawn',1,None)
    black_pika = Pawn((0, 0), 1, 'Pawn', 1, None)

    # Test couleur, var color = 0 implique blanc et 1 implique noir
    print(f"{white_pika.color} est la couleur")
    print(f"{black_pika.color} est la couleur")

    # Tester l'override pièce= lettre
    print(white_pika.type_piece)
    print(white_pika.__str__())
    if white_pika.__str__() == 'P':
        print('ok')
    else:
        print('not ok')



