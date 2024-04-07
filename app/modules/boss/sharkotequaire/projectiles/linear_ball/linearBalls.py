import pygame


class LinearBall:
    def __init__(self, game, pos, direction, speed):
        self.game = game
        self.pos = pos
        self.direction = direction
        self.speed = speed
        self.radius = 15
        self.collider = pygame.Rect(self.pos[0] - self.radius, self.pos[1] - self.radius, self.radius * 1.5,
                                    self.radius * 1.5)

    def update(self):
        # Update ball position based on direction and speed
        self.pos[0] += self.speed * self.direction[0]  # Update x-coordinate
        self.pos[1] += self.speed * self.direction[1]  # Update y-coordinate
        self.collider.x = self.pos[0] - 10
        self.collider.y = self.pos[1] - 10

        # Check for wall collisions (example)
        if self.pos[0] < 0 or self.pos[0] + self.collider.width > self.game.screen.get_width():
            self.direction[0] *= -1  # Reverse horizontal direction on collision

        if self.pos[1] < 0 or self.pos[1] + self.collider.height > self.game.screen.get_height():
            self.direction[1] *= -1  # Reverse vertical direction on collision

        if self.collider.colliderect(self.game.player.collider):
            self.game.player.take_damage(1)

    def draw(self):
        # Draw the circle using pygame.draw.circle()
        color = (255, 255, 255)  # White by default
        pygame.draw.circle(self.game.screen, color, self.pos, self.radius)
        # pygame.draw.rect(self.game.screen, (255, 0, 0), self.collider, 5)
