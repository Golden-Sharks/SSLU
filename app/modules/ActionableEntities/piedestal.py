import pygame

from app.modules.ActionableEntities.actionableEntities import ActionableEntities


class Piedestal(ActionableEntities):
    def __init__(self, game, pos, sprite_path,id):
        super().__init__(game, pos)
        self.sprite = pygame.transform.scale(pygame.image.load('./assets/environnement/Tiles/piedestal.png'),
                                             (144, 144))
        self.itemSprite = pygame.transform.scale(pygame.image.load(sprite_path), (60, 60))
        self.objet_id = id
        self.collider = pygame.Rect(self.pos[0] + 25, self.pos[1], 96, 144)
        self.isAvailaible = True

    def draw(self):
        self.game.screen.blit(self.sprite, self.pos)
        if self.isAvailaible:
            self.game.screen.blit(self.itemSprite, [self.pos[0] + 40, self.pos[1] + 20])

    def interact(self):
        if not self.game.player.has_item:
            self.game.player.has_item = True
            self.game.player.item = self.objet_id
            self.isAvailaible = False
            self.game.currentRoom.door.is_closed = False
