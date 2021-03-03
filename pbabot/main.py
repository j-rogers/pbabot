"""PBABot

Powered By the Apocolypse (PBA) is a engine for playing tabletop roleplaying games such as The Sprawl and Apocolype
World. Each PBA game has features that are common between them, such as the use of basic moves, playbooks, rolling
2d6, clocks, contacts, etc. To make playing PBA games online (specifically over Discord) easier, this bot has been
created that handles the common features of PBA games. Specific game features can be easily added by creating a
class and giving it the required functionality as outlined in the games module.

Currently supported PBA games:
    The Sprawl

Author: Josh Rogers (2020)
Github: https://github.com/j-rogers/pbabot
"""
import discord
import random
import pickle
import argparse
from pbabot.games import Game, Sprawl
from typing import Optional

# Flags
NO_DISCORD = False   # Prevents logging into Discord and instead receiving input and sending output to console

# API Token
TOKEN = open('token.txt', 'r').read() if not NO_DISCORD else None

# Data files
DATA_FILE = 'data/data.pickle'

# Image folder
IMAGES = 'images'


class Clock:
    """Countdown Clock

    This class maintains the state of a countdown clock. It also increases and decreases their value.

    Attributes:
        name -> String: Name of the clock
        time -> String: Time of the clock (defaults to 1200 on creation)
    """
    def __init__(self, name: str, time: str = '1200'):
        """Init"""
        self.name = name
        self.time = time

    def __str__(self):
        """String representation of a clock"""
        switch = {
            '1200': '□□□□ □□□□ □□□□ □ □ □',
            '1500': '■■■■ □□□□ □□□□ □ □ □',
            '1800': '■■■■ ■■■■ □□□□ □ □ □',
            '2100': '■■■■ ■■■■ ■■■■ □ □ □',
            '2200': '■■■■ ■■■■ ■■■■ ■ □ □',
            '2300': '■■■■ ■■■■ ■■■■ ■ ■ □',
            '0000': '■■■■ ■■■■ ■■■■ ■ ■ ■'
        }

        return f'{self.name}: {switch[self.time]}'

    def increase(self) -> str:
        """Increases the clock's time by one segment"""
        if self.time == "1200":
            self.time = "1500"
        elif self.time == "1500":
            self.time = "1800"
        elif self.time == "1800":
            self.time = "2100"
        elif self.time == "2100":
            self.time = "2200"
        elif self.time == "2200":
            self.time = "2300"
        elif self.time == "2300":
            self.time = "0000"
        elif self.time == "0000":
            return '```Clock is already at midnight.```'

    def decrease(self) -> str:
        """Decreases the clock's time by one segment"""
        if self.time == "0000":
            self.time = "2300"
        elif self.time == "2300":
            self.time = "2200"
        elif self.time == "2200":
            self.time = "2100"
        elif self.time == "2100":
            self.time = "1800"
        elif self.time == "1800":
            self.time = "1500"
        elif self.time == "1500":
            self.time = "1200"
        elif self.time == "1200":
            return '```Clock is already at 1200.```'


class Contact:
    """Contact

    Stores a contacts name and description.

    Attributes:
        name -> String: Name of the contact
        description -> String: Description of the contact
    """
    def __init__(self, name: str, description: str):
        """Init"""
        self.name = name
        self.description = description


