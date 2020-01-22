import pickle

from pbabot.games import Move

basic = [
    Move(
        'Act Under Pressure',
        'When you race against the clock, act while in danger, or act to avoid danger, roll Cool.\n\t10+: you do it, '
        'no problem\n\t7-9: you stumble, hesitate, or flinch: the MC will offer you a worse outcome, hard bargain, '
        'or ugly choice',
        '.actunderpressure'
    ),
    Move(
        'Apply First Aid',
        'When you treat someone’s wounds using appropriate medical equipment, roll Cool.\n\t10+: if their Harm Clock '
        'is at 2100 or less, reduce their harm by two segments. If their Harm Clock is at more than 2100, '
        'reduce their harm by one segment\n\t7-9: reduce their harm by one segment. If their Harm Clock is still at '
        'more than 2100, they take -1 ongoing until they receive proper medical attention',
        '.applyfirstaid',
        '.firstaid',
        '.aid'
    ),
    Move(
        'Assess',
        'When you closely study a person, place or situation, or when you quickly size up an opponent or a charged '
        'situation, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nIn the ensuing action, you may spend 1 '
        'hold at any time to ask the MC a question from the list below if your examination could have revealed the '
        'answer. The MC may ask you questions to clarify your intent. Take +1 forward when acting on the '
        'answers.\n\n\tЂ What potential complication do I need to be wary of?\n\tЂ What do I notice despite an effort '
        'to conceal it?\n\tЂ How is ______ vulnerable to me?\n\tЂ How can I avoid trouble or hide here?\n\tЂ What is '
        'my best way in/way out/way past?\n\tЂ Where can I gain the most advantage?\n\tЂ Who or what is my biggest '
        'threat in this situation?\n\tЂ Who or what is in control here?',
        '.assess'
    ),
    Move(
        'Play Hardball',
        'When you get in someone’s face threatening violence and you intend to carry through, roll Edge.\n\n\t10+: NPCs do what you want. PCs choose: do what you want, or suffer the established consequences\n\t7–9: For NPCs, the MC chooses 1:\n\t\tЂ they attempt to remove you as a threat, but not before suffering the established consequences\n\t\tЂ they do it, but they want payback. Add them as a Threat\n\t\tЂ they do it, but tell someone all about it. Advance the appropriate Mission Clock\nPCs choose: do what you want, or suffer the established consequences. They gain +1 forward to act against you.',
        '.playhardball',
        '.hardball'
    ),
    Move(
        'Acquire Agricultural Property',
        'When you hit 0000 on your Harm Clock, roll Meat.\n\n\t10+: you survive until the medics arrive\n\t7-9: you survive at a cost. Pick one: +owned, substandard treatment (-1 to a stat), cyberware damage (give one piece of cyberware a negative tag)\n\t6-: you bleed out on the street',
        '.amidead'
    ),
    Move(
        'Mix it Up',
        'When you use violence against an armed force to seize control of an objective, state that objective and roll Meat.\n\n\t7+: you achieve your objective\n\t7-9: choose 2:\n\t\tЂ you make too much noise. Advance the relevant Mission Clock\n\t\tЂ you take harm as established by the fiction\n\t\tЂ an ally takes harm as establish',
        '.mixitup',
        '.mix'
    ),
    Move(
        'Research',
        'When you investigate a person, place, object, or service using a library, dossier or database (or combination of them), ask a question from the list below and roll Mind.\n\n\t10+: take [intel]; the MC will answer your question and answer a follow-up question from this list as well:\n\t\tЂ Where would I find ______?\n\t\tЂ How secure is ______?\n\t\tЂ Who or what is related to ______?\n\t\tЂ Who owned or employed ______?\n\t\tЂ Who or what is ______ most valuable to?\n\t\tЂ What is the relationship between ______ and ______?\n\t7-9: take [intel]; the MC will answer your question\n\t6-: the MC will answer your question... and make a move',
        '.research'
    ),
    Move(
        'Fast Talk',
        'When you try to convince someone to do what you want with promises, lies or bluster, roll Style.\n\n\t10+: NPCs do what you want. PCs choose whether to do it or not. If they do, they mark experience. If they don’t, they must act under pressure to go against your stated wishes.\n\t7-9: NPCs do it, but someone will find out: the MC will advance the appropriate Countdown Clock. For PCs choose one:\n\t\tЂ If they do what you want, they mark experience\n\t\tЂ If they don’t do it, they must act under pressure to go against your stated wishes\n\tThen its up to them.',
        '.fasttalk',
    ),
    Move(
        'Hit the Street',
        'When you go to a Contact for help, roll Style.\n\n\t7+: You get what you want.\n\t10+: You get a little something extra (choose either [intel] or [gear]).\n\t7-9: choose 2 from the list below:\n\t\tЂ Your request is going to cost you extra\n\t\tЂ Your request is going to take some time to put together\n\t\tЂ Your request is going to attract unwanted attention, complications or consequences\n\t\tЂ Your contact needs you to help them out with something. If you turn them down take -1 ongoing to this move till you make it right',
        '.hitthestreet'
    ),
    Move(
        'Go Under the Knife',
        'When you have new cyberware installed by a street doctor, roll Cred spent (max +2).\n\n\t10+: the operation was a complete success\n\t7-9: the cyberware doesn’t work as well as advertised, choose one: +unreliable, +substandard, +hardware decay, +damaging.\n\t6-: there have been... complications\n\nWhen you have new cyberware installed in accordance with a corporate contract, ignore all of that bad stuff. You’re +owned. Your cyberware works exactly the way they intend it.',
        '.goundertheknife',
        '.undertheknife',
        '.under',
        '.knife'
    ),
    Move(
        'Harm',
        'NULL',
        '.fuckmeup'
    ),
    Move(
        'Harm 10',
        'Choose 1:\n\tЂ you’re out of action: unconscious, trapped, incoherent or panicked\n\tЂ take the full harm of the attack, before it was reduced by armour; if you already took the full harm of the attack, take +1-harm\n\tЂ lose the use of a piece of cyberware until you can get it repaired\n\tЂ lose a body part (arm, leg, eye)'
    ),
    Move(
        'Harm 7',
        'The MC will choose 1:\n\tЂ you lose your footing\n\tЂ you lose your grip on whatever you’re holding\n\tЂ you lose track of someone or something you’re attending to\n\tЂ someone gets the drop on you'
    ),
    Move(
        'Get the Job',
        'When you negotiate the terms of a job, roll Edge.\n\n\t10+: choose 3 from the list below\n\t7-9: choose 1 from the list below\n\t\tЂ the employer provides useful information ([intel])\n\t\tЂ the employer provides useful assets ([gear])\n\t\tЂ the job pays well\n\t\tЂ the meeting doesn’t attract attention\n\t\tЂ the employer is identifiable',
        '.getthejob',
        '.job'
    ),
    Move(
        'Getting Paid',
        'When you go to a meet to get paid by your employer, roll and add the number of unfilled segments on the '
        'Legwork Clock.\n\n\t10+: choose 3 from the list below\n\t7-9: choose 1 from the list below\n\t\tЂ It’s not a '
        'set-up or an ambush\n\t\tЂ You are paid in full\n\t\tЂ The employer is identifiable\n\t\tЂ The meeting '
        'doesn’t attract the attention of outside parties\n\t\tЂ You learned something from the mission; everyone '
        'marks experience',
        '.gettingpaid',
        '.getpaid',
        '.paid'
    )
]

