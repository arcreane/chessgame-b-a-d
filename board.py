from const import *
from square import Square
from piece import *
from move import Move
import copy

class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]  # car pour l'instant le plateau que l'on a dessiné est juste un dessin mais il sert a rien pour l instant donc on va le décomposer pour que l'ordinateur comprenne ce qui se passe
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move, testing=False):  # testing=False permet d'éviter une boucle infinie lors du calcul des échecs
        initial = move.initial
        final = move.final

        en_passant_empty = self.squares[final.row][final.col].isempty()

        # console board move update
        self.squares[initial.row][initial.col].piece = None  # car on veut que la piece se deplace sur le final et non l initiale
        self.squares[final.row][final.col].piece = piece

        # promotion pion
        if isinstance(piece, Pawn):  # on va verifier si c bien un pion
            # prise en passant
            diff = final.col - initial.col
            if diff != 0 and en_passant_empty:
                self.squares[initial.row][initial.col + diff].piece = None
                self.squares[final.row][final.col].piece = piece
            else:
                self.check_promotion(piece, final)

        # roque
        if isinstance(piece, King):
            if self.castling(initial, final) and not testing:
                diff = final.col - initial.col
                rook = piece.left_rook if (diff < 0) else piece.right_rook  # permet de savoir si c un queen ou un roi castle
                self.move(rook, rook.moves[-1])  # permet de faire agir le dernier mouv quand initialise dans rook.move pdt le castle ( ex left_rook)

        # move
        piece.moved = True
        # clear valid moves car une fois que la piece s est deplacée on remet les compteurs à zero
        piece.clear_moves()
        self.last_move = move

    def valid_move(self, piece, move):  # cependant si on met juste return move in piece.move Pycharm ne pourra pas savoir comment comparer 2 mouvements
        return move in piece.moves

    def check_promotion(self, piece, final):
        if final.row == 0 or final.row == 7:
            self.squares[final.row][final.col].piece = Queen(piece.color)

    def castling(self, initial, final):
        return abs(initial.col - final.col) == 2  # le roi peut seulement se deplacer d une case alors si il se deplace de 2 c un roque

    def set_true_en_passant(self, piece):
        if not isinstance(piece, Pawn):
            return
        # on remet en_passant à False pour tous les pions
        for row in range(ROWS):
            for col in range(COLS):
                if isinstance(self.squares[row][col].piece, Pawn):
                    self.squares[row][col].piece.en_passant = False
        # uniquement le pion qui vient de se déplacer peut être pris en passant
        piece.en_passant = True

    def in_check(self, piece, move):
        # on copie la piece et le plateau pour simuler le mouvement sans modifier le vrai plateau
        temp_piece = copy.deepcopy(piece)
        temp_board = copy.deepcopy(self)
        temp_board.move(temp_piece, move, testing=True)

        for row in range(ROWS):
            for col in range(COLS):
                if temp_board.squares[row][col].has_enemy_piece(piece.color):
                    p = temp_board.squares[row][col].piece
                    temp_board.calc_moves(p, row, col, bool=False)
                    for m in p.moves:
                        if isinstance(m.final.piece, King):
                            return True
        return False

    def calc_moves(self, piece, row, col, bool=True):

        def pawn_moves():
            # Start : au debut un pion peut s avancer de 2 cases
            steps = 1 if piece.moved else 2

            # vertical move
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # create a new move
                        move = Move(initial, final)
                        # on regarde si il y a des check potentielles
                        if bool:
                            if not self.in_check(piece, move):  # si on met juste if not in_check alors elle va appeler mouv mais mouv appelle in_check donc boucle infinie
                                piece.add_move(move)
                        else:
                            piece.add_move(move)
                    else:  # bloqué par quelque chose
                        break
                else:  # atteint la valeur limite
                    break

            # diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col - 1, col + 1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        move = Move(initial, final)
                        if bool:
                            if not self.in_check(piece, move):
                                piece.add_move(move)
                        else:
                            piece.add_move(move)

            # prise en passant
            r = 3 if piece.color == 'white' else 4
            fr = 2 if piece.color == 'white' else 5
            # gauche
            if Square.in_range(col - 1) and row == r:
                if self.squares[row][col - 1].has_enemy_piece(piece.color):
                    p = self.squares[row][col - 1].piece
                    if isinstance(p, Pawn):
                        if p.en_passant:
                            initial = Square(row, col)
                            final = Square(fr, col - 1, p)
                            move = Move(initial, final)
                            if bool:
                                if not self.in_check(piece, move):
                                    piece.add_move(move)
                            else:
                                piece.add_move(move)
            # droite
            if Square.in_range(col + 1) and row == r:
                if self.squares[row][col + 1].has_enemy_piece(piece.color):
                    p = self.squares[row][col + 1].piece
                    if isinstance(p, Pawn):
                        if p.en_passant:
                            initial = Square(row, col)
                            final = Square(fr, col + 1, p)
                            move = Move(initial, final)
                            if bool:
                                if not self.in_check(piece, move):
                                    piece.add_move(move)
                            else:
                                piece.add_move(move)

        def knight_moves():
            # 8 move possible donc on va créer des tuples car on a besoin des lignes et des colonnes
            possible_moves = [
                (row - 2, col + 1),
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row - 2, col - 1),
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        # creation du mouv
                        move = Move(initial, final)
                        if bool:
                            if not self.in_check(piece, move):
                                piece.add_move(move)
                            else: break
                        else:
                            piece.add_move(move)

        def straightline_moves(incrs):
            # pour les pièces qui se déplacent en ligne droite : fou, tour, reine
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        move = Move(initial, final)

                        # vide on continue car les déplacements vers l infini en lignes droites alors pk s arreter
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            if bool:
                                if not self.in_check(piece, move):
                                    piece.add_move(move)
                            else:
                                piece.add_move(move)

                        # has enemy piece
                        elif self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            if bool:
                                if not self.in_check(piece, move):
                                    piece.add_move(move)
                            else:
                                piece.add_move(move)
                            break

                        # piece alliée : on s'arrête sans capturer
                        elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break

                    else: break

                    # on incrémente les incréments
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def king_moves():
            adjs = [
                (row - 1, col + 0),  # up
                (row - 1, col + 1),  # up-right
                (row + 0, col + 1),  # right
                (row + 1, col + 1),  # down-right
                (row + 1, col + 0),  # down
                (row + 1, col - 1),  # down-left
                (row + 0, col - 1),  # left
                (row - 1, col - 1),  # up-left
            ]
            # et on va faire comme pour le knight c est a dire pour chaque mouv on va verifier 1 par 1 si il est valide car peu de mouv
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        if bool:
                            if not self.in_check(piece, move):
                                piece.add_move(move)
                            else: break
                        else:
                            piece.add_move(move)

            if not piece.moved:
                # Rook Reine (roque côté gauche)
                left_rook = self.squares[row][0].piece
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            if self.squares[row][c].has_piece():  # tout ces if permettent de verifier un par un si il y a des pieces entre les deux
                                break
                            if c == 3:
                                # la piece est un roi , mais pour changer de position on va l attribuer à un rook
                                piece.left_rook = left_rook
                                # rook move
                                initial = Square(row, 0)
                                final = Square(row, 3)
                                moveR = Move(initial, final)
                                # king move
                                initial = Square(row, col)
                                final = Square(row, 2)
                                moveK = Move(initial, final)
                                if bool:
                                    if not self.in_check(piece, moveK) and not self.in_check(left_rook, moveR):
                                        left_rook.add_move(moveR)
                                        piece.add_move(moveK)
                                else:
                                    left_rook.add_move(moveR)
                                    piece.add_move(moveK)

                # Rook roi (roque côté droit)
                right_rook = self.squares[row][7].piece
                if isinstance(right_rook, Rook):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            if self.squares[row][c].has_piece():  # tout ces if permettent de verifier un par un si il y a des pieces entre les deux
                                break
                            if c == 6:
                                # la piece est un roi , mais pour changer de position on va l attribuer à un rook
                                piece.right_rook = right_rook
                                # rook move
                                initial = Square(row, 7)
                                final = Square(row, 5)
                                moveR = Move(initial, final)
                                # king move
                                initial = Square(row, col)
                                final = Square(row, 6)
                                moveK = Move(initial, final)
                                if bool:
                                    if not self.in_check(piece, moveK) and not self.in_check(right_rook, moveR):
                                        right_rook.add_move(moveR)
                                        piece.add_move(moveK)
                                else:
                                    right_rook.add_move(moveR)
                                    piece.add_move(moveK)

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            straightline_moves([
                (-1, 1),   # up-right
                (-1, -1),  # up-left
                (1, 1),    # down-right
                (1, -1),   # down-left
            ])
        elif isinstance(piece, Rook):
            straightline_moves([
                (-1, 0),  # up
                (0, 1),   # right
                (1, 0),   # down
                (0, -1),  # left
            ])
        elif isinstance(piece, Queen):
            straightline_moves([
                (-1, 1),   # up-right
                (-1, -1),  # up-left
                (1, 1),    # down-right
                (1, -1),   # down-left
                (-1, 0),   # up
                (0, 1),    # right
                (1, 0),    # down
                (0, -1),   # left
            ])
        elif isinstance(piece, King):
            king_moves()

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)  # On parcourt ce plateau et au lieu d'ajouter des 0, on va ajouter l'objet square ce qui est plus pratique

    def _add_pieces(self, color):  # _ encapsulation. On le met _ pour signifier que c une fonction privée. Bref, on ne veut pas que l'utilisateur l'utilise
        if color == 'white':
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))  # on veut toute les pieces donc on doit import le piece et comme add pieces a pour paramètre color alors dans Pawn doit mettre aussi color

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))  # on met 1 et 6, car les cavaliers sont uniquement sur ces colonnes 1 et 6
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))  # on a seulement 1 reine et un roi

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))
