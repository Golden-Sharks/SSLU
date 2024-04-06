#Importation
import pygame
import pygame as pg
from app.modules.ActionableEntities.ActionableEntities import ActionableEntities


#Classe
class Door(ActionableEntities):
    def __init__(self, game, pos):
        self.room_init = (255, 255, 255)
        self.room_arrival = (70, 70, 70)
        self.pos = pos  # Position of the door (x, y)
        self.pos_arrival = (30, 570)
        self.game = game
        self.locked = False
        self.collider = pygame.Rect(self.pos[0], self.pos[1], 50, 50)
        self.sprite = pygame.image.load('./assets/environnement/Tile/porte_ouverte.png')

    def Interact(self):
        if self.locked:
            return self.room_init
            print("The door is locked.")
        else:
            self.game.roomFactory.switch_room()

    def draw(self):
        #self.game.screen.blit(self.sprite, (0, 0))
        pg.draw.rect(self.game.screen, (0, 0, 0), (self.pos[0], self.pos[1], 50, 50))
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.collider, 5)
