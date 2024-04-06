from abc import ABC, abstractmethod
from app.modules.textDisplay.textDisplay import TextDisplay
import pygame


class Room(ABC):
    def __init__(self, game):
        self.game = game
        self.ground_collider = pygame.Rect(0, 415, 1000, 100)

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def check_for_interaction(self):
        pass
