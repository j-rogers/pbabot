import pickle


class Game:
    def __init__(self):
        self.commands = {}
        self.datafile = None
        self.data = None

    def loaddata(self):
        try:
            with open(self.datafile, 'rb') as file:
                self.data = pickle.loads(file.read())
        except EOFError:
            print("No data in file.")
        except FileNotFoundError:
            print("No data file found.")

    def handle(self, command, args):
        raise NotImplementedError

    def moves(self, message):
        moves = 'Use the following commands to find detailed information about each move.'
        for move in self.data['basic']:
            if move.commands:
                moves += f'\n\t{move.name} {move.commands}'

        return moves

    def playbooks(self, message):
        playbooks = 'Use the following commands to find each playbook-specific move.'
        for playbook in self.data['playbooks']:
            playbooks += f'\n\t.{playbook}'

        return playbooks

    def _getplaybook(self, playbook, move):
        if playbook not in self.data['playbooks']:
            return None

        if not move:
            moves = f'Use .{playbook} <move> to see more details about the following moves:'
            for move in self.data['playbooks'][playbook]:
                moves += f'\n\t{move.print()}'
            return moves

        m = self._getmove(move, playbook=playbook)
        return m.fulldescription if m else None

    def _getmove(self, query, index='basic', name=False, playbook=None):
        if playbook:
            for move in self.data['playbooks'][playbook]:
                if query in move.commands:
                    return move

        for move in self.data[index]:
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
