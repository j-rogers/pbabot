"""Base Game Module

This module contains base classes to implement a PBA game. The Game class should be inherited by the implementing PBA
Game with each move and playbook specified by the Move and Playbook classes.

Author: Joshua Rogers (2021)
"""
from discord.ext import commands
from typing import List


class Move(commands.Command):
    """Base Move class

    Each move is a commands.Command object so we can call each move as .<move> with ease. Each move requires a full name
    (usually as printed in the games book) and a brief description (to be displayed in the help/context dialogs). You
    can then specify the main command as well as any aliases for the move. A full description can be included that will
    give additional information when the command is called. This is recommended when a move contains more detail.

    Each move all has the same callback in Move.call(). This will simply send the full description of the move. Any more
    functionality for a regular move is rare (usually they just tell you roll results) and shouldn't be needed.

    Attributes:
        full_name -> String: Full name of the move
        full_description -> String: Full description of the move
    """
    def __init__(self, full_name: str, brief: str, command: str = None, aliases: List[str] = None, full_description: str = None):
        """Init

        If a command is not given then it will default to a lowercase and no whitespace version of the full name. The
        full description will be set to the brief description if not given.

        Arguments:
            full_name -> String: Full name of the move
            brief -> String: Short description of the move
            command -> String: Command to be used to call the move
            aliases -> List[String]: List of aliases that can also be used to call the move
            full_description -> String: Full description of the move
        """
        # Move attributes
        self.full_name = full_name
        self.full_description = full_description if full_description else brief

        # Command attributes and init the command
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

    async def call(self, ctx: commands.Context) -> None:
        """Sends full description of move"""
        await ctx.send(f'```{self.full_description}```')


class Playbook(commands.Command):
    """Playbook

    Playbooks should be initialised as a command containing a list of their moves so we can easily list the playbooks
    moves using a command such as .<playbook>. This functionality is reflected in the common command callback function
    Playbook.call().

    Attributes:
        moves -> List[pbabot.games.Move]: List of moves associated with this playbook
    """
    def __init__(self, name: str, moves: List[Move]):
        """Init"""
        self.moves = moves
        super().__init__(self.call, name=name, hidden=True)

    async def call(self, ctx: commands.Context) -> None:
        """Sends a list of all moves associated with this playbook"""
        moves = f'Use .{self.name} <move> to see more details about the following moves:'
        for move in self.moves:
            moves += f'\n\t{move}'
        await ctx.send(f'```{moves}```')


class Game(commands.Cog):
    """Base Game class

    The base Game class initialises game moves and contains common methods across all games, such as retrieving moves
    and playbooks. Further game moves that require functionality should be defined as commands within the inherited
    Game class.

    Attributes:
        BASIC_MOVES -> List[pbabot.games.Move]: List of all basic (common) moves
        PLAYBOOK_MOVES -> List[pbabot.games.Playbook]: List of playbooks (and their respective moves)
        GAME_MOVES -> Dict[String, List[pbabot.games.Move]]: Dictionary of any remaining game-specific moves.
        bot -> commands.Bot: Reference to the bot so we can add the game commands.
    """
    BASIC_MOVES = []
    PLAYBOOK_MOVES = []
    GAME_MOVES = {}

    def __init__(self, bot: commands.Bot):
        """Init"""
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
    async def print_basic_moves(self, ctx: commands.Context) -> None:
        """Lists all basic (common) moves"""
        if not self.BASIC_MOVES:
            await ctx.send('Data not found. Have you loaded a game using .game?')
            return
        moves = 'Use the following commands to find detailed information about each move.'
        for move in self.BASIC_MOVES:
            moves += f'\n\t{move}'

        await ctx.send(f'```{moves}```')

    @commands.command(name='playbooks')
    async def print_playbooks(self, ctx: commands.Context) -> None:
        """Lists all playbooks"""
        if not self.PLAYBOOK_MOVES:
            await ctx.send('Data not found. Have you loaded a game using .game?')
            return
        playbooks = 'Use the following commands to find each playbook-specific move.'
        for playbook in self.PLAYBOOK_MOVES:
            playbooks += f'\n\t.{playbook.name}'

        await ctx.send(f'```{playbooks}```')
