import random

def handle(message):
	messageString = message.content
	response = ''
	
	'''
	Listing
	'''

	# Basic moves
	if messageString == ".moves":
		response = """```Use the following commands to find detailed information about each move.\n
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

For matrix specific moves see '.matrix'.```"""

	# List of playbooks
	elif messageString == ".playbooks":
		response = """```Use the following commands to find each playbook-specific move.\n
.driver
.fixer
.hacker
.hunter
.infiltrator
.killer
.pusher
.reporter
.soldier
.tech```"""

	# Driver
	elif messageString == ".driver":
		response = """```Roll moves:
.hotshitdriver: Bonus while hight-tension driving. (Roll)\n
    Other moves:
Wheels: You start with a car.
Second Skin: When jacked into your vehicle with a neural interface you get bonuses to your rolls.
Chromed: Choose another piece of cyberware at character creation or in downtime.
Daredevil: Bonus when you drive straight into danger.
Drone Jockey: You get with two drones.
Iceman: Fast talk replacement.
Right Tool for the Job: You have two additional cyber-linked vehicles.
Sweet Ride: Replacement and bonus to Hit the street while in your vehicle.```"""

	# Fixer
	elif messageString == ".fixer":
		response = """```Roll moves:
.hustling: Gives hustling jobs. (Roll)
.iknowpeople: Specialized contact decleration. (Roll)\n
	Other moves:
Backup: You have a group of associates. 
Balls in the Air: +1 crew and choose another job.
Chromed: Choose another piece of cyberware at character creation or in downtime.
Deal of a Lifetime: Hit the street bonus when selling something.
Facetime: Fast talk bonus.
Hard to Find: Hit the street bonus.
Reputation: Various social bonuses.
Sales Engineer: Produce equipment bonus.
Smooth: Helping or hindering replacement.
Street King Pin: +1 crew, choose an additional job.
Word on the Street: Meatspace research bonus.```"""

	# Hacker
	elif messageString == '.hacker':
		response = """```Roll moves:
.consolecowboy: Bonus within current system. (Roll)\n
    Other moves:
.jackin: You can access the matrix.
.consolecowboy: Bonus within current system. (Roll)
.blackicevet: Bonus against black ICE.
.chromed: Choose another piece of cyberware at character creation or in downtime. 
.icebreaker: Bonus against all ICE.
.neuralscars: Bonus against black ICE.
.programmingonthefly: Bonus to matrix moves.
.rep: Fast talk and Play hard ball replacements while in the matrix.
.searchoptimisation: Matrix research bonus.
.techsupport: Bonus when helping or interfering while in the matrix.
.zeroed: Cyberdeck bonus.```"""

	# Hunter
	elif messageString == '.hunter':
		response = """```Roll moves:
.itallfits: Research bonus. (Roll)
.biggamehunter: Bonus when springing a trap against a researced target. (Roll)
.sniper: Bonus when hiding. (Roll)\n
    Other moves:
.eartotheground: Meatspace reseach bonus. 
.chromed: Choose another piece of cyberware at character creation or in downtime.
.deadbeat: Hit the street bonus.
.enhance: Research bonus.
.eyefordetail: Bonus when calmly assessing a person or place.
.humanterrain: Bonus when investigating a group.
.onthetrail: Additional use of intel against a single person.
.seetheangles: At the start of the action phase gain [intel] and [gear].```"""

	# Infiltrator
	elif messageString == '.infiltrator':
		response = """```Roll moves:
.covertentry: Bonus when infilatrating alone. (Roll)
.casethejoint: Bonus when examining a locations weaknesses. (Roll)
.planb: When shit hits the fan and you have to get out. (Roll)
.psychologicalwarfare: When you attempt to demoralise the enemy by leaving evidence of violence. (Roll)\n
    Other moves:
.catburgler: On the job [gear] procurement. Used with Covert Entry.
.face: On the job [intel] procurement. Used with Covert Entry.
.assassin: Bonus to attacking unexpectedly.
.chromed: Choose another piece of cyberware at character creation or in downtime.
.jackin: You can access the matrix.
.masterofdisguise: Fast talk bonus.
.motherduck: Allows Covert Entry hold you spend to work for the whole team.
.stealthoperative: Assess bonus.```"""
	
	# Killer
	elif messageString == '.killer':
		response = """```Roll moves:
.seriousbadass: Bonus when entering a charged situation. (Roll)
.trainedeye: Bonus when sizing up a person, vehicle, drone or gang. (Roll)\n
    Other moves:
.customweapon: You begin with a custom weapon.
.emotionless: Play hard ball replacement.
.hard: Harm move bonus.
.loadedforbear: Choose another bonus weapon.
.moremachinethanmeat: Choose another piece of cyberware at character creation or in downtime.
.corporatesecrets: Bonus when researching a corporation.
.militarybackground: Bonus when hitting the street.
.milspecs: Bonus to mix it up.```"""

	# Pusher
	elif messageString == '.pusher':
		response = """```Roll moves:
.driven: Bonus when the mission furthers your vision. (Roll)
.visionthing: Bonus when passionately advocating your vision. (Roll)\n
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
.silvertongue: Fast Talk bonus.```"""

	# Reporter
	elif messageString == '.reporter':
		response = """```Roll moves:
.liveandontheair: You can broadcast a stream to hurt your target. (Roll)
.noseforastory: Various mission bonuses. (Roll)
.gatherevidence: Various effects on story and noise clocks. (Roll)
.monstering: You can corner someone and hound them with questions. (Roll)\n
    Other moves:
.24/7livefeeds: Bonus to researching when scanning live feeds.
.chromed: Choose another piece of cyberware at character creation or in downtime.
.filthyassistants: Bonus when using research obtained [intel].
.presspass: Bonus when revealing yourself to fast talk your way in.
.reliablesources: Research bonus.
.warcorrespondent: Bonus when Acting Under Pressure.```"""

	# Soldier
	elif messageString == '.soldier':
		response = """```Roll moves:
.iloveitwhenaplancomestogether: Bonus [gear] and [intel]. (Roll)
.exitstrategy: Bonus to getting the fuck out of there. (Roll)
.recruiter: Contact / Hit the Street bonus. (Roll)
.slippery: Prevents Corps from finding the teams involvement. (Roll)\n
    Other moves:
.herestheplan: Team bonus when you plan the mission and if you get paid.
.auraofprofessionalism: Bonus when Getting the Job or Getting Paid.
.chromed: Choose another piece of cyberware at character creation or in downtime.
.corporateknowledge: Bonus when researching a corporation.
.handsonmanagement: Mix it up bonus.
.steadypresence: You can give pep-talks.
.tacticaloperations: Assess bonus.```"""

	# Tech
	elif messageString == '.tech':
		response = """```Roll moves:
.storage: Pre-mission [gear] bonus. (Roll)
.blendin: You can act like you belong in places you don't. (Roll)
.bypass: You can subvert security measures. (Roll)\n
    Other moves:
.expert: You get an area of expertise.
.customiser: You can examine and modify technology.
.analytic: Assess replacement.
.chromed: Choose another piece of cyberware at character creation or in downtime.
.diverseinterests: Choose another area of expertise.
.jackofalltrades: Choose another area of expertise.
.obsessive: Research bonus.
.onit: Replacement when helping or hindering someone in a topic relating to your expertise.
.renaissanceman: Choose another area of expertise.```"""

	# Lists matrix specific moves
	elif messageString == '.matrix':
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

	'''
	Basic Move Commands
	'''

	# Act Under Pressure
	elif messageString == ".actunderpressure":
		response = """```When you race against the clock, act while in danger or act to avoid danger, roll Cool.\n
	10+: you do it, no problem
	7-9: you stumble, hesitate, or flinch: the MC will offer you a worse outcome, hard bargain, or ugly choice```"""

	# Apply First Aid
	elif messageString == ".applyfirstaid" or messageString == ".firstaid" or messageString == "aid":
		
		response = """```When you treat someone’s wounds using appropriate medical equipment, roll Cool.\n
	10+: if their Harm Clock is at 2100 or less, reduce their harm by two segments. If their Harm Clock is at more than 2100, reduce their harm by one segment
	7-9: reduce their harm by one segment. If their Harm Clock is still at more than 2100, they take -1 ongoing until they receive proper medical attention```"""
		
	# Assess
	elif messageString == ".assess":
		
		response = """```When you closely study a person, place or situation, or when you quickly size up an opponent or a charged situation, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
In the ensuing action, you may spend 1 hold at any time to ask the MC a question from the list below if your examination could have revealed the answer. The MC may ask you questions to clarify your intent. Take +1 forward when acting on the answers.\n
	Ђ What potential complication do I need to be wary of?
	Ђ What do I notice despite an effort to conceal it?
	Ђ How is ______ vulnerable to me?
	Ђ How can I avoid trouble or hide here?
	Ђ What is my best way in/way out/way past?
	Ђ Where can I gain the most advantage?
	Ђ Who or what is my biggest threat in this situation?
	Ђ Who or what is in control here?```"""
		
	# Play Hardball
	elif messageString == ".playhardball" or messageString == ".hardball":
		
		response = """```When you get in someone’s face threatening violence and you intend to carry through, roll Edge.\n
	10+: NPCs do what you want. PCs choose: do what you want, or suffer the established consequences
	7–9: For NPCs, the MC chooses 1:
		Ђ they attempt to remove you as a threat, but not before suffering the established consequences
		Ђ they do it, but they want payback. Add them as a Threat
		Ђ they do it, but tell someone all about it. Advance the appropriate Mission Clock
	PCs choose: do what you want, or suffer the established consequences. They gain +1 forward to act against you.```"""
		
	# Acquire Agricultural Property
	elif messageString == ".amidead":
		
		response = """```When you hit 0000 on your Harm Clock, roll Meat.\n
	10+: you survive until the medics arrive
	7-9: you survive at a cost. Pick one: +owned, substandard treatment (-1 to a stat), cyberware damage (give one piece of cyberware a negative tag)
	6-: you bleed out on the street```"""
		
	# Mix it Up
	elif messageString == ".mixitup" or messageString == ".mix":
		
		response = """```When you use violence against an armed force to seize control of an objective, state that objective and roll Meat.\n
	7+: you achieve your objective
	7-9: choose 2:
		Ђ you make too much noise. Advance the relevant Mission Clock
		Ђ you take harm as established by the fiction
		Ђ an ally takes harm as establish```"""
		
	# Research
	elif messageString == ".research":
		
		response = """```When you investigate a person, place, object, or service using a library, dossier or database (or combination of them), ask a question from the list below and roll Mind.\n
	10+: take [intel]; the MC will answer your question and answer a follow-up question from this list as well:
		Ђ Where would I find ______?
		Ђ How secure is ______?
		Ђ Who or what is related to ______?
		Ђ Who owned or employed ______?
		Ђ Who or what is ______ most valuable to?
		Ђ What is the relationship between ______ and ______?
	7-9: take [intel]; the MC will answer your question
	6-: the MC will answer your question... and make a move```"""
		
	# Fast Talk
	elif messageString == ".fasttalk":
		
		response = """```When you try to convince someone to do what you want with promises, lies or bluster, roll Style.\n
	10+: NPCs do what you want. PCs choose whether to do it or not. If they do, they mark experience. If they don’t, they must act under pressure to go against your stated wishes.
	7-9: NPCs do it, but someone will find out: the MC will advance the appropriate Countdown Clock. For PCs choose one:
		Ђ If they do what you want, they mark experience
		Ђ If they don’t do it, they must act under pressure to go against your stated wishes
	Then its up to them.```"""
		
	# Hit the Street
	elif messageString == ".hitthestreet":
		
		response = """```When you go to a Contact for help, roll Style.\n
	7+: You get what you want.
	10+: You get a little something extra (choose either [intel] or [gear]).
	7-9: choose 2 from the list below:
		Ђ Your request is going to cost you extra
		Ђ Your request is going to take some time to put together
		Ђ Your request is going to attract unwanted attention, complications or consequences
		Ђ Your contact needs you to help them out with something. If you turn them down take -1 ongoing to this move till you make it right```"""
		
	# Go Under the Knife
	elif messageString == ".undertheknife" or messageString == ".under" or messageString == ".knife":
		
		response = """```When you have new cyberware installed by a street doctor, roll Cred spent (max +2).\n
	10+: the operation was a complete success
	7-9: the cyberware doesn’t work as well as advertised, choose one: +unreliable, +substandard, +hardware decay, +damaging.
	6-: there have been... complications\n
When you have new cyberware installed in accordance with a corporate contract, ignore all of that bad stuff. You’re +owned. Your cyberware works exactly the way they intend it.```"""
		
	# Harm
	elif messageString == ".fuckmeup":
		# Get the harm roll
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		roll = dice1 + dice2
		response = ""

		# Message based on harm roll
		if roll >= 10:
			response = """```Oh you fucked up now, you rolled """ + str(roll) + """. Choose 1:
	Ђ you’re out of action: unconscious, trapped, incoherent or panicked
	Ђ take the full harm of the attack, before it was reduced by armour; if you already took the full harm of the attack,
take +1-harm
	Ђ lose the use of a piece of cyberware until you can get it repaired
	Ђ lose a body part (arm, leg, eye)```"""
		elif roll >= 7 and roll <= 9:
			response = """```You're going to have to suck off the MC on this one, you rolled """ + str(roll) + """. The MC will choose 1:
	Ђ you lose your footing
	Ђ you lose your grip on whatever you’re holding
	Ђ you lose track of someone or something you’re attending to
	Ђ someone gets the drop on you```"""
		else:
			response = "```You rolled " + str(roll) + ". You're gucci flip flops fam *dabs* haha yeet :3```"
		
	# Get the Job
	elif messageString == ".getthejob" or messageString == ".job":
		
		response = """```When you negotiate the terms of a job, roll Edge.\n
	10+: choose 3 from the list below
	7-9: choose 1 from the list below
		Ђ the employer provides useful information ([intel])
		Ђ the employer provides useful assets ([gear])
		Ђ the job pays well
		Ђ the meeting doesn’t attract attention
		Ђ the employer is identifiable```"""
		
	# Getting Paid
	elif messageString == ".gettingpaid" or messageString == ".getpaid" or messageString == ".paid":
		
		response = """```When you go to a meet to get paid by your employer, roll and add the number of unfilled segments on the Legwork Clock.\n
	10+: choose 3 from the list below
	7-9: choose 1 from the list below
		Ђ It’s not a set-up or an ambush
		Ђ You are paid in full
		Ђ The employer is identifiable
		Ђ The meeting doesn’t attract the attention of outside parties
		Ђ You learned something from the mission; everyone marks experience```"""
		
		
		










	return response