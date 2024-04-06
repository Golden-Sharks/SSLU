import pygame

from app.modules.ActionableEntities.Door import Door
from app.modules.room.room import Room


class TutorialRoom(Room):
    def __init__(self, game):
        super().__init__(game)
        self.id = "TutorialRoom"
        self.door = Door(self.game, (950, 450))

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 255, 0), self.ground_collider)
        self.door.draw()

    def check_for_interaction(self):
        if self.game.player.collider.colliderect(self.door.collider):
            self.game.roomFactory.switch_room()


