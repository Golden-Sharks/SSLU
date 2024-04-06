from app.modules.room.rootRoom import RootRoom
import pygame

class RoomFactory:
    def __init__(self, game):
        self.game = game

    def switch_room(self):
        self.transition(False)
        if self.game.currentRoom.id == 'TutorialRoom':
            self.game.currentRoom = RootRoom(self.game)
        self.game.player.pos = [30, 0]
        self.transition()

    def transition(self,open=True):
        if open:
            transition_color = (0, 0, 0)  # Adjust color for opening effect
            transition_alpha = 255

            while transition_alpha > 0:
                # Create transition surface with current screen size
                transition_surface = pygame.Surface(self.game.screen.get_size())

                # Fill transition surface with opening color and decreasing alpha
                transition_surface.fill(
                    (transition_color[0], transition_color[1], transition_color[2], transition_alpha))

                # Update alpha for fading effect
                transition_alpha -= 13  # Adjust speed as needed (higher for slower fade)

                # Draw a circle on the transition surface with decreasing radius
                pygame.draw.circle(transition_surface, (255, 255, 255),
                                   (self.game.screen.get_width() // 2, self.game.screen.get_height() // 2),
                                   (100 - abs(transition_alpha)) * 5)

                # Blit transition surface onto the screen
                self.game.screen.blit(transition_surface, (0, 0))

                # Update the display to show the transition
                pygame.display.update()
                self.game.clock.tick(15)  # Maintain consistent frame rate

        else:
            # Handle closing transition (already implemented in previous response)
            transition_color = (0, 0, 0)  # Adjust color for closing effect
            transition_alpha = 0

            while transition_alpha < 255:
                # Create transition surface with current screen size
                transition_surface = pygame.Surface(self.game.screen.get_size())

                # Fill transition surface with closing color and increasing alpha
                transition_surface.fill(
                    (transition_color[0], transition_color[1], transition_color[2], transition_alpha))

                # Update alpha for fading effect
                transition_alpha += 13  # Adjust speed as needed (higher for slower fade)

                # Draw a circle on the transition surface with decreasing radius
                pygame.draw.circle(transition_surface, (255, 255, 255),
                                   (self.game.screen.get_width() // 2, self.game.screen.get_height() // 2),
                                   (100 - abs(transition_alpha)) * 5)
                # Blit transition surface onto the screen
                self.game.screen.blit(transition_surface, (0, 0))

                # Update the display to show the transition
                pygame.display.update()
                self.game.clock.tick(30)  # Maintain consistent frame rate
