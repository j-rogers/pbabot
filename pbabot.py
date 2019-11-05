import discord  # version 0.16.12
import random
import pickle
import argparse
import xml.etree.ElementTree as et
from games import *


# requires python 3.6.8

# Updates and refreshes data file
def updateAndRefreshData(index, newData):
    global data
    data[index] = newData
    file = open(filename, "wb")
    file.write(pickle.dumps(data))
    file.close()

    data = pickle.loads(open(filename, "rb").read())
    clocks = data["clocks"]
    contacts = data["contacts"]
    print("File reloaded")


# Functions
def help(message):
    return """```Use \".command\" when using this bot.\n
.help: Displays this help message.
.roll: Rolls 2d6 dice.
.moves: Displays a list of basic moves.
.playbooks: Displays a list of playbooks.
.matrix: Displays a list of matrix-specific moves. [SPRAWL ONLY]
.custom: Displays a list of custom moves.
.clocks: Displays the current list of clocks.
.weapons: Displays a list of weapons and their profiles.
.addclock <clock name>: Adds a clock with a value of 1500.
.increaseclock <clock name>: Increases a clock by one segment.
.decreaseclock <clock name>: Decreases a clock by one segment.
.deleteclock <clock name>: Deletes the specified clock.
.contacts: Displays the current list of contacts.
.addcontact <contact name> <description>: Adds a new contact.
.deletecontact <contact name>: Deletes a contact.
.drugs: Displays a list of drugs
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
```"""


def invalid(message):
    return "```Invalid command. Type '.help' for a list of commands.```"


def showclocks(message):
    msg = "```"
    global clocks
    for clock in clocks:
        name = clock[0]
        value = clock[1]

        if value == "1200":
            msg += name + ": □□□□ □□□□ □□□□ □ □ □\n"
        elif value == "1500":
            msg += name + ": ■■■■ □□□□ □□□□ □ □ □\n"
        elif value == "1800":
            msg += name + ": ■■■■ ■■■■ □□□□ □ □ □\n"
        elif value == "2100":
            msg += name + ": ■■■■ ■■■■ ■■■■ □ □ □\n"
        elif value == "2200":
            msg += name + ": ■■■■ ■■■■ ■■■■ ■ □ □\n"
        elif value == "2300":
            msg += name + ": ■■■■ ■■■■ ■■■■ ■ ■ □\n"
        elif value == "0000":
            msg += name + ": ■■■■ ■■■■ ■■■■ ■ ■ ■\n"

    if msg == "```":
        msg += "No clocks have been added."

    msg += "```"

    return msg


def showcontacts(message):
    msg = "```"
    global contacts
    for contact in contacts:
        name = contact[0]
        desc = contact[1]
        msg += name + ": " + desc + "\n"

    if msg == "```":
        msg += "No contacts have been added."

    msg += "```"

    return msg


def f(message):
    msg = "```"

    tree = et.parse('data/personal')
    rip = tree.getroot().find('rip')

    ripMsg = message.split()
    if len(ripMsg) > 1: #specific message
        player = rip.find(ripMsg[1])
        print (player)
        if player:
            for character in list(player):
                msg += f"{character.get('name')}: {character.get('cause')}\n\n"
                
           
    else: #short list
        for player in list(rip):
            msg += f'{player.tag}: '
            for character in list(player):
                msg += f"{character.get('name')}, "
            msg += '\n'

    msg += "```"
    msg = msg.strip()
    return msg

def roll(message):
    # Generate the roll
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll = dice1 + dice2
    msg = ""

    # Unique response based on roll
    if roll == 1:
        msg = "```Throwbacks to when Martin's bot could roll a 1 from 2d6. Good times, not for you though, you rolled a 1.```"
    elif roll == 2:
        msg = "```I hope you have a lot of health cause this is gonna hurt. You rolled a 2.```"
    elif roll == 3:
        msg = "```The Thing is going to have fun with this, you rolled a 3.```"
    elif roll == 4:
        msg = "```You rolled the length of your penis, 4 inches.```"
    elif roll == 5:
        msg = "```Maybe you should have taken those drugs, you rolled a 5.```"
    elif roll == 6:
        msg = "```The RNG gods are displeased with you. You rolled a 6.```"
    elif roll == 7:
        msg = "```You know what, it could be worse. You rolled a 7.```"
    elif roll == 8:
        msg = "```Someones going to be sleeping with the fishes, is it going to be you or him with a roll of 8.```"
    elif roll == 9:
        msg = "```Almost hit that sweet spot. You rolled a 9.```"
    elif roll == 10:
        msg = "```Now we're talking, you rolled a 10.```"
    elif roll == 11:
        msg = "```You could fuck up someones day with this. You rolled an 11.```"
    elif roll == 12:
        msg = "```Okay, now THIS is epic. You rolled a 12.```"

    return msg


