import pygame


class Player:

    def __init__(self, game, pos):
        self.pos = pos
        self.game = game
        self.velocity = [0, 0]  # Initialize velocity for smooth movement
        self.speed = 5
        self.gravity = 0.5  # Acceleration due to gravity
        self.collider = pygame.Rect(self.pos[0] - 30, self.pos[1] - 30, 60, 60)
        self.isJumping = False
        self.has_item = False

    def update(self, keys):
        # Handle horizontal movement with QD SPACE controls
        if keys[pygame.K_q] and self.pos[0] > 30:
            self.velocity[0] = -self.speed  # Set horizontal velocity
        elif keys[pygame.K_d] and self.pos[0] < 970:
            self.velocity[0] = self.speed
        else:
            self.velocity[0] = 0  # Stop horizontal movement when no keys pressed
        if (keys[pygame.K_SPACE] and self.collider.bottom == self.game.currentRoom.ground_collider.top
                and not self.isJumping):
            self.isJumping = True
            self.velocity[1] = -10
        # Apply gravity
        self.velocity[1] += self.gravity

        # Limit vertical movement at the bottom
        if self.collider.bottom >= self.game.currentRoom.ground_collider.top:
            if not self.isJumping:
                self.pos[1] = self.game.currentRoom.ground_collider.top - 30
                self.velocity[1] = 0  # Reset vertical velocity when hitting the ground
            self.isJumping = False

        # Update position based on velocity
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        if keys[pygame.K_e]:
            self.game.currentRoom.check_for_interaction()
        if keys[pygame.K_a]:
            self.game.currentRoom.next_text()
        # Update collider position to match player position
        self.collider.x = self.pos[0] - 30
        self.collider.y = self.pos[1] - 30

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 0, 255), (self.pos[0] - 30, self.pos[1] - 30, 60, 60))
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.collider, 5)
