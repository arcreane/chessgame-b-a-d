import pygame as pg
from board import Board
from reine import Reine

pg.init()

screen = pg.display.set_mode((800, 800))
cote_l = 800 // 8

board = Board()

image_reine = pg.image.load("sources/Qb.png").convert_alpha()

queen = Reine(3, 7, 9, "white", image_reine)
board.place_piece(queen)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((200, 200, 200))

    for y in range(8):
        for x in range(8):
            piece = board.grid[y][x]
            if piece is not None:
                screen.blit(piece.image, (x * cote_l, y * cote_l))

    pg.display.flip()

pg.quit()
