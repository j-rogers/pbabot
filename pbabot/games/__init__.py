import pickle


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

    def _getplaybook(self, playbook, move):
        with open(self.data, 'rb') as file:
            data = pickle.loads(file.read())

            if playbook not in data['playbooks']:
                return None

            if not move:
                moves = ''
                for move in data['playbooks'][playbook]:
                    moves += move.print() + '\n'
                return moves

            m = self._getmove(move, playbook=playbook)
            return m.fulldescription if m else None

    def _getmove(self, query, name=False, playbook=None):
        with open(self.data, 'rb') as file:
            moves = pickle.loads(file.read())

            if playbook:
                for move in moves['playbooks'][playbook]:
                    if query in move.commands:
                        return move

            for move in moves['basic']:
                if name:
                    if query in move.name:
                        return move
                else:
                    if query in move.commands:
                        return move


class Move:
    def __init__(self, name, description, *commands, fulldescription=None):
        self.name = name
        self.description = description
        self.fulldescription = fulldescription if fulldescription else description
        self.commands = set(commands)

    def print(self):
        return f'{self.name}: {self.description} (Commands: {self.commands}'
