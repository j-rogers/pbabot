import pickle
from typing import Optional


class Move:
    """Base Move class

    Attributes:
        name -> String: Name of the move
        description -> String: Short description of the move
        commands -> Set: Set of commands that reference this move
        full_description -> String: Full description of the move.
    """
    def __init__(self, name: str, description: str, *commands: str, full_description: str = None):
        """Init"""
        self.name = name
        self.description = description
        self.full_description = full_description if full_description else description
        self.commands = set(commands)

    def __str__(self) -> str:
        """String representation of the move"""
        return f'{self.name}: {self.description} {self.commands if self.commands else ""}'


class Game:
    """Base Game class

    The base Game class contains common methods across all games, such as retrieving moves and playbooks from the data.

    Attributes:
        commands -> Dictionary: Dictionary of game-specific commands
        data_file -> String: Name of file containing game-specific data
        data -> Dictionary: Unpacked data from file
        stats -> Dictionary: Game-specific stats and values
    """
    BASIC_MOVES = []
    PLAYBOOK_MOVES = {}
    GAME_MOVES = {}
    STATS = {}
    COMMANDS = {}

    def handle(self, command: str, args: str) -> Optional[str]:
        """Handler for game-specific commands. To be implemented in the actual game class."""
        raise NotImplementedError

    def moves(self, message: str) -> str:
        """Lists all basic (common) moves"""
        if not self.BASIC_MOVES:
            return 'Data not found. Have you loaded a game using .game?'
        moves = 'Use the following commands to find detailed information about each move.'
        for move in self.BASIC_MOVES:
            if move.commands:
                moves += f'\n\t{move.name} {move.commands}'

        return moves

    def playbooks(self, message: str) -> str:
        """Lists all playbooks"""
        if not self.BASIC_MOVES:
            return 'Data not found. Have you loaded a game using .game?'
        playbooks = 'Use the following commands to find each playbook-specific move.'
        for playbook in self.PLAYBOOK_MOVES:
            playbooks += f'\n\t.{playbook}'

        return playbooks

    def _get_playbook(self, playbook: str, move: str) -> Optional[str]:
        """Gets the specified move from the given playbook, if it exists"""
        if playbook not in self.PLAYBOOK_MOVES:
            return None

        if not move:
            moves = f'Use .{playbook} <move> to see more details about the following moves:'
            for move in self.PLAYBOOK_MOVES[playbook]:
                moves += f'\n\t{move}'
            return moves

        m = self._get_move(move, playbook=playbook)
        return m.full_description if m else None

    def _get_move(self, query: str, index: list = None, name: bool = False, playbook: str = None) -> Optional[Move]:
        """Queries for the given move

        Searches for a move based on its name or command. Can be a playbook or other move (e.g. basic).

        Args:
            query -> String: Move name or command to be searched for.
            index -> String: Data index to be used, defaults to basic.
            name -> Boolean: Indicates if we are searching the move by command (if false) or name (if true). Defaults
                to false.
            playbook -> String: Name of the playbook, if we are searching for a playbook move. Defaults to None,
                indicating we are not searching for a playbook move.

        Returns:
            The move matching the query, otherwise None if no matching move was found.
        """
        # Search playbook for the move
        if playbook:
            for move in self.PLAYBOOK_MOVES[playbook]:
                if query in move.commands:
                    return move

        # Not a playbook move, search specified index for the move instead
        if not index:
            index = self.BASIC_MOVES
        for move in index:
            if name:
                if query in move.name:
                    return move
            else:
                if query in move.commands:
                    return move

        return None