def remember(message):
    # Generates random number to get remember message from  events that have happened.
    min = 1
    max = 271
    member = random.randint(min, max)
    notRandom = message.split()  # puts message into a string array seperated by " "

    if len(notRandom) > 1:  # If more values other than .remember
        number = int(notRandom[1])  # converts stringArray  (['.remember' 'num']) to int
        if number >= min and number <= max:  # Ensures it will exist within the range of .remember
            member = number  # sets member to the number.

    tree = et.parse('data/personal')
    remember = tree.find('remember')

    memories = {}
    for memory in list(remember):
        memories[memory.get('index')] = memory.text

    msg = f"```{memories[str(member)]}```"

    return msg


def rememberlist(message):
    msg = """```
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
    ```"""
    msg = msg.replace("\t", "")
    return msg

def chess(message):
    msg = "**```THE\t  TECHSORCIST\n\tIS    THE\nCHESS\t\tMASTER!```**"
    return msg


def links(message):
    msg = """
    **Apocalpyse World:** https://www.dropbox.com/sh/fmsh9kyaiplqhom/AACw1iLMQ7f53Q40FUnMjlz4a?dl=0
    **The Sprawl:** https://www.dropbox.com/sh/9fr35ivzbvfh06p/AACarsYBpNXxBpEUk_-fz_PXa?dl=0
    **Tremulas:** https://www.dropbox.com/sh/tbhk0w0zgihrf2h/AACtvyv9l5ruLBE6UG3XeGfba?dl=0
    **Dungeon World:** https://www.dropbox.com/sh/p61lutt9m6dfpa3/AACTvHhbJa7K1RIHFYVvJqIza?dl=0
    """
    msg = msg.replace("\t", "")
    return msg


def answerphone(message):
    min = 1
    max = 1
    member = random.randint(min, max)
    notRandom = message.split()  # puts message into a string array seperated by " "

    if len(notRandom) > 1:  # If more values other than .remember
        number = int(notRandom[1])  # converts stringArray  (['.remember' 'num']) to int
        if number >= min and number <= max:  # Ensures it will exist within the range of .remember
            member = number  # sets member to the number.

    switch = {
        1: """```css
Welcome to the Wii Fit helpline how can I help you?```""",
    }

    return switch[member]


def addclock(message):
    # Get the clock name and assign it default value of 1200
    tokens = message.split(".addclock ")
    print(tokens)
    clock = (tokens[1], "1200")

    # Checks if clock has already been added
    for c in clocks:
        # Case insensitive
        name = c[0].lower()
        inName = tokens[1].lower()

        if name == inName:
            return "```Clock already exists.```"

    # Append to clocks list
    clocks.append(clock)

    # Update and refresh file
    updateAndRefreshData("clocks", clocks)
    print("Clock added to file: {" + tokens[1] + ", 1200}")

    # Form message and send
    return "```Clock added: " + tokens[1] + " at 1200.```"


def deleteclock(message):
    # Get the clock name
    tokens = message.split(".deleteclock ")
    name = tokens[1]

    # Find the clock to be deleted
    for clock in clocks:
        # Case insensitive
        clockName = clock[0].lower()
        inName = name.lower()

        if clockName == inName:
            clocks.remove(clock)

    # Update and refresh file
    updateAndRefreshData("clocks", clocks)
    print("Clock deleted from file: " + tokens[1])

    # Form message and send
    return "```Deleted clock " + name + ".```"


def increaseclock(message):
    # Get the clock name
    tokens = message.split(".increaseclock ")
    name = tokens[1]

    # Flag for catching incorrect input
    found = False

    # Find the clock to be increased
    updatedClock = ()
    for clock in clocks:
        # Case insensitive
        cName = clock[0].lower()
        inName = name.lower()

        if cName == inName:
            # Set flag
            found = True

            # Find the next value
            value = clock[1]
            if value == "1200":
                value = "1500"
            elif value == "1500":
                value = "1800"
            elif value == "1800":
                value = "2100"
            elif value == "2100":
                value = "2200"
            elif value == "2200":
                value = "2300"
            elif value == "2300":
                value = "0000"
            elif value == "0000":
                return "```Clock is already at midnight.```"

            # Create new tuple and replace previous one
            updatedClock = (clock[0], value)
            index = clocks.index(clock)
            clocks[index] = updatedClock

    # Check if the clock was found
    if not found:
        return "```Clock \"" + name + "\" not found.```"

    # Update and refresh file
    updateAndRefreshData("clocks", clocks)
    print("Clock update reflected in file (INCREASE): (" + updatedClock[0] + ", " + updatedClock[1] + ")")

    # Form message and send
    return "```" + updatedClock[0] + " clock increased to " + updatedClock[1] + ".```"


def decreaseclock(message):
    # Get the clock name
    tokens = message.split(".decreaseclock ")
    name = tokens[1]

    # Flag for if the clock was found
    found = False

    # Find the clock to be decreased
    updatedClock = ()
    for clock in clocks:
        # Case insensitive
        cName = clock[0].lower()
        inName = name.lower()

        if cName == inName:
            # Set flag
            found = True

            # Find the previous value
            value = clock[1]
            if value == "0000":
                value = "2300"
            elif value == "2300":
                value = "2200"
            elif value == "2200":
                value = "2100"
            elif value == "2100":
                value = "1800"
            elif value == "1800":
                value = "1500"
            elif value == "1500":
                value = "1200"
            elif value == "1200":
                return "```Clock is already at 1200.```"

            # Create new tuple and replace previous one
            updatedClock = (clock[0], value)
            print(updatedClock)
            index = clocks.index(clock)
            clocks[index] = updatedClock

    # Check if the clock was found
    if not found:
        return "```Clock \"" + name + "\" not found.```"

    # Update and refresh file
    updateAndRefreshData("clocks", clocks)
    print("Clock update reflected in file (DECREASE): (" + updatedClock[0] + ", " + updatedClock[1] + ")")

    # Form message and send
    return "```" + updatedClock[0] + " clock decreased to " + updatedClock[1] + ".```"


