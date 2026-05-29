
import pygame as pg
import sys

class Time:
    def __init__(self, length):
        pg.init()
        self.screen = pg.display.set_mode((200, 100))
        pg.display.set_caption("Time")

        self.clock = pg.time.Clock()
        self.length = length
        self.start_time = pg.time.get_ticks()

        self.font = pg.font.Font(None, 40)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()


            elapsed = (pg.time.get_ticks() - self.start_time) // 1000
            remaining = max(0, self.length - elapsed)


            self.screen.fill((0, 0, 0))
            text = self.font.render(str(remaining), True, (255, 255, 255))
            self.screen.blit(text, (70, 30))

            pg.display.update()
            self.clock.tick(60)

