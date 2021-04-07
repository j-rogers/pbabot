"""PBABot

Powered By the Apocolypse (PBA) is a engine for playing tabletop roleplaying games such as The Sprawl and Apocolype
World. Each PBA game has features that are common between them, such as the use of basic moves, playbooks, rolling
2d6, clocks, contacts, etc. To make playing PBA games online (specifically over Discord) easier, this bot has been
created that handles the common features of PBA games. Specific game features can be easily added by creating a
class and giving it the required functionality as outlined in the games module.

TODO: Clean up game extensions

Currently supported PBA games:
    The Sprawl

Author: Josh Rogers (2021)
Github: https://github.com/j-rogers/pbabot
Version: 3.0
"""
import discord
from discord.ext import commands
import pickle
import random
import argparse
import inspect
from pbabot.games import Game
from pbabot.util import Clock, Contact
import pbabot.games

# API Token
TOKEN = open('token.txt', 'r').read()

# Data files
DATA_FILE = 'data/data.pickle'

# Image folder
IMAGES = 'images'


class ClockCommands(commands.Cog, name='Clock Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clocks')
    async def print_clocks(self, ctx):
        """Displays the current list of clocks. If the private_clocks property is set then only the MC can view the
        clocks"""
        if self.bot.private_clocks and self.bot.mc != hash(ctx.author):
            await ctx.send('```You are not the MC. Increasing all clocks to 0000 (not really).```')
            return

        # Check that there are clocks
        if not self.bot.clocks:
            await ctx.send('```No clocks have been added```')
            return

        await ctx.send('```'+'\n'.join([str(clock) for clock in self.bot.clocks])+'```')

    @commands.command(name='addclock', aliases=['clock', 'newclock'])
    async def add_clock(self, ctx, *, clock_name):
        """Adds a clock of the given name at 1200"""
        # Check private clock and MC permissions
        if self.bot.private_clocks and self.bot.mc != hash(ctx.author):
            await ctx.send('```You are not the MC. Cheeky.```')
            return

        # Checks if clock has already been added
        try:
            clock = [c for c in self.bot.clocks if c.name.lower() == clock_name.lower()].pop()
        except IndexError:
            # Append to clocks list
            self.bot.clocks.append(Clock(clock_name))

            # Update and refresh file
            self.bot.save_data()

            # Form message and send
            await ctx.send(f'```{clock_name} clock added at 1200.```')
        else:
            await ctx.send(f'```Clock "{clock.name}" has already been added.```')

    @commands.command(name='deleteclock', aliases=['removeclock'],)
    async def delete_clock(self, ctx, *, clock_name):
        """Deletes the clock with specified name"""
        if self.bot.private_clocks and self.bot.mc != hash(ctx.author):
            await ctx.send('```You are not the MC. Naughty.```')
            return

        # Find the clock to be deleted
        try:
            clock = [c for c in self.bot.clocks if c.name.lower() == clock_name.lower()].pop()
        except IndexError:
            await ctx.send(f'```Clock "{clock_name}" not found.```')
        else:
            # Delete clock
            self.bot.clocks.remove(clock)

            # Update and refresh file
            self.bot.save_data()

            # Form message and send
            await ctx.send(f'```Deleted {clock.name} clock.```')

    @commands.command(name='increaseclock')
    async def increase_clock(self, ctx, *, clock_name):
        """Increases the clock of specified name by one segment"""
        if self.bot.private_clocks and self.bot.mc != hash(ctx.author):
            await ctx.send('```You are not the MC. I\'m going to dob on you.```')
            return

        # Find the clock to be increased
        try:
            clock = [c for c in self.bot.clocks if c.name.lower() == clock_name.lower()].pop()
        except IndexError:
            await ctx.send(f'```Clock "{clock_name}" not found.```')
        else:
            # Increase clock
            res = clock.increase()

            # Update and refresh file
            self.bot.save_data()

            # Form message and send
            await ctx.send(f'```{res}```' if res else f'```{clock.name} clock increased to {clock.time}.```')

    @commands.command(name='decreaseclock')
    async def decrease_clock(self, ctx, *, clock_name):
        """Decreases the clock of specified name by one segment"""
        if self.bot.private_clocks and self.bot.mc != hash(ctx.author):
            await ctx.send('```You are not the MC. -1 ongoing.```')
            return

        # Find clock

        try:
            clock = [c for c in self.bot.clocks if c.name.lower() == clock_name.lower()].pop()
        except IndexError:
            await ctx.send(f'```Clock "{clock_name}" not found.```')
        else:
            # Decrease clock
            res = clock.decrease()

            # Update and save data
            self.bot.save_data()

            await ctx.send(f'```{res}```' if res else f'```{clock.name} clock decreased to {clock.time}.```')

    @commands.command(name='resetclock')
    async def reset_clock(self, ctx, *, clock_name):
        """Reset a clock of specified name to 1200"""
        if self.bot.private_clocks and self.bot.mc != hash(ctx.author):
            await ctx.send('```You are not the MC. The Thing has been alerted to your position.```')
            return

        try:
            clock = [c for c in self.bot.clocks if c.name.lower() == clock_name.lower()].pop()
        except IndexError:
            await ctx.send(f'```Clock "{clock_name}" not found.```')
        else:
            # Reset the clock
            clock.time = '1200'

            # Update and save data
            self.bot.save_data()

            await ctx.send(f'```{clock.name} clock reset to 1200.```')


