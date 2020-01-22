import random
import pickle

from . import Game


class Sprawl(Game):
    def __init__(self):
        super().__init__()
        self.data = 'data/sprawl_data.pickle'
        self.commands = {
            '.matrix': 'Displays a list of matrix-specific moves.',
            '.custom': 'Displays a list of custom moves.',
            '.weapons': 'Displays a list of weapons and their profiles.',
            '.drugs': 'Displays a list of drugs.'
        }

    def handle(self, command, args):
        # Handle custom moves
        if command == '.fuckmeup':
            return self._fuckmeup(args)

        # If not a custom move, check if playbook move
        if command in ('.driver', '.fixer', '.hacker', '.hunter', '.infiltrator', '.killer', '.pusher', '.reporter', '.soldier', '.tech'):
            return self._getplaybook(command[1:], args)

        # Finally, check if basic move, otherwise return None
        move = self._getmove(command)
        return move.description if move else None

    def moves(self, message):
        return """Use the following commands to find detailed information about each move.\n
.actunderpressure: Act Under Pressure (Cool)
.applyfirstaid: Apply First Aid (Cool)
.assess: Assess (Edge)
.playhardball: Play Hardball (Edge)
.amidead: Acquire Agricultural Property (Meat)
.mixitup: Mix it Up (Meat)
.research: Research (Mind)
.fasttalk: Fast Talk (Style)
.hitthestreet: Hit The Street (Style)
.undertheknife: Go Under the Knife (Cred)
.fuckmeup: Harm
.getthejob: Get the Job (Edge)
.gettingpaid: Getting Paid (Legwork)

For playbook specific moves see '.playbooks'.

For matrix specific moves see '.matrix'."""

    def playbooks(self, message):
        return """Use the following commands to find each playbook-specific move.\n
.driver
.fixer
.hacker
.hunter
.infiltrator
.killer
.pusher
.reporter
.soldier
.tech"""

    def _driver(self, move):
        if not move:
            return """Use .driver <move> to see details about a specific move.
Roll moves:
    hotshitdriver: Bonus while high-tension driving. (Roll)\n
Other moves:
    Wheels: You start with a car.
    Second Skin: When jacked into your vehicle with a neural interface you get bonuses to your rolls.
    Chromed: Choose another piece of cyberware at character creation or in downtime.
    Daredevil: Bonus when you drive straight into danger.
    Drone Jockey: You get with two drones.
    Iceman: Fast talk replacement.
    Right Tool for the Job: You have two additional cyber-linked vehicles.
    Sweet Ride: Replacement and bonus to Hit the street while in your vehicle."""

        m = self._getmove(move, playbook='driver')
        return m.description if m else None

    def _fixer(self, move):
        if not move:
            return """Roll moves:
    hustling: Gives hustling jobs. (Roll)
    iknowpeople: Specialized contact decleration. (Roll)\n
    reputation: Various social  (Roll).
Other moves:
    Backup: You have a group of associates. 
    Balls in the Air: +1 crew and choose another job.
    Chromed: Choose another piece of cyberware at character creation or in downtime.
    Deal of a Lifetime: Hit the street bonus when selling something.
    Facetime: Fast talk bonus.
    Hard to Find: Hit the street bonus.
    Sales Engineer: Produce equipment bonus.
    Smooth: Helping or hindering replacement.
    Street King Pin: +1 crew, choose an additional job.
    Word on the Street: Meatspace research bonus."""

        m = self._getmove(move, playbook='fixer')
        return m.description if m else None

    def _hacker(self, move):
        if not move:
            return """Roll Moves:
    consolecowboy: Hold over systems (Roll)
Other moves:
    .jackin: You can access the matrix moves.
    .antivirus: Legwork roll+cred for chrome chips.
    .chromed: Choose another piece of cyberware at character creation or in downtime. 
    .insidejob: When you login through a comprimised site +1 matrix moves.
    .ivehadworse: +1 armor against ice
    .humansareeasyprey: Go on the offensive against Sysop roll synth.
    .rep: Fast talk and Play hard ball replacements while in the matrix.
    .searchoptimisation: Matrix research bonus.
    .rigenthusiast: extra deck tag.
    .sneakdoorbeta: create a backdoor in for future use.
    .techsupport: Bonus when helping or interfering while in the matrix.
    .diabolusexmchina When Ice is activated against you roll + synth."""

        m = self._getmove(move, playbook='hacker')
        return m.description if m else None

    def _hunter(self, move):
        if not move:
            return """Roll moves:
    itallfits: Research bonus. (Roll)
    biggamehunter: Bonus when springing a trap against a researced target. (Roll)
    sniper: Bonus when hiding. (Roll)\n
Other moves:
    .eartotheground: Meatspace reseach bonus. 
    .chromed: Choose another piece of cyberware at character creation or in downtime.
    .deadbeat: Hit the street bonus.
    .enhance: Research bonus.
    .eyefordetail: Bonus when calmly assessing a person or place.
    .humanterrain: Bonus when investigating a group.
    .onthetrail: Additional use of intel against a single person.
    .seetheangles: At the start of the action phase gain [intel] and [gear]."""

        m = self._getmove(move, playbook='hunter')
        return m.description if m else None

    def _infiltrator(self, move):
        if not move:
            return """Roll moves:
    covertentry: Bonus when infilatrating alone. (Roll)
    casethejoint: Bonus when examining a locations weaknesses. (Roll)
    planb: When shit hits the fan and you have to get out. (Roll)
    psychologicalwarfare: When you attempt to demoralise the enemy by leaving evidence of violence. (Roll)\n
Other moves:
    .catburgler: On the job [gear] procurement. Used with Covert Entry.
    .face: On the job [intel] procurement. Used with Covert Entry.
    .assassin: Bonus to attacking unexpectedly.
    .chromed: Choose another piece of cyberware at character creation or in downtime.
    .jackin: You can access the matrix.
    .masterofdisguise: Fast talk bonus.
    .motherduck: Allows Covert Entry hold you spend to work for the whole team.
    .stealthoperative: Assess bonus."""

        m = self._getmove(move, playbook='infiltrator')
        return m.description if m else None

    def _killer(self, move):
        if not move:
            return """Roll moves:
    seriousbadass: Bonus when entering a charged situation. (Roll)
    trainedeye: Bonus when sizing up a person, vehicle, drone or gang. (Roll)\n
Other moves:
    .customweapon: You begin with a custom weapon.
    .emotionless: Play hard ball replacement.
    .hard: Harm move bonus.
    .loadedforbear: Choose another bonus weapon.
    .moremachinethanmeat: Choose another piece of cyberware at character creation or in downtime.
    .corporatesecrets: Bonus when researching a corporation.
    .militarybackground: Bonus when hitting the street.
    .milspecs: Bonus to mix it up."""

        m = self._getmove(move, playbook='killer')
        return m.description if m else None

    def _pusher(self, move):
        if not move:
            return """Roll moves:
    driven: Bonus when the mission furthers your vision. (Roll)
    visionthing: Bonus when passionately advocating your vision. (Roll)\n
Other moves:
    .believers: You are a part of a gang, tribe, band, corporation or similar group.
    .bringitonhome: Bonus when using Vision Thing or One Million Points of Light.
    .chromed: Choose another piece of cyberware at character creation or in downtime.
    .famous: Bonus against people who recognise you.
    .innercircle: You have a loyal inner circle of believers.
    .onemillionpointsoflight: Bonus to vision thing.
    .opportunistic: Replacement when helping or interfering.
    .peopleperson: Hit the street bonus.
    .rabblerouser: Vision Thing bonus.
    .silvertongue: Fast Talk bonus."""

        m = self._getmove(move, playbook='pusher')
        return m.description if m else None

    def _reporter(self, move):
        if not move:
            return """Roll moves:
    liveandontheair: You can broadcast a stream to hurt your target. (Roll)
    noseforastory: Various mission bonuses. (Roll)
    gatherevidence: Various effects on story and noise clocks. (Roll)
    monstering: You can corner someone and hound them with questions. (Roll)\n
Other moves:
    .24/7livefeeds: Bonus to researching when scanning live feeds.
    .chromed: Choose another piece of cyberware at character creation or in downtime.
    .filthyassistants: Bonus when using research obtained [intel].
    .presspass: Bonus when revealing yourself to fast talk your way in.
    .reliablesources: Research bonus.
    .warcorrespondent: Bonus when Acting Under Pressure."""

        m = self._getmove(move, playbook='reporter')
        return m.description if m else None

    def _soldier(self, move):
        if not move:
            return """Roll moves:
    iloveitwhenaplancomestogether: Bonus [gear] and [intel]. (Roll)
    exitstrategy: Bonus to getting the fuck out of there. (Roll)
    recruiter: Contact / Hit the Street bonus. (Roll)
    slippery: Prevents Corps from finding the teams involvement. (Roll)\n
Other moves:
    .herestheplan: Team bonus when you plan the mission and if you get paid.
    .auraofprofessionalism: Bonus when Getting the Job or Getting Paid.
    .chromed: Choose another piece of cyberware at character creation or in downtime.
    .corporateknowledge: Bonus when researching a corporation.
    .handsonmanagement: Mix it up bonus.
    .steadypresence: You can give pep-talks.
    .tacticaloperations: Assess bonus."""

        m = self._getmove(move, playbook='soldier')
        return m.description if m else None

    def _tech(self, move):
        if not move:
            return """Roll moves:
    storage: Pre-mission [gear] bonus. (Roll)
    blendin: You can act like you belong in places you don't. (Roll)
    bypass: You can subvert security measures. (Roll)\n
Other moves:
    .expert: You get an area of expertise.
    .customiser: You can examine and modify technology.
    .analytic: Assess replacement.
    .chromed: Choose another piece of cyberware at character creation or in downtime.
    .diverseinterests: Choose another area of expertise.
    .jackofalltrades: Choose another area of expertise.
    .obsessive: Research bonus.
    .onit: Replacement when helping or hindering someone in a topic relating to your expertise.
    .renaissanceman: Choose another area of expertise."""

        m = self._getmove(move, playbook='tech')
        return m.description if m else None

    def _fuckmeup(self, damage):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        modifier = 0
        if damage:
            modifier = int(damage)
        roll = dice1 + dice2 + modifier

        with open(self.data, 'rb') as file:
            moves = pickle.loads(file.read())
            if roll >= 10:
                harm = self._getmove('Harm 10', name=True)
                return f'Oh you fucked up now, you rolled a {roll}. {harm.description}'
            elif 7 <= roll <= 9:
                harm = self._getmove('Harm 7', name=True)
                return f'You\'re going to have to suck off the MC on this one, you rolled a {roll}. {harm.description}'
            else:
                return f'You rolled {roll}. You\'re gucci flip flops fam *dabs* haha yeet :3'





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

    #########################################################
    ################## MATRIX MOVE COMMANDS #################
    #########################################################

    # Login
    elif messageString == ".login":
        response = """```
		Login :When you attempt to gain access to a system, roll Synth.
		10+: you’re in clean
		7-9: you’re in, but choose one:
		Sysops are alerted
		ICE is activated
		They’re onto you, +1 trace
		Your access is restricted – take -1 ongoing to matrix moves in this system while your access is restricted
		6-: you’re in, but the MC chooses two, and a relevant clock is advanced```"""

    # Melt Ice
    elif messageString == ".melt" or messageString == ".meltice":
        response = """```When you attempt to evade, destroy or disable an activated ICE construct, roll Edge.\n
	7+: you evade, destroy, or temporarily disable the system, your choice
	7-9: the system successfully executes a routine before you can disable it```"""

    # Compromise Security
    elif messageString == ".compsec" or messageString == ".compromisesecurity":
        response = """```When you attempt to compromise a sub-system’s security, roll Mind.\n
		10+: gain 3 hold over the sub-system you have compromised
		7-9: gain 1 hold
		6-: you trigger an alert, which may have additional consequences\n
You may spend 1 hold to activate a security measure on that sub-system.```"""

    # Manipulate Systems
    elif messageString == ".mansys" or messageString == ".manipulatesystem" or messageString == ".manipulatesystems":
        response = """```When you attempt to manipulate a digitally-controlled aspect of a facility, roll Synth.\n
	10+: gain 3 hold over the sub-system you are manipulating
	7-9: gain 1 hold\n
You may spend 1 hold to activate routines on that sub-system.```"""

    # Jack Out
    elif messageString == ".jackout":
        response = """```
		Jackout: When you, your programs, or your deck are about to be damaged by ICE, you can try to jack out. Roll Cool.
		10+: you disconnect yourself from the system before any serious harm occurs
		7-9: you jack out, but choose one:
			You lose some data
			You take some of the established consequences
			The owners of the target system trace you to your current location
		6-: you take the established consequences... and you’re still connected
```"""

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
