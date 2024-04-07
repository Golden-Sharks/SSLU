import pygame

from app.modules.ActionableEntities.Door import Door
from app.modules.monstre.shirak import Shirak
from app.modules.room.room import Room


class SlimRoom(Room):

    def __init__(self, game):
        super().__init__(game)
        self.id = "Slimroom"
        self.background_image = pygame.image.load('./assets/environnement/Map/salle_objets.png')
        self.background_gradiant = pygame.image.load('./assets/environnement/Fonds/water_background.png')
        self.door = Door(self.game, (865, 252))
        self.text = game.text
        self.monstre_interaction_cooldown = 0
        self.damage_cooldown = 0
        self.monstres = [Shirak(self.game, [500, 356])]

    def update(self):
        if self.monstre_interaction_cooldown > 0:
            self.monstre_interaction_cooldown -= self.game.clock.get_time()
            if self.monstre_interaction_cooldown < 0:
                self.monstre_interaction_cooldown = 0
        if self.damage_cooldown > 0:
            self.damage_cooldown -= self.game.clock.get_time()
        if self.damage_cooldown < 0:
            self.damage_cooldown = 0
        if self.monstres != None:
            for monstre in self.monstres:
                monstre.update()
        else:
            self.game.player.karma = -1

    def draw(self):
        self.game.screen.blit(self.background_gradiant, (0, 0))
        self.game.screen.blit(self.background_image, (0, 0))
        if (self.monstres != None):
            self.monstres[0].draw()
        self.door.draw()

    def check_for_interaction(self):
        if self.game.player.collider.colliderect(self.door.collider):
            self.game.roomFactory.switch_room()
        if self.monstres != None:
            if self.game.player.collider.colliderect(
                    self.monstres[
                        0].interaction_zone_player) and self.monstre_interaction_cooldown == 0 and self.game.player.status != "Attaque":
                self.monstre_interaction_cooldown = 300  # Set cooldown to 2 seconds
                self.monstres[0].interact(self.game.player.status)

    def attack_interaction(self):
        self.text.update()
        if self.monstres != None:
            if self.game.player.collider.colliderect(
                    self.monstres[0].interaction_zone_player) and self.monstre_interaction_cooldown == 0:
                self.monstre_interaction_cooldown = 200  # Set cooldown to 2 seconds
                if (self.monstres[0].life <= 0):
                    self.monstres = None
                if (self.monstres != None):
                    self.monstres[0].interact(self.game.player.status)
