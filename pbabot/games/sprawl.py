import random
import pickle

from . import Game


class Sprawl(Game):
    def __init__(self):
        super().__init__()
        self.datafile = 'data/sprawl_data.pickle'
        self.commands = {
            '.matrix': 'Displays a list of matrix-specific moves.',
            '.custom': 'Displays a list of custom moves.',
            '.weapons': 'Displays a list of weapons and their profiles.',
            '.drugs': 'Displays a list of drugs.'
        }
        self._loaddata()

    def handle(self, command, args):
        # Handle game-specific moves
        if command == '.fuckmeup':
            return self._fuckmeup(args)
        elif command == '.matrix':
            return self._matrix()

        # Check matrix moves
        move = self._getmove(command, index='matrix')
        if move:
            return move.fulldescription

        # If not a game-specific move, check if playbook move
        if command in ('.driver', '.fixer', '.hacker', '.hunter', '.infiltrator', '.killer', '.pusher', '.reporter', '.soldier', '.tech'):
            return self._getplaybook(command[1:], args)

        # Finally, check if basic move, otherwise return None
        move = self._getmove(command)
        return move.description if move else None

    def _fuckmeup(self, damage):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        modifier = 0
        if damage:
            modifier = int(damage)
        roll = dice1 + dice2 + modifier

        if roll >= 10:
            harm = self._getmove('Harm 10', name=True)
            return f'Oh you fucked up now, you rolled a {roll}. {harm.description}'
        elif 7 <= roll <= 9:
            harm = self._getmove('Harm 7', name=True)
            return f'You\'re going to have to suck off the MC on this one, you rolled a {roll}. {harm.description}'
        else:
            return f'You rolled {roll}. You\'re gucci flip flops fam *dabs* haha yeet :3'

    def _matrix(self):
        matrixmoves = 'Use the following commands to find detailed information about each move.\n'
        for move in self.data['matrix']:
            matrixmoves += f'\n\t{move.print()}'

        return matrixmoves