playbooks = {
    'driver': [
        Move(
            'Hot Shit Driver',
            'Bonus while high-tension driving. (Roll)',
            'hotshitdriver',
            fulldescription='When you’re driving a cyber-linked vehicle in a high-pressure situation, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nYou may spend 1 hold to do one of the following:\n\t• Avoid one external danger (a rocket, a burst of gunfire, a collision, etc)\n\t• Escape one pursuing vehicle\n\t• Maintain control of the vehicle\n\t• Impress, dismay or frighten someone',
        ),
        Move(
            'Wheels',
            'You start with a car.'
        ),
        Move(
            'Second Skin',
            'When jacked into your cehicle with a neural interface you get bonuses to your rolls.'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime.'
        ),
        Move(
            'Daredevil',
            'Bonus when you drive straight into danger.'
        ),
        Move(
            'Drone Jockey',
            'You get two drones.'
        ),
        Move(
            'Iceman',
            'Fast talk replacement.'
        ),
        Move(
            'Right Tool for the Job',
            'You have two additional cyber-linked vehicles.'
        ),
        Move(
            'Sweet Ride',
            'Replacement and bonus to Hit the Street while in your vehicle.'
        )
    ],
    'fixer': [
        Move(
            'Hustling',
            'Gives hustling jobs. (Roll)'
            'hustling',
            fulldescription='You have people who work for you in various ways. You start with 2-crew and two jobs from the list below. Between missions, choose a number of those jobs equal to or less than your current crew, describe what each job is, and roll Edge.\n\n\t10+: you profit from each of your jobs\n\t7-9: one of them is a Disaster and you Profit from the rest\n\t6-: everything’s FUBAR. The MC will make a move based on the Disaster for each job\n\nChoose two:\n\tЂ Surveillance: You have a small network of informants who report on events; you then sell that information\n\t\t• Profit: gain [intel]\n\t\t• Disaster: someone acts on bad info\n\tЂ Debt collection: You have a few burly looking fuckers who collect outstanding debts\n\t\t• Profit: gain [gear]\n\t\t• Disaster: someone’s out of pocket\n\tЂ Petty theft: You have a small crew who perform minor local robberies\n\t\t• Profit: gain [gear]\n\t\t• Disaster: they robbed the wrong guy\n\tЂ Deliveries: People hire you to transport things and you have a driver who takes care of that\n\t\t• Profit: gain 1 Cred\n\t\t• Disaster: the delivery never arrives\n\tЂ Brokering deals: You arrange for the right people to meet each other\n\t\t• Profit: gain 1 Cred\n\t\t• Disaster: the deal that you arranged goes wrong\n\tЂ Technical work: You have a couple of techs whom you supply with work\n\t\t• Profit: gain [gear]\n\t\t• Disaster: something bad happens to someone else’s property\n\tЂ Pimping: You manage a small stable of physical or virtual sex workers\n\t\t• Profit: gain [intel]\n\t\t• Disaster: something goes wrong with a customer\n\tЂ Addictive substances: You manage a small lab producing either drugs or simstim chips\n\t\t• Profit: gain [intel]\n\t\t• Disaster: something goes wrong for a user or for the lab itself',
        ),
        Move(
            'I Know People',
            'Specialized contact decleration. (Roll)',
            'iknowpeople',
            fulldescription='Once per mission you may introduce a new Contact. Name the contact, say what they do, then roll Style.\n\n\t10+: you’ve worked with the contact before; they have talent. Write them down as a Contact\n\t7-9: you’ve never met them before, they’re an unknown quantity\n\t6-: you know them all right. Tell the MC why they dislike you\n\nAfter you’ve rolled, describe how you contact them; the MC will ask some questions.',
        ),
        Move(
            'Reputation',
            'Various social (Roll).',
            'reputation',
            fulldescription = 'When you meet someone of consequence who might have heard of you, roll Edge. On a hit, say what they know about you. On a 10+, take +1 forward with them. On a miss, the MC will decide what they’ve heard about you, if anything. Either you or the MC can say whether someone is “of consequence”, but once you’ve made the reputation move on someone, they’re “of consequence” and will be a recurring part of the story.',
        ),
        Move(
            'Backup',
            'You have a group of associates'
        ),
        Move(
            'Balls in the Air',
            '+1 crew and choose another job.'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime'
        ),
        Move(
            'Deal of a Lifetime',
            'Hit the Street bonus when selling something'
        ),
        Move(
            'Facetime',
            'Fast talk bonus'
        ),
        Move(
            'Hard to Find',
            'Hit the Street bonus.'
        ),
        Move(
            'Sales Engineer',
            'Produce equipment bonus.'
        ),
        Move(
            'Smooth',
            'Helping or hindering replacement'
        ),
        Move(
            'Street King Pin',
            '+1 crew, choose an additional job.'
        ),
        Move(
            'Word on the Street',
            'Meatspace research bonus'
        )
    ],
    'hacker': [
        # Move(
        #     'Console Cowboy',
        #     'Hold over systems (Roll)',
        #     'consolecowboy',
        #     fulldescription='Console cowboy: When you connect to a secure system, roll Mind.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nWhile in that system, you may spend 1 hold for any of the following effects:\n\t• Prevent a construct from triggering an alert\n\t• Avoid an ICE routine executed against you, your deck, or your programs\n\t• Increase your hold over compromised security or manipulated systems by 1',
        # ),
        Move(
            'Jack in',
            'You get access the matrix moves'
        ),
        Move(
            'Antivirus Subscription',
            'Legwork roll+cred for chrome chips',
            'antivirus',
            'antivirussubscription',
            fulldescription='Antivirus Subscription: During legwork, you may request a delivery of 2 Single Use Chrome Chips. Roll + Cred Spent:\n\t7+: Mark 2 gear to spend in the matrix.\n\t10+: Next day delivery.'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime'
        ),
        Move(
            'Inside Job',
            'When you login through a compromised site, +1 matrix moves.',
            'insidejob'
        ),
        Move(
            'I\'ve had worse',
            '+1 armour against ice subroutines.',
            'ivehadworse'
        ),
        Move(
            'Humans are Easy Prey',
            'Go on the offensive against Sysop, roll synth',
            'humansareeasyprey',
            fulldescription='Humans are such easy prey: When you go on the offensive against a Sysop, roll Synth:\n\n\t10+: Choose two, or one twice:\n\t7-9: Choose one:\n\t\tYou shake them off your trail, for now.\n\t\tYou damage their rig, slowing them down.\n\t\tYou overload their system, zapping their brain'
        ),
        Move(
            'Rep',
            'Fast talk and play hardball replacements while in the matrix.',
            'rep',
            fulldescription='Rep: When you appear in the Matrix with a recognisable avatar, roll Synth instead of Style for fast talk and instead of Edge for play hardball.\nWhen your reputation gets you into trouble, mark experience'
        ),
        Move(
            'Search Optimisation',
            'Matrix research bonus',
            'searchoptimisation',
            fulldescription='When you research a topic in the Matrix, you may always ask a follow up question. On a 10+, take an additional [intel].'
        ),
        Move(
            'Rig Enthusiast',
            'Extra deck tag'
        ),
        Move(
            'Sneak Door Beta',
            'Create a backdoor for future use.',
            'sneakdoorbeta',
            fulldescription='Sneakdoor Beta: When you have successfully infiltrated a system, you may create a backdoor for quick re-entry. Roll Mind:\n\n\t10+: It’s set up, it’s clean, you’re the only one that knows about it.\n\t7-9: It’s set up, but choose one:\n\t\tSysops will find it sooner rather than later\n\t\tIt’s not silent entry, using it may raise alarms\n\t\tIt’s not a clean backdoor, may still have to attempt to login '
        ),
        Move(
            'Tech Support',
            'Bonus when helping or interfering while in the matrix'
        ),
        Move(
            'Diabolus Ex Machina',
            'When Ice is activated against you, roll +synth',
            'diabolusexmachina',
            fulldescription='When ICE is activated against you in the Matrix, roll +Synth:\n\n\t10+: The ICE is under your control.\n\t7-9: Choose one temporary effect:\n\t\tThe ICE is deactivated, this server is open season.\n\t\tThe ICE is retargeted, you’re not its priority anymore.\n\t\tYou slip past it, it’s the next guy’s problem.'
        )
    ],
    'hunter': [
        Move(
            'It All Fits Together',
            'Research bonus. (Roll)',
            'itallfitstogether',
            'itallfits',
            fulldescription='You’re a master of making connections between seemingly unrelated events. At the start of a mission, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nAs you put everything together during the mission, spend 1 hold at any time to ask a question from the research list.',

        ),
        Move(
            'Big Game Hunter',
            'Bonus when springing a trap against a researced target. (Roll)',
            'biggamehunter',
            fulldescription='When you spring a trap for a target you have investigated, roll Edge.\n\n\t7+: you have them trapped, the only way out is through you\n\t10+: they are at your mercy; if the target attempts to escape, roll Edge instead of Meat to mix it up',

        ),
        Move(
            'Sniper',
            'Bonus when hiding. (Roll)',
            'sniper',
            fulldescription='When you set up a covered and concealed place to hide, roll Cool.\n\n\t10+: choose 3\n\t7-9: choose 2\n\t\t• Your site is well hidden\n\t\t• Your site has excellent cover\n\t\t• Your site has an excellent field of view\n\t\t• You have a similarly covered and concealed backup location\n\t\t• Your spot is well secured\n\nThen describe your hide site.',

        ),
        Move(
            'Ear to the Ground',
            'Meatspace research bonus'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime'
        ),
        Move(
            'Deadbeat',
            'Hit the Street bonus'
        ),
        Move(
            'Enhance',
            'Research bonus'
        ),
        Move(
            'Eye for Detail',
            'Bonus when calmly assessing a person or place'
        ),
        Move(
            'Human Terrain',
            'Bonus when investigating a group'
        ),
        Move(
            'On the Trail',
            'Additional use of intel against a single person'
        ),
        Move(
            'See the Angles',
            'At the start of the action phase gain [intel] and [gear].'
        )
    ],
    'infiltrator': [
        Move(
            'Covert Entry',
            'Bonus when infilatrating alone. (Roll)',
            'covertentry',
            fulldescription='When you attempt to infiltrate a secure area alone, roll Cool.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nAs the MC describes the infiltration and the security measures you must overcome, you may spend 1 hold to describe how you overcome the obstacle and:\n\t• Bypass a security system or guard.\n\t• Disable a security system you have bypassed.\n\t• Disable a guard.\n\t• Escape notice',

        ),
        Move(
            'Case the Joint',
            'Bonus when examining a locations weaknesses. (Roll)',
            'casethejoint',
            fulldescription='When you take time to examine a location for security weaknesses you can exploit, roll Edge.\n\n\t10+: gain three [intel]\n\t7-9: gain [intel]\n\nYou may spend this [intel] in the normal way, or you can spend one point of this [intel] to ask questions from the assess or research lists.',

        ),
        Move(
            'Plan B',
            'When shit hits the fan and you have to get out. (Roll)',
            'planb',
            fulldescription='When shit hits the fan and you have to get out, name your escape route and roll Cool.\n\n\t10+: sweet, you’re gone\n\t7–9: you can go or stay, but if you go it costs you: leave something behind, or take something with you; in either case, the MC will tell you what\n\t6-: you’re caught in a vulnerable position, half in and half out. The MC will make a move',

        ),
        Move(
            'Psychological Warfare',
            'When you attempt to demoralise the enemy by leaving evidence of violence. (Roll)',
            'psychologicalwarfare',
            'psychwarfare',
            fulldescription='When you attempt to influence the morale of your enemies by leaving evidence of violence while remaining undetected, roll Edge.\n\n\t7+: your enemies are impressed and overly cautious, scared and demoralised, or angry and careless (MC’s choice)\n\t10+: you choose',

        ),
        Move(
            'Cat Burgler',
            'On the job [gear] procurement. Used with Covert Entry'
        ),
        Move(
            'Face',
            'On the job [intel] procurement. Used with Covert Entry'
        ),
        Move(
            'Assassin',
            'Bonus to attacking unexpectedly.'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime.'
        ),
        Move(
            'Jack In',
            'You gain access to matrix moves.'
        ),
        Move(
            'Master of Disguise',
            'Fast talk bonus'
        ),
        Move(
            'Mother Duck',
            'Allows Covert Entry hold you spend to work for the whole team.'
        ),
        Move(
            'Stealth Operative',
            'Assess bonus'
        )
    ],
    'killer': [
        Move(
            'Serious Badass',
            'Bonus when entering a charged situation. (Roll)',
            'seriousbadass',
            fulldescription='When you enter a charged situation, roll Style.\n\n\t10+: gain 2 hold\n\t7–9: gain 1 hold\n\t6-: your enemies identify you immediately as their foremost threat\n\nSpend 1 hold to make eye contact with an NPC present, who freezes or flinches and can’t act until you break it off.',

        ),
        Move(
            'Trained Eye',
            'Bonus when sizing up a person, vehicle, drone or gang. (Roll)',
            'trainedeye',
            fulldescription='When you evaluate a person, vehicle, drone or gang, roll Cool.\n\n\t7+: ask the target “How are you vulnerable to me?” Take +1 forward when acting on the answer\n\t10+: gain +1 ongoing when acting against that target',

        ),
        Move(
            'Custom Weapon',
            'You begin with a custom weapon.'
        ),
        Move(
            'Emotionless',
            'Play hard ball replacement.'
        ),
        Move(
            'Hard',
            'Harm move bonus'
        ),
        Move(
            'Loaded for Bear',
            'Choose another bonus weapon.'
        ),
        Move(
            'More Machine than Meat',
            'Choose another piece of cyberware at character creation or in downtime.'
        ),
        Move(
            'Corporate Secrets',
            'Bonus when researching a corporation'
        ),
        Move(
            'Military Background',
            'Bonus when hitting the street.'
        ),
        Move(
            'Milspecs',
            'Bonus to mix it up.'
        )
    ],
    'pusher': [
        Move(
            'Driven',
            'Bonus when the mission furthers your vision. (Roll)',
            'driven',
            fulldescription='When you begin a mission that furthers your vision, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nYou may spend 1 hold before rolling any other move to take +1 or -2 forward to the move.',

        ),
        Move(
            'Vision Thing',
            'Bonus when passionately advocating your vision. (Roll)',
            'visionthing',
            fulldescription='When you have time and space for an emotional connection with someone and you passionately advocate for your vision, roll Style.\n\n\t10+: gain 2 hold\n\t7-9: gain 1 hold\n\nSpend 1 hold to have the targeted NPCs:\n\t• give you something you want\n\t• do something you ask\n\t• fight to protect you or your cause\n\t• disobey an order given by someone with authority or leverage over them\n\nWhen you use this move on a PC, spend your hold to help or interfere as if you had rolled a 10+ (i.e. give them +1 or -2). If you miss against a PC, they gain 2 hold against you which they can use in the same way.',

        ),
        Move(
            'Believers',
            'You are part of a gang, tribe, band, corporation, or similar group'
        ),
        Move(
            'Bring it on Home',
            'Bonus when using Vision Thing or One Million Points of Light'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime'
        ),
        Move(
            'Famous',
            'Bonus against people who recognise you.'
        ),
        Move(
            'Inner Circle',
            'You have a loyal inner circle of believers'
        ),
        Move(
            'One Million Points of Lights',
            'Bonus to vision thing.'
        ),
        Move(
            'Opportunistic',
            'Replacement when helping or interfering.'
        ),
        Move(
            'People Person',
            'Hit the Street bonus.'
        ),
        Move(
            'Rabble Rouser',
            'Vision Thing bonus'
        ),
        Move(
            'Silver Tongue',
            'Fast Talk bonus'
        )
    ],
    'reporter': [
        Move(
            'Live and on the Air',
            'You can broadcast a stream to hurt your target. (Roll)',
            'liveandontheair',
            'live',
            'liveontheair',
            fulldescription='When you go live from the scene and broadcast a stream to avoid harm and expose your target, roll Edge.\n\n\t7+: you get the shot you want and are “escorted” to a position of safety\n\t7-9: choose one:\n\t\t• Your story irritates your target (The MC will advance a relevant Threat Clock)\n\t\t• Someone on your team gets hurt off camera\n\t\t• Your story angers your employer\n\t\t• Your rushed narrative is misinterpreted by the public with unintended consequences',

        ),
        Move(
            'Nose for a Story',
            'Various mission bonuses. (Roll)',
            'noseforastory',
            'nose',
            fulldescription='At the start of a mission, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\nDuring the mission, spend 1 hold to invoke one of the following effects:\n\t• Ask one question from the research list\n\t• Take +1 forward when monstering\n\t• Find a piece of evidence that links this mission to a current story; start a Story Clock and a linked Noise Clock or roll to gather evidence',

        ),
        Move(
            'Gather Evidence',
            'Various effects on story and noise clocks. (Roll)',
            'gatherevidence',
            'gather',
            fulldescription='When you gather evidence to break a story, roll Mind.\n\n\t10+: you get the evidence you need, advance that Story Clock\n\t7-9: you get the evidence, but tip your hand to someone implicated in your story; tell the MC which clock to advance: a relevant Corporate Clock, the linked Noise Clock or the relevant Mission Clock (Legwork or Action, depending on which phase of the current mission you’re in)\n\t6-: the MC will advance the Noise Clock and make a move\n\nIf the Story Clock reaches 0000 before the Noise Clock, the Reporter has broken the story before the implicated parties could cover up the evidence, or stop the investigation. The exact implications of this for the game will vary based on the story, but it should have a major impact on the implicated parties and will affect at least one Corporate Clock.\n\nIf the Noise Clock reaches 0000 before the Story Clock, the implicated parties have tied up all the loose ends and the story is dead. Now that damage control is complete, they can deal with the Reporter permanently. Advance any relevant Corporate or Threat Clocks.',

        ),
        Move(
            'Press Pass',
            'Bonus when revealing yourself to fast talk your way in.',
            'presspass',
            'press',
            'pass',
            fulldescription='If you reveal your public persona to fast talk your way in,do not roll the dice, you count as rolling a 10+.\nTake [intel] and advance the Legwork Clock.',

        ),
        Move(
            'Monstering',
            'You can corner someone and hound them with questions. (Roll)',
            'monstering',
            fulldescription='When you corner someone and hound them with questions to get to the bottom of a story, roll Edge.\n\n\t10+: they tell you the truth, regardless of the consequences\n\t7-9: they give you enough to get you off their back, then when they’re safe, they choose one:\n\t\t• they respond with fear\n\t\t• they respond with anger\n\t\t• they respond with clinical calm',

        ),
        Move(
            '24/7 Livefeed',
            'Bonus to researching when scanning live feeds.'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime.'
        ),
        Move(
            'Filthy Assistants',
            'Bonus when using research obtained [intel]'
        ),
        Move(
            'Reliable Sources',
            'Research bonus'
        ),
        Move(
            'Warcorrepondent',
            'Bonus when Acting Under Pressure'
        )
    ],
    'soldier': [
        Move(
            'I Love It When A Plan Comes Together',
            'Bonus [gear] and [intel]. (Roll)',
            'iloveitwhenaplancomestogether',
            'plan',
            fulldescription='At the start of a mission, roll Edge.\n\n\t10+: gain 3 hold\n\t7-9: gain 1 hold\n\t6-: gain 1 hold anyway, but your opponent has predicted your every move; the MC will advance the Legwork Clock\n\nDuring the mission, spend 1 hold for one of the following effects:\n\t• You have that piece of gear that you need, right now\n\t• You appear in a scene where you are needed, right now',

        ),
        Move(
            'Exit Strategy',
            'Bonus to getting the fuck out of there. (Roll)',
            'exitstrategy',
            'exit',
            fulldescription='You always have an escape plan prepared. When shit hits the fan and you decide to bail out, roll Mind.\n\n\t7+: You escape the situation\n\t10+: choose one thing to leave behind\n\t7-9: choose two things\n\t\t• Your team\n\t\t• A mission objective\n\t\t• Identifiable evidence\n\t\t• Your staked Cred',

        ),
        Move(
            'Recruiter',
            'Contact / Hit the Street bonus. (Roll)',
            'recruiter',
            fulldescription='When you attempt to recruit a specialist or a team of specialists to directly assist with your mission, roll Edge.\n\n\t10+: choose 2\n\t7-9: choose 1\n\t\t• Reliable professional(s)\n\t\t• A small team (up to 5)\n\t\t• As competent as required',

        ),
        Move(
            'Slippery',
            'Prevents Corps from finding the teams involvement. (Roll)',
            'slippery',
            fulldescription='At the end of a mission during which you planted or hid evidence to shift blame away from you and your team, name who you threw under the corporate bus and roll Edge.\n\n\t7+: the MC will not increase Corporate Clocks in the retaliation phase\n\t10+: the MC will reduce a Corporate Clock by one\n\t6-: create or increase the Threat Clock of whoever you threw under the bus',

        ),
        Move(
            'Here\'s the Plan',
            'Team bonus when you plan the mission and if you get paid.'
        ),
        Move(
            'Aura of Professionalism',
            'Bonus when Getting the Job or Getting Paid'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime'
        ),
        Move(
            'Corporate Knowledge',
            'Bonus when researching a corporation'
        ),
        Move(
            'Hands On Management',
            'Mix it Up bonus.'
        ),
        Move(
            'Steady Presence',
            'You can give pep-talks.'
        ),
        Move(
            'Tactical Operations',
            'Assess bonus'
        )
    ],
    'tech': [
        Move(
            'Storage',
            'Pre-mission [gear] bonus. (Roll)',
            'storage',
            fulldescription='After receiving a job you may look through your accumulated parts and supplies for equipment that might help with the current mission. Roll Mind.\n\n\t10+: gain 3 [gear] relevant to your chosen area(s) of expertise.\n\t7-9: gain 1 [gear] relevant to your chosen area(s) of expertise.',

        ),
        Move(
            'Blend In',
            'You can act like you belong in places you don\'t. (Roll)'
            'blendin',
            fulldescription='When you’re about to be caught somewhere you shouldn’t be, but look and act like you belong there, roll Cool.\n\n\t10+: no one thinks twice about your presence until you do something to attract attention\n\t7-9: you’ll be fine as long as you leave right now, but if you do anything else, your presence will arouse suspicion',

        ),
        Move(
            'Bypass',
            'You can subvert security measures. (Roll)',
            'bypass',
            fulldescription='When you attempt to subvert security measures (bypassing a locked door, disabling an alarm, camera or motion detector, etc), roll Cool.\n\n\t7+: you successfully bypass the system without leaving a trace\n\t10+: you gain some valuable insight into the facility’s security, gain [intel]',

        ),
        Move(
            'Expert',
            'You get an area of expertise'
        ),
        Move(
            'Customiser',
            'You can examine and modify technology.'
        ),
        Move(
            'Analytic',
            'Assess replacement'
        ),
        Move(
            'Chromed',
            'Choose another piece of cyberware at character creation or in downtime'
        ),
        Move(
            'Diverse Interests',
            'Choose another area of expertise'
        ),
        Move(
            'Jack of All Trades',
            'Choose another area of expertise'
        ),
        Move(
            'Obsessive',
            'Research bonus'
        ),
        Move(
            'On It',
            'Replacement when helping or hindering someone in a topic relating to your expertise'
        ),
        Move(
            'Renaissance Man',
            'Choose another area of expertise'
        )
    ]
}

