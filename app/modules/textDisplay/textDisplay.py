import pygame
import json

class TextDisplay:
    def __init__(self, game,db):
        self.db = db
        self.game = game
        self.pos = (250,525)
        self.hist = ""
        self.number = 1
        self.current_text = ""
        self.cooldown = 0

    def move_hist(self):
        match self.game.currentRoom.id:
            case "TutorialRoom":
                if self.hist != self.db["tuto"]:
                    self.number=1
                self.hist=self.db["tuto"]
            case "RootRoom":
                if self.hist != self.db["choose"]:
                    self.number=1
                self.hist=self.db["choose"]
            case "SlimRoom":
                if self.hist != self.db["slim"]:
                    self.number=1
                self.hist=self.db["slim"]

    def move_number(self):
        if self.cooldown <= 0 and self.number < len(self.hist):
            self.number += 1
            self.cooldown = 60

    def display_txt(self):
        self.move_hist()
        self.text = self.hist[str(self.number)]
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (0, 0, 0))  # Ne pas indexer à nouveau
        self.game.screen.blit(text, self.pos)
        # Decrement cooldown each frame
        self.cooldown = max(0, self.cooldown - 1)



