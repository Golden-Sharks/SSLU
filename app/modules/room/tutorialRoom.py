import pygame

from app.modules.ActionableEntities.Door import Door
from app.modules.textDisplay.textDisplay import TextDisplay
from app.modules.room.room import Room


class TutorialRoom(Room):
    def __init__(self, game):
        super().__init__(game)
        self.id = "TutorialRoom"
        self.background_image = pygame.image.load('./assets/environnement/Map/couloir_hublos.png')
        self.background_gradiant = pygame.image.load('./assets/environnement/Fonds/water_background.png')
        self.door = Door(self.game, (950, 345))

    def draw(self):
        self.game.screen.blit(self.background_gradiant, (0, 0))
        self.game.screen.blit(self.background_image, (0, 0))
        self.door.draw()

    def check_for_interaction(self):
        if self.game.player.collider.colliderect(self.door.collider):
            self.game.roomFactory.switch_room()

    def next_text(self):
        self.text.move_number()

