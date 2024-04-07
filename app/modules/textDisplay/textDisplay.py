import pygame
import json

class TextDisplay:
    def __init__(self, game,db):
        self.db = db
        self.game = game
        self.pos = (250,525)
        self.hist = ""
        self.number = 0
        self.current_text = ""
        self.cooldown = 120

    def move_hist(self):
        match self.game.currentRoom.id:
            case "TutorialRoom":
                if self.hist != self.db["tuto"]:
                    self.number=1
                self.hist=self.db["tuto"]
            case "RootRoom":
                if self.hist != self.db["choose"] and self.game.player.has_item == False:
                    self.number=1
                    self.cooldown = 120
                    self.hist=self.db["choose"]
                if self.hist != self.db["epee"] and self.game.player.item == 0:
                    self.hist=self.db["epee"]
                    self.number=1
                    self.cooldown = 120
                if self.hist != self.db["livre"] and self.game.player.item == 1:
                    self.hist=self.db["livre"]
                    self.number=1
                    self.cooldown = 120

            case "SlimRoom":
                print(self.game.player.item)
                if self.hist != self.db["slim_epee"] and self.game.player.item == 0:
                    self.hist=self.db["slim_epee"]
                    self.number=1
                    self.cooldown = 120
                if self.hist != self.db["slim_livre"] and self.game.player.item == 1:
                    self.hist=self.db["slim_livre"]
                    self.number=1
                    self.cooldown = 120

    def move_number(self):
        match self.game.currentRoom.id:
            case "TutorialRoom":
                if self.cooldown <= 0 and self.number < len(self.hist):
                    self.number += 1
                    self.cooldown = 120
            case "RootRoom":
                if self.cooldown <= 0 and self.number < len(self.hist):
                    self.number += 1
                    self.cooldown = 120

            case "SlimRoom":
                if self.game.player.item == 0:
                    if self.cooldown <= 0 and self.number < len(self.hist):
                        self.number += 1
                        self.cooldown = 120
                if self.game.player.item == 1:
                    if self.cooldown <= 0 and self.number < len(self.hist):
                        self.number += 1
                        self.cooldown = 120


    def display_txt(self):
        self.move_hist()
        self.text = self.hist[str(self.number)]
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (0, 0, 0))  # Ne pas indexer à nouveau
        self.game.screen.blit(text, self.pos)
        # Decrement cooldown each frame
        self.cooldown = max(0, self.cooldown - 1)

    def update(self):
        self.move_number()


