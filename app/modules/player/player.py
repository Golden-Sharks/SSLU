import pygame

class Player:

    def __init__(self, game, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.game = game
        self.velocity = [0, 0]  # Initialize velocity for smooth movement
        self.speed = 5
        self.gravity = 0.5  # Acceleration due to gravity

    def update(self, keys):
        # Handle horizontal movement with QD SPACE controls
        if keys[pygame.K_q] and self.pos_x > 30:
            self.velocity[0] = -self.speed  # Set horizontal velocity
        elif keys[pygame.K_d] and self.pos_x < 970:
            self.velocity[0] = self.speed
        else:
            self.velocity[0] = 0  # Stop horizontal movement when no keys pressed
        if keys[pygame.K_SPACE] and self.pos_y==570:
            self.velocity[1] = -10
        # Apply gravity
        self.velocity[1] += self.gravity

        # Limit vertical movement at the bottom
        if self.pos_y + self.velocity[1] > 570:
            self.pos_y = 570
            self.velocity[1] = 0  # Reset vertical velocity when hitting the ground

        # Update position based on velocity
        self.pos_x += self.velocity[0]
        self.pos_y += self.velocity[1]

        self.draw()

    def draw(self):
        pygame.draw.rect(self.game, (0, 0, 255), (self.pos_x - 30, self.pos_y - 30, 60, 60))