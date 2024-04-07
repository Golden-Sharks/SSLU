import pygame


class Projectile:
    def __init__(self, game, pos, speed):
        self.game = game
        self.pos = pos
        self.speed = speed
        self.radius = 5
        self.collider = pygame.Rect(self.pos[0] - self.radius, self.pos[1] - self.radius, self.radius * 1.5,
                                    self.radius * 1.5)

    def update(self):
        # Move the projectile to the left
        self.pos = (self.pos[0] - self.speed, self.pos[1])  # Update x-coordinate only

        # Update the collider position based on the new ball position
        self.collider.x = self.pos[0] - self.radius
        self.collider.y = self.pos[1] - self.radius

        if self.collider.colliderect(self.game.player.collider):
            self.game.player.take_damage(2)
        # Check if the projectile has gone off-screen (disappear logic)
        if self.pos[0] < -self.radius:  # Check if x-coordinate is off-screen (left)
            self.game.currentRoom.boss.bullets.remove(self)

    def draw(self):
        # Draw the circle using pygame.draw.circle()
        color = (0, 0, 0)  # White by default
        pygame.draw.circle(self.game.screen, color, self.pos, self.radius)
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.collider, 5)
