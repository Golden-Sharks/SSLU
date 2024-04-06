import pygame


class Player:

    def __init__(self, game, pos):
        self.pos = pos
        self.game = game
        self.velocity = [0, 0]  # Initialize velocity for smooth movement
        self.speed = 5
        self.gravity = 0.5  # Acceleration due to gravity
        self.collider = pygame.Rect(self.pos[0], self.pos[1], 66, 116)
        self.isJumping = False
        self.has_item = False
        self.direction = "immobile"
        self.cooldown_timer = pygame.time.Clock()
        self.animation = {
            "immobile": ["sprite_0.png","sprite_0.png"],
            "marche": ["sprite_1.png","sprite_2.png"],
            "saut": ["sprite_3.png","sprite_3.png"],
        }
        self.animation_frame_index = 0
        self.remaining_life = 10
        self.status = "Neutre"

    def update(self, keys):
        self.cooldown_timer.tick()
        # Handle horizontal movement with QD SPACE controls
        if keys[pygame.K_q] and self.pos[0] > 0:
            self.velocity[0] = -self.speed  # Set horizontal velocity
            self.direction = "marche"
            if self.cooldown_timer.get_time() >= 50000:  # 500 milliseconds cooldown
                self.cooldown_timer.reset()  # Reset timer after cooldown period
                self.animation_frame_index = (self.animation_frame_index + 1) % 2

        elif keys[pygame.K_d] and self.pos[0] < 934:
            self.velocity[0] = self.speed
            self.direction = "marche"
            if self.cooldown_timer.get_time() >= 50000:  # 500 milliseconds cooldown
                self.cooldown_timer.reset()  # Reset timer after cooldown period
                self.animation_frame_index = (self.animation_frame_index + 1) % 2
        else:
            self.velocity[0] = 0  # Stop horizontal movement when no keys pressed
            self.direction = "immobile"
        if (keys[pygame.K_SPACE] and self.collider.bottom == self.game.currentRoom.ground_collider.top
                and not self.isJumping):
            self.direction = "saut"
            self.isJumping = True
            self.velocity[1] = -10
        # Apply gravity
        self.velocity[1] += self.gravity

        # Limit vertical movement at the bottom
        if self.collider.bottom >= self.game.currentRoom.ground_collider.top:
            if not self.isJumping:
                self.pos[1] = self.game.currentRoom.ground_collider.top - 116
                self.velocity[1] = 0  # Reset vertical velocity when hitting the ground
            self.isJumping = False

        # Update position based on velocity

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        if keys[pygame.K_e]:
            self.game.currentRoom.check_for_interaction()
        if keys[pygame.K_a]:
            self.status = "Attaque"
            self.game.currentRoom.check_for_interaction()
        # Update collider position to match player position
        self.collider.x = self.pos[0]
        self.collider.y = self.pos[1]

    def draw(self):
        current_image = pygame.image.load("./assets/environnement/Animations/main_char/"+self.animation[self.direction][self.animation_frame_index])
        scaled_image = pygame.transform.scale(current_image, (66, 116))
        if self.velocity[0] >= 0:
            scaled_image = pygame.transform.flip(scaled_image, True, False)
        self.game.screen.blit(scaled_image, self.pos)
        #pygame.draw.rect(self.game.screen, (255, 0, 0), self.collider, 5)
        pygame.draw.rect(self.game.screen, (255, 0, 0), (0, 0, self.remaining_life * 20, 20))


    def take_damage(self, damage):
        self.remaining_life -= damage
        if self.remaining_life <= 0:
            self.game.game_over()
        print("Player took damage, remaining life: ", self.remaining_life)