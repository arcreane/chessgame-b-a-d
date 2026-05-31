import pygame
import sys  # import sys va permettre de quitter l application lorsque on le souhaite cad faire apparaitre la croix

from const import *
from game import Game
from square import Square
from move import Move

class Main:

    def __init__(self):
        pygame.init()  # permet d'initialiser pygame ce qui est obligatoire lorsqu'on travaille avec pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # permet de créer le screen sur lequel on va jouer
        pygame.display.set_caption('Chess')  # c tout simplement le nom de l'application
        self.game = Game()  # Permet de referencer et de donner l'accès de game à main

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():  # permet d acceder a tout les évènements possibles pour pygame

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE  # il faut comprendre que les coord et les drag sont 2 choses différentes . l'un prend les coord de l'ecran l'autre celui du plateau qu'on a crée
                    clicked_col = dragger.mouseX // SQSIZE

                    # SI on click dans une case qui a une piece
                    if board.squares[clicked_row][clicked_col].has_piece():  # evite de prendre une piece qui n'existe pas car si il y a rien dans la case on va pas prendre quelque chose puisqu'il y a rien
                        piece = board.squares[clicked_row][clicked_col].piece
                        # on vérifie que c'est bien le tour de cette couleur
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)  # permet de save si on a pris une piece ou pas
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                # bouger la souris
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                # relacher le click
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # on crée le mouvement entre la case initiale et la case finale
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # mouvement valide ?
                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece, move)
                            board.set_true_en_passant(dragger.piece)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            # tour suivant
                            game.next_turn()

                    dragger.undrag_piece()

                # touches clavier
                elif event.type == pygame.KEYDOWN:
                    # changer de thème avec T
                    if event.key == pygame.K_t:
                        game.change_theme()
                    # reset avec R
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                elif event.type == pygame.QUIT:  # Permet de quitter si le joueur appuie sur la croix pour quitter
                    pygame.quit()
                    sys.exit()

            pygame.display.update()  # Toujours la dernière ligne de code car ça va update le screen


main = Main()
main.mainloop()