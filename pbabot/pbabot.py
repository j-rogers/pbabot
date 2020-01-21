import discord  # version 0.16.12
import random
import pickle
import argparse
import xml.etree.ElementTree as et
from pbabot.games import *
from collections import namedtuple

# API Token
TOKEN = open('token.txt', 'r').read()
DATA_FILE = 'data/data.pickle'
PERSONAL_DATA = 'data/personal'
IMAGES = 'images'


class Clock:
    def __init__(self, name, time='1200'):
        self.name = name
        self.time = time

    def increase(self):
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
    def __init__(self, name, description):
        self.name = name
        self.description = description


class PBABot(discord.Client):
    def __init__(self, game, datafile=DATA_FILE, personaldata = PERSONAL_DATA):
        super().__init__()

        game_switch = {
            'sprawl': sprawl.Sprawl(),
        }
        self.game = game_switch.get(game, None)

        if not self.game:
            raise Exception

        self.clocks = []
        self.contacts = []

        # Extract data from file
        self.personaldata = personaldata
        self.datafile = datafile
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

    async def on_message(self, message):
        # Prevents bot replying to itself
        if message.author == self.user:
            return

        # Prevents bot responding to regular messages
        if not message.content.startswith("."):
            return

        # Parse message
        content = message.content.lower().split(' ', 1)
        command = content[0]
        args = content[1] if len(content) > 1 else ''

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

        response = text_switch.get(command, None)(args)

        image_switch = {
            '.map': discord.File(f'{IMAGES}/map.jpg', 'map.jpg'),
            '.fuckmendle': discord.File(f'{IMAGES}/mendle.png', 'mendle.png'),
            '.fridge': discord.File(f'{IMAGES}/FRIDGE.jpg', 'fridge.jpg'),
            '.clones': discord.File(f'{IMAGES}/clones.png', 'clones.png')
        }

        image = image_switch.get(command, None)

        if not response and not image:
            response = self.game.handle(command, args)
            if not response:
                response = 'Invalid command. Type ".help" for a list of commands.'

        if response and not image:
            response = f'```{response}```'

        await message.channel.send(response, files=image)

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    def help(self, message):
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
    .ripsprawl1: Detailed deaths from the Sprawl1
    .ripsprawl2: Detailed deaths from Sprawl2 
    .ripapoc: Detailed deaths from Apoc World
    .rip: List all dead characters.
    .rememberlist: Displays rough numbers for specific moments. 
    .remember: Displays a message of a memorable moment.
    .refresh: Reloads the clock and contact data.
    .log <message>: Saves a message to the log file.
    .links: Displays a link to all the PBA games.
    
