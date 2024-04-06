# Importation
from abc import ABC, abstractmethod


# Classe
class ActionableEntities(ABC):
    def __init__(self, game, pos):
        self.game = game
        self.pos = pos

    @abstractmethod
    def interact(self):
        pass
