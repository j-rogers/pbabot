import discord
import random
import pickle

# API Token
#TOKEN = "NTE3MTQyNTcyMzkzODI0MjY2.Dt9-Jg.d0QaXh9Gi0CyR16bWps_KFwwbds"
TOKEN = "NTA5NTc5MjMwMTk2MjY5MDY2.DsP2mA.poKbR9OIjKp_cE02vCASuMPeIVM"

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

# MESSAGE COMMANDS
@client.event
async def on_message(message):
	# Prevents bot replying to itself
	if message.author == client.user:
		return

	# Prevents bot responding to regular messages
	if not message.content.startswith("."):
		return

	###############################################################################################################################################
	###############################################################################################################################################
	################################################################ LISTING COMMANDS #############################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Lists all commands
	if message.content.startswith(".help"):
		# Form the message
		msg = """```Use \".command\" when using this bot.\n
.help: Displays this help message.
.roll: Rolls 2d6 dice.
.moves: Displays a list of basic moves.
.playbooks: Displays a list of playbook specific moves.
.matrix: Displays a list of matrix-specific moves.
.custom: Displays a list of custom moves.
.clocks: Displays the current list of clocks.
.addclock <clock name>: Adds a clock with a value of 1500.
.increaseclock <clock name>: Increases a clock by one segment.
.decreaseclock <clock name>: Decreases a clock by one segment.
.deleteclock <clock name>: Deletes the specified clock.
.contacts: Displays the current list of contacts.
.addcontact <contact name> <description>: Adds a new contact.
.deletecontact <contact name>: Deletes a contact.
.drugs: Displays a list of drugs
.rip: Displays a list of dead characters and how they died.
.f: Same as '.rip'
.refresh: Reloads the clock and contact data.
.log <message>: Saves a message to the log file.```"""

		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Displays a list of moves
	elif message.content.startswith(".moves"):
		# Form the message
		msg = 	"""```Use the following commands to find detailed information about each move.\n
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

		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Displays list of playbooks
	elif message.content.startswith(".playbooks"):
		# Form the message
		msg = """```Use the following commands to find each playbook-specific move. Note only moves that require a dice roll are included, for other moves check the book.\n
Driver:
	.hotshitdriver: Hot shit driver (Edge)\n
Fixer:
	.hustling: Hustling (Edge)
	.iknowpeople: I know people (Style)
	.reputation: Reputation (Edge)\n
Hacker:
	.consolecowboy: Console cowboy (Mind)\n
Hunter:
	.itallfits: It all fits together! (Edge)
	.biggamehunter: Big game hunter (Edge)
	.sniper: Sniper (Cool)\n
Infiltrator:
	.covertentry: Covert Entry (Cool)
	.casethejoint: Case the joint (Edge)
	.planb: Plan B (Cool)
	.psychwarfare: Psychological warfare (Edge)\n
Killer:
	.seriousbadass: Serious badass (Style)
	.trainedeye: Trained eye (Cool)\n
Pusher:
	.driven: Driven (Edge)
	.visionthing: Vision thing (Style)\n
Reporter:
	.live: Live and on the air (Edge)
	.nose: Nose for a story (Edge)
	.gatherevidence: Gather evidence (Mind)
	.monstering: Monstering (Edge)\n
Soldier:
	.plan: I love it when a plan comes together (Edge)
	.exitstrategy: Exit strategy (Mind)
	.recruiter: Recruiter (Edge)
	.slippery: Slippery (Edge)\n
Tech:
	.storage: Storage (Mind)
	.blendin: Blend in (Cool)
	.bypass: Bypass (Cool)```"""
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Displays a list of matrix specific moves
	elif message.content.startswith(".matrix"):
		# Form the message
		msg = """```Use the following commands to find detailed information about each move.\n
.login: Login (Synth)
.melt: Melt Ice (Edge)
.compsec: Compromise Security (Mind)
.mansys: Manipulate Systems (Synth)
.jackout: Jack Out (Cool)```"""
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Displays a list of custom moves
	elif message.content.startswith(".custom"):
		# Form the message
		msg = """```Use the following commands to find detailed information about each move.\n
.dogie: Git along little dogie (Style)
.trouble: Nose for trouble (Cool)
.goodbetter: He's good, but I'm better (Edge)```"""
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Displays the current list of clocks
	elif message.content.startswith(".clocks"):
		msg = "```"
		global clocks
		for clock in clocks:
			name = clock[0]
			value = clock[1]

			if value == "1200": msg += name + ": □□□□ □□□□ □□□□ □ □ □\n"
			elif value == "1500": msg += name + ": ■■■■ □□□□ □□□□ □ □ □\n"
			elif value == "1800": msg += name + ": ■■■■ ■■■■ □□□□ □ □ □\n"
			elif value == "2100": msg += name + ": ■■■■ ■■■■ ■■■■ □ □ □\n"
			elif value == "2200": msg += name + ": ■■■■ ■■■■ ■■■■ ■ □ □\n"
			elif value == "2300": msg += name + ": ■■■■ ■■■■ ■■■■ ■ ■ □\n"
			elif value == "0000": msg += name + ": ■■■■ ■■■■ ■■■■ ■ ■ ■\n"

		if msg == "```":
			msg += "No clocks have been added."

		msg += "```"

		# Send message
		await client.send_message(message.channel, msg.format(message))

	# Displays the current list of contacts
	elif message.content.startswith(".contacts"):
		msg = "```"
		global contacts
		for contact in contacts:
			name = contact[0]
			desc = contact[1]
			msg += name + ": " + desc + "\n"

		if msg == "```":
			msg += "No contacts have been added."

		msg += "```"

		# Send message
		await client.send_message(message.channel, msg.format(message))

	# Displays a list of characters who've died, and how they died
	elif message.content.startswith(".rip") or message.content == ".f":
		# Form the message
		msg = """```Martin:
	Christof died to the hands of Syntax Terror's drones whilst pounded by police.\n
F in chat please.```"""

		# Send message
		await client.send_message(message.channel, msg.format(message))

	# Display a list of drugs
	elif message.content.startswith(".drugs"):
		# Form the message
		msg = """```Use the following commands to find detailed information about each drug.\n
.spank: Spank
.motherfuck: Motherfuck
.domo: Domo
.clutch: Clutch
.meatloaf: Meatloaf```"""
		# Send the message
		await client.send_message(message.channel, msg.format(message))


	###############################################################################################################################################
	###############################################################################################################################################
	############################################################## BASIC MOVE COMMANDS ############################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Act Under Pressure
	elif message.content.startswith(".actunderpressure"):
		# Form the message
		msg = """```When you race against the clock, act while in danger or act to avoid danger, roll Cool.\n
	10+: you do it, no problem
	7-9: you stumble, hesitate, or flinch: the MC will offer you a worse outcome, hard bargain, or ugly choice```"""

		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Apply First Aid
	elif message.content.startswith(".applyfirstaid") or message.content.startswith(".firstaid"):
		# Form the message
		msg = """```When you treat someone’s wounds using appropriate medical equipment, roll Cool.\n
	10+: if their Harm Clock is at 2100 or less, reduce their harm by two segments. If their Harm Clock is at more than 2100, reduce their harm by one segment
	7-9: reduce their harm by one segment. If their Harm Clock is still at more than 2100, they take -1 ongoing until they receive proper medical attention```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Assess
	elif message.content.startswith(".assess"):
		# Form the message
		msg = """```When you closely study a person, place or situation, or when you quickly size up an opponent or a charged situation, roll Edge.\n
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
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Play Hardball
	elif message.content.startswith(".playhardball"):
		# Form the message
		msg = """```When you get in someone’s face threatening violence and you intend to carry through, roll Edge.\n
	10+: NPCs do what you want. PCs choose: do what you want, or suffer the established consequences
	7–9: For NPCs, the MC chooses 1:
		Ђ they attempt to remove you as a threat, but not before suffering the established consequences
		Ђ they do it, but they want payback. Add them as a Threat
		Ђ they do it, but tell someone all about it. Advance the appropriate Mission Clock
	PCs choose: do what you want, or suffer the established consequences. They gain +1 forward to act against you.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Acquire Agricultural Property
	elif message.content.startswith(".amidead"):
		# Form the message
		msg = """```When you hit 0000 on your Harm Clock, roll Meat.\n
	10+: you survive until the medics arrive
	7-9: you survive at a cost. Pick one: +owned, substandard treatment (-1 to a stat), cyberware damage (give one piece of cyberware a negative tag)
	6-: you bleed out on the street```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Mix it Up
	elif message.content.startswith(".mixitup"):
		# Form the message
		msg = """```When you use violence against an armed force to seize control of an objective, state that objective and roll Meat.\n
	7+: you achieve your objective
	7-9: choose 2:
		Ђ you make too much noise. Advance the relevant Mission Clock
		Ђ you take harm as established by the fiction
		Ђ an ally takes harm as establish```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Research
	elif message.content.startswith(".research"):
		# Form the message
		msg = """```When you investigate a person, place, object, or service using a library, dossier or database (or combination of them), ask a question from the list below and roll Mind.\n
	10+: take [intel]; the MC will answer your question and answer a follow-up question from this list as well:
		Ђ Where would I find ______?
		Ђ How secure is ______?
		Ђ Who or what is related to ______?
		Ђ Who owned or employed ______?
		Ђ Who or what is ______ most valuable to?
		Ђ What is the relationship between ______ and ______?
	7-9: take [intel]; the MC will answer your question
	6-: the MC will answer your question... and make a move```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Fast Talk
	elif message.content.startswith(".fasttalk"):
		# Form the message
		msg = """```When you try to convince someone to do what you want with promises, lies or bluster, roll Style.\n
	10+: NPCs do what you want. PCs choose whether to do it or not. If they do, they mark experience. If they don’t, they must act under pressure to go against your stated wishes.
	7-9: NPCs do it, but someone will find out: the MC will advance the appropriate Countdown Clock. For PCs choose one:
		Ђ If they do what you want, they mark experience
		Ђ If they don’t do it, they must act under pressure to go against your stated wishes
	Then its up to them.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Hit the Street
	elif message.content.startswith(".hitthestreet"):
		# Form the message
		msg = """```When you go to a Contact for help, roll Style.\n
	7+: You get what you want.
	10+: You get a little something extra (choose either [intel] or [gear]).
	7-9: choose 2 from the list below:
		Ђ Your request is going to cost you extra
		Ђ Your request is going to take some time to put together
		Ђ Your request is going to attract unwanted attention, complications or consequences
		Ђ Your contact needs you to help them out with something. If you turn them down take -1 ongoing to this move till you make it right```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Go Under the Knife
	elif message.content.startswith(".undertheknife"):
		# Form the message
		msg = """```When you have new cyberware installed by a street doctor, roll Cred spent (max +2).\n
	10+: the operation was a complete success
	7-9: the cyberware doesn’t work as well as advertised, choose one: +unreliable, +substandard, +hardware decay, +damaging.
	6-: there have been... complications\n
When you have new cyberware installed in accordance with a corporate contract, ignore all of that bad stuff. You’re +owned. Your cyberware works exactly the way they intend it.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Harm
	elif message.content.startswith(".fuckmeup"):
		# Get the harm roll
		roll = random.randint(2, 12)
		msg = ""

		# Message based on harm roll
		if roll >= 10:
			msg = """```Oh you fucked up now, you rolled """ + str(roll) + """. Choose 1:
	Ђ you’re out of action: unconscious, trapped, incoherent or panicked
	Ђ take the full harm of the attack, before it was reduced by armour; if you already took the full harm of the attack,
