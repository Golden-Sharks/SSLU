import pygame


class Sharkotequaire:
    def __init__(self, game, pos):
        self.game = game
        self.pos = pos
        self.sprite = pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('./assets/environnement/Animations/sharkotequere/sprite_4.png'), (80, 100)), True, False)

    def draw(self):
        self.game.screen.blit(self.sprite, self.pos)
