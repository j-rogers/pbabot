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


class Move:
    def __init__(self, name, description, *commands):
        self.name = name
        self.description = description
        self.commands = commands