take +1-harm
	Ђ lose the use of a piece of cyberware until you can get it repaired
	Ђ lose a body part (arm, leg, eye)```"""
		elif roll >= 7 and roll <= 9:
			msg = """```You're going to have to suck off the MC on this one, you rolled """ + str(roll) + """. The MC will choose 1:
	Ђ you lose your footing
	Ђ you lose your grip on whatever you’re holding
	Ђ you lose track of someone or something you’re attending to
	Ђ someone gets the drop on you```"""
		else:
			msg = "```You rolled " + str(roll) + ". You're gucci flip flops fam *dabs* haha yeet :3```"
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Get the Job
	elif message.content.startswith(".getthejob"):
		# Form the message
		msg = """```When you negotiate the terms of a job, roll Edge.\n
	10+: choose 3 from the list below
	7-9: choose 1 from the list below
		Ђ the employer provides useful information ([intel])
		Ђ the employer provides useful assets ([gear])
		Ђ the job pays well
		Ђ the meeting doesn’t attract attention
		Ђ the employer is identifiable```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Getting Paid
	elif message.content.startswith(".gettingpaid") or message.content.startswith(".getpaid"):
		# Form the message
		msg = """```When you go to a meet to get paid by your employer, roll and add the number of unfilled segments on the Legwork Clock.\n
	10+: choose 3 from the list below
	7-9: choose 1 from the list below
		Ђ It’s not a set-up or an ambush
		Ђ You are paid in full
		Ђ The employer is identifiable
		Ђ The meeting doesn’t attract the attention of outside parties
		Ђ You learned something from the mission; everyone marks experience```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	#########################################################
	################## MATRIX MOVE COMMANDS #################
	#########################################################

	# Login
	elif message.content.startswith(".login"):
		# Form the message
		msg = """```When you attempt to gain access to a system, roll Synth.\n
	10+: you’re in clean
	7-9: you’re in, but choose one:
		Ђ Passive trace (+1 trace)
		Ђ ICE is activated
		Ђ An alert is triggered (advance the active Mission Clock)
		Ђ Your access is restricted – take -1 ongoing to matrix moves in this system while your access is restricted
		6-: you’re in, but the MC chooses two```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Melt Ice
	elif message.content.startswith(".melt"):
		# Form the message
		msg = """```When you attempt to evade, destroy or disable an activated ICE construct, roll Edge.\n
	7+: you evade, destroy, or temporarily disable the system, your choice
	7-9: the system successfully executes a routine before you can disable it```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Compromise Security
	elif message.content.startswith(".compsec") or message.content.startswith(".compromisesecurity"):
		# Form the message
		msg = """```When you attempt to compromise a sub-system’s security, roll Mind.\n
		10+: gain 3 hold over the sub-system you have compromised
		7-9: gain 1 hold
		6-: you trigger an alert, which may have additional consequences\n
You may spend 1 hold to activate a security measure on that sub-system.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Manipulate Systems
	elif message.content.startswith(".mansys") or message.content.startswith(".manipulatesystem") or message.content.startswith(".manipulatesystems"):
		# Form the message
		msg = """```When you attempt to manipulate a digitally-controlled aspect of a facility, roll Synth.\n
	10+: gain 3 hold over the sub-system you are manipulating
	7-9: gain 1 hold\n
You may spend 1 hold to activate routines on that sub-system.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Jack Out
	elif message.content.startswith(".jackout"):
		# Form the message
		msg = """```When you, your programs, or your deck are about to be damaged by ICE, you can try to jack out. Roll Cool.\n
	10+: you disconnect yourself from the system before any serious harm occurs
	7-9: you jack out, but choose one:
		Ђ You lose some data
		Ђ You take some of the established consequences
		Ђ The owners of the target system trace you to your current location
	6-: you take the established consequences... and you’re still connected```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	###############################################################################################################################################
	###############################################################################################################################################
	############################################################# PLAYBOOK MOVE COMMANDS ##########################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Hot shit driver
	elif message.content.startswith(".hotshitdriver"):
		# Form the message
		msg = """```When you’re driving a cyber-linked vehicle in a high-pressure situation, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