Game-specific Commands:
"""
        for command, description in self.game.commands.items():
            commands += f'\t{command}: {description}\n'

        commands.strip()
        return commands

    def links(self, message):
        msg = """
        **Apocalpyse World:** https://www.dropbox.com/sh/fmsh9kyaiplqhom/AACw1iLMQ7f53Q40FUnMjlz4a?dl=0
        **The Sprawl:** https://www.dropbox.com/sh/9fr35ivzbvfh06p/AACarsYBpNXxBpEUk_-fz_PXa?dl=0
        **Tremulas:** https://www.dropbox.com/sh/tbhk0w0zgihrf2h/AACtvyv9l5ruLBE6UG3XeGfba?dl=0
        **Dungeon World:** https://www.dropbox.com/sh/p61lutt9m6dfpa3/AACTvHhbJa7K1RIHFYVvJqIza?dl=0
        """
        msg = msg.replace("\t", "")
        return msg

    def printclocks(self, message):
        if not self.clocks:
            return 'No clocks have been added.'

        switch = {
            '1200': '□□□□ □□□□ □□□□ □ □ □',
            '1500': '■■■■ □□□□ □□□□ □ □ □',
            '1800': '■■■■ ■■■■ □□□□ □ □ □',
            '2100': '■■■■ ■■■■ ■■■■ □ □ □',
            '2200': '■■■■ ■■■■ ■■■■ ■ □ □',
            '2300': '■■■■ ■■■■ ■■■■ ■ ■ □',
            '0000': '■■■■ ■■■■ ■■■■ ■ ■ ■'
        }

        clocks = ''
        for clock in self.clocks:
            clocks += f'{clock.name}: {switch[clock.time]}\n'

        return clocks

    def printcontacts(self, message):
        if not self.contacts:
            return 'No contacts have been added.'

        contacts = ''
        for contact in self.contacts:
            contacts += f'{contact.name}: {contact.description}\n'


        return contacts

    def rememberlist(self, message):
        rememberindexes = """
        1-9: Christoff focused
        10-13: Laramy focused
        14-19: Seraph focused
        20: I missed a number..
        21-23:  Syntax Terror focused
        24-27: H4KKK3R focused
        28-32: Noor focused
        33-60: Reat of Sprawl campaign 1 (in order things happened after I stopped grouping by character.)
        61-73: Sprawl campaign 2, while Jayden(swarf) was still playing
        74-106: Sprawl 2 while Mercer was still alive.
        107-114: The last of Sprawl 2.
        115-134: First time playing Apoc world, what a mess that was, also lots of pvp.
        135-178: The last of Apoc world campaign 1, lots of weird stuff and overtrowing.
        179-206: Back to the Sprawl, oh how we missed the Sprawls writing. A one shot spanned over a couple of sessions.
        207-219: Apoc world, Tat and Cowboy.
        220-244: Jayden comes back and Tat dies.
        245: The sprawl and pissing on machines... 
        """
        rememberindexes = rememberindexes.replace("\t", "")
        return rememberindexes

    def roll(self, message):
        # Generate the roll
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2
        result = ''

        # Unique response based on roll
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
        # Find the clock to be deleted
        clock = self._getclock(name)

        if not clock:
            return f'Clock {name} not found.'

        self.clocks.remove(clock)

        # Update and refresh file
        self._savedata()
        print(f'Clock deleted from file: {name}')

        # Form message and send
        return f'Deleted clock {name}.'

    def increaseclock(self, name):
        # Find the clock to be increased
        clock = self._getclock(name)

        # Check if the clock was found
        if not clock:
            return f'Clock "{name}" not found.'

        clock.increase()

        # Update and refresh file
        self._savedata()
        print(f'Clock update reflected in file (INCREASE): ({clock.name} {clock.time})')

        # Form message and send
        return f'{clock.name} clock increased to {clock.time}.'

    def decreaseclock(self, name):
        clock = self._getclock(name)

        if not clock:
            return f'Clock "{name}" not found.'

        clock.decrease()

        self._savedata()

        return f'{clock.name} clock decreased to {clock.time}'

    def addcontact(self, args):
        # Get the contact name and description
        name = None
        description = None
        tokens = args.split('"', 2)
        if len(tokens) > 1:
            name = tokens[1]
            description = tokens[2].strip()
        else:
            tokens = args.split(' ', 1)
            name = tokens[0]
            description = tokens[1]

        if self._getcontact(name):
            return f'Contact "{name}" already added as a contact.'

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
        # Generates random number to get remember message from  events that have happened.
        min = 1
        max = 280
        member = random.randint(min, max)

        if index:  # If more values other than .remember
            number = int(index)  # converts stringArray  (['.remember' 'num']) to int
            if number >= min and number <= max:  # Ensures it will exist within the range of .remember
                member = number  # sets member to the number.

        tree = et.parse(self.personaldata)
        remember = tree.find('remember')

        memories = {}
        for memory in list(remember):
            memories[memory.get('index')] = memory.text

        msg = f"{memories[str(member)]}"

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
            data = pickle.loads(open(self.datafile, "rb").read())
            self.clocks = data["clocks"]
            self.contacts = data["contacts"]
            msg = 'Data has been refreshed.'
            print("Data extracted")
        except EOFError:
            print("No data in file.")
        except FileNotFoundError:
            print("No data file found.")

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

        #data = pickle.loads(open(filename, "rb").read())
        #clocks = data["clocks"]
        #contacts = data["contacts"]
        #print("File reloaded")


def main():
    # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--game', type=str, required=True, choices=['sprawl', 'apoc'])
    args = parser.parse_args()
    game = vars(args)['game']

    client = PBABot(game)
    client.run(TOKEN)


if __name__ == '__main__':
    main()