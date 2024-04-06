from app.modules.room.rootRoom import RootRoom


class RoomFactory:
    def __init__(self, game):
        self.game = game

    def switch_room(self):
        if self.game.currentRoom.id == 'TutorialRoom':
            self.game.currentRoom = RootRoom(self.game)
        self.game.player.pos = [30, 0]