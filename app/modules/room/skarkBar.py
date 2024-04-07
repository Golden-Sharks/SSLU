import time

import pygame

from app.modules.boss.sharkeneger.sharkeneger import Sharkeneger
from app.modules.musicPlayer.musicPlayer import MusicPlayer
from app.modules.room.room import Room


class Sharkbar(Room):
    def __init__(self, game):
        super().__init__(game)
        self.music_player = MusicPlayer()
        self.text = game.text
        self.id = 'Sharkotheque'
        self.background_image = pygame.image.load('./assets/environnement/Map/bar2.png')
        self.background_gradiant = pygame.image.load('./assets/environnement/Fonds/water_background.png')
        self.boss = Sharkeneger(self.game, [800, 295])
        self.detector = pygame.Rect([325, 150], [10, 300])
        self.has_played_animation = False

    def draw(self):
        self.game.screen.blit(self.background_gradiant, (0, 0))
        self.game.screen.blit(self.background_image, (0, 0))
        # pygame.draw.rect(self.game.screen, (255, 0, 0), self.detector, 5)
        self.boss.draw()
        # self.text.display_txt()
        # TODO: Dialogues boss

    def check_for_interaction(self):
        pass

    def update(self):
        if not self.has_played_animation and self.detector.colliderect(self.game.player.collider):
            self.start_fight_animation()
            self.has_played_animation = True
            self.boss.first_attack_time = time.time()
            self.music_player.play('./data/musics/sharkeneger.mp3')
        self.boss.update()

        if self.has_played_animation and not self.boss.is_attacking:
            self.game.draw_end_screen('Felicitations, vous avez survecu !')

    def start_fight_animation(self):
        self.game.player.can_move = False
        if self.game.player.karma < 0:
            self.game.draw_end_screen(
                'Felicitation ! Route génocide finie.')
        else:
            self.boss.is_attacking = True
            self.boss.first_shot_time = time.time()
            self.game.player.can_move = True
