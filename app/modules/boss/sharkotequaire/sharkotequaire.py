import time

import pygame

from app.modules.boss.sharkotequaire.projectiles.linear_ball.linearBalls import LinearBall


class Sharkotequaire:
    def __init__(self, game, pos):
        self.game = game
        self.pos = pos
        self.is_attacking = False
        self.sprite = pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('./assets/environnement/Animations/sharkotequere/sprite_4.png'), (84, 105)), True, False)

        self.bullets = []
        self.can_shot = True
        self.phase = 0
        self.last_shot_time = 0

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
        self.game.screen.blit(self.sprite, self.pos)

    def update(self):
        if self.is_attacking:
            if self.can_shot:
                if self.phase == 0:
                    self.last_shot_time = time.time()
                    self.bullets.append(LinearBall(self.game, [500, 75], [-1, 1], 5))
                    self.bullets.append(LinearBall(self.game, [700, 75], [1, 1], 7))
                elif self.phase == 1:
                    self.last_shot_time = time.time()
                    self.bullets.append(LinearBall(self.game, [500, 75], [-1, 1], 8))
                    self.bullets.append(LinearBall(self.game, [700, 75], [1, 1], 10))
                elif self.phase == 2:
                    self.last_shot_time = time.time()
                    self.bullets.append(LinearBall(self.game, [500, 75], [-1, 1], 8))
                    self.bullets.append(LinearBall(self.game, [700, 75], [1, 1], 10))
                    self.bullets.append(LinearBall(self.game, [600, 100], [1, 1], 10))
                elif self.phase == 3:
                    self.is_attacking = False
                    pass
                self.can_shot = False
                self.phase += 1
            if time.time() - self.last_shot_time > 25:
                self.can_shot = True
                self.bullets.clear()

            for bullet in self.bullets:
                bullet.update()