matrix = [
    Move(
        '[OG/CUSTOM] Login',
        'When attempting to gain access to a system, login.',
        '.login',
        fulldescription='When you attempt to gain access to a system, roll Synth.\n\t10+: you’re in clean\n\t7-9: you’re in, but choose one:\n\t\tSysops are alerted\n\t\tICE is activated\n\t\tThey’re onto you, +1 trace\n\t\tYour access is restricted – take -1 ongoing to matrix moves in this system while your access is restricted\n\t6-: you’re in, but the MC chooses two, and a relevant clock is advanced',
    ),
    Move(
        '[OG] Melt ICE',
        'When fighting ICE, melt ICE.',
        '.meltice',
        '.melt',
        fulldescription='When you attempt to evade, destroy or disable an activated ICE construct, roll Edge.\n\n\t7+: you evade, destroy, or temporarily disable the system, your choice\n\t7-9: the system successfully executes a routine before you can disable it'
    ),
    Move(
        '[OG] Compromise Security',
        'When screwing around with a system\'s digital security, comprimise security.',
        '.compromisesecurity',
        '.compsec',
        fulldescription='When you attempt to compromise a sub-system’s security, roll Mind.\n\n\t10+: gain 3 hold over the sub-system you have compromised\n\t7-9: gain 1 hold\n\t6-: you trigger an alert, which may have additional consequences\n\nYou may spend 1 hold to activate a security measure on that sub-system.'
    ),
    Move(
        '[OG] Manipulate Systems',
        'When interacting with the meatspace through a system, manipulate systems.',
        '.manipulatesystems',
        '.manipulatesystem',
        '.mansys',
        fulldescription='When you attempt to manipulate a digitally-controlled aspect of a facility, roll Synth.\n\n\t10+: gain 3 hold over the sub-system you are manipulating\n\t7-9: gain 1 hold\n\nYou may spend 1 hold to activate routines on that sub-system.'
    ),
    Move(
        '[OG/CUSTOM] Jack out',
        'When you need to get out quick, jack out.',
        '.jackout',
        fulldescription='Jackout: When you, your programs, or your deck are about to be damaged by ICE, you can try to jack out. Roll Cool.\n\t10+: you disconnect yourself from the system before any serious harm occurs\n\t7-9: you jack out, but choose one:\n\t\tYou lose some data\n\t\tYou take some of the established consequences\n\t\tThe owners of the target system trace you to your current location6-: you take the established consequences... and you’re still connected'
    ),
    Move(
        '[CUSTOM] Bypass Countermeasures',
        'Outmaneuver or evade system countermeasures.'
        '.bypasscountermeasures',
        fulldescription='Bypass Countermeasures: When you attempt to outmaneuver or evade system countermeasures, roll Edge:\n\n\t10+: You’re straight through, no worries\n\t7-9: You’re through, but they’re still on you. Choose one:\n\t\tAdvance Mission Clock\n\t\tICE is activated\n\t\t+1 trace\n\t\tTake established consequences\n\t6-: You’re caught, and the MC chooses one'
    ),
    Move(
        '[CUSTOM] Hijack',
        'Attempt to gain control over a system.',
        '.hijack',
        fulldescription='Hijack System: When you attempt to gain control over a system, roll Mind.\n\n\t7+: You’re in control. You may search, destroy, or wreak whatever chaos you want.\n\t7-9:  Choose one:\n\t\tTime is limited, you can only do so much before they cut you off.\n\t\tAccess is limited, you can’t get into everything you want.\n\t\t+1 trace.'
    )
]

custom = []

data = {
    'basic': basic,
    'playbooks': playbooks,
    'matrix': matrix,
    'custom': custom
}

with open('sprawl_data.pickle', 'wb') as file:
    file.write(pickle.dumps(data))
