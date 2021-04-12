from discord.ext import commands
from typing import List

# TODO: documentation

class Move(commands.Command):
    """Base Move class

    Attributes:
        name -> String: Name of the move
        description -> String: Short description of the move
        commands -> Set: Set of commands that reference this move
        full_description -> String: Full description of the move.
    """
    def __init__(self, full_name: str, brief: str, command: str = None, aliases: List[str] = None, full_description: str = None):
        """Init"""
        # Move attributes
        self.full_name = full_name
        self.full_description = full_description if full_description else brief

        # Command attributes and init
        super().__init__(
            func=self.call,
            name=command if command else ''.join(full_name.lower().split()),
            brief=brief,
            aliases=aliases if aliases else [],
            hidden=True
        )

    def __str__(self) -> str:
        """String representation of the move"""
        return f'{self.full_name}: {self.brief} [{", ".join([self.name] + self.aliases)}]'

    async def call(self, ctx):
        await ctx.send(f'```{self.full_description}```')


class Playbook(commands.Command):
    def __init__(self, name: str, moves: List[Move]):
        self.moves = moves
        super().__init__(self.call, name=name, hidden=True)

    async def call(self, ctx):
        moves = f'Use .{self.name} <move> to see more details about the following moves:'
        for move in self.moves:
            moves += f'\n\t{move}'
        await ctx.send(f'```{moves}```')


class Game(commands.Cog):
    """Base Game class

    The base Game class contains common methods across all games, such as retrieving moves and playbooks from the data.

    Attributes:
        commands -> Dictionary: Dictionary of game-specific commands
        data_file -> String: Name of file containing game-specific data
        data -> Dictionary: Unpacked data from file
    """
    BASIC_MOVES = []
    PLAYBOOK_MOVES = {}
    GAME_MOVES = {}

    def __init__(self, bot):
        self.bot = bot

        # Add basic move commands
        for move in self.BASIC_MOVES:
            try:
                self.bot.add_command(move)
            except commands.errors.CommandRegistrationError:
                pass

        # Add playbook move commands
        for playbook in self.PLAYBOOK_MOVES:
            self.bot.add_command(playbook)
            for move in playbook.moves:
                try:
                    self.bot.add_command(move)
                except commands.errors.CommandRegistrationError:
                    pass

        # Add game move commands
        for mode, moves in self.GAME_MOVES.items():
            for move in moves:
                try:
                    self.bot.add_command(move)
                except commands.errors.CommandRegistrationError:
                    pass

    @commands.command(name='moves')
    async def print_basic_moves(self, ctx):
        """Lists all basic (common) moves"""
        if not self.BASIC_MOVES:
            await ctx.send('Data not found. Have you loaded a game using .game?')
            return
        moves = 'Use the following commands to find detailed information about each move.'
        for move in self.BASIC_MOVES:
            moves += f'\n\t{move}'

        await ctx.send(f'```{moves}```')

    @commands.command(name='playbooks')
    async def print_playbooks(self, ctx):
        """Lists all playbooks"""
        if not self.PLAYBOOK_MOVES:
            await ctx.send('Data not found. Have you loaded a game using .game?')
            return
        playbooks = 'Use the following commands to find each playbook-specific move.'
        for playbook in self.PLAYBOOK_MOVES:
            playbooks += f'\n\t.{playbook.name}'

        await ctx.send(f'```{playbooks}```')
