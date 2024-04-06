from abc import ABC, abstractmethod

class Room(ABC) :
    @abstractmethod
    def draw(self):
        pass