import random
import pickle

from . import Game


class Sprawl(Game):
    def __init__(self):
        super().__init__()
        self.datafile = 'data/sprawl_data.pickle'
        self.commands = {
            '.matrix': 'Displays a list of matrix-specific moves.',
            '.cred': 'Shows you what you can do with cred.',
            '.weapons': 'Displays a list of weapons and their profiles.'
        }
        self.loaddata()

    def handle(self, command, args):
        # Handle game-specific moves
        if command == '.fuckmeup':
            return self._fuckmeup(args)
        elif command == '.matrix':
            return self._matrix()
        elif command == '.cred':
            return self._cred()
        elif command == '.weapons':
            return self._weapons()

        # Check matrix moves
        move = self._getmove(command, index='matrix')
        if move:
            return move.fulldescription

        # If not a game-specific move, check if playbook move
        if command in (
        '.driver', '.fixer', '.hacker', '.hunter', '.infiltrator', '.killer', '.pusher', '.reporter', '.soldier',
        '.tech'):
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

    def _cred(self):
        return """Spending 1 Cred will get you:
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
    >cutting-edge, military or extortionately expensive gear from a fixer (cyberdecks, military vehicles, most cyberware)"""

    def _weapons(self):
        return """Firearms:
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
    » Shuriken or throwing knives (2-harm close numerous)"""