You may spend 1 hold to do one of the following:
	• Avoid one external danger (a rocket, a burst of gunfire, a collision, etc)
	• Escape one pursuing vehicle
	• Maintain control of the vehicle
	• Impress, dismay or frighten someone```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Hustling
	elif message.content.startswith(".hustling"):
		# Form the message
		msg = """```You have people who work for you in various ways. You start with 2-crew and two jobs from the list below. Between missions, choose a number of those jobs equal to or less than your current crew, describe what each job is, and roll Edge.\n
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
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# iknowpeople
	elif message.content.startswith(".iknowpeople"):
		# Form the message
		msg = """```Once per mission you may introduce a new Contact. Name the contact, say what they do, then roll Style.\n
	10+: you’ve worked with the contact before; they have talent. Write them down as a Contact
	7-9: you’ve never met them before, they’re an unknown quantity
	6-: you know them all right. Tell the MC why they dislike you\n
After you’ve rolled, describe how you contact them; the MC will ask some questions.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Reputation
	elif message.content.startswith(".reputation"):
		# Form the message
		msg = """```When you meet someone of consequence who might have
heard of you, roll Edge. On a hit, say what they know about you. On a 10+,
take +1 forward with them. On a miss, the MC will decide what they’ve heard
about you, if anything. Either you or the MC can say whether someone is
“of consequence”, but once you’ve made the reputation move on someone,
they’re “of consequence” and will be a recurring part of the story.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Console Cowboy
	elif message.content.startswith(".consolecowboy"):
		# Form the message
		msg = """```Console cowboy: When you connect to a secure system, roll Mind.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
