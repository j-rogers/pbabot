"""The Sprawl (Customised)

This is The Sprawl but with modified and custom rules/playbooks. We have made the following changes:
    - Updated Matrix moves
    - Updated Hacker playbook
    - Changed currency (added Rep in addition to Cred)
        -> This includes changes to the Get the Job and Get Paid basic moves
    - Cyberware overhaul
    - Updated Reporter playbook

# Add updated reporter
Author: Joshua Rogers (2021)
"""
from . import Game, Move, Playbook
from discord.ext import commands
import random


class SprawlCustom(Game):
    """Custom Sprawl Game

    Uses the same commands as regular Sprawl with the following extras:
        currency: Prints custom currency rules
        cyberware: Prints custom cyberware rules
    """
    BASIC_MOVES = [
        Move(
            'Act Under Pressure',
            'Do something under pressure (Cool).',
            full_description='When you race against the clock, act while in danger, or act to avoid danger, roll Cool.'
                             '\n\t10+: you do it, no problem\n\t7-9: you stumble, hesitate, or flinch: the MC will '
                             'offer you a worse outcome, hard bargain, or ugly choice'
        ),
        Move(
            'Apply First Aid',
            'Attempt to heal someone (Cool).',
            aliases=['firstaid', 'aid'],
            full_description='When you treat someone’s wounds using appropriate medical equipment, roll Cool.\n\t10+: '
                             'if their Harm Clock is at 2100 or less, reduce their harm by two segments. If their Harm '
                             'Clock is at more than 2100, reduce their harm by one segment\n\t7-9: reduce their harm by'
                             ' one segment. If their Harm Clock is still at more than 2100, they take -1 ongoing until '
                             'they receive proper medical attention'
        ),
        Move(
            'Assess',
            'Study a person, place or sitaution (Edge).',

            full_description='When you closely study a person, place or situation, or when you quickly size up an '
                             'opponent or a charged situation, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\n'
                             'In the ensuing action, you may spend 1 hold at any time to ask the MC a question from the'
                             ' list below if your examination could have revealed the answer. The MC may ask you '
                             'questions to clarify your intent. Take +1 forward when acting on the answers.\n\n\tЂ What'
                             ' potential complication do I need to be wary of?\n\tЂ What do I notice despite an effort '
                             'to conceal it?\n\tЂ How is ______ vulnerable to me?\n\tЂ How can I avoid trouble or hide '
                             'here?\n\tЂ What is my best way in/way out/way past?\n\tЂ Where can I gain the most '
                             'advantage?\n\tЂ Who or what is my biggest threat in this situation?\n\tЂ Who or what is '
                             'in control here?'
        ),
        Move(
            'Play Hardball',
            'Threaten someone with the intent to carry through (Edge).',
            aliases=['hardball'],
            full_description='When you get in someone’s face threatening violence and you intend to carry through, roll'
                             ' Edge.\n\n\t10+: NPCs do what you want. PCs choose: do what you want, or suffer the '
                             'established consequences\n\t7–9: For NPCs, the MC chooses 1:\n\t\tЂ they attempt to '
                             'remove you as a threat, but not before suffering the established consequences\n\t\tЂ they'
                             ' do it, but they want payback. Add them as a Threat\n\t\tЂ they do it, but tell someone '
                             'all about it. Advance the appropriate Mission Clock\nPCs choose: do what you want, or'
                             ' suffer the established consequences. They gain +1 forward to act against you.',
        ),
        Move(
            'Acquire Agricultural Property',
            'When you hit 0000 on your Harm Clock (Meat).',
            command='amidead',
            aliases=['acquire', 'acquireagriculturalproperty'],
            full_description='When you hit 0000 on your Harm Clock, roll Meat.\n\n\t10+: you survive until the medics '
                             'arrive\n\t7-9: you survive at a cost. Pick one: +owned, substandard treatment (-1 to a '
                             'stat), cyberware damage (give one piece of cyberware a negative tag)\n\t6-: you bleed out'
                             ' on the street',
        ),
        Move(
            'Mix it Up',
            'Using violence to achieve a goal (Meat).',
            aliases=['mix'],
            full_description='When you use violence against an armed force to seize control of an objective, state that'
                             ' objective and roll Meat.\n\n\t7+: you achieve your objective\n\t7-9: choose 2:\n\t\tЂ '
                             'you make too much noise. Advance the relevant Mission Clock\n\t\tЂ you take harm as '
                             'established by the fiction\n\t\tЂ an ally takes harm as established by the fiction\n\t\t'
                             'Ђ Something of value breaks',
        ),
        Move(
            'Research',
            'Investigate something or someone using an external resource (Mind).',
            full_description='When you investigate a person, place, object, or service using a library, dossier or '
                             'database (or combination of them), ask a question from the list below and roll Mind.'
                             '\n\n\t10+: take [intel]; the MC will answer your question and answer a follow-up question'
                             ' from this list as well:\n\t\tЂ Where would I find ______?\n\t\tЂ How secure is ______?'
                             '\n\t\tЂ Who or what is related to ______?\n\t\tЂ Who owned or employed ______?\n\t\tЂ Who'
                             ' or what is ______ most valuable to?\n\t\tЂ What is the relationship between ______ and'
                             ' ______?\n\t7-9: take [intel]; the MC will answer your question\n\t6-: the MC will answer'
                             ' your question... and make a move',
        ),
        Move(
            'Fast Talk',
            'Trying to bluff someone (Style).',
            full_description='When you try to convince someone to do what you want with promises, lies or bluster, roll'
                             ' Style.\n\n\t10+: NPCs do what you want. PCs choose whether to do it or not. If they do, '
                             'they mark experience. If they don’t, they must act under pressure to go against your '
                             'stated wishes.\n\t7-9: NPCs do it, but someone will find out: the MC will advance the '
                             'appropriate Countdown Clock. For PCs choose one:\n\t\tЂ If they do what you want, they '
                             'mark experience\n\t\tЂ If they don’t do it, they must act under pressure to go against '
                             'your stated wishes\n\tThen its up to them.',
        ),
        Move(
            'Hit the Street',
            'Going to a contact for help (Style).',
            aliases=['hithestreet', 'street'],
            full_description='When you go to a Contact for help, roll Style.\n\n\t7+: You get what you want.\n\t10+: '
                             'You get a little something extra (choose either [intel] or [gear]).\n\t7-9: choose 2 from'
                             ' the list below:\n\t\tЂ Your request is going to cost you extra\n\t\tЂ Your request is '
                             'going to take some time to put together\n\t\tЂ Your request is going to attract unwanted '
                             'attention, complications or consequences\n\t\tЂ Your contact needs you to help them out '
                             'with something. If you turn them down take -1 ongoing to this move till you make it right'
        ),
        Move(
            'Go Under the Knife',
            'Having new cyberware installed by a street doctor (Cred).',
            aliases=['undertheknife', 'under', 'knife'],
            full_description='When you have new cyberware installed by a street doctor, roll Cred spent (max +2).'
                             '\n\n\t10+: the operation was a complete success\n\t7-9: the cyberware doesn’t work as '
                             'well as advertised, choose one: +unreliable, +substandard, +hardware decay, +damaging.'
                             '\n\t6-: there have been... complications\n\nWhen you have new cyberware installed in '
                             'accordance with a corporate contract, ignore all of that bad stuff. You’re +owned. Your '
                             'cyberware works exactly the way they intend it.',
        ),
        Move(
            'Get the Job',
            'Negotiating the terms of a job (Edge).',
            aliases=['job'],
            full_description='When you negotiate the terms of a job, roll Edge.\n\n\t10+: choose 3 from the list '
                             'below\n\t7-9: choose 1 from the list below\n\t\tЂ The employer is a professional {You get'
                             ' 1 Cred upfront for expenses; this option can be chosen multiple times}\n\t\tЂ The '
                             'employer is hedging their bets {You may ask a research question using the employer\'s '
                             'Corp network}\n\t\tЂ The job pays well {When getting paid you make back triple the amount'
                             ' of staked rep}\n\t\tЂ The meeting isnt being monitored by outside forces {A player '
                             'staking 3 Rep does not increase the Legwork clock; this option can be chosen multiple '
                             'times}\n\t\tЂ The employer has made a misstep and is implicated in the mission {Only the'
                             ' employer\'s Corporate clock can be raised in retaliation to this mission}',
        ),
        Move(
            'Getting Paid',
            'Meeting with your employer to get paid (Legwork).',
            aliases=['getpaid', 'paid'],
            full_description='When you go to a meet to get paid by your employer, roll and add the number of unfilled '
                             'segments on the Legwork Clock.\n\n\t10+: choose 3 from the list below\n\t7-9: choose 1 '
                             'from the list below\n\t\tЂ It’s not a set-up or an ambush\n\t\tЂ You are paid in full '
                             '{You split your earnings in any integer combination of Rep/Cred you choose}\n\t\tЂ The '
                             'employer is impressed with your professionalism {Everyone gets one additional Rep; this '
                             'option can be chosen multiple times}\n\t\tЂ The meeting doesn’t attract the attention of '
                             'outside parties\n\t\tЂ You learned something from the mission; everyone marks experience',
        )
    ]
    PLAYBOOK_MOVES = [
        Playbook('driver', [
            Move(
                'Hot Shit Driver',
                'Bonus while high-tension driving. (Roll)',
                full_description='When you’re driving a cyber-linked vehicle in a high-pressure situation, roll Edge.'
                                 '\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nYou may spend 1 hold to do one of the '
                                 'following:\n\t• Avoid one external danger (a rocket, a burst of gunfire, a collision,'
                                 ' etc)\n\t• Escape one pursuing vehicle\n\t• Maintain control of the vehicle\n\t• '
                                 'Impress, dismay or frighten someone',
            ),
            Move(
                'Wheels',
                'You start with a car.',
            ),
            Move(
                'Second Skin',
                'When jacked into your vehicle with a neural interface you get bonuses to your rolls.',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime.',
            ),
            Move(
                'Daredevil',
                'Bonus when you drive straight into danger.',
            ),
            Move(
                'Drone Jockey',
                'You get two drones.',
            ),
            Move(
                'Iceman',
                'Fast talk replacement.',
            ),
            Move(
                'Right Tool for the Job',
                'You have two additional cyber-linked vehicles.',
            ),
            Move(
                'Sweet Ride',
                'Replacement and bonus to Hit the Street while in your vehicle.',
            )
        ]),
        Playbook('fixer', [
            Move(
                'Hustling',
                'Gives hustling jobs. (Roll)',
                full_description='You have people who work for you in various ways. You start with 2-crew and two jobs '
                                 'from the list below. Between missions, choose a number of those jobs equal to or less'
                                 ' than your current crew, describe what each job is, and roll Edge.\n\n\t10+: you '
                                 'profit from each of your jobs\n\t7-9: one of them is a Disaster and you Profit from '
                                 'the rest\n\t6-: everything’s FUBAR. The MC will make a move based on the Disaster for'
                                 ' each job\n\nChoose two:\n\tЂ Surveillance: You have a small network of informants '
                                 'who report on events; you then sell that information\n\t\t• Profit: gain [intel]'
                                 '\n\t\t• Disaster: someone acts on bad info\n\tЂ Debt collection: You have a few burly'
                                 ' looking fuckers who collect outstanding debts\n\t\t• Profit: gain [gear]\n\t\t'
                                 '• Disaster: someone’s out of pocket\n\tЂ Petty theft: You have a small crew who '
                                 'perform minor local robberies\n\t\t• Profit: gain [gear]\n\t\t• Disaster: they robbed'
                                 ' the wrong guy\n\tЂ Deliveries: People hire you to transport things and you have a'
                                 ' driver who takes care of that\n\t\t• Profit: gain 1 Cred\n\t\t• Disaster: the'
                                 ' delivery never arrives\n\tЂ Brokering deals: You arrange for the right people to'
                                 ' meet each other\n\t\t• Profit: gain 1 Cred\n\t\t• Disaster: the deal that you '
                                 'arranged goes wrong\n\tЂ Technical work: You have a couple of techs whom you supply'
                                 ' with work\n\t\t• Profit: gain [gear]\n\t\t• Disaster: something bad happens to '
                                 'someone else’s property\n\tЂ Pimping: You manage a small stable of physical or '
                                 'virtual sex workers\n\t\t• Profit: gain [intel]\n\t\t• Disaster: something goes wrong'
                                 ' with a customer\n\tЂ Addictive substances: You manage a small lab producing either'
                                 ' drugs or simstim chips\n\t\t• Profit: gain [intel]\n\t\t• Disaster: something goes'
                                 ' wrong for a user or for the lab itself',
            ),
            Move(
                'I Know People',
                'Specialized contact decleration. (Roll)',
                full_description='Once per mission you may introduce a new Contact. Name the contact, say what they do,'
                                 ' then roll Style.\n\n\t10+: you’ve worked with the contact before; they have talent. '
                                 'Write them down as a Contact\n\t7-9: you’ve never met them before, they’re an unknown'
                                 ' quantity\n\t6-: you know them all right. Tell the MC why they dislike you\n\nAfter '
                                 'you’ve rolled, describe how you contact them; the MC will ask some questions.',
            ),
            Move(
                'Reputation',
                'Various social (Roll).',
                full_description='When you meet someone of consequence who might have heard of you, roll Edge. On a '
                                 'hit, say what they know about you. On a 10+, take +1 forward with them. On a miss, '
                                 'the MC will decide what they’ve heard about you, if anything. Either you or the MC '
                                 'can say whether someone is “of consequence”, but once you’ve made the reputation move'
                                 ' on someone, they’re “of consequence” and will be a recurring part of the story.',
            ),
            Move(
                'Backup',
                'You have a group of associates',
            ),
            Move(
                'Balls in the Air',
                '+1 crew and choose another job.',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime',
            ),
            Move(
                'Deal of a Lifetime',
                'Hit the Street bonus when selling something',
            ),
            Move(
                'Facetime',
                'Fast talk bonus',
            ),
            Move(
                'Hard to Find',
                'Hit the Street bonus.',
            ),
            Move(
                'Sales Engineer',
                'Produce equipment bonus.',
            ),
            Move(
                'Smooth',
                'Helping or hindering replacement',
            ),
            Move(
                'Street King Pin',
                '+1 crew, choose an additional job.',
            ),
            Move(
                'Word on the Street',
                'Meatspace research bonus',
            )
        ]),
        Playbook('hacker', [
            Move(
                'Jack in',
                'You get access the matrix moves',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime',
            ),
            Move(
                'Inside Job',
                'When you login through a compromised site, +1 matrix moves.',
            ),
            Move(
                'I\'ve had worse',
                '+1 armour against ice subroutines.',
            ),
            Move(
                'Humans are Easy Prey',
                'Go on the offensive against Sysop, roll synth',
                full_description='Humans are such easy prey: When you go on the offensive against a Sysop, roll '
                                 'Synth:\n\n\t10+: Choose two, or one twice:\n\t7-9: Choose one:\n\t\tYou shake them'
                                 ' off your trail, for now.\n\t\tYou damage their rig, slowing them down.\n\t\tYou '
                                 'overload their system, zapping their brain'
            ),
            Move(
                'Rep',
                'Fast talk and play hardball replacements while in the matrix.',
                full_description='Rep: When you appear in the Matrix with a recognisable avatar, roll Synth instead of '
                                 'Style for fast talk and instead of Edge for play hardball.\nWhen your reputation gets'
                                 ' you into trouble, mark experience'
            ),
            Move(
                'Search Optimisation',
                'Matrix research bonus',
                full_description='When you research a topic in the Matrix, you may always ask a follow up question. On '
                                 'a 10+, take an additional [intel].'
            ),
            Move(
                'Rig Enthusiast',
                'Extra deck tag',
            ),
            Move(
                'Sneak Door Beta',
                'Create a backdoor for future use.',
                full_description='Sneakdoor Beta: When you have successfully infiltrated a system, you may create a '
                                 'backdoor for quick re-entry. Roll Mind:\n\n\t10+: It’s set up, it’s clean, you’re '
                                 'the only one that knows about it.\n\t7-9: It’s set up, but choose one:\n\t\tSysops '
                                 'will find it sooner rather than later\n\t\tIt’s not silent entry, using it may raise '
                                 'alarms\n\t\tIt’s not a clean backdoor, may still have to attempt to login '
            ),
            Move(
                'Tech Support',
                'Bonus when helping or interfering while in the matrix',
            ),
            Move(
                'Diabolus Ex Machina',
                'When Ice is activated against you, roll +synth',
                full_description='When ICE is activated against you in the Matrix, roll +Synth:\n\n\t10+: The ICE is'
                                 ' under your control.\n\t7-9: Choose one temporary effect:\n\t\tThe ICE is '
                                 'deactivated, this server is open season.\n\t\tThe ICE is retargeted, you’re not its '
                                 'priority anymore.\n\t\tYou slip past it, it’s the next guy’s problem.'
            )
        ]),
        Playbook('hunter', [
            Move(
                'It All Fits Together',
                'Research bonus. (Roll)',
                aliases=['itallfits'],
                full_description='You’re a master of making connections between seemingly unrelated events. At the '
                                 'start of a mission, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nAs you '
                                 'put everything together during the mission, spend 1 hold at any time to ask a '
                                 'question from the research list.',
            ),
            Move(
                'Big Game Hunter',
                'Bonus when springing a trap against a researced target. (Roll)',
                full_description='When you spring a trap for a target you have investigated, roll Edge.\n\n\t7+: you '
                                 'have them trapped, the only way out is through you\n\t10+: they are at your mercy; if'
                                 ' the target attempts to escape, roll Edge instead of Meat to mix it up',
            ),
            Move(
                'Sniper',
                'Bonus when hiding. (Roll)',
                full_description='When you set up a covered and concealed place to hide, roll Cool.\n\n\t10+: choose 3'
                                 '\n\t7-9: choose 2\n\t\t• Your site is well hidden\n\t\t• Your site has excellent '
                                 'cover\n\t\t• Your site has an excellent field of view\n\t\t• You have a similarly '
                                 'covered and concealed backup location\n\t\t• Your spot is well secured\n\nThen '
                                 'describe your hide site.',
            ),
            Move(
                'Ear to the Ground',
                'Meatspace research bonus',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime',
            ),
            Move(
                'Deadbeat',
                'Hit the Street bonus',
            ),
            Move(
                'Enhance',
                'Research bonus',
            ),
            Move(
                'Eye for Detail',
                'Bonus when calmly assessing a person or place',
            ),
            Move(
                'Human Terrain',
                'Bonus when investigating a group',
            ),
            Move(
                'On the Trail',
                'Additional use of intel against a single person',
            ),
            Move(
                'See the Angles',
                'At the start of the action phase gain [intel] and [gear].',
            )
        ]),
        Playbook('infiltrator', [
            Move(
                'Covert Entry',
                'Bonus when infilatrating alone. (Roll)',
                full_description='When you attempt to infiltrate a secure area alone, roll Cool.\n\n\t10+: gain 3 hold'
                                 '\n\t7-9: gain 1 hold\n\nAs the MC describes the infiltration and the security '
                                 'measures you must overcome, you may spend 1 hold to describe how you overcome the '
                                 'obstacle and:\n\t• Bypass a security system or guard.\n\t• Disable a security system '
                                 'you have bypassed.\n\t• Disable a guard.\n\t• Escape notice',
            ),
            Move(
                'Case the Joint',
                'Bonus when examining a locations weaknesses. (Roll)',
                full_description='When you take time to examine a location for security weaknesses you can exploit, '
                                 'roll Edge.\n\n\t10+: gain three [intel]\n\t7-9: gain [intel]\n\nYou may spend this '
                                 '[intel] in the normal way, or you can spend one point of this [intel] to ask '
                                 'questions from the assess or research lists.',
            ),
            Move(
                'Plan B',
                'When shit hits the fan and you have to get out. (Roll)',
                full_description='When shit hits the fan and you have to get out, name your escape route and roll '
                                 'Cool.\n\n\t10+: sweet, you’re gone\n\t7–9: you can go or stay, but if you go it '
                                 'costs you: leave something behind, or take something with you; in either case, the '
                                 'MC will tell you what\n\t6-: you’re caught in a vulnerable position, half in and half'
                                 ' out. The MC will make a move',
            ),
            Move(
                'Psychological Warfare',
                'When you attempt to demoralise the enemy by leaving evidence of violence. (Roll)',
                aliases=['psychwarfare', 'psywarfare'],
                full_description='When you attempt to influence the morale of your enemies by leaving evidence of '
                                 'violence while remaining undetected, roll Edge.\n\n\t7+: your enemies are impressed '
                                 'and overly cautious, scared and demoralised, or angry and careless (MC’s choice)'
                                 '\n\t10+: you choose',
            ),
            Move(
                'Cat Burgler',
                'On the job [gear] procurement. Used with Covert Entry',
            ),
            Move(
                'Face',
                'On the job [intel] procurement. Used with Covert Entry',
            ),
            Move(
                'Assassin',
                'Bonus to attacking unexpectedly.',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime.',
            ),
            Move(
                'Jack In',
                'You gain access to matrix moves.',
            ),
            Move(
                'Master of Disguise',
                'Fast talk bonus',
            ),
            Move(
                'Mother Duck',
                'Allows Covert Entry hold you spend to work for the whole team.',
            ),
            Move(
                'Stealth Operative',
                'Assess bonus',
            )
        ]),
        Playbook('killer', [
            Move(
                'Serious Badass',
                'Bonus when entering a charged situation. (Roll)',
                full_description='When you enter a charged situation, roll Style.\n\n\t10+: gain 2 hold\n\t7–9: gain 1 '
                                 'hold\n\t6-: your enemies identify you immediately as their foremost threat\n\nSpend 1'
                                 ' hold to make eye contact with an NPC present, who freezes or flinches and can’t act '
                                 'until you break it off.',
            ),
            Move(
                'Trained Eye',
                'Bonus when sizing up a person, vehicle, drone or gang. (Roll)',
                full_description='When you evaluate a person, vehicle, drone or gang, roll Cool.\n\n\t7+: ask the '
                                 'target “How are you vulnerable to me?” Take +1 forward when acting on the answer'
                                 '\n\t10+: gain +1 ongoing when acting against that target',
            ),
            Move(
                'Custom Weapon',
                'You begin with a custom weapon.',
            ),
            Move(
                'Emotionless',
                'Play hard ball replacement.',
            ),
            Move(
                'Hard',
                'Harm move bonus',
            ),
            Move(
                'Loaded for Bear',
                'Choose another bonus weapon.',
            ),
            Move(
                'More Machine than Meat',
                'Choose another piece of cyberware at character creation or in downtime.',
            ),
            Move(
                'Corporate Secrets',
                'Bonus when researching a corporation',
            ),
            Move(
                'Military Background',
                'Bonus when hitting the street.',
            ),
            Move(
                'Milspecs',
                'Bonus to mix it up.',
            )
        ]),
        Playbook('pusher', [
            Move(
                'Driven',
                'Bonus when the mission furthers your vision. (Roll)',
                full_description='When you begin a mission that furthers your vision, roll Edge.\n\n\t10+: gain 3 hold'
                                 '\n\t7-9: gain 1 hold\n\nYou may spend 1 hold before rolling any other move to take +1'
                                 ' or -2 forward to the move.',
            ),
            Move(
                'Vision Thing',
                'Bonus when passionately advocating your vision. (Roll)',
                full_description='When you have time and space for an emotional connection with someone and you '
                                 'passionately advocate for your vision, roll Style.\n\n\t10+: gain 2 hold\n\t7-9: gain'
                                 ' 1 hold\n\nSpend 1 hold to have the targeted NPCs:\n\t• give you something you want'
                                 '\n\t• do something you ask\n\t• fight to protect you or your cause\n\t• disobey an '
                                 'order given by someone with authority or leverage over them\n\nWhen you use this move'
                                 ' on a PC, spend your hold to help or interfere as if you had rolled a 10+ (i.e. give '
                                 'them +1 or -2). If you miss against a PC, they gain 2 hold against you which they can'
                                 ' use in the same way.',
            ),
            Move(
                'Believers',
                'You are part of a gang, tribe, band, corporation, or similar group',
            ),
            Move(
                'Bring it on Home',
                'Bonus when using Vision Thing or One Million Points of Light',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime',
            ),
            Move(
                'Famous',
                'Bonus against people who recognise you.',
            ),
            Move(
                'Inner Circle',
                'You have a loyal inner circle of believers',
            ),
            Move(
                'One Million Points of Lights',
                'Bonus to vision thing.',
            ),
            Move(
                'Opportunistic',
                'Replacement when helping or interfering.',
            ),
            Move(
                'People Person',
                'Hit the Street bonus.',
            ),
            Move(
                'Rabble Rouser',
                'Vision Thing bonus',
            ),
            Move(
                'Silver Tongue',
                'Fast Talk bonus',
            )
        ]),
        Playbook('reporter', [
            Move(
                'Live and on the Air',
                'You can broadcast a stream to hurt your target. (Roll)',
                aliases=['live', 'liveontheair'],
                full_description='When you go live from the scene and broadcast a stream to avoid harm and expose your '
                                 'target, roll Edge.\n\n\t7+: you get the shot you want and are “escorted” to a '
                                 'position of safety\n\t7-9: choose one:\n\t\t• Your story irritates your target (The '
                                 'MC will advance a relevant Threat Clock)\n\t\t• Someone on your team gets hurt off '
                                 'camera\n\t\t• Your story angers your employer\n\t\t• Your rushed narrative is '
                                 'misinterpreted by the public with unintended consequences',
            ),
            Move(
                'Nose for a Story',
                'Various mission bonuses. (Roll)',
                aliases=['nose'],
                full_description='At the start of a mission, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\n'
                                 'During the mission, spend 1 hold to invoke one of the following effects:\n\t• Ask one'
                                 ' question from the research list\n\t• Take +1 forward when monstering\n\t• Find a '
                                 'piece of evidence that links this mission to a current story; start a Story Clock and'
                                 ' a linked Noise Clock or roll to gather evidence',
            ),
            Move(
                'Gather Evidence',
                'Various effects on story and noise clocks. (Roll)',
                aliases=['gather'],
                full_description='When you gather evidence to break a story, roll Mind.\n\n\t10+: you get the evidence'
                                 ' you need, advance that Story Clock\n\t7-9: you get the evidence, but tip your hand '
                                 'to someone implicated in your story; tell the MC which clock to advance: a relevant '
                                 'Corporate Clock, the linked Noise Clock or the relevant Mission Clock (Legwork or '
                                 'Action, depending on which phase of the current mission you’re in)\n\t6-: the MC will'
                                 ' advance the Noise Clock and make a move\n\nIf the Story Clock reaches 0000 before '
                                 'the Noise Clock, the Reporter has broken the story before the implicated parties '
                                 'could cover up the evidence, or stop the investigation. The exact implications of '
                                 'this for the game will vary based on the story, but it should have a major impact on '
                                 'the implicated parties and will affect at least one Corporate Clock.\n\nIf the Noise '
                                 'Clock reaches 0000 before the Story Clock, the implicated parties have tied up all '
                                 'the loose ends and the story is dead. Now that damage control is complete, they can '
                                 'deal with the Reporter permanently. Advance any relevant Corporate or Threat Clocks.',
            ),
            Move(
                'Press Pass',
                'Bonus when revealing yourself to fast talk your way in.',
                aliases=['press', 'pass'],
                full_description='If you reveal your public persona to fast talk your way in, do not roll the dice, you'
                                 ' count as rolling a 10+.\nTake [intel] and advance the Legwork Clock.',
            ),
            Move(
                'Monstering',
                'You can corner someone and hound them with questions. (Roll)',
                full_description='When you corner someone and hound them with questions to get to the bottom of a '
                                 'story, roll Edge.\n\n\t10+: they tell you the truth, regardless of the consequences'
                                 '\n\t7-9: they give you enough to get you off their back, then when they’re safe, they'
                                 ' choose one:\n\t\t• they respond with fear\n\t\t• they respond with anger\n\t\t• they'
                                 ' respond with clinical calm',
            ),
            Move(
                '24/7 Livefeed',
                'Bonus to researching when scanning live feeds.',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime.',
            ),
            Move(
                'Filthy Assistants',
                'Bonus when using research obtained [intel]',
            ),
            Move(
                'Reliable Sources',
                'Research bonus',
            ),
            Move(
                'Warcorrepondent',
                'Bonus when Acting Under Pressure',
            )
        ]),
        Playbook('soldier', [
            Move(
                'I Love It When A Plan Comes Together',
                'Bonus [gear] and [intel]. (Roll)',
                aliases=['plan'],
                full_description='At the start of a mission, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\t'
                                 '6-: gain 1 hold anyway, but your opponent has predicted your every move; the MC will '
                                 'advance the Legwork Clock\n\nDuring the mission, spend 1 hold for one of the '
                                 'following effects:\n\t• You have that piece of gear that you need, right now\n\t• You'
                                 ' appear in a scene where you are needed, right now',
            ),
            Move(
                'Exit Strategy',
                'Bonus to getting the fuck out of there. (Roll)',
                aliases=['exit'],
                full_description='You always have an escape plan prepared. When shit hits the fan and you decide to '
                                 'bail out, roll Mind.\n\n\t7+: You escape the situation\n\t10+: choose one thing to '
                                 'leave behind\n\t7-9: choose two things\n\t\t• Your team\n\t\t• A mission objective'
                                 '\n\t\t• Identifiable evidence\n\t\t• Your staked Cred',
            ),
            Move(
                'Recruiter',
                'Contact / Hit the Street bonus. (Roll)',
                full_description='When you attempt to recruit a specialist or a team of specialists to directly assist '
                                 'with your mission, roll Edge.\n\n\t10+: choose 2\n\t7-9: choose 1\n\t\t• Reliable '
                                 'professional(s)\n\t\t• A small team (up to 5)\n\t\t• As competent as required',
            ),
            Move(
                'Slippery',
                'Prevents Corps from finding the teams involvement. (Roll)',
                full_description='At the end of a mission during which you planted or hid evidence to shift blame away '
                                 'from you and your team, name who you threw under the corporate bus and roll Edge.'
                                 '\n\n\t7+: the MC will not increase Corporate Clocks in the retaliation phase\n\t10+: '
                                 'the MC will reduce a Corporate Clock by one\n\t6-: create or increase the Threat '
                                 'Clock of whoever you threw under the bus',
            ),
            Move(
                'Here\'s the Plan',
                'Team bonus when you plan the mission and if you get paid.',
            ),
            Move(
                'Aura of Professionalism',
                'Bonus when Getting the Job or Getting Paid',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime',
            ),
            Move(
                'Corporate Knowledge',
                'Bonus when researching a corporation',
            ),
            Move(
                'Hands On Management',
                'Mix it Up bonus.',
            ),
            Move(
                'Steady Presence',
                'You can give pep-talks.',
            ),
            Move(
                'Tactical Operations',
                'Assess bonus',
            )
        ]),
        Playbook('tech', [
            Move(
                'Storage',
                'Pre-mission [gear] bonus. (Roll)',
                full_description='After receiving a job you may look through your accumulated parts and supplies for '
                                 'equipment that might help with the current mission. Roll Mind.\n\n\t10+: gain 3 '
                                 '[gear] relevant to your chosen area(s) of expertise.\n\t7-9: gain 1 [gear] relevant '
                                 'to your chosen area(s) of expertise.',
            ),
            Move(
                'Blend In',
                'You can act like you belong in places you don\'t. (Roll)',
                full_description='When you’re about to be caught somewhere you shouldn’t be, but look and act like you '
                                 'belong there, roll Cool.\n\n\t10+: no one thinks twice about your presence until you '
                                 'do something to attract attention\n\t7-9: you’ll be fine as long as you leave right '
                                 'now, but if you do anything else, your presence will arouse suspicion',
            ),
            Move(
                'Bypass',
                'You can subvert security measures. (Roll)',
                full_description='When you attempt to subvert security measures (bypassing a locked door, disabling an '
                                 'alarm, camera or motion detector, etc), roll Cool.\n\n\t7+: you successfully bypass '
                                 'the system without leaving a trace\n\t10+: you gain some valuable insight into the '
                                 'facility’s security, gain [intel]',
            ),
            Move(
                'Expert',
                'You get an area of expertise',
            ),
            Move(
                'Customiser',
                'You can examine and modify technology.',
            ),
            Move(
                'Analytic',
                'Assess replacement',
            ),
            Move(
                'Chromed',
                'Choose another piece of cyberware at character creation or in downtime',
            ),
            Move(
                'Diverse Interests',
                'Choose another area of expertise',
            ),
            Move(
                'Jack of All Trades',
                'Choose another area of expertise',
            ),
            Move(
                'Obsessive',
                'Research bonus',
            ),
            Move(
                'On It',
                'Replacement when helping or hindering someone in a topic relating to your expertise',
            ),
            Move(
                'Renaissance Man',
                'Choose another area of expertise',
            )
        ])
    ]
    GAME_MOVES = {
        'matrix': [
            Move(
                'Login',
                'When attempting to gain access to a system, login.',
                full_description='When you attempt to gain access to a system, roll Synth.\n\t10+: you’re in clean\n\t'
                                 '7-9: you’re in, but choose one:\n\t\tSysops are alerted\n\t\tICE is activated\n\t\t'
                                 'They’re onto you, +1 trace\n\t\tYour access is restricted – take -1 ongoing to matrix'
                                 ' moves in this system while your access is restricted\n\t6-: you’re in, but the MC '
                                 'chooses two, and a relevant clock is advanced',
            ),
            Move(
                'Jack out',
                'When you need to get out quick, jack out.',
                full_description='Jackout: When you, your programs, or your deck are about to be damaged by ICE, you '
                                 'can try to jack out. Roll Cool.\n\t10+: you disconnect yourself from the system '
                                 'before any serious harm occurs\n\t7-9: you jack out, but choose one:\n\t\tYou lose '
                                 'some data\n\t\tYou take some of the established consequences\n\t\tThe owners of the '
                                 'target system trace you to your current location6-: you take the established '
                                 'consequences... and you’re still connected'
            ),
            Move(
                'Bypass Countermeasures',
                'Outmaneuver or evade system countermeasures.',
                aliases=['bypass'],
                full_description='Bypass Countermeasures: When you attempt to outmaneuver or evade system '
                                 'countermeasures, roll Edge:\n\n\t10+: You’re straight through, no worries\n\t7-9: '
                                 'You’re through, but they’re still on you. Choose one:\n\t\tAdvance Mission Clock'
                                 '\n\t\tICE is activated\n\t\t+1 trace\n\t\tTake established consequences\n\t6-: You’re'
                                 ' caught, and the MC chooses one'
            ),
            Move(
                'Hijack Systems',
                'Attempt to gain control over a system.',
                aliases=['hijack'],
                full_description='Hijack System: When you attempt to gain control over a system, roll Mind.\n\n\t7+: '
                                 'You’re in control. You may search, destroy, or wreak whatever chaos you want.\n\t7-9:'
                                 '  Choose one:\n\t\tTime is limited, you can only do so much before they cut you off.'
                                 '\n\t\tAccess is limited, you can’t get into everything you want.\n\t\t+1 trace.'
            )
        ]
    }

    @commands.command(name='fuckmeup')
    async def fuck_me_up(self, ctx: commands.Context, damage: int = None) -> None:
        """Check how fucked you are after taking damage"""
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        modifier = 0
        if damage:
            try:
                modifier = int(damage)
            except ValueError:
                await ctx.send('```Incorrect damage given.```')
                return
        roll = dice1 + dice2 + modifier

        if roll >= 10:
            await ctx.send(
                f'```Oh you fucked up now, you rolled a {roll}. Choose 1:\n\tЂ you’re out of action: unconscious, '
                f'trapped, incoherent or panicked\n\tЂ take the full harm of the attack, before it was reduced by '
                f'armour; if you already took the full harm of the attack, take +1-harm\n\tЂ lose the use of a piece of'
                f' cyberware until you can get it repaired\n\tЂ lose a body part (arm, leg, eye)```')
        elif 7 <= roll <= 9:
            await ctx.send(
                f'```You\'re going to have to suck off the MC on this one, you rolled a {roll}. The MC will choose 1:'
                f'\n\tЂ you lose your footing\n\tЂ you lose your grip on whatever you’re holding\n\tЂ you lose track of'
                f' someone or something you’re attending to\n\tЂ someone gets the drop on you```')
        else:
            await ctx.send(f'```You rolled {roll}. You\'re gucci flip flops fam *dabs* haha yeet :3```')

    @commands.command(name='matrix')
    async def print_matrix_moves(self, ctx: commands.Context) -> None:
        """Displays a list of matrix-specific moves"""
        matrix_moves = 'Use the following commands to find detailed information about each move.\n'
        for move in self.GAME_MOVES['matrix']:
            matrix_moves += f'\n\t{move}'

        await ctx.send(f'```{matrix_moves}```')

    @commands.command(name='cred')
    async def print_cred_options(self, ctx: commands.Context) -> None:
        """Shows you what you can do with cred"""
        await ctx.send("""```Spending 1 Cred will get you:
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
        >cutting-edge, military or extortionately expensive gear from a fixer (cyberdecks, military vehicles, most\
    cyberware)```""")

    @commands.command(name='weapons')
    async def print_weapons(self, ctx: commands.Context) -> None:
        """Displays a list of weapons and their profiles"""
        await ctx.send("""```Firearms:
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
        » Shuriken or throwing knives (2-harm close numerous)```""")

    @commands.command(name='currency')
    async def print_currency(self, ctx: commands.Context) -> None:
        """Print rep/cred rules"""
        await ctx.send("""```Rep is a measure of how well respected/feared/liked a character is. {10 max}
Cred is a measure of the funds a character has access to.

Before rolling to get the job, stake your Rep. {Maximum 3 per player}
When getting paid you may take back double the amount of staked Rep in either Rep OR Cred.```""")

    @commands.command(name='cyberware')
    async def print_cyberware(self, ctx: commands.Context) -> None:
        """Print cybereware options"""
        await ctx.send("""```
Cybereyes
When you have cybereyes installed, choose two of the following tags:
+thermographic, +light amplification, +magnification, +flare compensation, +recording, +encrypted, +inaccessible \
partition
When your cybereyes give you advantage in the situation add your synth to the roll in addition to the relevant stat.

Cyberears
When you have cyberears installed, choose two of the following tags:
+dampening, +wide frequency, +recording, +encrypted, +inaccessible partition
When your cyberears give you advantage in the situation add your synth to the roll in addition to the relevant stat.

Cybercoms
When you have cybercoms installed, choose two of the following tags:
+encrypted, +jamming, +recording, +satellite relay, +inaccessible partition
When your cybercoms give you advantage in the situation add your synth to the roll in addition to the relevant stat.

Cyberarm
When you have a cyberarm installed, select one of the following packages below (You may only have one package installed\
 in an arm at a time):
    Courier:
        Your arm has undetectable storage for small objects, this storage additionally allows you to retain a [gear] \
between missions.
        Your arm is indistinguishable from a biological arm to all scans and has the +encrypted tag.

    Tinkerer:
        Your arm has a suite of tools installed in it and additional precision that goes beyond human capabilities.
        When your tools and/or increased precision give you advantage in the situation add your synth to the roll in \
addition to the relevant stat.

    Brawler:
        Your arm has been enhanced to endure and inflict severe punishment.
        +2 harm when using a melee weapon.
        +1 armour when receiving harm from a melee weapon.```""")
        await ctx.send("""```
Cyberlegs
When you have cyberlegs installed, choose two of the following tags:
+encrypted, +fast, +quiet, +powerful, +stabilizing, +rough terrain 
When your cyberlegs give you advantage in the situation add your synth to the roll in addition to the relevant stat.

Dermal Plating
The +AP tag on weapons used against you now only cause you to subtract 1 armour value.
+1 armour

Implant Weapon
When you have a implant weapon installed, choose two of the following tags:
+fast, +discrete, -clumsy, -reload, +quiet, +powerful, +undisarmable
All implant weapons installed have the two tags chosen in additonal to the weapon's natural tags.

Muscle Grafts
When your muscle grafts give you an advantage in the situation add your synth to the roll in addition to the relevant \
stat.

Neural Interface
When you have a neural interface installed you are able to jack in to the matrix, interface with drones and drive \
vehicles.
When you have a neural interface installed, select one of the following packages below (You may only have one package \
installed at a time):
    Multi-Tasker:
        Your neural interface allows you to perform 2 separate matrix actions at once, or act both in the matrix and \
meatspace at once.

    Hacker:
        Choose two of the following tags:
        +high capacity, +high speed, +inaccesible partition, +encrypted
        When rolling the research move add your synth to the roll in addition to the relevant stat.

    Combatant:
        When using a weapon with the +linked tag add +2 harm to all damage done with that weapon.
        You may also precisely define targets when using a weapon with the +area tag.

Synthetic Nerves
When your quick reactions give you an advantage in the situation add your synth to the roll in addition to the relevant\
 stat.```""")
        await ctx.send("""```
Skillwires
When you have skillwires installed, choose one stat.
When rolling with the selected stat and a weak hit occurs, choose one less negative outcome. This cannot reduce \
negative outcomes to less than one.

Tactical Computer
When assessing a situation take +1 hold even on a miss.
When using a weapon with the +linked tag add your synth to the mix it up roll in addition to the relevant stat.

Negative Tags:
    Negative tags on a piece of cyberware cannot be removed, except by replacing the entire piece of cyberware.
    +damaging: On a miss the user of this cyberware takes +1 Harm.
    +hardware decay: Each use of this cyberware gives -1 forward when using this cyberware again. Spending 1 cred per \
-1 forward on a hit the street roll can reset your cyberware.
    +substandard: When selecting +tags for this cyberware select one less than stated.
    When adding your synth to a roll because of this cyberware, add half your synth instead.
    +unreliable:  Weak hits using this cyberware count as a miss.```""")