class PBABot(discord.Client):
    """PBABot

    Inherits the discord client so it can receive commands and respond to them appropriately. Clock and contact data is
    saved within a pickled file. For fun, this bot includes a feature where you can record dead characters and
    memorable moments and look back on them. This personal data is currently saved in XML format.

    Attributes:
        game -> pbabot.games.Game: Default game to load.
        clocks -> List: The clocks currently being used
        contacts -> List: The contacts currently being used
        data_file -> String: Data file containing current clock and contact data
    """
    COMMANDS = {
        'help': 'Displays the help message.',
        'roll': 'Rolls 2d6 dice and applies your +/- modifier. Usage: .roll <modifier>',
        'moves': 'Displays a list of basic moves.',
        'playbooks': 'Displays a list of playbooks',
        'clocks': 'Displays the current list of clocks. If the private_clocks property is set then only the MC can view'
                  'the clocks.',
        'addclock': 'Adds a clock with a value of 1200. Usage: .addclock <clock-name>',
        'increaseclock': 'Increases the specified clock by one segment. Usage: .increaseclock <clock-name>',
        'decreaseclock': 'Decreases the specified clock by one segment. Usage: .decreaseclock <clock-name>',
        'resetclock': 'Resets the specified clock to 1200. Usage: .resetclock <clock-name>',
        'deleteclock': 'Deletes the specified clock. Usage: .deleteclock <clock-name>',
        'contacts': 'Displays the current list of contacts',
        'addcontact': 'Adds a new contact. Usage: .addcontact "<contact-name>"',
        'deletecontact': 'Deletes a contact. Usage: .deletecontact "<contact-name>"',
        'set': 'Sets a bot property. Current properties: game, private_clocks, mc. Usage: .set <property> <value>',
        'map': 'Displays the current map.',
        'image': 'Displays the specified image. Usage: .image <image-name>',
        'kill': 'Add a dead character with a description of how they died. Usage: .kill "<player>" "<character>"'
                '<description>',
        'rip': 'List all dead characters.',
        'remember': 'Displays a message of a memorable moment, or add a new memory. Usage: .remember [when <memory>] '
                     '[<index>]',
        'forget': 'Delete a memory. Usage: .forget <index>',
        'log': 'Saves a message to the log file. Usage: .log <message>',
        'links': 'Displays a link to all the PBA games.',
    }

    def __init__(self, game: str, data_file: str = DATA_FILE):
        """Init"""
        if not NO_DISCORD:
            super().__init__()

        # Bot properties
        self.game = self.set_game(game)[1] if game else Game()
        self.private_clocks = True
        self.mc = None

        # Extract data from file
        self.memories = []
        self.dead_characters = {}
        self.data_file = data_file
        self.clocks = []
        self.contacts = []
        try:
            with open(self.data_file, 'rb') as file:
                data = pickle.loads(file.read())
            self.clocks = data['clocks']
            self.contacts = data['contacts']
            self.memories = data['memories']
            self.dead_characters = data['dead_characters']
            print('Data extracted')
        except EOFError:
            print('No data in file.')
        except FileNotFoundError:
            print('No data file found.')
        except KeyError as ke:
            print(f'KeyError while loading data: {ke}')

    def debug_on_message(self, message: str) -> str:
        """Alternative to on_message when NO_DISCORD flag is set to True

        When debugged without discord, we instead need to read input from console, and also print to console. This
        method is used instead of on_message when the NO_DISCORD flag is set, allowing us to do just that.

        NOTE: Functionality that requires a hash of the user is currently disabled

        Args:
            message: Message received from console

        Returns:
            Response to be printed out
        """
        # Prevents bot responding to regular messages
        if not message.startswith('.'):
            return 'Incorrect command.'

        # Parse message
        content = message.split(' ', 1)
        command = content[0].lower()
        args = content[1] if len(content) > 1 else ''

        # Lookup table of commands the the respective callback
        text_switch = {
            # Listing commands
            '.help': self.help,
            '.links': self.links,
            '.clocks': self.print_clocks,
            '.contacts': self.print_contacts,
            '.moves': self.game.moves,
            '.playbooks': self.game.playbooks,
            # Functional commands
            '.roll': self.roll,
            '.dice': self.roll,
            '.addclock': self.add_clock,
            '.deleteclock': self.delete_clock,
            '.increaseclock': self.increase_clock,
            '.decreaseclock': self.decrease_clock,
            '.addcontact': self.add_contact,
            '.deletecontact': self.delete_contact,
            '.set': self.set_property,
            # Miscellaneous commands
            '.rip': self.rip,
            '.f': self.rip,
            '.remember': self.remember,
            '.forget': self.forget,
            '.kill': self.kill,
            '.chess': self.chess,
            '.answerphone': self.answerphone,
            # Dev commands
            '.refresh': self.refresh,
            '.log': self.log
        }
        callback = text_switch.get(command, None)
        response = callback(args) if callback else None

        # Lookup table if command is requesting an image
        image_switch = {
            '.map': self.map,
            '.image': self.image,
        }
        image_callback = image_switch.get(command, None)

        image = None
        if image_callback:
            image = image_callback(args)

        # If command didn't match a PBA or image command, try game-specific command
        if not response and not image:
            try:
                response = self.game.handle(command, args)
            except NotImplementedError:
                response = 'No game has been loaded. Use .game'
            else:
                # Didn't match game-specific command, send back invalid command
                if not response:
                    response = 'Invalid command. Type ".help" for a list of commands.'

        # If text response, surround in "```" for discord formatting
        if response and not image:
            response = f'```{response}```'

        # Respond if we have something to send back
        return response

    async def on_message(self, message: discord.Message) -> None:
        """Event callback when receiving a message

        From discord.Client, this method is an event callback for when the bot receives a message. It checks the message
        to make sure it is a command (identified by a '.' in front of the message), and if it is then parses the message
        and attempts to form a response. If the message does not match any known commands, the bot will reply with a
        invalid command error.

        Args:
            message -> discord.Message: Message received from Discord
        """
        # Prevents bot replying to itself
        if message.author == self.user:
            return

        # Prevents bot responding to regular messages
        if not message.content.startswith('.'):
            return

        # Parse message
        content = message.content.split(' ', 1)
        command = content[0].lower()
        args = content[1] if len(content) > 1 else ''

        # Lookup table of commands the the respective callback
        text_switch = {
            # Listing commands
            '.help': self.help,
            '.links': self.links,
            '.contacts': self.print_contacts,
            '.moves': self.game.moves,
            '.playbooks': self.game.playbooks,
            # Functional commands
            '.roll': self.roll,
            '.dice': self.roll,
            '.addcontact': self.add_contact,
            '.deletecontact': self.delete_contact,
            # Miscellaneous commands
            '.rip': self.rip,
            '.f': self.rip,
            '.remember': self.remember,
            '.forget': self.forget,
            '.kill': self.kill,
            '.chess': self.chess,
            '.answerphone': self.answerphone,
            # Dev commands
            '.refresh': self.refresh,
            '.log': self.log
        }
        callback = text_switch.get(command, None)
        response = callback(args) if callback else None

        # Include hash of message author for some commands
        user_switch = {
            '.addclock': self.add_clock,
            '.deleteclock': self.delete_clock,
            '.increaseclock': self.increase_clock,
            '.decreaseclock': self.decrease_clock,
            '.resetclock': self.reset_clock,
            '.clocks': self.print_clocks,
            '.set': self.set_property,
        }
        callback = user_switch.get(command, None)
        response = callback(args, hash(message.author)) if callback else response

        # Lookup table if command is requesting an image
        image_switch = {
            '.map': self.map,
            '.image': self.image,
        }
        image_callback = image_switch.get(command, None)
        image = image_callback(args) if image_callback else None

        # If command didn't match a PBA or image command, try game-specific command
        if not response and not image:
            try:
                response = self.game.handle(command, args)
            except NotImplementedError:
                response = 'No game has been loaded. Use .set game <game>'
            else:
                # Didn't match game-specific command, send back invalid command
                if not response:
                    response = 'Invalid command. Type ".help" for a list of commands.'

        # If text response, surround in "```" for discord formatting
        if response and not image:
            response = f'```{response}```'

        # Respond if we have something to send back
        if response or image:
            await message.channel.send(response, file=image)

    async def on_ready(self):
        """Event callback for when discord.Client is ready"""
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def help(self, message: str) -> str:
        """Prints list of commands"""
        # General commands
        commands = 'Use \".command\" when using this bot.\n\nGeneral commands:\n'
        for command, description in self.COMMANDS.items():
            commands += f'\t{command}: {description}\n'

        commands += "\nGame-specific Commands:\n"
        # Add game-specific commands
        for command, description in self.game.COMMANDS.items():
            commands += f'\t{command}: {description}\n'

        commands.strip()
        return commands

    def set_property(self, args: str, user: int) -> str:
        property = None
        value = None
        try:
            property, value = args.split(' ', 1)
        except ValueError:
            if 'mc' not in args:
                return 'Usage: .set <property> <value>'
            else:
                property = 'mc'

        if property.lower() == 'game':
            response, game = self.set_game(value)
            self.game = game if game else self.game
            return response
        elif property.lower() == 'private_clocks':
            if value.lower() == 'true':
                self.private_clocks = True
            elif value.lower() == 'False':
                self.private_clocks = False
            else:
                return 'Invalid value given, either true or false.'
        elif property.lower() == 'mc':
            self.mc = user
            return 'MC has been set.'
        else:
            return 'Invalid property. Properties are game, private_clocks, mc.'

    def set_game(self, game: str) -> str:
        """Sets the current game being played"""
        if not game:
            if self.game:
                return f'Currently playing {self.game}.'
            else:
                return 'No game is currently set. Set a game with .game <game>.'

        game_switch = {
            'sprawl': Sprawl,
        }

        game_callback = game_switch.get(game.lower(), None)

        if game_callback:
            return f'Now playing {game}.', game_callback()
        else:
            return f'No game {game} found.', None

    def links(self, message: str) -> str:
        """Prints links to PBA games"""
        return """**Apocalpyse World:** https://www.dropbox.com/sh/fmsh9kyaiplqhom/AACw1iLMQ7f53Q40FUnMjlz4a?dl=0
**The Sprawl:** https://www.dropbox.com/sh/9fr35ivzbvfh06p/AACarsYBpNXxBpEUk_-fz_PXa?dl=0
**Tremulas:** https://www.dropbox.com/sh/tbhk0w0zgihrf2h/AACtvyv9l5ruLBE6UG3XeGfba?dl=0
**Dungeon World:** https://www.dropbox.com/sh/p61lutt9m6dfpa3/AACTvHhbJa7K1RIHFYVvJqIza?dl=0"""

    def print_clocks(self, message: str, user: int) -> str:
        """Prints current clock times"""
        if self.private_clocks and self.mc != user:
            return 'You are not the MC. Increasing all clocks to 0000 (not really).'

        # Check that there are clocks
        if not self.clocks:
            return 'No clocks have been added.'

        # Print clocks
        clocks = ''
        for clock in self.clocks:
            clocks += f'{clock}\n'

        return clocks

    def print_contacts(self, message: str) -> str:
        """Prints list of contacts"""
        # Check there are contacts
        if not self.contacts:
            return 'No contacts have been added.'

        # Build string
        contacts = ''
        for contact in self.contacts:
            contacts += f'{contact.name}: {contact.description}\n'

        return contacts

    def roll(self, modifier: str) -> str:
        """Rolls 2d6 and prints the result"""
        # Generate the roll
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2

        # Add any modifiers
        num = None
        if modifier:
            try:
                num = int(modifier)
            except ValueError:
                pass
            else:
                roll += num

        # Unique response based on roll
        result = ''
        if roll <= 0:
            result = f'How did you even get this roll? Oh well, you\'ve basically killed yourself since you rolled a {roll}'
        if roll == 1:
            result = 'Throwbacks to when Martin\'s bot could roll a 1 from 2d6. Good times, not for you though, you rolled a 1.'
        elif roll == 2:
            result = 'I hope you have a lot of health cause this is gonna hurt. You rolled a 2.'
        elif roll == 3:
            result = 'The Thing is going to have fun with this, you rolled a 3.'
        elif roll == 4:
            result = 'You rolled the length of your penis, 4 inches.'
        elif roll == 5:
            result = 'Maybe you should have taken those drugs, you rolled a 5.'
        elif roll == 6:
            result = 'The RNG gods are displeased with you. You rolled a 6.'
        elif roll == 7:
            result = 'You know what, it could be worse. You rolled a 7.'
        elif roll == 8:
            result = 'Someones going to be sleeping with the fishes, is it going to be you or him with a roll of 8.'
        elif roll == 9:
            result = 'Almost hit that sweet spot. You rolled a 9.'
        elif roll == 10:
            result = 'Now we\'re talking, you rolled a 10.'
        elif roll == 11:
            result = 'You could fuck up someones day with this. You rolled an 11.'
        elif roll == 12:
            result = 'Okay, now THIS is epic. You rolled a 12.'
        elif roll >= 13:
            result = f'Thank you dice gods, very cool! You rolled a {roll}'

        if num:
            result += f' ({dice1 + dice2} + {num})'

        return result

    def add_clock(self, name: str, user: int) -> str:
        """Adds a clock of the given name at 1200"""
        # Check private clock and MC permissions
        if self.private_clocks and self.mc != user:
            return 'You are not the MC. Cheeky.'

        # Checks if clock has already been added
        clock = self._get_clock(name)
        if clock:
            return f'Clock {name} already exists.'

        # Append to clocks list
        self.clocks.append(Clock(name))

        # Update and refresh file
        self._save_data()
        print(f'Clock added to file: {name} at 1200')

        # Form message and send
        return f'Clock added to file: {name} at 1200'

    def delete_clock(self, name: str, user: int) -> str:
        """Deletes the clock with specified name"""
        if self.private_clocks and self.mc != user:
            return 'You are not the MC. Naughty.'

        # Find the clock to be deleted
        clock = self._get_clock(name)
        if not clock:
            return f'Clock {name} not found.'

        # Delete clock
        self.clocks.remove(clock)

        # Update and refresh file
        self._save_data()
        print(f'Clock deleted from file: {name}')

        # Form message and send
        return f'Deleted clock {name}.'

    def increase_clock(self, name: str, user: int) -> str:
        """Increases the clock of specified name by one segment"""
        if self.private_clocks and self.mc != user:
            return 'You are not the MC. I\'m going to dob on you.'

        # Find the clock to be increased
        clock = self._get_clock(name)

        # Check if the clock was found
        if not clock:
            return f'Clock "{name}" not found.'

        # Increase clock
        clock.increase()

        # Update and refresh file
        self._save_data()
        print(f'Clock update reflected in file (INCREASE): ({clock.name} {clock.time})')

        # Form message and send
        return f'{clock.name} clock increased to {clock.time}.'

    def decrease_clock(self, name: str, user: int) -> str:
        """Decreases the clock of specified name by one segment"""
        if self.private_clocks and self.mc != user:
            return 'You are not the MC. -1 ongoing.'

        # Find clock
        clock = self._get_clock(name)

        # Check if clock exists
        if not clock:
            return f'Clock "{name}" not found.'

        # Decrease clock
        clock.decrease()

        # Update and save data
        self._save_data()

        return f'{clock.name} clock decreased to {clock.time}'

    def reset_clock(self, name: str, user: int) -> str:
        """Reset a clock of specified name to 1200"""
        if self.private_clocks and self.mc != user:
            return 'You are not the MC. The Thing has been alerted to your position.'

        # Find clock
        clock = self._get_clock(name)

        # Check if clock exists
        if not clock:
            return f'Clock "{name}" not found.'

        # Reset the clock
        clock.time = '1200'

        # Update and save data
        self._save_data()

        return f'{clock.name} clock reset to 1200.'

    def add_contact(self, args: str) -> str:
        """Adds a contact with specified information

        A contact can be added by either using .add_contact name description, where name is a single word and description
        is multiple. If you want to add a contact with a name that has multiple words then you can use
        .add_contact "first last" description.

        Args:
            args -> String: Information of contact to be added
        """
        # Get the contact name and description
        name = None
        description = None
        tokens = args.split('"', 2)

        # Check if name was surround by double quotes
        if len(tokens) > 1:
            name = tokens[1]
            description = tokens[2].strip()
        # No quotes
        else:
            return 'You must surround the contact\'s name in double quotes.'

        # Check if contact already exists
        if self._get_contact(name):
            return f'Contact "{name}" already added as a contact.'

        # Add contact and save data
        self.contacts.append(Contact(name, description))
        self._save_data()

        return f'Contact added: {name}.'

    def delete_contact(self, name: str) -> str:
        """Deletes the given contact"""
        contact = self._get_contact(name)

        if not contact:
            return f'Contact {name} not found.'

        self.contacts.remove(contact)

        self._save_data()

        return f'Deleted contact {name}'

    def rip(self, player: str) -> str:
        """Displays a list of dead characters (in total or for the given player)"""
        death = ''
        if player in self.dead_characters:
            for character, description in self.dead_characters[player].items():
                death += f'{character}: {description}'
        else:
            for player, characters in self.dead_characters.items():
                death += f'{player}: '
                death += ', '.join(characters.keys()) + '\n'

        if not death:
            death = 'No dead characters.'

        return death

    def kill(self, args: str) -> str:
        """Adds a dead character"""
        tokens = [arg for arg in args.split('"', 4) if arg.strip()]

        if len(tokens) != 3:
            return 'Please surround player and character names in double quotes.'

        player = tokens[0]
        character = tokens[1]
        description = tokens[2]

        if player not in self.dead_characters:
            self.dead_characters[player] = {character: description}
        else:
            self.dead_characters[player][character] = description

        self._save_data()

        return f'{player}\'s character {character} was killed: {description}.'

    def remember(self, args: str) -> str:
        """Displays a memory or list of memory indices"""
        if 'when' in args.split(' ', 1)[0].lower():
            self.memories.append(args.split(' ', 1)[1])
            self._save_data()
            return f'Memory added at index {len(self.memories)-1}'
        else:
            try:
                index = int(args)
            except ValueError:
                max = len(self.memories)
                if not max:
                    return 'No memories have been added.'
                index = random.randint(0, max-1)

            try:
                memory = self.memories[index]
            except IndexError:
                return f'No memory at index {index}.'

            return f'{index}: {memory}' if memory else f'No memory found at index {index}.'

    def forget(self, index: str) -> str:
        """Forgets the memory at given index"""
        try:
            i = int(index)
        except ValueError:
            return f'Invalid index given: {index} (should be an integer).'

        try:
            memory = self.memories.pop(i)
        except IndexError:
            return f'No memory at index {i}.'
        else:
            return f'Memory deleted at index {i}: "{memory}".'

    def map(self, args: str) -> discord.File:
        """Returns the default map"""
        return self.image('map.jpg')

    def image(self, name: str) -> discord.File:
        """Returns the given image"""
        image = None
        if name:
            try:
                image = discord.File(f'{IMAGES}/{name}', f'{name}')
            except FileNotFoundError:
                image = discord.File(f'{IMAGES}/no_map.jpg', 'no_map.jpg')
        else:
            image = discord.File(f'{IMAGES}/no_map.jpg', 'no_map.jpg')

        return image

    def chess(self, message: str) -> str:
        """idk what this is"""
        msg = "**THE\t  TECHSORCIST\n\tIS    THE\nCHESS\t\tMASTER!**"
        return msg

    def answerphone(self, index: str) -> str:
        """idk what this is either"""
        min = 1
        max = 1
        member = random.randint(min, max)

        if index:  # If more values other than .remember
            number = int(index)  # converts stringArray  (['.remember' 'num']) to int
            if number >= min and number <= max:  # Ensures it will exist within the range of .remember
                member = number  # sets member to the number.

        switch = {
            1: 'css\nWelcome to the Wii Fit helpline how can I help you?',
        }

        return switch[member]

    def refresh(self, message: str) -> str:
        """Reloads game data"""
        msg = ''
        try:
            data = pickle.loads(open(self.data_file, 'rb').read())
            self.clocks = data['clocks']
            self.contacts = data['contacts']
            self.memories = data['memories']
            self.dead_characters = data['dead_characters']
            msg = 'Data has been refreshed.'
            print('Data refreshed.')
        except EOFError:
            print('No data in file.')
        except FileNotFoundError:
            print('No data file found.')
        except KeyError:
            print(f'KeyError while loading data.')

        return msg

    def log(self, message: str) -> str:
        """Writes the message to a log file"""
        # Write to the file
        file = open("log.txt", "a")
        file.write(message + "\n")
        file.close()
        print(f'Log saved: {message}')

        # Form and send message
        return 'Log saved.'

    def _get_contact(self, name: str) -> Optional[Contact]:
        """Retrieves the given contact"""
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                return contact

        return None

    def _get_clock(self, name: str) -> Optional[Clock]:
        """Retrieves the given clock"""
        for clock in self.clocks:
            if name.lower() == clock.name.lower():
                return clock

        return None

    def _save_data(self) -> None:
        """Saves the current data to file"""
        data = {
            'clocks': self.clocks,
            'contacts': self.contacts,
            'memories': self.memories,
            'dead_characters': self.dead_characters
        }

        with open(self.data_file, 'wb') as file:
            file.write(pickle.dumps(data))


def main():
    # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--game', type=str, default=None, choices=['sprawl', 'apoc'])
    args = parser.parse_args()
    game = vars(args)['game']

    client = PBABot(game)
    if not NO_DISCORD:
        client.run(TOKEN)
    else:
        while True:
            message = input()
            response = client.debug_on_message(message)
            print(response)


if __name__ == '__main__':
    main()
