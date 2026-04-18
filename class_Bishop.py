import class_test.py
import pygame as pg
import os
class Bishop(Piece):
    def action(self, board, x, y):
        moves = []
      directions = [
            (1, 1),    
            (1, -1),  
            (-1, 1),   
            (-1, -1)   
        ]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            while board.is_inside(nx, ny):
                piece = board.get_piece(nx, ny)

                if piece is None:
                    moves.append((nx, ny))

                elif piece.color != self.color:
                    moves.append((nx, ny))
                    break  
                else:
                    break   
                nx += dx
                ny += dy
                
        return moves
