class Move:

    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def __str__(self):
        s = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final  # on va forcer pygame a d abord aller dans square car avant de valider le mouv il faut voir si ils sont sur la meme case