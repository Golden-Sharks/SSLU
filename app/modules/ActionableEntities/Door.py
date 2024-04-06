import pygame
from app.modules.ActionableEntities.ActionableEntities import ActionableEntities


class Door(ActionableEntities):
    def __init__(self, game, pos):
        self.room_init = (255, 255, 255)
        self.room_arrival = (70, 70, 70)
        self.pos = pos
        self.pos_arrival = (30, 570)
        self.game = game
        self.locked = False
        self.collider = pygame.Rect(self.pos[0], self.pos[1], 96, 144)
        self.sprite = pygame.transform.scale(pygame.image.load('./assets/environnement/Tiles/porte_ouverte.png'),
                                             (96, 144))

    def Interact(self):
        if self.locked:
            return self.room_init
        else:
            self.game.roomFactory.switch_room()

    def draw(self):
        self.game.screen.blit(self.sprite, (self.pos[0], self.pos[1]))