class ContactCommands(commands.Cog, name='Contact Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='contacts')
    async def print_contacts(self, ctx):
        """Displays the current list of contacts"""
        # Check there are contacts
        if not self.bot.contacts:
            await ctx.send('```No contacts have been added.```')
            return

        await ctx.send('```'+'\n'.join([str(contact) for contact in self.bot.contacts])+'```')

    @commands.command(name='addcontact', aliases=['newcontact'], usage='"<contact_name>" <contact_description>')
    async def add_contact(self, ctx, *, args):
        """Adds a contact with specified information"""
        # Get the contact name and description
        try:
            a, name, description = args.split('"', 2)
        except ValueError:
            await ctx.send('```You must surround the contact\'s name in double quotes.```')
        else:
            description = description.strip(' "')

            # Check if contact already exists
            try:
                contact = [c for c in self.bot.contacts if c.name.lower() == name.lower()].pop()
            except IndexError:
                # Add contact and save data
                self.bot.contacts.append(Contact(name, description))
                self.bot.save_data()

                await ctx.send(f'```Contact added: {name}.```')
            else:
                await ctx.send(f'```Contact "{contact.name}" already added as a contact.```')

    @commands.command(name='deletecontact', aliases=['removecontact'])
    async def delete_contact(self, ctx, *, contact_name):
        """Deletes the given contact"""
        try:
            contact = [c for c in self.bot.contacts if c.name.lower() == contact_name.strip('"').lower()].pop()
        except IndexError:
            await ctx.send(f'```Contact {contact_name} not found.```')
        else:
            self.bot.contacts.remove(contact)
            self.bot.save_data()

            await ctx.send(f'```Deleted contact {contact.name}```')


class FunctionalCommands(commands.Cog, name='Functional Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll', aliases=['dice'])
    async def roll(self, ctx, modifier=None):
        """Rolls 2d6 dice and applies the given +/- modifier"""
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

        await ctx.send(f'```{result}```')

    @commands.command(name='image', enabled=False)
    async def get_image(self, ctx, image_name):
        """[TEMPORARILY DISABLED] Displays the specified image."""
        # TODO: fix the local file inclusion vuln before adding this
        image = None
        if image_name:
            try:
                image = discord.File(f'{IMAGES}/{image_name}', f'{image_name}')
            except FileNotFoundError:
                image = discord.File(f'{IMAGES}/no_map.jpg', 'no_map.jpg')
        else:
            image = discord.File(f'{IMAGES}/no_map.jpg', 'no_map.jpg')

        await ctx.send(file=image)

    @commands.command(name='map')
    async def get_map(self, ctx):
        """Displays the current map"""
        image = None
        try:
            image = discord.File('images/map.jpg', 'map.jpg')
        except FileNotFoundError:
            image = discord.File('images/no_map.jpg', 'no_map.jpg')

        await ctx.send(file=image)

    @commands.command(name='log')
    async def save_log_message(self, ctx, *, message):
        """Saves a message to the log file"""
        with open('log.txt', 'a') as file:
            file.write(f'{message}\n')
            print(f'Log saved: {message}')

        await ctx.send('```Log saved.```')

    @commands.command(name='set')
    async def set_property(self, ctx, property, value=None):
        """Sets a bot property. Current properties: game, private_clocks, mc."""
        if property.lower() == 'game':
            if value.lower() in self.bot.game:
                self.bot.game = self.bot.GAMES[value.lower()](self.bot)
                await ctx.send(f'```Now playing {value}.```')
            else:
                await ctx.send(f'```The game {value} was not found.```')
        elif property.lower() == 'private_clocks':
            if value.lower() == 'true':
                self.bot.private_clocks = True
                await ctx.send('```Property private_clocks set to true.```')
            elif value.lower() == 'false':
                self.bot.private_clocks = False
                await ctx.send('```Property private_clocks set to false.```')
            else:
                await ctx.send('```Invalid value given, either true or false.```')
        elif property.lower() == 'mc':
            if value and value == 'none':
                self.bot.mc = None
                await ctx.send('```MC has been cleared.```')
            elif not value:
                self.bot.mc = hash(ctx.author)
                print(f'MC has been set to {hash(ctx.author)}.')
                await ctx.send('```MC has been set.```')
        else:
            await ctx.send('```Invalid property. Properties are game, private_clocks, mc.```')


class MiscCommands(commands.Cog, name='Miscellaneous Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='links')
    async def print_links(self, ctx):
        """Displays links to all PBA games"""
        links = """**Apocalpyse World:** https://www.dropbox.com/sh/fmsh9kyaiplqhom/AACw1iLMQ7f53Q40FUnMjlz4a?dl=0
**The Sprawl:** https://www.dropbox.com/sh/9fr35ivzbvfh06p/AACarsYBpNXxBpEUk_-fz_PXa?dl=0
**Tremulas:** https://www.dropbox.com/sh/tbhk0w0zgihrf2h/AACtvyv9l5ruLBE6UG3XeGfba?dl=0
**Dungeon World:** https://www.dropbox.com/sh/p61lutt9m6dfpa3/AACTvHhbJa7K1RIHFYVvJqIza?dl=0"""
        await ctx.send(links)

    @commands.command(name='rip', aliases=['f'])
    async def print_dead_characters(self, ctx, *, player=None):
        """Displays a list of dead characters (in total or for the given player)"""
        death = ''
        if player in self.bot.dead_characters:
            for character, description in self.bot.dead_characters[player].items():
                death += f'{character}: {description}'
        else:
            for player, characters in self.bot.dead_characters.items():
                death += f'{player}: '
                death += ', '.join(characters.keys()) + '\n'

        if not death:
            death = '```No dead characters.```'

        await ctx.send(f'```{death}```')

    @commands.command(name='kill', usage='"<player>" "<character>" <description>')
    async def kill_character(self, ctx, *, args):
        """Add a dead character with a description of how they died"""
        try:
            player, character, description = [arg.strip(' "') for arg in args.split('"', 4) if arg.strip()]
        except ValueError:
            await ctx.send('```Please surround player and character names in double quotes.```')
        else:
            if player not in self.bot.dead_characters:
                self.bot.dead_characters[player] = {character: description}
            else:
                self.bot.dead_characters[player][character] = description

            self.bot.save_data()

            await ctx.send(f'```{player}\'s character {character} was killed: {description}.```')

    @commands.command(name='remember', usage='[when <memory>]|[<index>]')
    async def remember_memory(self, ctx, *, args=None):
        """Displays a message of a memorable moment, or add a new memory."""
        if not args:
            args = ''
        if 'when' in args.split(' ', 1)[0].lower():
            self.bot.memories.append(args.split(' ', 1)[1])
            self.bot.save_data()
            await ctx.send(f'```Memory added at index {len(self.bot.memories) - 1}```')
        else:
            try:
                index = int(args)
            except ValueError:
                max = len(self.bot.memories)
                if not max:
                    await ctx.send('```No memories have been added.```')
                    return
                index = random.randint(0, max - 1)

            try:
                memory = self.bot.memories[index]
            except IndexError:
                await ctx.send(f'```No memory at index {index}.```')
            else:
                await ctx.send(f'```{index}: {memory}```' if memory else f'```No memory found at index {index}.```')

    @commands.command(name='forget')
    async def forget_memory(self, ctx, index):
        """Forgets the memory at given index"""
        try:
            i = int(index)
        except ValueError:
            await ctx.send(f'```Invalid index given: {index} (should be an integer).```')
        else:
            try:
                memory = self.bot.memories.pop(i)
                self.bot.save_data()
            except IndexError:
                await ctx.send(f'```No memory at index {i}.```')
            else:
                await ctx.send(f'```Memory deleted at index {i}: "{memory}".```')


class HiddenCommands(commands.Cog, name='Hidden Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='chess', hidden=True)
    async def chess(self, ctx):
        """Who is the chess master?"""
        await ctx.send('**THE\t  TECHSORCIST\n\tIS    THE\nCHESS\t\tMASTER!**')

    @commands.command(name='answerphone', hidden=True)
    async def answer_phone(self, ctx, index=None):
        """Wii Fit Helpline"""
        min = 1
        max = 1
        member = random.randint(min, max)

        if index:  # If more values other than .remember
            number = int(index)  # converts stringArray  (['.remember' 'num']) to int
            if min <= number <= max:  # Ensures it will exist within the range of .remember
                member = number  # sets member to the number.

        switch = {
            1: 'css\nWelcome to the Wii Fit helpline how can I help you?',
        }

        await ctx.send(f'```{switch[member]}```')

    @commands.command(name='quote', hidden=True)
    async def duke_nukem_quote(self, ctx):
        quotes = [
            "You're wrong, Proton breath. I'll be done with you and still have time to watch Oprah!",
            "I'm back!",
            "AAhhh... much better!",
            "Bitchin'!",
            "Blow it out your ass!",
            "Boooorn tooo beee wiiiiiiild...",
            "Come get some!",
            "Come on!",
            "Damn....",
            "Damn!",
            "Damn it.",
            "Damn, I'm good!",
            "Damn... I'm looking good!",
            "Damn, those alien bastards are gonna pay for shooting up my ride.",
            "Damn, that was annoying!",
            "Damn, that's the second time those alien bastards shot up my ride!",
            "Damn, you're ugly.",
            "Die, you son of a bitch!",
            "Eat shit and die.",
            "Get that crap outta here!",
            "Get back to work, you slacker!",
            "Go ahead, make my day.",
            "Gonna rip 'em a new one.",
            "Groovy!",
            "Hail to the king, baby!",
            "Heh, heh, heh... what a mess!",
            "HHHHHHHHHHHEEEEEEEEEEAAAAAAAAAAAHHHHHHHHHHHH!!!!!!!",
            "Hmm, don't have time to play with myself.",
            "Hmm, that's one \"Doomed\" Space Marine.",
            "Holy cow!",
            "Holy shit!",
            "I'll rip your head off and shit down your neck.",
            "I'm Duke Nukem - and I'm coming to get the rest of you alien bastards!",
            "I'm gonna get medieval on your asses!",
            "I'm gonna kick your ass, bitch!",
            "I'm gonna put this smack dab on your ass!",
            "I ain't afraid of no quake!",
            "I should have known those alien maggots booby-trapped this sub.",
            "It's time to kick ass and chew bubble gum... and I'm all outta gum.",
            "It's down to you and me, you one-eyed freak!",
            "It's time to abort your whole freaking species!",
            "Let God sort 'em out!",
            "Let's rock!",
            "Looks like cleanup on aisle four.",
            "Lucky son of a bitch.",
            "Mess with the best, you will die like the rest",
            "My boot, your face; the perfect couple.",
            "No way I'm eating this shit!",
            "Nobody steals our chicks... and lives!",
            "Now this is a force to be reckoned with!",
            "Oh...your ass is grass and I've got the weed-whacker.",
            "Ooh, I needed that!",
            "Ooh, that's gotta hurt.",
            "Piece of Cake.",
            "See you in Hell!",
            "Shake it, baby!",
            "Shit happens.",
            "Sometimes I even amaze myself.",
            "Staying alive, staying alive, la.",
            "Suck it down!",
            "Terminated!",
            "This really pisses me off!",
            "This is KTIT, K-Tit! Playing the breast- uhh, the best tunes in town.",
            "That's gonna leave a mark!",
            "We meet again, Doctor Jones!",
            "What? There's only one of you?",
            "What are you waitin' for? Christmas?",
            "What are you? Some bottom-feeding, scum-sucking algae eater?",
            "Where is it?",
            "Who wants some?",
            "Why so serious, Sam?",
            "Wohoo!",
            "Yeah, piece of cake!",
            "Yippie ka-yay, motherfucker!",
            "You guys suck!",
            "You're an inspiration for birth control.",
            "Your face, your ass - what's the difference?",
            "You wanna dance?",
            "COME GET SOME!!!",
            "Dying ain't much of a living, boy.",
            "Friends, Romans, countrymen, lend me your chicks.",
            "Have you seen my rubber...duckie?",
            "Hello? McFly?",
            "Hey! Get your ass out of here and bring me back my chicks!",
            "I'll blow you a new hole!",
            "I'm God's gift to women!",
            "I love the smell of bacon in the morning.",
            "I make this look good.",
            "Lara, is that you?",
            "Looks like it's TIME TO KILL!",
            "My home away from home!",
            "I prefer a good cigar, and a bad woman!",
            "Gimme a Jack and Coke anyday!",
            "Suck my boom stick!",
            "The bigger they are, the more they bleed!",
            "…and I thought cigars smelled bad!",
            "There's a new sheriff in town.",
            "You'll make a great belt.",
            "Little pig, little pig, let me in. Or I'll huff and I'll puff and I'll kick your ass in!",
            "Rubba-dub-dub. Get out of the tub.",
            "It's locked, and I'm an ass kicker not a safe cracker.",
            "Mmmm! Who wants bacon and eggs?",
            "So much for the new boots...Has anyone seen Mr. Hankey?",
            "Is it true that Roman girls have Roman hands?",
            "Lizard skin makes great boots.",
            "Not in this lifetime!",
            "Where's Doc Brown when ya need him?",
            "Who wants some?",
            "Hey... what can I say?",
            "Come on!",
            "All aboard!",
            "Let's settle this once and for all!",
            "I'll kick you in the \"nuts\"!",
            "Oh Yeah!",
            "Ahhhhhhhh!",
            "Shake it, baby!",
            "I'm an ass kicker not a rock digger.",
            "Die, you overgrown winged lizard from Hell!",
            "Shut your hole!",
            "What are you waiting for, Christmas?",
            "IT'S ASS-KICKING TIME!",
            "Mmm, it's good to be king!",
            "Blow it out your ass!",
            "Your face, Your ass what's the difference?",
            "Don't worry about it, saving chicks is what I'm all about!",
            "I ain't got time to bleed!",
            "Who the hell are you? My evil twin?",
            "Alien boys, there's a new sheriff in town.",
            "I don't die that easy boys. Come on time for a jail break.... by balls.",
            "I'm an ass kicker, not an aviator.",
            "It ain't no bike, but it sure beats the hell outta walking.",
            "Squeal piggy ! Squeal shove it in here !",
            "Oh boy, it's clobberin' time!",
            "Eh... Just a flesh wound.",
            "nuts roasting... as I open fire",
            "Ahhh, smell those traffic fumes. And no damn aliens! Time for some R & R!",
            "Hey kids you remember i'm a professional, don't try this at home!",
            "What the fuck is goin' on here?!",
            "This won't buuuudge.",
            "Looks like the crap has hit the fan.",
            "Time for the shit to hit the fan",
            "It ain't no bike but it sure beats the hell out of walking",
            "Well, enough talk then. Come get some! Oh, Silverback, one more thing. I'm gonna enjoy pissin' on your dead body!",
            "Welcome to \"Cool's-Ville\", Population: Me.",
            "I'm your worst nightmare, you uninvited alien scum-sucker! And right now you're all that stands between me and a planet full of babes - so get ready to bend over and kiss your ass goodbye!",
            "I'm climbing a ladder........to heaven.",
            "Suck my dick you little alien fucks!",
            "That hurt you more than it hurt me.",
            "Damn you're ugly!",
            "Bug off!",
            "You guys suck!",
            "The Bigger they are the harder they fall",
            "New York! It's my kind of town. // If I can kill 'em here...I can kill 'em anywhere!",
            "Aaah, I love the smell of sewers in the morning. I bet Morphix is hiding under a turd somewhere.",
            "Ahh, something smells rotten around here.",
            "Ahh, that’s better!",
            "All aboard the Midtown Express... to hell!",
            "You must be 18 or older to ride.",
            "Babes, bullets, bombs. Damn - I love this job!",
            "Batteries not included!",
            "Bingo, the motherload! Sorry Morphix, I'm gonna have to flash your G.L.O.P.P. factory!",
            "Call me now, for your free whipping!",
            "Come on out, Morphix. There's only two ways this can end, and in both of them... you die!",
            "Confucius say... Die!",
            "Crouching mutant, hidden pipebomb!",
            "Dance for me, baby!",
            "Death before Disco!",
            "Die, bitch!",
            "Don't get your panties all in a bunch.",
            "Don't worry girls, there's plenty of Duke to go around.",
            "[beep, beep, beep] The number you have reached: 9-1-1 has been changed to a non-published number.",
            "End of the line - last stop: Total destruction!",
            "Get ready for big trouble in little China. Duke style! Morphix, I'm right on your heels!",
            "Gotta find the exit now.",
            "Guns don't kill mutants, I kill mutants!",
            "Half man, half animal, all dead!",
            "Hey, careful with those things!",
            "Hey, I know this classy place where you put quarters into the bed and...",
            "Hmm, that stuff doesn’t look bio-degradable.",
            "Hmm, so there is life after death...",
            "Hmm, no lights... must be part of Morphix's energy conservation plan.",
            "Hmm... the other white meat.",
            "Hmm, wonder what this does.",
            "I always said, if there was a way to go, it'd have something to do with women, whips, and oil... Let's rock.",
            "I am the king of the world, baby!",
            "Ooh, I better get the hell out of here!",
            "I'm an equal opportunity ass kicker!",
            "I'm not gonna fight you, I'm gonna kick your ass!",
            "I can do this all day...",
            "I could use some new boots.",
            "I don't do windows.",
            "I did not have sexual relations with that robot.",
            "I go where I please, and I please where I go.",
            "I hate pigs!",
            "I kill bugs... Dead!",
            "I like big guns, and I cannot lie.",
            "I love the smell of bird crap in the morning.",
            "I see dead people.",
            "I want a damn refund! This cruise sucks!",
            "It's a good day to die!",
            "It's clobbering time!",
            "It's my way or... Hell, it's my way!",
            "It's gear stripping time!",
            "Let's rock!",
            "Life is like a box of ammo.",
            "Looks like I'm on Candid Camera",
            "Looks like Morphix puts workers' safety first... Right after everything else",
            "Looks like your hardware's gone a little soft, Morphix!",
            "Looks like you've gotten ahead of yourself there.",
            "Looks like we're about to reach our final destination.",
            "Makin'... bacon!",
            "Mimic that!",
            "Morphix and his G.L.O.P.P. rig are going down faster than Enron. Let's rock.",
            "Mother Fucking keycards!",
            "My gun's bigger than yours.",
            "No goin' back now!",
            "No token? No ride!",
            "No disassembly required.",
            "Now I'm really pissed off!",
            "Oops, I did it again!",
            "Ooh, that's gonna leave a mark.",
            "Pigs will fly before Morphix rules the world on my watch!",
            "Pucker up, buttercup!",
            "Rest in pieces!",
            "Say hello to my little friend!",
            "Sewer scum!",
            "Should've stayed in the swamp!",
            "So many babes, so little time.",
            "So much for the rat pack!",
            "So, who wants to dance?",
            "Someone's gonna pay for making me find these friggin' key cards!",
            "Something tells me this won't pass any safety inspections...",
            "Sometimes I even amaze myself.",
            "Son of a bitch!",
            "Sorry, honey, I've got some ass kickin' to do first!",
            "Squeal like a pig!",
            "Stop eyeballin' me!",
            "Surprise, surprise, I need a keycard.",
            "Take that, you dirty rat!",
            "The deeper I go, the worse this city smells!",
            "This is why I have games named after me!",
            "Time for mutation-mutilation!",
            "Time for a reboot!",
            "Time to deliver max pain on the A-Train... now where'd I put that subway token?",
            "Time to de-worm the Big Apple!",
            "This'll be a barrel of laughs!",
            "This room is bugged.",
            "This train is going nowhere fast.",
            "This thing’s a train wreck waiting to happen.",
            "The queen must be around here somewhere… That bitch is gonna pay!",
            "What a pussy!",
            "What am I? A frog?",
            "What the hell does Morphix need all this G.L.O.P.P. for?",
            "Where is a light switch when you need one?",
            "Who wants to glow in the dark?",
            "You’re beautiful when you dying.",
            "You're goin' down faster than the XFL!",
            "You're starting to bug me.",
            "You are the missing link. Goodbye.",
            "Your kung-fu is through!",
            "Space, the final frontier. These are the voyages of Duke Nukem. My continuing mission: to explore strange new babes, to seek out new aliens and kick their asses.",
            "Jeez… You’d think Morphix could afford a few light bulbs?",
            "I oughta break a broomhandle off in your ass.",
            "Quit wasting my time.",
        ]
        index = random.randint(0, len(quotes)-1)

        await ctx.send(f'```{quotes[index]}```')


class PBABot(commands.Bot):
    """PBABot

    Inherits the discord commands.Bot so it can receive commands and respond to them appropriately. Clock, contact,
    memory, and dead character data is saved within a pickled file. There are also a number of bot properties that can
    be configured to change bot behaviour.

    Attributes:
        Current bot properties:
            game -> pbabot.games.Game: Currently game data to load.
            private_clocks -> Boolean: Flag to determine if clocks should only be printed to the current MC
            mc -> Integer: A hash of the Discord user who is the current MC
        Data attributes:
            data_file -> String: Data file containing data
            clocks -> List: The clocks currently being used
            contacts -> List: The contacts currently being used
            memories -> List: List of memorable moments
            dead_characters -> Dict: Dictionary of player's dead characters and how they died
    """
    GAMES = {}

    def __init__(self, game: str, data_file: str = DATA_FILE):
        """Init"""
        # Set command prefix
        super().__init__(command_prefix='.')

        # Get all games
        for name, obj in inspect.getmembers(pbabot.games, inspect.ismodule):
            if name != 'base':
                for n, o in inspect.getmembers(inspect.getmodule(obj), inspect.isclass):
                    if n not in ('Move', 'Game'):
                        self.GAMES[n.lower()] = o

        # Bot properties
        self.game = self.GAMES[game](self) if game else Game(self)
        self.private_clocks = False
        self.mc = None

        # Add commands
        self.add_cog(ClockCommands(self))
        self.add_cog(ContactCommands(self))
        self.add_cog(FunctionalCommands(self))
        self.add_cog(MiscCommands(self))
        self.add_cog(HiddenCommands(self))
        self.add_cog(self.game)

        # Extract data from file
        self.memories = []
        self.dead_characters = {}
        self.clocks = []
        self.contacts = []
        self.data_file = data_file
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

    async def on_message(self, message):
        """On message event callback - currently used so previous Game functionality works"""
        await self.process_commands(message)
        # Prevents bot replying to itself
        if message.author == self.user:
            return

        # Prevents bot responding to regular messages
        if not message.content.startswith('.'):
            return
        content = message.content.split(' ', 1)
        command = content[0].lower()
        args = content[1] if len(content) > 1 else ''
        try:
            response = self.game.handle(command, args)
            if response:
                await message.channel.send(f'```{response}```')
            return
        except NotImplementedError:
            await message.channel.send('```No game has been loaded. Use .set game <game>```')
        except discord.errors.HTTPException:
            pass

    async def on_ready(self):
        """Event callback for when discord.Client is ready"""
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def save_data(self):
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

    pbabot = PBABot(game)
    pbabot.run(TOKEN)


if __name__ == '__main__':
    main()
