import pygame

from const import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square

class Game:

    def __init__(self):
        self.next_player = 'white'
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()

    # blit methods

    def show_bg(self, surface):  # surface va s'être le self.screen qu'on a créée avant
        theme = self.config.theme

        for row in range(ROWS):
            for col in range(COLS):
                # le plateau d'échecs est décomposé en 2 cases blanches et noires donc on va commencer par poser les blancs d'abord
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # un rectangle tuple a plusieurs paramètres : d'où on commence sur x, commence sur y puis la hauteur et la largeur qu'on veut
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

                # coordonnées des lignes
                if col == 0:
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    lbl = self.config.font.render(str(ROWS - row), 1, color)
                    lbl_pos = (5, 5 + row * SQSIZE)
                    surface.blit(lbl, lbl_pos)

                # coordonnées des colonnes
                if row == 7:
                    color = theme.bg.dark if (row + col) % 2 == 0 else theme.bg.light
                    lbl = self.config.font.render(Square.get_alphacol(col), 1, color)
                    lbl_pos = (col * SQSIZE + SQSIZE - 20, HEIGHT - 20)
                    surface.blit(lbl, lbl_pos)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # On veut regarder sur chaque case s'il y a une piece ou non
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # toutes les pieces sauf celle qu'on est en train de drag
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)  # On utilise la methode load de pygame pour convertir la texture en une image
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2  # permet de centrer l'image afin d'éviter des bugs
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        theme = self.config.theme

        if self.dragger.dragging:
            piece = self.dragger.piece

            # on parcourt tous les mouvements valides
            for move in piece.moves:
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            color = (180, 180, 180)
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(surface, color, rect, width=3)

    # other methods

    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()

    def reset(self):
        self.__init__()
