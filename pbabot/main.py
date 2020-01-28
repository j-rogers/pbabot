"""PBABot

Powered By the Apocolypse (PBA) is a engine for playing tabletop roleplaying games such as The Sprawl and Apocolype
World. Each PBA game has features that are common between them, such as the use of basic moves, playbooks, rolling
2d6, clocks, contacts, etc. To make playing PBA games online (specifically over Discord) easier, this bot has been
created that handles the common features of PBA games. Specific game features can be easily added by creating a
class and giving it the required functionality as outlined in the games module.

Currently supported PBA games:
    The Sprawl

Author: Josh Rogers (2020)
Github: https://github.com/j-rogers/thesprawlbot
"""
import discord
import random
import pickle
import argparse
import xml.etree.ElementTree as et
from pbabot.games import sprawl
from collections import namedtuple

# API Token
TOKEN = open('token.txt', 'r').read()
DATA_FILE = 'data/data.pickle'
PERSONAL_DATA = 'data/personal'
IMAGES = 'images'


class Clock:
    """Countdown Clock

    This class maintains the state of a countdown clock. It also increaes and decreases their value.

    Attributes:
        name -> String: Name of the clock
        time -> String: Time of the clock (defaults to 1200 on creation)
    """
    def __init__(self, name, time='1200'):
        """Init"""
        self.name = name
        self.time = time

    def increase(self):
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

    def decrease(self):
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
    def __init__(self, name, description):
        self.name = name
        self.description = description


