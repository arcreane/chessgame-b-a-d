import os

class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign  # Permettra a l'ia plus tard de voir que les blancs qu il faut manger et non les noirs
        self.moves = []      # Permet d enregistrer les actions qu on a fait . Donc utile plus tard
        self.moved = False   # Permet de savoir si on a bougé ou pas
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):  # ça sera le chemin pour trouver l'image de la piece tout simplement
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )  # le {} permet d indiquer que c une variable donc parfait quand on veut 2 fichier different

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []  # une fois que la piece s est deplacée on remet les compteurs à zero


class Pawn(Piece):  # Pions hérite de Piece

    def __init__(self, color):  # Le pion a une seule direction qui est définie par sa couleur ( haut et bas )
        self.dir = -1 if color == 'white' else 1  # dans pygame les valeurs de x augmentent de gauche a droite mais y de haut en bas . Donc si on veut monter alors il faut faire -1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)  # super sera Piece , la classe mere. On force le nom qui sera tj pawn , et la valeur est de 1 . Comme ça pour l'ia elle sera quelle piece ou non elle pourra sacrifier


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):

    def __init__(self, color):
        self.left_rook = None   # Nécessaire pour le roque côté reine
        self.right_rook = None  # Nécessaire pour le roque côté roi
        super().__init__('king', color, 10000.0)
