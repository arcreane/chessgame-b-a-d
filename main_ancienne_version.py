import pygame as pg
import sys
import class_Piece as piece
longueur= 400
largeur = 400
cote_l = longueur/8
width_rect = (cote_l)/2
cl= int(width_rect)
screen = pg.display.set_mode((longueur, largeur))
clock = pg.time.Clock()
background= pg.draw.rect(screen,(128,128,128),(0,0,longueur,largeur))
clock.tick(60)
l = longueur/8
# Plateu généré mais par optimisé (Pas de proportionnalité avec la fenêtre)
for i in range(0,8):
    m=l*i
    if i%2==0:
        pg.draw.rect(screen, (255, 255, 255), (m, 0, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0, 0, 0), (m, l, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255, 255, 255), (m, 100, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0, 0, 0), (m, 150, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255, 255, 255), (m, 200, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0, 0, 0), (m, 250, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255, 255, 255), (m, 300, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0, 0, 0), (m, 350, cote_l, cote_l), cl)

    else:
        pg.draw.rect(screen, (0, 0, 0), (m, 0, cote_l,cote_l), cl)
        pg.draw.rect(screen, (255, 255, 255), (m, l, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0, 0, 0), (m, 100, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255, 255, 255), (m, 150, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0, 0, 0), (m, 200, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255, 255, 255), (m, 250, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0, 0, 0), (m, 300, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255, 255, 255), (m, 350, cote_l, cote_l), cl)




#pg.draw.rect(screen,(255,255,255),(0,0,cote_l,cote_l),cl)
#pg.draw.rect(screen,(0,0,0),(cote_l,0,cote_l,cote_l),cl)
#pg.draw.rect(screen,(255,255,255),(cote_l*2,0,cote_l,cote_l),cl)
#pg.draw.rect(screen,(255,255,255),(cote_l*3,0,cote_l,cote_l),cl)
#im= pg.image.load('sources\Pb.png').convert()
#im= pg.image.load('playertag.bmp').convert().set_colorkey('black')
#piece= Piece(0,0,1,None,im)


screen.blit(piece.white_king.King.im,(60,60))
pg.display.update()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()