class PBABot(discord.Client):
    """PBABot

    Inherits the discord client so it can receive commands and respond to them appropriately. Clock and contact data is
    saved within a pickled file. For fun, this bot includes a feature where you can record dead characters and
    memorable moments and look back on them. This personal data is currently saved in XML format.

    Attributes:
        game -> pbabot.games.Game: The game currently loaded into PBABot that contains game-specific features
        clocks -> List: The clocks currently being used
        contacts -> List: The contacts currently being used
        personaldata -> String: Data file containing dead characters and rememberable moments.
        datafile -> String: Data file containing current clock and contact data
    """
    def __init__(self, game, datafile=DATA_FILE, personaldata=PERSONAL_DATA):
        """Init"""
        super().__init__()

        # Get game
        game_switch = {
            'sprawl': sprawl.Sprawl(),
        }
        self.game = game_switch.get(game, None)

        # No game found
        if not self.game:
            raise Exception

        # Extract data from file
        self.personaldata = personaldata
        self.datafile = datafile
        self.clocks = []
        self.contacts = []
        try:
            with open(self.datafile, 'rb') as file:
                data = pickle.loads(file.read())
            self.clocks = data["clocks"]
            self.contacts = data["contacts"]
            print("Data extracted")
        except EOFError:
            print("No data in file.")
        except FileNotFoundError:
            print("No data file found.")

    def on_message(self, message):
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
        content = message.content.lower().split(' ', 1)
        command = content[0]
        args = content[1] if len(content) > 1 else ''

        # Lookup table of commands the the respective callback
        text_switch = {
            # Listing commands
            '.help': self.help,
            '.links': self.links,
            '.clocks': self.printclocks,
            '.contacts': self.printcontacts,
            '.rememberlist': self.rememberlist,
            '.moves': self.game.moves,
            '.playbooks': self.game.playbooks,
            # Functional commands
            '.roll': self.roll,
            '.dice': self.roll,
            '.addclock': self.addclock,
            '.deleteclock': self.deleteclock,
            '.increaseclock': self.increaseclock,
            '.decreaseclock': self.decreaseclock,
            '.addcontact': self.addcontact,
            '.deletecontact': self.deletecontact,
            # Miscellaneous commands
            '.rip': self.rip,
            '.f': self.rip,
            '.remember': self.remember,
            '.chess': self.chess,
            '.answerphone': self.answerphone,
            # Dev commands
            '.refresh': self.refresh,
            '.log': self.log
        }
        callback = text_switch.get(command, None)

        # If match was found, get response
        response = None
        if callback:
            response = callback(args)

        # Lookup table if command is requesting an image
        image_switch = {
            '.map': discord.File(f'{IMAGES}/map.jpg', 'map.jpg'),
            '.fuckmendle': discord.File(f'{IMAGES}/mendle.png', 'mendle.png'),
            '.fridge': discord.File(f'{IMAGES}/FRIDGE.jpg', 'fridge.jpg'),
            '.clones': discord.File(f'{IMAGES}/clones.png', 'clones.png')
        }
        image = image_switch.get(command, None)

        # If command didn't match a PBA or image command, try game-specific command
        if not response and not image:
            response = self.game.handle(command, args)
            # Didn't match game-specific command, send back invalid command
            if not response:
                response = 'Invalid command. Type ".help" for a list of commands.'

        # If text response, surround in "```" for discord formatting
        if response and not image:
            response = f'```{response}```'

        # Respond if we have something to send back
        if response or image:
            return response
            #await message.channel.send(response, files=image)

    async def on_ready(self):
        """Event callback for when discord.Client is ready"""
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def help(self, message):
        """Prints list of commands
        """
        commands = """Use \".command\" when using this bot.\n
    .help: Displays this help message.
    .roll: Rolls 2d6 dice.
    .moves: Displays a list of basic moves.
    .playbooks: Displays a list of playbooks.
    .clocks: Displays the current list of clocks.
    .addclock <clock name>: Adds a clock with a value of 1500.
    .increaseclock <clock name>: Increases a clock by one segment.
    .decreaseclock <clock name>: Decreases a clock by one segment.
    .deleteclock <clock name>: Deletes the specified clock.
    .contacts: Displays the current list of contacts.
    .addcontact <contact name> <description>: Adds a new contact.
    .deletecontact <contact name>: Deletes a contact.
    .map: Displays a current map
    .rip: List all dead characters.
    .rememberlist: Displays rough numbers for specific moments. 
    .remember: Displays a message of a memorable moment.
    .refresh: Reloads the clock and contact data.
    .log <message>: Saves a message to the log file.
    .links: Displays a link to all the PBA games.
    
Game-specific Commands:
"""
        # Add game-specific commands
        for command, description in self.game.commands.items():
            commands += f'\t{command}: {description}\n'

        commands.strip()
        return commands

    def links(self, message):
        """Prints links to PBA games"""
        msg = """
        **Apocalpyse World:** https://www.dropbox.com/sh/fmsh9kyaiplqhom/AACw1iLMQ7f53Q40FUnMjlz4a?dl=0
        **The Sprawl:** https://www.dropbox.com/sh/9fr35ivzbvfh06p/AACarsYBpNXxBpEUk_-fz_PXa?dl=0
        **Tremulas:** https://www.dropbox.com/sh/tbhk0w0zgihrf2h/AACtvyv9l5ruLBE6UG3XeGfba?dl=0
        **Dungeon World:** https://www.dropbox.com/sh/p61lutt9m6dfpa3/AACTvHhbJa7K1RIHFYVvJqIza?dl=0
        """
        msg = msg.replace('\t', '')
        return msg

    def printclocks(self, message):
        """Prints current clock times"""
        # Check that there are clocks
        if not self.clocks:
            return 'No clocks have been added.'

        # Convert time values to segments
        switch = {
            '1200': '□□□□ □□□□ □□□□ □ □ □',
            '1500': '■■■■ □□□□ □□□□ □ □ □',
            '1800': '■■■■ ■■■■ □□□□ □ □ □',
            '2100': '■■■■ ■■■■ ■■■■ □ □ □',
            '2200': '■■■■ ■■■■ ■■■■ ■ □ □',
            '2300': '■■■■ ■■■■ ■■■■ ■ ■ □',
            '0000': '■■■■ ■■■■ ■■■■ ■ ■ ■'
        }

        # Build string
        clocks = ''
        for clock in self.clocks:
            clocks += f'{clock.name}: {switch[clock.time]}\n'

        return clocks

    def printcontacts(self, message):
        """Prints list of contacts"""
        # Check there are contacts
        if not self.contacts:
            return 'No contacts have been added.'

        # Build string
        contacts = ''
        for contact in self.contacts:
            contacts += f'{contact.name}: {contact.description}\n'

        return contacts

    def rememberlist(self, message):
        """Prints indexes of remember moments"""
        # TODO remove personal file from tracking
        try:
            tree = et.parse(self.personaldata)
        except FileNotFoundError:
            return 'No personal file found.'

        remember = tree.find('remember')

        rememberindexes = ''
        for group in list(remember):
            memories = list(group)
            min = memories[0].get('index')
            max = memories[-1].get('index')
            description = group.get('description')
            rememberindexes += f'\n{min}-{max}: {description}'

        return rememberindexes

    def roll(self, message):
        """Rolls 2d6 and prints the result"""
        # Generate the roll
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2

        # Unique response based on roll
        result = ''
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

        return result

    def addclock(self, name):
        """Adds a clock of the given name at 1200"""
        # Checks if clock has already been added
        clock = self._getclock(name)
        if clock:
            return f'Clock {name} already exists.'

        # Append to clocks list
        self.clocks.append(Clock(name))

        # Update and refresh file
        self._savedata()
        print(f'Clock added to file: {name} at 1200')

        # Form message and send
        return f'Clock added to file: {name} at 1200'

    def deleteclock(self, name):
        """Deletes the clock with specified name"""
        # Find the clock to be deleted
        clock = self._getclock(name)
        if not clock:
            return f'Clock {name} not found.'

        # Delete clock
        self.clocks.remove(clock)

        # Update and refresh file
        self._savedata()
        print(f'Clock deleted from file: {name}')

        # Form message and send
        return f'Deleted clock {name}.'

    def increaseclock(self, name):
        """Increases the clock of specified name by one segment"""
        # Find the clock to be increased
        clock = self._getclock(name)

        # Check if the clock was found
        if not clock:
            return f'Clock "{name}" not found.'

        # Increase clock
        clock.increase()

        # Update and refresh file
        self._savedata()
        print(f'Clock update reflected in file (INCREASE): ({clock.name} {clock.time})')

        # Form message and send
        return f'{clock.name} clock increased to {clock.time}.'

    def decreaseclock(self, name):
        """Decreases the clock of specified name by one segment"""
        # Find clock
        clock = self._getclock(name)

        # Check if clock exists
        if not clock:
            return f'Clock "{name}" not found.'

        # Decrease clock
        clock.decrease()

        # Update and save data
        self._savedata()

        return f'{clock.name} clock decreased to {clock.time}'

    def addcontact(self, args):
        """Adds a contact with specified information

        A contact can be added by either using .addcontact name description, where name is a single word and description
        is multiple. If you want to add a contact with a name that has multiple words then you can use
        .addcontact "first last" description.

        Args:
            args -> String: Information of contact to be added
        """
        # Get the contact name and description
        name = None
        description = None
        tokens = args.split('"', 2)

        # Multiple word name
        if len(tokens) > 1:
            name = tokens[1]
            description = tokens[2].strip()
        # Single world name
        else:
            tokens = args.split(' ', 1)
            name = tokens[0]
            description = tokens[1]

        # Check if contact already exists
        if self._getcontact(name):
            return f'Contact "{name}" already added as a contact.'

        # Add contact and save data
        self.contacts.append(Contact(name, description))
        self._savedata()

        return f'Contact added: {name}.'

    def deletecontact(self, name):
        contact = self._getcontact(name)

        if not contact:
            return f'Contact {name} not found.'

        self.contacts.remove(contact)

        self._savedata()

        return f'Deleted contact {name}'

    def rip(self, player):
        tree = et.parse(self.personaldata)
        rip = tree.getroot().find('rip')

        death = ''
        if player:  # specific message
            player = rip.find(player)
            if player:
                for character in list(player):
                    death += f"{character.get('name')}: {character.get('cause')}\n"
        else:  # short list
            for player in list(rip):
                death += f'{player.tag}: '
                for character in list(player):
                    death += f'{character.get("name")}, '
                death += '\n'

        death = death.strip()
        return death

    def remember(self, index):
        try:
            tree = et.parse(self.personaldata)
        except FileNotFoundError:
            return 'No personal file found.'

        remember = tree.find('remember')
        memories = [list(group) for group in list(remember)]

        min = memories[0][0].get('index')
        max = memories[-1][-1].get('index')

        if index:
            try:
                num = int(index)
            except ValueError:
                return 'Incorrect selection.'
            else:
                if num < int(min) or num > int(max):
                    index = str(random.randint(int(min), int(max)))
        else:
            index = str(random.randint(int(min), int(max)))

        msg = None
        for group in memories:
            for remember in group:
                if remember.get('index') == index:
                    msg = remember.text

        return msg

    def chess(self, message):
        msg = "**THE\t  TECHSORCIST\n\tIS    THE\nCHESS\t\tMASTER!**"
        return msg

    def answerphone(self, index):
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

    def refresh(self, message):
        msg = ''
        try:
            data = pickle.loads(open(self.datafile, 'rb').read())
            self.clocks = data["clocks"]
            self.contacts = data["contacts"]
            msg = 'Data has been refreshed.'
            print("Data extracted")
        except EOFError:
            print("No data in file.")
        except FileNotFoundError:
            print("No data file found.")

        # Refresh game data as well
        self.game.loaddata()

        return msg

    def log(self, message):
        # Write to the file
        file = open("log.txt", "a")
        file.write(message + "\n")
        file.close()
        print(f'Log saved: {message}')

        # Form and send message
        return 'Log saved.'

    def _getcontact(self, name):
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                return contact

        return None

    def _getclock(self, name):
        for clock in self.clocks:
            if name.lower() == clock.name.lower():
                return clock

        return None

    def _savedata(self):
        data = {'clocks': self.clocks, 'contacts': self.contacts}
        with open(self.datafile, 'wb') as file:
            file.write(pickle.dumps(data))




def main():
    # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--game', type=str, required=True, choices=['sprawl', 'apoc'])
    args = parser.parse_args()
    game = vars(args)['game']

    client = PBABot(game)
    i = ''
    while i != 'q':
        i = input()
        Message = namedtuple('Message', 'content author')
        msg = Message(i, 'jeff')
        print(client.on_message(msg))
    #client.run(TOKEN)


if __name__ == '__main__':
    main()
