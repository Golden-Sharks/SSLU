import pygame

from app.modules.ActionableEntities.Door import Door
from app.modules.ActionableEntities.piedestal import Piedestal
from app.modules.room.room import Room


class RootRoom(Room):
    def __init__(self, game):
        super().__init__(game)
        self.id = 'RootRoom'
        self.background_image = pygame.image.load('./assets/environnement/Map/salle_objets.png')
        self.background_gradiant = pygame.image.load('./assets/environnement/Fonds/water_background.png')
        self.piedestal_sword = Piedestal(self.game, [240, 252], './assets/items/sharksword.png')
        self.piedestal_book = Piedestal(self.game, [435, 252], './assets/items/sharkbook.png')
        self.piedestal_egg = Piedestal(self.game, [625, 252], './assets/items/sharkegg.png')
        self.piedestals = [self.piedestal_sword, self.piedestal_book, self.piedestal_egg]
        self.door = Door(self.game, (865, 252), True)
        self.text = game.text

    def draw(self):
        self.game.screen.blit(self.background_gradiant, (0, 0))
        self.game.screen.blit(self.background_image, (0, 0))
        for piedestal in self.piedestals:
            piedestal.draw()
        self.text.display_txt()
        self.door.draw()

    def check_for_interaction(self):
        if self.game.player.collider.colliderect(self.door.collider):
            if (not self.door.is_closed):
                self.game.roomFactory.switch_room()
        for piedestal in self.piedestals:
            if self.game.player.collider.colliderect(piedestal.collider):
                piedestal.interact()

    def next_text(self):
        self.text.move_number()

    def update(self):
        pass
