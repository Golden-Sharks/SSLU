import pygame
from app.modules.monstre.monstre import Monstre

class Shirak(Monstre):
    def __init__(self, game, pos):
        super().__init__(game, pos, 102, 58)
        self.current_image = pygame.image.load('./assets/environnement/Animations/shirak/sprite_0.png')
        self.life = 3
        self.interaction_zone_slime = pygame.Rect(pos[0]-55, pos[1]-60, 200, 200)  # Rectangle de base
        self.interaction_zone_player = pygame.Rect(pos[0]-55, pos[1]-60, 200, 200)  # Rectangle de base
        self.following = False  # Flag to track following state
    def draw(self):
        if self.life>0:
            scaled_image = pygame.transform.scale(self.current_image, (102, 58))
            scaled_image=pygame.transform.flip(scaled_image, True, False)
            self.game.screen.blit(scaled_image, self.pos)
            # Optionally draw interaction zone for debugging (comment out for final version)
            pygame.draw.circle(self.game.screen, (255, 0, 0), self.interaction_zone_slime.center, 85, 2)
            pygame.draw.circle(self.game.screen, (0, 255, 0), self.interaction_zone_player.center, 155, 2)

    def interact(self,status):
        if status == "Attaque":
            print("Shirak says: 'Ouch! That hurts!'")
            self.life -= 1
            self.following = True  # Start following on attack
        else:
            print("Shirak says: 'I am Shirak, the slime!'")

    def update(self):
        if self.following and self.life > 0:
            # Move towards the player's x-position
            player_center_x = self.game.player.pos[0]
            slime_center_x = self.pos[0]
            speed = 2  # Adjust speed as needed

            if player_center_x > slime_center_x:
                self.pos[0] += min(speed, player_center_x - slime_center_x)  # Move right
            elif player_center_x < slime_center_x:
                self.pos[0] -= min(speed, slime_center_x - player_center_x)  # Move left

            # Update interaction zones based on new position
            self.interaction_zone_slime[0] = self.pos[0] - 55
            self.interaction_zone_player[0]= self.pos[0] - 55