While in that system, you may spend 1 hold for any of the following effects:
	• Prevent a construct from triggering an alert
	• Avoid an ICE routine executed against you, your deck, or your programs
	• Increase your hold over compromised security or manipulated systems by 1```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# It all fits together!
	elif message.content.startswith(".itallfits"):
		# Form the message
		msg = """```You’re a master of making connections between seemingly unrelated events. At the start of a mission, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
As you put everything together during the mission, spend 1 hold at any time to ask a question from the research list.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Big game hunter
	elif message.content.startswith(".biggamehunter"):
		# Form the message
		msg = """```When you spring a trap for a target you have investigated, roll Edge.\n
	7+: you have them trapped, the only way out is through you
	10+: they are at your mercy; if the target attempts to escape, roll Edge instead of Meat to mix it up```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Sniper
	elif message.content.startswith(".sniper"):
		# Form the message
		msg = """```When you set up a covered and concealed place to hide, roll Cool.\n
	10+: choose 3
	7-9: choose 2
		• Your site is well hidden
		• Your site has excellent cover
		• Your site has an excellent field of view
		• You have a similarly covered and concealed backup location
		• Your spot is well secured\n
Then describe your hide site.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Covert entry
	elif message.content.startswith(".covertentry"):
		# Form the message
		msg = """```When you attempt to infiltrate a secure area alone, roll Cool.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
