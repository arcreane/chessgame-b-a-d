import pygame as pg
import sys,os
import class_Piece as pc

longueur= 400
largeur = 400
cote_l = longueur/8
width_rect = (cote_l)/2
cl= int(width_rect)
#NE PAS TOUCHER à flags
#flags = pg.FULLSCREEN
flags = pg.RESIZABLE
screen = pg.display.set_mode((longueur, largeur),flags,vsync=1)
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
#if __name__ == "__main__":
im =pg.image.load(os.path.join('Kings','Kw.png'))
ima=pg.transform.scale(im,(cote_l,cote_l))

white_king = pc.King((cote_l*3, 0), 0,'Bishop',0,ima)
# un problème de gamma, les bords sont pas trop visibles
#Positionne l'image white_king
screen.blit(ima,(white_king.position))
# get les dimensions de la fenêtre
get_sizes=pg.display.get_desktop_sizes()
print(get_sizes)
pg.display.update()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()






