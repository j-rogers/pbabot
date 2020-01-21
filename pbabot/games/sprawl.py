import random

from . import Game


class Sprawl(Game):
	def __init__(self):
		super().__init__()
		self.commands = {
			'.matrix': 'Displays a list of matrix-specific moves.',
			'.custom': 'Displays a list of custom moves.',
			'.weapons': 'Displays a list of weapons and their profiles.',
			'.drugs': 'Displays a list of drugs.'
		}

	def handle(self, message):
		pass

	def moves(self, message):
		pass

	def playbooks(self, message):
		pass

def handle(message):
	messageString = message.content
	response = ''
	
	'''
	Listing
	'''
	print (messageString)


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
		response = """```
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
.diabolusexmchina When Ice is activated against you roll + synth.
```"""

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

	###
	# Basic moves
	###

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
	elif ".fuckmeup" in messageString: 
		# Get the harm roll
		harmMod = 0
		harmParam= messageString.split() #puts message into a string array seperated by " "
	
		if len(harmParam)>1: #If more values other than .remember
			harmMod = int(harmParam[1]) #converts stringArray  (['.remember' 'num']) to int 

		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		roll = dice1 + dice2
		roll= roll+harmMod 
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
	############################################################# PLAYBOOK MOVE COMMANDS ##########################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Hot shit driver
	elif messageString == ".hotshitdriver":
		response = """```When you’re driving a cyber-linked vehicle in a high-pressure situation, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
You may spend 1 hold to do one of the following:
	• Avoid one external danger (a rocket, a burst of gunfire, a collision, etc)
	• Escape one pursuing vehicle
	• Maintain control of the vehicle
	• Impress, dismay or frighten someone```"""
		
	# Hustling
	elif messageString == ".hustling":
		response = """```You have people who work for you in various ways. You start with 2-crew and two jobs from the list below. Between missions, choose a number of those jobs equal to or less than your current crew, describe what each job is, and roll Edge.\n
	10+: you profit from each of your jobs
	7-9: one of them is a Disaster and you Profit from the rest
	6-: everything’s FUBAR. The MC will make a move based on the Disaster for each job\n
Choose two:
	Ђ Surveillance: You have a small network of informants who report on events; you then sell that information
		• Profit: gain [intel]
		• Disaster: someone acts on bad info
	Ђ Debt collection: You have a few burly looking fuckers who collect outstanding debts
		• Profit: gain [gear]
		• Disaster: someone’s out of pocket
	Ђ Petty theft: You have a small crew who perform minor local robberies
		• Profit: gain [gear]
		• Disaster: they robbed the wrong guy
	Ђ Deliveries: People hire you to transport things and you have a driver who takes care of that
		• Profit: gain 1 Cred
		• Disaster: the delivery never arrives
	Ђ Brokering deals: You arrange for the right people to meet each other
		• Profit: gain 1 Cred
		• Disaster: the deal that you arranged goes wrong
	Ђ Technical work: You have a couple of techs whom you supply with work
		• Profit: gain [gear]
		• Disaster: something bad happens to someone else’s property
	Ђ Pimping: You manage a small stable of physical or virtual sex workers
		• Profit: gain [intel]
		• Disaster: something goes wrong with a customer
	Ђ Addictive substances: You manage a small lab producing either drugs or simstim chips
		• Profit: gain [intel]
		• Disaster: something goes wrong for a user or for the lab itself```"""
		
	# iknowpeople
	elif messageString == ".iknowpeople":
		response = """```Once per mission you may introduce a new Contact. Name the contact, say what they do, then roll Style.\n
	10+: you’ve worked with the contact before; they have talent. Write them down as a Contact
	7-9: you’ve never met them before, they’re an unknown quantity
	6-: you know them all right. Tell the MC why they dislike you\n
After you’ve rolled, describe how you contact them; the MC will ask some questions.```"""
		
	# Reputation
	elif messageString == ".reputation":
		response = """```When you meet someone of consequence who might have
heard of you, roll Edge. On a hit, say what they know about you. On a 10+,
take +1 forward with them. On a miss, the MC will decide what they’ve heard
about you, if anything. Either you or the MC can say whether someone is
“of consequence”, but once you’ve made the reputation move on someone,
they’re “of consequence” and will be a recurring part of the story.```"""
		
	# Console Cowboy
	elif messageString == ".consolecowboy":
		response = """```Console cowboy: When you connect to a secure system, roll Mind.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
While in that system, you may spend 1 hold for any of the following effects:
	• Prevent a construct from triggering an alert
	• Avoid an ICE routine executed against you, your deck, or your programs
	• Increase your hold over compromised security or manipulated systems by 1```"""
		
	# It all fits together!
	elif messageString == ".itallfits":
		response = """```You’re a master of making connections between seemingly unrelated events. At the start of a mission, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
As you put everything together during the mission, spend 1 hold at any time to ask a question from the research list.```"""
	
	# Big game hunter
	elif messageString == ".biggamehunter":
		response = """```When you spring a trap for a target you have investigated, roll Edge.\n
	7+: you have them trapped, the only way out is through you
	10+: they are at your mercy; if the target attempts to escape, roll Edge instead of Meat to mix it up```"""
		
	# Sniper
	elif messageString == ".sniper":
		response = """```When you set up a covered and concealed place to hide, roll Cool.\n
	10+: choose 3
	7-9: choose 2
		• Your site is well hidden
		• Your site has excellent cover
		• Your site has an excellent field of view
		• You have a similarly covered and concealed backup location
		• Your spot is well secured\n
Then describe your hide site.```"""
		
	# Covert entry
	elif messageString == ".covertentry":
		response = """```When you attempt to infiltrate a secure area alone, roll Cool.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
As the MC describes the infiltration and the security measures you must overcome, you may spend 1 hold to describe how you overcome the obstacle and:
	• Bypass a security system or guard.
	• Disable a security system you have bypassed.
	• Disable a guard.
	• Escape notice```"""
		
	# Case the joint
	elif messageString == ".casethejoint":
		response = """```When you take time to examine a location for security weaknesses you can exploit, roll Edge.\n
	10+: gain three [intel]
	7-9: gain [intel]\n
You may spend this [intel] in the normal way, or you can spend one point of this [intel] to ask questions from the assess or research lists.```"""
		
	# Plan B
	elif messageString == ".planb":
		response = """```When shit hits the fan and you have to get out, name your escape route and roll Cool.\n
	10+: sweet, you’re gone
	7–9: you can go or stay, but if you go it costs you: leave something behind, or take something with you; in either case, the MC will tell you what
	6-: you’re caught in a vulnerable position, half in and half out. The MC will make a move```"""
		
	# Psychological warfare
	elif messageString == ".psychwarfare":
		response = """```When you attempt to influence the morale of your enemies by leaving evidence of violence while remaining undetected, roll Edge.\n
	7+: your enemies are impressed and overly cautious, scared and demoralised, or angry and careless (MC’s choice)
	10+: you choose```"""
		
	# Serious badass
	elif messageString == ".seriousbadass":
		response = """```When you enter a charged situation, roll Style.\n
	10+: gain 2 hold
	7–9: gain 1 hold
	6-: your enemies identify you immediately as their foremost threat\n
Spend 1 hold to make eye contact with an NPC present, who freezes or flinches and can’t act until you break it off.```"""
		
	# Trained eye
	elif messageString == ".trainedeye":
		response = """```When you evaluate a person, vehicle, drone or gang, roll Cool.\n
	7+: ask the target “How are you vulnerable to me?” Take +1 forward when acting on the answer
	10+: gain +1 ongoing when acting against that target```"""
		
	# Driven
	elif messageString == ".driven":
		response = """```When you begin a mission that furthers your vision, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
You may spend 1 hold before rolling any other move to take +1 or -2 forward to the move.```"""
		
	# Vision thing
	elif messageString == ".visionthing":
		response = """```When you have time and space for an emotional connection with someone and you passionately advocate for your vision, roll Style.\n
	10+: gain 2 hold
	7-9: gain 1 hold\n
Spend 1 hold to have the targeted NPCs:
	• give you something you want
	• do something you ask
	• fight to protect you or your cause
	• disobey an order given by someone with authority or leverage over them\n
When you use this move on a PC, spend your hold to help or interfere as if you had rolled a 10+ (i.e. give them +1 or -2). If you miss against a PC, they gain 2 hold against you which they can use in the same way.```"""
		
	# Live and on the air
	elif messageString == ".live":
		response = """```When you go live from the scene and broadcast a stream to avoid harm and expose your target, roll Edge.\n
	7+: you get the shot you want and are “escorted” to a position of safety
	7-9: choose one:
		• Your story irritates your target (The MC will advance a relevant Threat Clock)
		• Someone on your team gets hurt off camera
		• Your story angers your employer
		• Your rushed narrative is misinterpreted by the public with unintended consequences```"""
		
	# Nose for a story
	elif messageString == ".nose":
		response = """```At the start of a mission, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
During the mission, spend 1 hold to invoke one of the following effects:
	• Ask one question from the research list
	• Take +1 forward when monstering
	• Find a piece of evidence that links this mission to a current story; start a Story Clock and a linked Noise Clock or roll to gather evidence```"""
		
	# Gather evidence
	elif messageString == ".gatherevidence":
		response = """```When you gather evidence to break a story, roll Mind.\n
	10+: you get the evidence you need, advance that Story Clock
	7-9: you get the evidence, but tip your hand to someone implicated in your story; tell the MC which clock to advance: a relevant Corporate Clock, the linked Noise Clock or the relevant Mission Clock (Legwork or Action, depending on which phase of the current mission you’re in)
	6-: the MC will advance the Noise Clock and make a move\n
If the Story Clock reaches 0000 before the Noise Clock, the Reporter has broken the story before the implicated parties could cover up the evidence, or stop the investigation. The exact implications of this for the game will vary based on the story, but it should have a major impact on the implicated parties and will affect at least one Corporate Clock.\n
If the Noise Clock reaches 0000 before the Story Clock, the implicated parties have tied up all the loose ends and the story is dead. Now that damage control is complete, they can deal with the Reporter permanently. Advance any relevant Corporate or Threat Clocks.```"""

	elif messageString == ".press":
		response = """```Press pass: If you reveal your public persona to fast talk your way in,do not roll the dice, you count as rolling a 10+.\nTake [intel] and advance the Legwork Clock.```"""	
	# Monstering
	elif messageString == ".monstering":
		response = """```When you corner someone and hound them with questions to get to the bottom of a story, roll Edge.\n
	10+: they tell you the truth, regardless of the consequences
	7-9: they give you enough to get you off their back, then when they’re safe, they choose one:
		• they respond with fear
		• they respond with anger
		• they respond with clinical calm```"""
		
	# I love it when a plan comes together
	elif messageString == ".plan":
		response = """```At the start of a mission, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold
	6-: gain 1 hold anyway, but your opponent has predicted your every move; the MC will advance the Legwork Clock\n
During the mission, spend 1 hold for one of the following effects:
	• You have that piece of gear that you need, right now
	• You appear in a scene where you are needed, right now```"""
		
	# Exit strategy
	elif messageString == ".exitstrategy":
		response = """```You always have an escape plan prepared. When shit hits the fan and you decide to bail out, roll Mind.\n
	7+: You escape the situation
	10+: choose one thing to leave behind
	7-9: choose two things
		• Your team
		• A mission objective
		• Identifiable evidence
		• Your staked Cred```"""
		
	# Recruiter
	elif messageString == ".recruiter":
		response = """```When you attempt to recruit a specialist or a team of specialists to directly assist with your mission, roll Edge.\n
	10+: choose 2
	7-9: choose 1
		• Reliable professional(s)
		• A small team (up to 5)
		• As competent as required```"""
		
	# Slippery
	elif messageString == ".slippery":
		response = """```At the end of a mission during which you planted or hid evidence to shift blame away from you and your team, name who you threw under the corporate bus and roll Edge.\n
	7+: the MC will not increase Corporate Clocks in the retaliation phase
	10+: the MC will reduce a Corporate Clock by one
	6-: create or increase the Threat Clock of whoever you threw under the bus```"""
		
	# Storage
	elif messageString == ".storage":
		response = """```After receiving a job you may look through your accumulated parts and supplies for equipment that might help with the current mission. Roll Mind.\n
	10+: gain 3 [gear] relevant to your chosen area(s) of expertise.
	7-9: gain 1 [gear] relevant to your chosen area(s) of expertise.```"""
		
	# Blend in
	elif messageString == ".blendin":
		response = """```When you’re about to be caught somewhere you shouldn’t be, but look and act like you belong there, roll Cool.\n
10+: no one thinks twice about your presence until you do something to attract attention
7-9: you’ll be fine as long as you leave right now, but if you do anything else, your presence will arouse suspicion```"""
		
	# Bypass
	elif messageString == ".bypass":
		response = """```When you attempt to subvert security measures (bypassing a locked door, disabling an alarm, camera or motion detector, etc), roll Cool.\n
	7+: you successfully bypass the system without leaving a trace
	10+: you gain some valuable insight into the facility’s security, gain [intel]```"""

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



	