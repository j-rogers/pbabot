from .games import Game


class Character:
    def __init__(self, name, stats, player):
        self.name = name
        self.stats = stats
        self.player = player
        self.description = ''
        self.attributes = {}

    def handle(self, message, player):
        pass