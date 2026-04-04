from piece import Piece  

class Reine(Piece):

    def action(self, new_x, new_y, board):
        dx = new_x - self.x
        dy = new_y - self.y

        if dx == 0 and dy == 0:
            return False

        if not (dx == 0 or dy == 0 or abs(dx) == abs(dy)):
            return False

        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)

        cur_x = self.x + step_x
        cur_y = self.y + step_y

        while cur_x != new_x or cur_y != new_y:
            if board[cur_y][cur_x] is not None:
                return False
            cur_x += step_x
            cur_y += step_y

        target = board[new_y][new_x]
        if target is not None and target.color == self.color:
            return False

        return True
