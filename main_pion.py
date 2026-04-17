import pygame as pg
import sys,os
import class_test as pc
pg.display.init()
longueur= 400
largeur = 400
cote_l = longueur/8
width_rect = (cote_l)/2
cl= int(width_rect)
#NE PAS TOUCHER à flags
#flags = pg.FULLSCREEN
flags = pg.RESIZABLE | pg.SCALED
screen = pg.display.set_mode((longueur, largeur),flags)
#Ne pas toucher
#pg.display.toggle_fullscreen()
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

# Sans le .convert()
#
if __name__ == "__main__":
    im = pg.image.load(os.path.join('Pions', 'Pw.png'))
    ima = pg.transform.scale(im, (cote_l, cote_l))
    # Pas optimiser pour l'instant
    white_pawn = pc.King((0, cote_l), 0, 'Pawn', 1, ima)
    white_pawn1 = pc.King((cote_l, cote_l), 0, 'Pawn', 1, ima)
    white_pawn2 = pc.King((cote_l * 2, cote_l), 0, 'Pawn', 1, ima)
    white_pawn3 = pc.King((cote_l * 3, cote_l), 0, 'Pawn', 1, ima)
    white_pawn4 = pc.King((cote_l * 4, cote_l), 0, 'Pawn', 1, ima)
    white_pawn5 = pc.King((cote_l * 5, cote_l), 0, 'Pawn', 1, ima)
    white_pawn6 = pc.King((cote_l * 6, cote_l), 0, 'Pawn', 1, ima)
    white_pawn7 = pc.King((cote_l * 7, cote_l), 0, 'Pawn', 1, ima)




# un problème de gamma, les bords sont pas trop visibles
#Positionne l'image white_pawn
# Pas optimiser
screen.blit(ima,(white_pawn.position))
screen.blit(ima,(white_pawn1.position))
screen.blit(ima,(white_pawn2.position))
screen.blit(ima,(white_pawn3.position))
screen.blit(ima,(white_pawn4.position))
screen.blit(ima,(white_pawn5.position))
screen.blit(ima,(white_pawn6.position))
screen.blit(ima,(white_pawn7.position))


# get les dimensions de la fenêtre
get_sizes=pg.display.get_desktop_sizes()
print(get_sizes)
if __name__ == "__main__":
    pg.display.update()
    while True:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                sys.exit()
            pg.display.update()







