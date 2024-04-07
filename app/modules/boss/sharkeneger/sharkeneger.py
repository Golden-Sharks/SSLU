import random
import time

import pygame

from app.modules.boss.sharkeneger.projectiles.projectiles import Projectile


class Sharkeneger:
    def __init__(self, game, pos):
        self.game = game
        self.pos = pos
        self.is_attacking = False
        self.sprite = pygame.transform.scale(
            pygame.image.load('./assets/environnement/Animations/arnault_sharkeneger/sharkeneger.png'), (128, 128))

        self.bullets = []
        self.can_shot = True
        self.phase = 0
        self.last_shot_time = 0
        self.first_shot_time = 0

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
        self.game.screen.blit(self.sprite, self.pos)

    def update(self):
        if self.is_attacking:
            if time.time() - self.last_shot_time > 5:
                self.last_shot_time = time.time()
                rand = random.Random()
                for i in range(rand.randint(1, 3)):
                    self.bullets.append(Projectile(self.game, [790, 365], rand.randint(5, 12)))
                    self.bullets.append(Projectile(self.game, [790, 365], rand.randint(5, 12)))

                self.can_shot = False
            if time.time() - self.first_shot_time > 63:
                self.is_attacking = False
                self.bullets.clear()

            for bullet in self.bullets:
                bullet.update()
