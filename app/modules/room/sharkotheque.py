import pygame

from app.modules.boss.sharkotequaire.sharkotequaire import Sharkotequaire
from app.modules.musicPlayer.musicPlayer import MusicPlayer
from app.modules.room.room import Room


class Sharkotheque(Room):
    def __init__(self, game):
        super().__init__(game)
        self.music_player = MusicPlayer()
        self.text = game.text
        self.id = 'Sharkotheque'
        self.background_image = pygame.image.load('./assets/environnement/Map/bibliotheque2.png')
        self.background_gradiant = pygame.image.load('./assets/environnement/Fonds/water_background.png')
        self.boss = Sharkotequaire(self.game, [555, 295])
        self.detector = pygame.Rect([325, 150], [10, 300])
        self.has_played_animation = False

    def draw(self):
        self.game.screen.blit(self.background_gradiant, (0, 0))
        self.game.screen.blit(self.background_image, (0, 0))
        self.boss.draw()
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.detector, 5)
        # self.text.display_txt()
        # TODO: Dialogues boss

    def check_for_interaction(self):
        pass

    def update(self):
        if not self.has_played_animation and self.detector.colliderect(self.game.player.collider):
            self.start_animation()
            self.has_played_animation = True

    def start_animation(self):
        print("ANIMATION !")
        self.game.player.
