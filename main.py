import pygame as pg
import sys
longueur= 800
largeur = 800
cote_l = longueur/8
width_rect = (cote_l)/2
cl= int(width_rect)
screen = pg.display.set_mode((longueur, largeur))
clock = pg.time.Clock()
background= pg.draw.rect(screen,(128,128,128),(0,0,longueur,largeur))
clock.tick(60)



pg.draw.rect(screen,(255,255,255),(0,0,cote_l,cote_l),cl)
pg.draw.rect(screen,(0,0,0),(cote_l,0,cote_l,cote_l),cl)
pg.draw.rect(screen,(255,255,255),(cote_l*2,0,cote_l,cote_l),cl)
pg.draw.rect(screen,(255,255,255),(cote_l*3,0,cote_l,cote_l),cl)
class Piece:
    def __init__(self,x,y,point,color,image):
        self.x=x
        self.y=y
        self.point=point
        self.color=color
        self.image=image
        def action (self):
           pass
class Pion(Piece):
     def action(self):
        return 'kk'
#im= pg.image.load('sources\Pb.png').convert()
#im= pg.image.load('playertag.bmp').convert().set_colorkey('black')
#piece= Piece(0,0,1,None,im)

pg.display.update()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()






