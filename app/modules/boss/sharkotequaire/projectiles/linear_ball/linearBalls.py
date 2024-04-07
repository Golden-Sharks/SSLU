import pygame


class LinearBall:
    def __init__(self, game, pos, direction, speed):
        self.game = game
        self.pos = pos
        self.direction = direction
        self.speed = speed
        self.collider = pygame.Rect(self.pos[0], self.pos[1], 66, 116)  # Update collider size if needed

    def update(self):
        # Update ball position based on direction and speed
        self.pos[0] += self.speed * self.direction[0]  # Update x-coordinate
        self.pos[1] += self.speed * self.direction[1]  # Update y-coordinate

        self.collider.y = self.pos[1]

        # Check for wall collisions (example)
        if self.pos[0] < 0 or self.pos[0] + self.collider.width > self.game.screen.get_width():
            self.direction[0] *= -1  # Reverse horizontal direction on collision

        if self.pos[1] < 0 or self.pos[1] + self.collider.height > self.game.screen.get_height():
            self.direction[1] *= -1  # Reverse vertical direction on collision

    def draw(self):
        # Draw the circle using pygame.draw.circle()
        color = (255, 255, 255)  # White by default
        radius = 33  # Half of the width and height for a circle
        pygame.draw.circle(self.game.screen, color, self.pos, radius)