def handle(message):
    messageString = message.content
    response = ''

    '''
	Listing
	'''
    print(messageString)

    # Lists matrix specific moves
    if messageString == '.matrix':
        response = """```Use the following commands to find detailed information about each move.\n
.login: When attepting to gain access to a system, Login. (Synth)
.meltice: When figting ICE, Melt Ice (Edge)
.compromisesecurity: When screwing around with a system's digital security, Compromise Security (Mind)
.manipulatesystems: When interacting with the meatspace through a system, Manipulate Systems (Synth)
.jackout: When you need to get out quick, Jack Out (Cool)```"""

    # List custom moves
    elif messageString == '.custom':
        response = """```Use the following commands to find detailed information about each move.\n
.dogie: Git along little dogie (Style)
.trouble: Nose for trouble (Cool)
.goodbetter: He's good, but I'm better (Edge)```"""

    # List drugs
    elif messageString == '.drugs':
        response = """```Use the following commands to find detailed information about each drug.\n
.spank: Spank
.motherfuck: Motherfuck
.domo: Domo
.clutch: Clutch
.meatloaf: Meatloaf```"""

    # List weapons
    elif messageString == '.weapons':
        response = """```Firearms:
	» Holdout pistol (2-harm hand/close discreet quick reload loud)
	» Flechette pistol (3-harm close/near quick flechette)
	» Revolver (2-harm close/near reload loud quick)
	» Semi-auto pistol (2-harm close/near loud quick)
	» Heavy revolver (3-harm close/near reload loud)
	» Heavy pistol (3-harm close/near loud)
	» Shotgun (3-harm close/near loud messy reload)
	» Automatic shotgun (3-harm close/near loud messy autofire)
	» Assault rifle (3-harm near/far loud autofire)
	» Machine pistol (2-harm close/near loud autofire)
	» SMG (2-harm close/near loud autofire)
	» LMG (3-harm near/far loud messy autofire clumsy)
	» Hunting rifle (2-harm far/ex loud)
	» Crossbow or hunting bow (2-harm close/near/far reload)
	» Sniper rifle (3-harm far/ex loud clumsy)
	» Anti-materiel rifle (3-harm far/ex loud messy breach clumsy)
	» Grenade launcher (4-harm near/far area loud messy clumsy)
	» Grenade tube (4-harm near area reload loud messy)
	» Assault cannon (4-harm near/far area messy breach clumsy)
	» Missile launcher (5-harm far area messy breach clumsy)\n
Grenades:
	» Fragmentation grenades (4-harm near area reload loud messy)
	» Flashbangs (s-harm near area loud reload)
	» Gas grenades (s-harm near area reload gas)\n
Hand weapons:
	» Knife (2-harm hand)
	» Club (2-harm hand)
	» Sword (3-harm hand messy)
	» Hand taser (s-harm hand reload)
	» Monofilament whip (4-harm hand messy area dangerous)
	» Shuriken or throwing knives (2-harm close numerous)```"""

    ###############################################################################################################################################
    ###############################################################################################################################################
    ############################################################## CUSTOM MOVE COMMANDS ###########################################################
    ###############################################################################################################################################
    ###############################################################################################################################################

    # Git along little dogie
    elif messageString == ".dogie":
        response = """```When you want to use Waleed to antagonise, roll Style (or +1 Synth if you both have Neural Interface).\n
	7+ you antagonise one character, giving you +1 Ongoing to act against that character
	7-9 Choose One:
	10+ Choose Two:
 		- Waleed antagonises one additional character, but will struggle to escape harm
 		- Waleed will escape harm, but will not antagonise for long
 		- Waleed will allow you to escape harm, but will struggle to escape harm
 		- Waleed will apply lethal force, but take his sweet time
 		- Waleed will chase down a lead over great distance, but you will struggle to maintain contact```"""

    # Nose for trouble
    elif messageString == ".trouble":
        response = """```When you want to use Waleed to Assess a person, place or thing, justify why dog senses are better than yours and roll Cool (or +1 Synth if you both have Neural Interface). On a hit, gain +1 additional hold.```"""

    # He's good, but I'm better
    elif messageString == ".goodbetter":
        response = """```When you attempt to outwit a sentient opponent in The Matrix, roll Edge.\n
	7+ you temporarily evade/escape/overcome your opponent
	10+ gain 1 hold. Spend this to temporarily evade/escape/overcome your opponent at any other time in this run. 
	6- your opponent gets the better of you.```"""

    elif messageString == ".jackin":
        response = """```
		Jack in: When you’re jacked into the matrix, you have access to the matrix moves .
		```"""
    elif messageString == ".antivirus":
        response = """```
		Antivirus Subscription: During legwork, you may request a delivery of 2 Single Use Chrome Chips Roll + Cred Spent:
		7+: Mark 2 gear to spend in the matrix.
		10+: Next day delivery.
		```"""
    elif messageString == ".insidejob":
        response = """```
		Inside Job: When you login through a compromised, on-site location, take +1 on all Matrix Moves. 
		```"""
    elif messageString == ".ivehadworse":
        response = """```
		I’ve had worse: Gain 1 Armour against ICE subroutines
		```"""
    elif messageString == ".humansareeasyprey":
        response = """```
		Humans are such easy prey: When you go on the offensive against a Sysop, roll Synth:
		10+: Choose two, or one twice: 
		7-9: Choose one:
		You shake them off your trail, for now.
		You damage their rig, slowing them down.
		You overload their system, zapping their brain
		```"""
    elif messageString == ".cred":
        response = """```
		Spending 1 Cred will get you:
			>useful information from a contact
			>basic restricted gear from a fixer (sidearms, hunting weapons, ammo)
			>replacement parts for a cyberdeck
			>unreliable gang members for muscle
			>a chauffeur
		Spending 2 Cred will get you:
			>a getaway driver for a mission
			>a hacker for a matrix run (but at this price he’ll be poking around for pay-data on the side)
			>professional muscle (a dangerous individual or a competent gang)
			>a street doctor for gunshot wounds
			>more complex, restricted gear from a fixer (grenades, assault weapons, legal drones, basic hacking programs)
		Spending 4 Cred will get you:
			>a hacker with a sense of professional integrity
			>discreet medical services for life-threatening wounds
			>expensive or illegal gear from a fixer (vehicles, security drones, heavy
			>weapons, cutting edge Russian attack software, basic cheap cyberware)
			Spending 8 cred will get you:
			>cutting-edge, military or extortionately expensive gear from a fixer (cyberdecks, military vehicles, most cyberware)
			```"""
    elif messageString == ".rep":
        response = """```
		Rep: When you appear in the Matrix with a recognisable avatar, 
		roll Synth instead of Style for fast talk and instead of Edge for play hardball. 
		When your reputation gets you into trouble, mark experience
		```"""
    elif messageString == ".sneakdoorbeta":
        response = """```
		Sneakdoor Beta: When you have successfully infiltrated a system, you may create a backdoor for quick re-entry. Roll Mind:
		10+: It’s set up, it’s clean, you’re the only one that knows about it.
		7-9: It’s set up, but choose one:
			Sysops will find it sooner rather than later
			It’s not silent entry, using it may raise alarms
			It’s not a clean backdoor, may still have to attempt to login 
		```"""
    elif messageString == ".searchoptimisation":
        response = """```
		Search optimisation: When you research a topic in the Matrix, 
		you may always ask a follow up question. On a 10+, take an additional [intel].
		```"""
    elif messageString == ".diabolusexmachina":
        response = """```
		Diabolus Ex Machina: When ICE is activated against you in the Matrix, roll +Synth: 
		10+: The ICE is under your control.
		7-9: Choose one temporary effect: 
			The ICE is deactivated, this server is open season. 
			The ICE is retargeted, you’re not its priority anymore. 
			You slip past it, it’s the next guy’s problem.
		```"""

    elif messageString == ".bypasscountermeasures":
        response = """```
		Bypass Countermeasures: When you attempt to outmaneuver or evade system countermeasures, roll Edge
		10+: You’re straight through, no worries
		7-9: You’re through, but they’re still on you. Choose one:
			Advance Mission Clock
			ICE is activated
			+1 trace
			Take established consequences 
		6-: You’re caught, and the MC chooses one

			```"""
    elif messageString == ".hijack":
        response = """```
		Hijack System: When you attempt to gain control over a system, roll Mind. 
		7+: You’re in control. You may search, destroy, or wreak whatever chaos you want.
		7-9:  Choose one:
			Time is limited, you can only do so much before they cut you off.
			Access is limited, you can’t get into everything you want.
			+1 trace.
			```"""
    elif messageString == ".":
        response = """```
			```"""
    elif messageString == ".":
        response = """```
			```"""
    elif messageString == ".":
        response = """```
			```"""
    elif messageString == ".":
        response = """```
			```"""


    ###############################################################################################################################################
    ###############################################################################################################################################
    ################################################################# DRUG COMMANDS ###############################################################
    ###############################################################################################################################################
    ###############################################################################################################################################

    # Spank
    elif messageString == ".spank":
        response = """```While Active:
	+1 Meat
	-1 Synth
	+unreliable on cyber gear
	+1 Harm on Melee Attacks
	+short\n
Withdrawal:
	-2 Style
	-1 Meat
	-long```"""

    # Motherfuck
    elif messageString == ".motherfuck":
        response = """```While Active:
	+2 Edge
	-2 Cool
	-long\n
Withdrawal:
	-1 Cool
	-day```"""

    # Domo
    elif messageString == ".domo":
        response = """```While Active:
	+2 Synth
	-1 Everything else
	Take 1 Harm (increases per use per day)
	-instant\n
Withdrawal:
	-1 Synth
	+Harmful on cybergear
	-short```"""

    # Clutch
    elif messageString == ".clutch":
        response = """```While Active:
	-1 to Take Harm move
	-1 Mind
	-short\n
Withdrawal:
	Cardiac arrest if taken more than twice a day```"""

    # Meatloaf
    elif messageString == ".meatloaf":
        response = """```While Active:
	+fast reflexes
	-short\n
Withdrawal:
	-2 Meat
	-2 Edge
	-long```"""

    return response
