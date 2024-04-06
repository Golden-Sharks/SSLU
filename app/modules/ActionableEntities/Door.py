#Importation
import pygame as pg
from app.modules.ActionableEntities.ActionableEntities import ActionableEntities
#Classe
class Door(ActionableEntities):
    def __init__(self, game, description, locked, key, pos):
        self.room_init = (255, 255, 255)
        self.room_arrival = (70, 70, 70)
        self.pos = pos      # Position of the door (x, y)
        self.pos_arrival = (30, 570)
        self.game = game
        self.description = description
        self.locked = locked
        self.key = key

    def Interact(self):
        if self.locked == True:
            return self.room_init
            print("The door is locked.")
        else:
            return self.room_arrival
            init=(self.room_init,self.pos)
            arrival=(self.room_arrival,self.pos_arrival)
            self.room_init=arrival[0]
            self.pos=arrival[1]
            self.room_arrival=init[0]
            self.pos_arrival=init[1]
            print(self.room_init)
            print("The door is unlocked.")

    def draw(self):
        pg.draw.rect(self.game, (0, 0, 0), (self.pos[0], self.pos[1], 50, 100))