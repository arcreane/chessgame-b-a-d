import pygame as pg
class Music:
    def __init__(self):
        pg.mixer.init()
        self.is_playing = False

    def play(self, son, boucle=True):
        pg.mixer.music.load(son)
        pg.mixer.music.play(-1 if boucle else 0)
        self.is_playing = True
        self.play("Mus/Test.mp3")

    def stop(self):
        pg.mixer.music.stop()
        self.is_playing = False
    def pause(self):
        pg.mixer.music.pause()
    def resume(self):
        pg.mixer.music.unpause()
    def regler_volume(self, volume):
        pg.mixer.music.set_volume(volume)