As the MC describes the infiltration and the security measures you must overcome, you may spend 1 hold to describe how you overcome the obstacle and:
	• Bypass a security system or guard.
	• Disable a security system you have bypassed.
	• Disable a guard.
	• Escape notice```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Case the joint
	elif message.content.startswith(".casethejoint"):
		# Form the message
		msg = """```When you take time to examine a location for security weaknesses you can exploit, roll Edge.\n
	10+: gain three [intel]
	7-9: gain [intel]\n
You may spend this [intel] in the normal way, or you can spend one point of this [intel] to ask questions from the assess or research lists.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Plan B
	elif message.content.startswith(".planb"):
		# Form the message
		msg = """```When shit hits the fan and you have to get out, name your escape route and roll Cool.\n
	10+: sweet, you’re gone
	7–9: you can go or stay, but if you go it costs you: leave something behind, or take something with you; in either case, the MC will tell you what
	6-: you’re caught in a vulnerable position, half in and half out. The MC will make a move```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Psychological warfare
	elif message.content.startswith(".psychwarfare"):
		# Form the message
		msg = """```When you attempt to influence the morale of your enemies by leaving evidence of violence while remaining undetected, roll Edge.\n
	7+: your enemies are impressed and overly cautious, scared and demoralised, or angry and careless (MC’s choice)
	10+: you choose```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Serious badass
	elif message.content.startswith(".seriousbadass"):
		# Form the message
		msg = """```When you enter a charged situation, roll Style.\n
	10+: gain 2 hold
	7–9: gain 1 hold
	6-: your enemies identify you immediately as their foremost threat\n
Spend 1 hold to make eye contact with an NPC present, who freezes or flinches and can’t act until you break it off.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Trained eye
	elif message.content.startswith(".trainedeye"):
		# Form the message
		msg = """```When you evaluate a person, vehicle, drone or gang, roll Cool.\n
	7+: ask the target “How are you vulnerable to me?” Take +1 forward when acting on the answer
	10+: gain +1 ongoing when acting against that target```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Driven
	elif message.content.startswith(".driven"):
		# Form the message
		msg = """```When you begin a mission that furthers your vision, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
You may spend 1 hold before rolling any other move to take +1 or -2 forward to the move.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Vision thing
	elif message.content.startswith(".visionthing"):
		# Form the message
		msg = """```When you have time and space for an emotional connection with someone and you passionately advocate for your vision, roll Style.\n
	10+: gain 2 hold
	7-9: gain 1 hold\n
Spend 1 hold to have the targeted NPCs:
	• give you something you want
	• do something you ask
	• fight to protect you or your cause
	• disobey an order given by someone with authority or leverage over them\n
When you use this move on a PC, spend your hold to help or interfere as if you had rolled a 10+ (i.e. give them +1 or -2). If you miss against a PC, they gain 2 hold against you which they can use in the same way.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Live and on the air
	elif message.content.startswith(".live"):
		# Form the message
		msg = """```When you go live from the scene and broadcast a stream to avoid harm and expose your target, roll Edge.\n
	7+: you get the shot you want and are “escorted” to a position of safety
	7-9: choose one:
		• Your story irritates your target (The MC will advance a relevant Threat Clock)
		• Someone on your team gets hurt off camera
		• Your story angers your employer
		• Your rushed narrative is misinterpreted by the public with unintended consequences```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Nose for a story
	elif message.content.startswith(".nose"):
		# Form the message
		msg = """```At the start of a mission, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold\n
