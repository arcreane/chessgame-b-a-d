import pygame as pg
import sys,os
import class_test as pc

pg.display.init()
longueur= 400
largeur = 400
cote_l = longueur/8
width_rect = (cote_l)/2
cl= int(width_rect)

# NE PAS TOUCHER à flags
flags = pg.RESIZABLE | pg.SCALED
screen = pg.display.set_mode((longueur, largeur),flags)

clock = pg.time.Clock()
background= pg.draw.rect(screen,(128,128,128),(0,0,longueur,largeur))
clock.tick(60)
l = longueur/8

# Plateau généré (même style que ton code)
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

# --- CHARGEMENT IMAGE REINE ---
if __name__ == "__main__":
    im = pg.image.load(os.path.join('Pions', 'Qw.png'))   # image reine blanche
    ima = pg.transform.scale(im, (cote_l, cote_l))

    # Création de la Reine (même style que tes pions)
    white_queen = pc.Queen((3 * cote_l, 0), 0, 'Queen', 9, ima)

# --- AFFICHAGE DE LA REINE ---
screen.blit(ima, (white_queen.position))

# --- INFOS SOURIS ---
if __name__ == "__main__":
    pg.mouse.set_pos((0, 0))
    mouse_x_y = pg.mouse.get_pos()
    print(mouse_x_y)

# Dimensions écran
get_sizes = pg.display.get_desktop_sizes()
print(get_sizes)

# --- BOUCLE PRINCIPALE ---
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
