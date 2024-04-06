#Importation
from abc import ABC, abstractmethod

#Classe
class ActionableEntities(ABC):
    @abstractmethod
    def Interact(self):
        pass