import json
import sys

import pygame

from app.modules.musicPlayer.musicPlayer import MusicPlayer
from app.modules.player.player import Player
from app.modules.room.room import Room
from app.modules.room.roomFactory import RoomFactory
from app.modules.room.tutorialRoom import TutorialRoom
from app.modules.textDisplay.textDisplay import TextDisplay


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        self.background = (255, 255, 255)
        self.running = True
        self.roomFactory = RoomFactory(self)
        self.text = TextDisplay(self, self.get_db())
        self.currentRoom: Room = TutorialRoom(self)
        self.player = Player(self, [45, self.currentRoom.ground_collider.top + 58])
        self.image = pygame.transform.scale(pygame.image.load("assets/logo_goldenSharks.png"), (200, 200))
        self.isGameOver = False
        self.hasWon = False
        self.music_player = MusicPlayer()

    def get_db(self):
        with open('./data/narrateur.json', 'r', encoding="utf-8") as file:
            return json.load(file)

    def update(self, keys):
        self.currentRoom.update()
        self.player.update(keys)
        self.clock.tick(60)

    def draw(self):
        self.screen.fill(self.background)
        self.currentRoom.draw()
        self.player.draw()
        pygame.display.update()

    def draw_menu_screen(self):
        self.screen.fill((50, 50, 50))
        self.screen.blit(self.image, (400, 50))
        title = "Super Shark Lab Undercover"
        text_surface_title = pygame.font.Font(None, 50).render(title, False, (15, 5, 107))
        self.screen.blit(text_surface_title, (250, 300))
        menuText = "Press Enter to start the game or Q to quit"
        text_surface_instructions = pygame.font.Font(None, 36).render(menuText, False, (15, 5, 107))
        self.screen.blit(text_surface_instructions, (260, 500))
        pygame.display.update()

    def run(self):
        pygame.display.flip()
        isInMenu = True
        self.draw_menu_screen()
        self.music_player.play('./data/musics/ecran.mp3')
        while isInMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    isInMenu = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        isInMenu = False
                    elif event.key == pygame.K_q:
                        self.running = False
                        isInMenu = False
                    elif event.key == pygame.K_e:
                        self.game_over()
                        isInMenu = False
                        self.running = False
        self.music_player.stop()
        self.music_player.play('./data/musics/main_loop.mp3')
        while self.running:
            self.draw()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update(keys)
        self.draw_end_screen()

    def game_over(self):
        self.isGameOver = True
        self.running = False
        self.draw_end_screen('Game Over')

    def draw_end_screen(self, texte=''):
        if texte == '':
            pygame.quit()
            sys.exit()
        self.music_player.play('./data/musics/ecran.mp3')
        self.screen.fill((50, 50, 50))
        text_surface_title = pygame.font.Font(None, 50).render(texte, False, (15, 5, 107))
        self.screen.blit(text_surface_title, (350, 300))
        menuText = "Press Enter to restart the game or Q to quit"
        text_surface_instructions = pygame.font.Font(None, 36).render(menuText, False, (15, 5, 107))
        self.screen.blit(text_surface_instructions, (260, 500))
        pygame.display.update()
        decision = False
        while not decision:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        decision = True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        self.__init__()
        self.run()


if __name__ == '__main__':
    game = Game()
    game.run()
