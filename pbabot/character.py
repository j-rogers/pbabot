

class Character:
    def __init__(self, name, stats, player):
        self.name = name
        self.stats = stats
        self.player = player
        self.description = ''
        self.attributes = {}

    def __str__(self):
        stat_line = ''
        for stat, value in self.stats.items():
            stat_line += f'\t{stat}: {value}\n'

        return f'{self.name}\nGame: TODO\nDescription: {self.description}\nStats:\n{stat_line}Attributes: TODO'

    def handle(self, message):
        if not message:
            return self.__str__()

        try:
            command, args = message.split(' ', 1)
        except ValueError:
            command = message
            args = None

        command_switch = {
            'help': self.print_help,
            'set': self.set_stat,
        }
        command_callback = command_switch.get(command, None)

        response = None
        if command_callback:
            response = command_callback(args)

        return response if response else f'Command {command} was not found.'

    def print_help(self, message: str) -> str:
        return """Usage: .character <command> <optional args>
        
To view a summary of your character, use .character with no commands.

Commands:
    help: Print this help menu.
    set <stat> <value>: Set a stat to the specified value.
"""

    def set_stat(self, values: str) -> str:
        stat, num = values.split(' ', 1)

        if stat not in self.stats:
            return f'No stat {stat} was found.'

        try:
            num = int(num)
        except ValueError:
            return f'Non-integer value given.'
        else:
            self.stats[stat] = num

        return f'{self.name}\'s {stat} stat has been changed to {num}.'
