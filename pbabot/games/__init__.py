#from . import sprawl
#from . import apoc


class Game:
    def __init__(self):
        self.commands = {}
        self.data = None

    def handle(self, command, args):
        raise NotImplementedError

    def moves(self, message):
        raise NotImplementedError

    def playbooks(self, message):
        raise NotImplementedError
