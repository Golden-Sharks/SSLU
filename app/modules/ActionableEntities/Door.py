import pygame

from app.modules.ActionableEntities.actionableEntities import ActionableEntities


class Door(ActionableEntities):
    def __init__(self, game, pos, is_closed=False):
        super().__init__(game, pos)
        self.room_init = (255, 255, 255)
        self.room_arrival = (70, 70, 70)
        self.pos = pos
        self.pos_arrival = (30, 570)
        self.game = game
        self.locked = False
        self.is_closed = is_closed
        self.collider = pygame.Rect(self.pos[0], self.pos[1], 96, 144)
        self.open_sprite = pygame.transform.scale(pygame.image.load('./assets/environnement/Tiles/porte_ouverte.png'),
                                                  (96, 144))
        self.closed_sprite = pygame.transform.scale(pygame.image.load('./assets/environnement/Tiles/porte_fermee.png'),
                                                    (96, 144))

    def interact(self):
        if self.locked:
            return self.room_init
            print("The door is locked.")
        else:
            self.game.roomFactory.switch_room()

    def draw(self):
        if self.is_closed:
            self.game.screen.blit(self.closed_sprite, (self.pos[0], self.pos[1]))
        else:
            self.game.screen.blit(self.open_sprite, (self.pos[0], self.pos[1]))