During the mission, spend 1 hold to invoke one of the following effects:
	• Ask one question from the research list
	• Take +1 forward when monstering
	• Find a piece of evidence that links this mission to a current story; start a Story Clock and a linked Noise Clock or roll to gather evidence```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Gather evidence
	elif message.content.startswith(".gatherevidence"):
		# Form the message
		msg = """```When you gather evidence to break a story, roll Mind.\n
	10+: you get the evidence you need, advance that Story Clock
	7-9: you get the evidence, but tip your hand to someone implicated in your story; tell the MC which clock to advance: a relevant Corporate Clock, the linked Noise Clock or the relevant Mission Clock (Legwork or Action, depending on which phase of the current mission you’re in)
	6-: the MC will advance the Noise Clock and make a move\n
If the Story Clock reaches 0000 before the Noise Clock, the Reporter has broken the story before the implicated parties could cover up the evidence, or stop the investigation. The exact implications of this for the game will vary based on the story, but it should have a major impact on the implicated parties and will affect at least one Corporate Clock.\n
If the Noise Clock reaches 0000 before the Story Clock, the implicated parties have tied up all the loose ends and the story is dead. Now that damage control is complete, they can deal with the Reporter permanently. Advance any relevant Corporate or Threat Clocks.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Monstering
	elif message.content.startswith(".monstering"):
		# Form the message
		msg = """```When you corner someone and hound them with questions to get to the bottom of a story, roll Edge.\n
	10+: they tell you the truth, regardless of the consequences
	7-9: they give you enough to get you off their back, then when they’re safe, they choose one:
		• they respond with fear
		• they respond with anger
		• they respond with clinical calm```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# I love it when a plan comes together
	elif message.content.startswith(".plan"):
		# Form the message
		msg = """```At the start of a mission, roll Edge.\n
	10+: gain 3 hold
	7-9: gain 1 hold
	6-: gain 1 hold anyway, but your opponent has predicted your every move; the MC will advance the Legwork Clock\n
During the mission, spend 1 hold for one of the following effects:
	• You have that piece of gear that you need, right now
	• You appear in a scene where you are needed, right now```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Exit strategy
	elif message.content.startswith(".exitstrategy"):
		# Form the message
		msg = """```You always have an escape plan prepared. When shit hits the fan and you decide to bail out, roll Mind.\n
	7+: You escape the situation
	10+: choose one thing to leave behind
	7-9: choose two things
		• Your team
		• A mission objective
		• Identifiable evidence
		• Your staked Cred```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Recruiter
	elif message.content.startswith(".recruiter"):
		# Form the message
		msg = """```When you attempt to recruit a specialist or a team of specialists to directly assist with your mission, roll Edge.\n
	10+: choose 2
	7-9: choose 1
		• Reliable professional(s)
		• A small team (up to 5)
		• As competent as required```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Slippery
	elif message.content.startswith(".slippery"):
		# Form the message
		msg = """```At the end of a mission during which you planted or hid evidence to shift blame away from you and your team, name who you threw under the corporate bus and roll Edge.\n
	7+: the MC will not increase Corporate Clocks in the retaliation phase
	10+: the MC will reduce a Corporate Clock by one
	6-: create or increase the Threat Clock of whoever you threw under the bus```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Storage
	elif message.content.startswith(".storage"):
		# Form the message
		msg = """```After receiving a job you may look through your accumulated parts and supplies for equipment that might help with the current mission. Roll Mind.\n
	10+: gain 3 [gear] relevant to your chosen area(s) of expertise.
	7-9: gain 1 [gear] relevant to your chosen area(s) of expertise.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Blend in
	elif message.content.startswith(".blendin"):
		# Form the message
		msg = """```When you’re about to be caught somewhere you shouldn’t be, but look and act like you belong there, roll Cool.\n
