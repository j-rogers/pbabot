from . import sprawl
from . import apoc


class Game:
    def __init__(self):
        self.commands = {}

    def handle(self, message):
        raise NotImplementedError

    def moves(self, message):
        raise NotImplementedError

    def playbooks(self, message):
        raise NotImplementedError