import pygame as pg
import sys, os
import class_test as pc

pg.display.init()

longueur = 400
largeur = 400
cote_l = longueur / 8
wdith_rect = (cote_l) / 2
cl = int(width_rect)

flags = pg.resizable | pg.scaled
screen = pg.display.set.mode((longueur, largeur), flags)

clock = pg.time.clock()
background = pg.draw.rect(screen, (128,128,128), (0,0,longueur,largeur))
clock.tick(60)

# Plateau (même style que ton code)
for i in range(0,8):
    m = l * i
    if i % 2 == 0:
        pg.draw.rect(screen, (255,255,255), (m, 0, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0,0,0), (m, l, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255,255,255), (m, 100, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0,0,0), (m, 150, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255,255,255), (m, 200, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0,0,0), (m, 250, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255,255,255), (m, 300, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0,0,0), (m, 350, cote_l, cote_l), cl)
    else:
        pg.draw.rect(screen, (0,0,0), (m, 0, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255,255,255), (m, l, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0,0,0), (m, 100, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255,255,255), (m, 150, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0,0,0), (m, 200, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255,255,255), (m, 250, cote_l, cote_l), cl)
        pg.draw.rect(screen, (0,0,0), (m, 300, cote_l, cote_l), cl)
        pg.draw.rect(screen, (255,255,255), (m, 350, cote_l, cote_l), cl)

# --- AFFICHAGE DU ROI ---

if __name__ == "__main__":
    # Charge l'image du Roi blanc
    im = pg.image.load(os.path.join('Pions', 'Kw.png'))
    ima = pg.transform.scale(im, (cote_l, cote_l))
    
    # Création du Roi
    white_king = pc.King((4 * cote_l, 0), 0, 'King', 1, ima)

# Affiche le Roi
screen.blit(ima, (white_king.position))

if __name__ == "__main__":
    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                print(pg.mouse.get_rel())
            if event.type == pg.MOUSEWHEEL:
                print("o")

            pg.display.update()







