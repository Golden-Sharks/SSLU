from abc import ABC, abstractmethod
import pygame

class Monstre(ABC):
    def __init__(self, game, pos,dim_x,dim_y):
        self.game = game
        self.pos = pos
        self.ground_collider = pygame.Rect(pos[0], pos[1], dim_x, dim_y)

    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def interact(self):
        pass