import pygame
import json
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
        self.player = Player(self, [30, 0])
        self.roomFactory = RoomFactory(self)
        self.text = TextDisplay(self, self.get_db())
        self.currentRoom: Room = TutorialRoom(self)


    def get_db(self):
        with open('./data/narrateur.json', 'r',encoding="utf-8") as file:
            return json.load(file)

    def update(self, keys):
        self.player.update(keys)
        self.clock.tick(60)

    def draw(self):
        self.screen.fill(self.background)
        self.currentRoom.draw()
        self.player.draw()
        pygame.display.update()

    def run(self):
        # Changing surface color
        pygame.display.flip()

        while self.running:
            self.draw()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update(keys)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
