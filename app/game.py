import pygame
from app.modules.player.player import Player
from app.modules.ActionableEntities.Door import Door

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 600))
        self.background = (255, 255, 255)
        self.running = True
        self.doors = [Door(self.screen, "Door 1", False, False, (950, 550))]
        self.player = Player(self.screen, (30, 570))

    def update(self,keys):
        self.doors[0].draw()
        if self.player.pos_x<self.doors[0].pos[0]+50 and self.player.pos_x>self.doors[0].pos[0]-50 and self.player.pos_y<self.doors[0].pos[1]+100 and self.player.pos_y>self.doors[0].pos[1]-100:
            if keys[pygame.K_e]:
                self.background = self.doors[0].Interact()
                self.player.pos_x = 30
                self.player.pos_y = 570
        self.player.update(keys)
        pygame.display.update()
        self.clock.tick(60)
    def run(self):
        # Changing surface color
        pygame.display.flip()
        while self.running:
            self.screen.fill(self.background)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update(keys)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()