10+: no one thinks twice about your presence until you do something to attract attention
7-9: you’ll be fine as long as you leave right now, but if you do anything else, your presence will arouse suspicion```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Bypass
	elif message.content.startswith(".bypass"):
		# Form the message
		msg = """```When you attempt to subvert security measures (bypassing a locked door, disabling an alarm, camera or motion detector, etc), roll Cool.\n
	7+: you successfully bypass the system without leaving a trace
	10+: you gain some valuable insight into the facility’s security, gain [intel]```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	###############################################################################################################################################
	###############################################################################################################################################
	############################################################## CUSTOM MOVE COMMANDS ###########################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Git along little dogie
	elif message.content.startswith(".dogie"):
		# Form the message
		msg = """```When you want to use Waleed to antagonise, roll Style (or +1 Synth if you both have Neural Interface).\n
	7+ you antagonise one character, giving you +1 Ongoing to act against that character
	7-9 Choose One:
	10+ Choose Two:
 		- Waleed antagonises one additional character, but will struggle to escape harm
 		- Waleed will escape harm, but will not antagonise for long
 		- Waleed will allow you to escape harm, but will struggle to escape harm
 		- Waleed will apply lethal force, but take his sweet time
 		- Waleed will chase down a lead over great distance, but you will struggle to maintain contact```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Nose for trouble
	elif message.content.startswith(".trouble"):
		# Form the message
		msg = """```When you want to use Waleed to Assess a person, place or thing, justify why dog senses are better than yours and roll Cool (or +1 Synth if you both have Neural Interface). On a hit, gain +1 additional hold.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# He's good, but I'm better
	elif message.content.startswith(".goodbetter"):
		# Form the message
		msg = """```When you attempt to outwit a sentient opponent in The Matrix, roll Edge.\n
	7+ you temporarily evade/escape/overcome your opponent
	10+ gain 1 hold. Spend this to temporarily evade/escape/overcome your opponent at any other time in this run. 
	6- your opponent gets the better of you.```"""
		
		# Send the message
		await client.send_message(message.channel, msg.format(message))

	###############################################################################################################################################
	###############################################################################################################################################
	################################################################# DRUG COMMANDS ###############################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Spank
	elif message.content.startswith(".spank"):
		# Form the message
		msg = """```While Active:
	+1 Meat
	-1 Synth
	+unreliable on cyber gear
	+1 Harm on Melee Attacks
	+short\n
Withdrawal:
	-2 Style
	-1 Meat
	-long```"""

		#Send the message
		await client.send_message(message.channel, msg.format(message))

	# Motherfuck
	elif message.content.startswith(".motherfuck"):
		# Form the message
		msg = """```While Active:
	+2 Edge
	-2 Cool
	-long\n
Withdrawal:
	-1 Cool
	-day```"""

		#Send the message
		await client.send_message(message.channel, msg.format(message))

	# Domo
	elif message.content.startswith(".domo"):
		# Form the message
		msg = """```While Active:
	+2 Synth
	-1 Everything else
	Take 1 Harm (increases per use per day)
	-instant\n
Withdrawal:
	-1 Synth
	+Harmful on cybergear
	-short```"""

		#Send the message
		await client.send_message(message.channel, msg.format(message))

	# Clutch
	elif message.content.startswith(".clutch"):
		# Form the message
		msg = """```While Active:
	-1 to Take Harm move
	-1 Mind
	-short\n
Withdrawal:
	Cardiac arrest if taken more than twice a day```"""

		#Send the message
		await client.send_message(message.channel, msg.format(message))

	# Meatloaf
	elif message.content.startswith(".meatloaf"):
		# Form the message
		msg = """```While Active:
	+fast reflexes
	-short\n
Withdrawal:
	-2 Meat
	-2 Edge
	-long```"""

		#Send the message
		await client.send_message(message.channel, msg.format(message))

	###############################################################################################################################################
	###############################################################################################################################################
	############################################################ MISCELLANEOUS COMMANDS ###########################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Rolls 2d6 dice
	elif message.content.startswith(".roll") or message.content.startswith(".dice"):
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

		# Send the message
		await client.send_message(message.channel, msg.format(message))

	# Adds a new clock
	elif message.content.startswith(".addclock"):
		# Get the clock name and assign it default value of 1200
		tokens = message.content.split(".addclock ")
		clock = (tokens[1], "1200")

		# Checks if clock has already been added
		for c in clocks:
			# Case insensitive
			name = c[0].lower()
			inName = tokens[1].lower()

			if name == inName:
				msg = "```Clock already exists.```"
				await client.send_message(message.channel, msg.format(message))
				return

		# Append to clocks list
		clocks.append(clock)

		# Update and refresh file
		updateAndRefreshData("clocks", clocks)
		print("Clock added to file: {" + tokens[1] + ", 1200}")

		# Form message and send
		msg = "```Clock added: " + tokens[1] + " at 1200.```"
		await client.send_message(message.channel, msg.format(message))

	# Deletes a clock
	elif message.content.startswith(".deleteclock"):
		# Get the clock name
		tokens = message.content.split(".deleteclock ")
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
		msg = "```Deleted clock " + name + ".```"
		await client.send_message(message.channel, msg.format(message))

	# Increases a clock by one segment
	elif message.content.startswith(".increaseclock"):
		# Get the clock name
		tokens = message.content.split(".increaseclock ")
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
				if value == "1200": value = "1500"
				elif value == "1500": value = "1800"
				elif value == "1800": value = "2100"
				elif value == "2100": value = "2200"
				elif value == "2200": value = "2300"
				elif value == "2300": value = "0000"
				elif value == "0000":
					msg = "```Clock is already at midnight.```"
					await client.send_message(message.channel, msg.format(message))
					return

				# Create new tuple and replace previous one
				updatedClock = (clock[0], value)
				index = clocks.index(clock)
				clocks[index] = updatedClock

		# Check if the clock was found
		if not found:
			msg = "```Clock \"" + name + "\" not found.```"
			await client.send_message(message.channel, msg.format(message))
			return

		# Update and refresh file
		updateAndRefreshData("clocks", clocks)
		print("Clock update reflected in file (INCREASE): (" + updatedClock[0] + ", " + updatedClock[1] + ")")

		# Form message and send
		msg = "```" + updatedClock[0] + " clock increased to " + updatedClock[1] + ".```"
		await client.send_message(message.channel, msg.format(message))

	# Decreases a clock by one segment
	elif message.content.startswith(".decreaseclock"):
		# Get the clock name
		tokens = message.content.split(".decreaseclock ")
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
				if value == "0000": value = "2300"
				elif value == "2300": value = "2200"
				elif value == "2200": value = "2100"
				elif value == "2100": value = "1800"
				elif value == "1800": value = "1500"
				elif value == "1500": value = "1200"
				elif value == "1200":
					msg = "```Clock is already at 1200.```"
					await client.send_message(message.channel, msg.format(message))
					return

				# Create new tuple and replace previous one
				updatedClock = (clock[0], value)
				print(updatedClock)
				index = clocks.index(clock)
				clocks[index] = updatedClock

		# Check if the clock was found
		if not found:
			msg = "```Clock \"" + name + "\" not found.```"
			await client.send_message(message.channel, msg.format(message))
			return

		# Update and refresh file
		updateAndRefreshData("clocks", clocks)
		print("Clock update reflected in file (DECREASE): (" + updatedClock[0] + ", " + updatedClock[1] + ")")

		# Form message and send
		msg = "```" + updatedClock[0] + " clock decreased to " + updatedClock[1] + ".```"
		await client.send_message(message.channel, msg.format(message))

	# Adds a new contact
	elif message.content.startswith(".addcontact"):
		# Get the contact name and description
		tokens = message.content.split()
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
				msg = "```Contact already exists.```"
				await client.send_message(message.channel, msg.format(message))
				return

		# Append to contacts list
		contacts.append(contact)

		# Update and refresh file
		updateAndRefreshData("contacts", contacts)
		print("Contact added to file: {" + tokens[1] + ", " + description + "}")

		# Form message and send
		msg = "```Contact added: " + tokens[1] + ".```"
		await client.send_message(message.channel, msg.format(message))

	# Deletes a contact
	elif message.content.startswith(".deletecontact"):
		# Get the clock name
		tokens = message.content.split()
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
		msg = "```Deleted contact " + name + ".```"
		await client.send_message(message.channel, msg.format(message))

	###############################################################################################################################################
	###############################################################################################################################################
	#################################################################### GARBAGE ##################################################################
	###############################################################################################################################################
	###############################################################################################################################################

	# Refreshes the clocks and contacts file
	elif message.content.startswith(".refresh"):
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

		# Send message
		await client.send_message(message.channel, msg.format(message))

	elif message.content.startswith(".log"):
		# Get log message from message
		tokens = message.content.split(".log ")
		log = tokens[1]

		# Write to the file
		file = open("log.txt", "a")
		file.write(log + "\n")
		file.close()
		print("Log saved: \"" + log + "\"")

		# Form and send message
		msg = "```Log saved.```"
		await client.send_message(message.channel, msg.format(message))

	else:
		msg = "```Invalid command. Type '.help' for a list of commands.```"
		await client.send_message(message.channel, msg.format(message))

# CONSOLE LOGGING
@client.event
async def on_ready():
	print("Logged in as")
	print (client.user.name)
	print(client.user.id)
	print("------")

client.run(TOKEN)
