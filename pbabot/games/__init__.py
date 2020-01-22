import pickle


class Game:
    def __init__(self):
        self.commands = {}
        self.datafile = None

    def handle(self, command, args):
        raise NotImplementedError

    def moves(self, message):
        with open(self.datafile, 'rb') as file:
            data = pickle.loads(file.read())

            moves = 'Use the following commands to find detailed information about each move.'
            for move in data['basic']:
                if move.commands:
                    moves += f'\n\t{move.name} {move.commands}'

            return moves

    def playbooks(self, message):
        with open(self.datafile, 'rb') as file:
            data = pickle.loads(file.read())

            playbooks = 'Use the following commands to find each playbook-specific move.'
            for playbook in data['playbooks']:
                playbooks += f'\n\t.{playbook}'

            return playbooks

    def _getplaybook(self, playbook, move):
        with open(self.datafile, 'rb') as file:
            data = pickle.loads(file.read())

            if playbook not in data['playbooks']:
                return None

            if not move:
                moves = f'Use .{playbook} <move> to see more details about the following moves:'
                for move in data['playbooks'][playbook]:
                    moves += f'\n\t{move.print()}'
                return moves

            m = self._getmove(move, playbook=playbook)
            return m.fulldescription if m else None

    def _getmove(self, query, name=False, playbook=None):
        with open(self.datafile, 'rb') as file:
            data = pickle.loads(file.read())

            if playbook:
                for move in data['playbooks'][playbook]:
                    if query in move.commands:
                        return move

            for move in data['basic']:
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
        return f'{self.name}: {self.description} {self.commands if self.commands else ""}'
