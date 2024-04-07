import pygame


class MusicPlayer:
    def __init__(self):
        self.player = pygame.mixer.music

    def play(self, path):
        self.player.load(path)
        self.player.play()

    def stop(self):
        self.player.stop()
        self.player.unload()