def addcontact(message):
    # Get the contact name and description
    tokens = message.split()
    description = ""
    for i in range(2, len(tokens)):
        description += tokens[i] + " "
    contact = (tokens[1], description)

    # Checks if clock has already been added
    for c in contacts:
        # Case insensitive
        name = c[0].lower()
        inName = tokens[1].lower()

        if name == inName:
            return "```Contact already exists.```"

    # Append to contacts list
    contacts.append(contact)

    # Update and refresh file
    updateAndRefreshData("contacts", contacts)
    print("Contact added to file: {" + tokens[1] + ", " + description + "}")

    # Form message and send
    return "```Contact added: " + tokens[1] + ".```"


def deletecontact(message):
    # Get the clock name
    tokens = message.split()
    name = tokens[1]

    # Find the clock to be deleted
    for c in contacts:
        # Case insensitive
        cName = c[0].lower()
        inName = name.lower()

        if cName == inName:
            contacts.remove(c)

    # Update and refresh file
    updateAndRefreshData("contacts", contacts)
    print("Contact deleted from file: " + tokens[1])

    # Form message and send
    return "```Deleted contact " + name + ".```"


def refresh(message):
    msg = "```"

    try:
        data = pickle.loads(open(filename, "rb").read())
        clocks = data["clocks"]
        contacts = data["contacts"]
        msg += "Data has been refreshed."
        print("Data extracted")
    except EOFError:
        print("No data in file.")
    except FileNotFoundError:
        print("No data file found.")

    msg += "```"

    return msg


def log(message):
    # Get log message from message
    tokens = message.split(".log ")
    log = tokens[1]

    # Write to the file
    file = open("log.txt", "a")
    file.write(log + "\n")
    file.close()
    print("Log saved: \"" + log + "\"")

    # Form and send message
    return "```Log saved.```"

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--game', type=str, required=True, choices=['sprawl', 'apoc'])
args = parser.parse_args()
game = vars(args)['game']

# API Token
TOKEN = open("token.txt", 'r').read()

# Extract data from file
filename = "data.pickle"
clocks = []
contacts = []
data = {"clocks": clocks, "contacts": contacts}
try:
    data = pickle.loads(open(filename, "rb").read())
    clocks = data["clocks"]
    contacts = data["contacts"]
    print("Data extracted")
except EOFError:
    print("No data in file.")
except FileNotFoundError:
    print("No data file found.")

client = discord.Client()

# Discord client functions
@client.event
async def on_message(message):
    msg = ""

    # Prevents bot replying to itself
    if message.author == client.user:
        return

    # Prevents bot responding to regular messages
    if not message.content.startswith("."):
        return

    # determine which game is being played
    if game == 'sprawl':
        msg = sprawl.handle(message)
    elif game == 'apoc':
        msg = apoc.handle(message)

    messageString = message.content
    messageString = messageString.lower()

    switch = {
        # Listing commands
        '.help': help,
        '.links': links,
        '.clocks': showclocks,
        '.contacts': showcontacts,
        '.rememberlist': rememberlist,
        '.answerphone': answerphone,
        # Functional commands
        '.roll': roll,
        '.dice': roll,
        '.addclock': addclock,
        '.deleteclock': deleteclock,
        '.increaseclock': increaseclock,
        '.decreaseclock': decreaseclock,
        '.addcontact': addcontact,
        '.deletecontact': deletecontact,
        # Miscellaneous commands
        '.rip': f,
        '.f': f,
        '.remember': remember,
        # Dev commands
        '.refresh': refresh,
        '.log': log,
        '.chess':chess,
    }
    check = False
    if msg != "":
        check = True
    # print (msg)
    if messageString in switch:
        msg = switch[messageString](messageString)
        check = True
    elif check == False:
        for case in switch:
            if case in messageString:
                msg = switch[case](messageString)

    if not msg: msg = invalid(messageString)

    # Sends the map
    if messageString == ".map":
        await client.send_file(message.channel, "images/map.jpg")

    elif messageString == ".fuckmendle":
        await client.send_file(message.channel, "images/mendle.png")
    elif messageString == ".fridge":
        await client.send_file(message.channel, "images/FRIDGE.jpg")
    elif messageString == ".clones":
        await client.send_file(message.channel, "images/clones.png")

    elif messageString != ".map" and messageString != ".fuckmendle" and messageString != ".factorymap":
        await client.send_message(message.channel, msg.format(message))
    else:
        pass

# CONSOLE LOGGING
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

client.run(TOKEN)