import discord
import random
import pickle
import argparse
from games import *

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

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--game', type=str, required=True, choices=['sprawl', 'apoc'])
args = parser.parse_args()
game = vars(args)['game']
print(game)

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



# MESSAGE COMMANDS
@client.event
async def on_message(message):
	# Prevents bot replying to itself
	if message.author == client.user:
		return

	# Prevents bot responding to regular messages
	if not message.content.startswith("."):
		return


	if game == 'sprawl':
		response = sprawl.handle(message)
		await client.send_message(message.channel, response.format(message))

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
.playbooks: Displays a list of playbooks.
.matrix: Displays a list of matrix-specific moves.
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
.rip: Displays a list of dead characters and how they died.
.f: Same as '.rip'
.remember: Displays a message of a memorable moment.
.refresh: Reloads the clock and contact data.
.log <message>: Saves a message to the log file.```"""

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
		msg = """```
Christof Romuald: Died to Syntax Terror's Bear Drones while being pounded on by Police. F in chat please.\n
Noor 'Shareef' Jerkof: Noor's death was on their own account, they ended up shooting themself in the head when they realized they couldn't talk to people and were on their way to jail.\n
Martin Monis Jr: That time MartinJr took the entire team on in bar shoot up, manged to walk out mostly fine then was shot in the head by a sniper.\n
Azrael: Azrael was a shit sniper and wouldn't follow the plan, resulting in complications for Laramy and Syntax Terror. Bad mistake Azrael as we framed him resulting in a brutal death.\n
H4KKK3R: H4KKK3R was in the car with Seraph, trying to guide Laramy to where Syntax Terror was so we could take our revenge. While Jacked into police cameras, Seraph shot them in the head. \n
Laramy Fisk: Was murdered by Seraph. After Laramy blammed Syntax Terror on why the van blew up, Seraph didn't take kindly, resulting in Seraph running Laramy over and shotting him after he manged to live.\n
Seraph: Seraph thought they were safe, thought Syntax Terror would be happy, were on their way to Byntax Berror, when a secret chip Syntax had implanted alerted a sniper from The business to shot Seraph dead.\n
Syntax Terror: Syntax Terror managed to live out his days, always being paranoid and on edge.\n
Swarf Gander: Swarf killed himself with flashbangs to try avoid hearing Mercer's music.\n
Mercer De'am: Mercer died by the hands of Tony when an orbital strike was set upon his location.\n
Desperato: Desperato also died to the hands of Tony when an orbital strike was set upon their location.\n
Velvet Thunder: Died to The Donald, bashed by the wall, and then shot in the head.\n
The Donald: The Donald died to the Valencia gang, if only he didn't shoot Velvet Thunder, but that's not how the art of the deal.\n
Daiki: Upon being tazzed by Velvet Thunder, and the Valencia gang going to take their shot, Daiki had his car blow everyone up, not just taking his on life but 8 of the Valencia gang.\n
```"""

		# Send message
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
	elif message.content.startswith(".applyfirstaid") or message.content.startswith(".firstaid") or message.content.startswith("aid"):
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
	elif message.content.startswith(".playhardball") or message.content.startswith(".hardball"):
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
	elif message.content.startswith(".mixitup") or message.content.startswith(".mix"):
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
	elif message.content.startswith(".undertheknife") or message.content.startswith(".under") or message.content.startswith(".knife"):
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
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		roll = dice1 + dice2
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
	elif message.content.startswith(".getthejob") or message.content.startswith(".job"):
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
	elif message.content.startswith(".gettingpaid") or message.content.startswith(".getpaid") or message.content.startswith(".paid"):
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
	elif message.content.startswith(".melt") or message.content.startswith(".meltice"):
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
	############################################################ Apocalpyse world #################################################################
	###############################################################################################################################################
	###############################################################################################################################################
	
	##			 ##
	##Angel Moves##
	##			 ##
	#Sixth Sense
	elif message.content.startswith(".sixthsense"):
		msg - """``` Sixth sense: when you open your brain to the world’s psychic maelstrom,
		roll+sharp instead of roll+weird.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#infirmary	
	elif message.content.startswith(".infrimary"):
		msg - """```Infirmary:
		you get an infirmary, a workspace with life support,
a drug lab and a crew of 2 (Shigusa & Mox, maybe). Get patients
into it and you can work on them like a savvyhead on tech (cf ). 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Professional compassion
	elif message.content.startswith(".yeeeeeeeeeeeeeet"):
		msg - """``` 
		Professional compassion: 
		you can choose to roll+sharp instead of roll+Hx when you help someone who’s rolling.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Battlefield grace
	elif message.content.startswith(".battlefieldgrace"):
		msg - """``` Battlefield grace: while you are caring for people, not fighting, you get +1armor.```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Healing touch	
	elif message.content.startswith(".healingtouch"):
		msg - """```Healing touch: 
		when you put your hands skin-to-skin on a
wounded person and open your brain to them, roll+weird. 
On a 10+, heal 1 segment. 
On a 7–9, heal 1 segment, but you’re acting under fire from your patient’s brain. 
On a miss: first,
you don’t heal them. Second, you’ve opened both your brain
and theirs to the world’s psychic maelstrom, without protection
or preparation. For you, and for your patient if your patient’s
a fellow player’s character, treat it as though you’ve made that
move and missed the roll. For patients belonging to the MC,
their experience and fate are up to the MC.```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Touched by death
	elif message.content.startswith(".touchedbydeath"):
		msg - """```
		Touched by death: whenever someone in your care dies, you get
		+1weird (max +3). 	
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	##			 ##
	##Battlebabe Moves##
	##			 ##
	#Dangerous and Sexy
	elif message.content.startswith(".dangerousandsexy"):
		msg - """```Dangerous & sexy:
		when you enter into a charged situation, roll+hot.
		On a 10+, hold 2. 
		On a 7–9, hold 1. 
		Spend your hold 1 for 1 to make eye contact with an NPC present,
who freezes or flinches and can’t take action until you break it off. 
On a miss, your enemies identify you immediately as their foremost threat. 
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Ice Cold
	elif message.content.startswith(".icecold"):
		msg - """```Ice cold: when you go aggro on an NPC, roll+cool instead of roll+hard.
		 When you go aggro on another player’s character, roll+Hx instead of roll+hard.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Merciless
	elif message.content.startswith(".merciless"):
		msg - """```Merciless: when you inflict harm, inflict +1harm. 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Visions of death.
	elif message.content.startswith(".visionsofdeath"):
		msg - """```Visions of death: 
		when you go into battle, roll+weird.
		 On a 10+, name one person who’ll die and one who’ll live.
		 On a 7–9, name one person who’ll die OR one person who’ll live. 
		 Don’t name a player’s character; name NPCs only. The MC will make your vision come true, if it’s even remotely possible. 
		 On a miss, you foresee your own death, and accordingly take -1 throughout the battle. 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Perfect Insticts
	elif message.content.startswith(".perfectinstincts"):
		msg - """```Perfect instincts: 
		when you’ve read a charged situation and you’re acting on the MC’s answers, take +2 instead of +1.		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Impossible Reflexes.
	elif message.content.startswith(".impossiblereflexes"):
		msg - """```Impossible reflexes: 
		the way you move unencumbered counts as armor. If you’re
naked or nearly naked, 2-armor; if you’re wearing non-armor fashion, 1-armor. If you’re
wearing armor, use it instead. 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))

	##			 ##
	##Brainer Moves##
	##			 ##
	#Unnatural lust transfixion
	elif message.content.startswith(".unnaturallusttransfixion"):
		msg - """```Unnatural lust transiixion: 
		when you try to seduce someone, roll+weird instead of roll+hot. 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Casual brain receptivity
	elif message.content.startswith(".casualbrainreceptivity"):
		msg - """```Casual brain receptivity: 
		when you read someone, roll+weird instead of roll+sharp.
Your victim has to be able to see you, but you don’t have to interact. 		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#preternatural at will brain atturnment
	elif message.content.startswith(".pretnernatual"):
		msg - """``` 
		Preternatural at-will brain attunement: 
		you get +1weird (weird+3).
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Deep brain scan
	elif message.content.startswith(".deepbrainscan"):
		msg - """``` Deep brain scan: 
		when you have time and physical intimacy
		with someone — mutual intimacy like holding them in your
		arms, or 1-sided intimacy like they’re restrained to a table — you
		can read them more deeply than normal. Roll+weird. 
		On a 10+,hold 3. 
		On a 7–9, hold 1. 
		While you’re reading them, spend your
		hold to ask their player questions, 1 for 1:
		• what was your character’s lowest moment?
		• for what does your character crave forgiveness, and of whom?
		• what are your character’s secret pains?
		• in what ways are your character’s mind and soul vulnerable?
		On a miss, you inflict 1-harm (ap) upon your subject, to no
		benefit.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Direct brain whisper projection
	elif message.content.startswith(".directbrainwhisperprojection"):
		msg - """```Direct-brain whisper projection: 
		you can roll+weird to get the effects of going aggro, without going aggro. Your victim has to
be able to see you, but you don’t have to interact. If your victim
forces your hand, your mind counts as a weapon (1-harm ap
close loud-optional).	
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#in brain puppet string
	elif message.content.startswith(".inbrainpupperstrings"):
		msg - """```In-brain puppet strings: 
		when you have time and physical
		intimacy with someone — again, mutual or 1-sided — you can
		plant a command inside their mind. Roll+weird.
		 On a 10+, hold 3. 
		 On a 7–9, hold 1. 
		At your will, no matter the circumstances,
		you can spend your hold 1 for 1:
		• inflict 1-harm (ap)
		• they take -1 right now
		If they fulfill your command, that counts for all your remaining
		hold. On a miss, you inflict 1-harm (ap) upon your subject, to no
		benefit. 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))

	##			 ##
	##Chopper moves##
	##			 ##

	#pack alpha
	elif message.content.startswith(".packalpha"):
		msg - """``` 
		Pack alpha: when you try to impose your will on your gang, roll+hard. 
		On a 10+, all 3. 
		On a 7–9, choose 1:
		• they do what you want
		• they don’t fight back over it
		• you don’t have to make an example of one of them
		On a miss, someone in your gang makes a dedicated bid to
		replace you for alpha.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#fuckingthieves
	elif message.content.startswith(".fuckingthieves"):
		msg - """```
		Fucking thieves: when you have your gang search their pockets and saddlebags for something, roll+hard. 
		It has to be something small enough to fit. 
		On a 10+, one of you happens to have just the thing, or close enough. 
		On a 7–9, one of you happens to have
		something pretty close, unless what you’re looking for is hi-tech,
		in which case no dice. On a miss, one of you used to have just the
		thing, but it turns out that some asswipe stole it from you.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))

	##			 ##
	##Driver moves##
	##			 ##

	#a no shit driver
	elif message.content.startswith(".noshitdriver"):
		msg - """``` A no shit driver: 
		when behind the wheel…
		…if you do something under fire, add your car’s power to your
		roll.
		…if you try to seize something by force, add your car’s power to
		your roll.
		…if you go aggro, add your car’s power to your roll.
		…if you try to seduce or manipulate someone, add your car’s
		looks to your roll.
		…if you help or interfere with someone, add your car’s power to
		your roll.
		…if someone interferes with you, add your car’s weakness to
		their roll.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#Good in the clinch
	elif message.content.startswith(".goodintheclinch"):
		msg - """```Good in the clinch:
		 when you do something under fire, roll+sharp instead of roll+cool.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#weather eye
	elif message.content.startswith(".weathereye"):
		msg - """```
		Weather eye: when you open your brain to the world’s psychic
maelstrom, roll+sharp instead of roll+weird.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))	
	#daredevil
	elif message.content.startswith(".daredevil"):
		msg - """``` Daredevil: if you go straight into danger without hedging your
bets, you get +1armor. If you happen to be leading a gang or
convoy, it gets +1armor too.
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#my other car is a tank
	elif message.content.startswith(".myothercarisatank"):
		msg - """``` My other car is a tank: 
		you get an additional car. Give it
		mounted machine guns (3-harm close/far area messy) or
		grenade launchers (4-harm close area messy) and +1armor.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))

	##			 ##
	##Gunslinger moves##
	##			 ##
	#battle-hardened
	elif message.content.startswith(".battlehardended"):
		msg - """```Battle-hardened: 
		when you act under fire, roll+hard instead of roll+cool. 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#fuck this shit
	elif message.content.startswith(".fuckthisshit"):
		msg - """```Fuck this shit:
		 name your escape route and roll+hard. 
		 On a 10+,sweet, you’re gone. 
		 On a 7–9, you can go or stay, but if you go it costs you: leave something behind, or take something with you, the MC will tell you what. 
		 On a miss, you’re caught vulnerable,
		 half in and half out.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#battlefieldinstincts
	elif message.content.startswith(".battlefieldinstints"):
		msg - """```Battlefield instincts:
		when you open your brain to the world’s
		psychic maelstrom, roll+hard instead of roll+weird, but only in
		battle.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#blood craze
	elif message.content.startswith(".bloodcrazed"):
		msg - """```Bloodcrazed: whenever you inflict harm, inflict +1harm.
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#not to be fucked with
	elif message.content.startswith(".nottobefuckedwith"):
		msg - """```NOT TO BE FUCKED WITH: in battle, you count as a gang
(3-harm gang small), with armor according to the circumstances. 
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))	
	##			 ##
	##Apoc basic Moves##
	##			 ##
	#battle-hardened
	elif message.content.startswith(".apocbasic"):
		msg - """```Do something under fire (.dosomethingunderfire)
					Go Aggro (.goaggro)
					Seize by force (.seizebyforce)
					Read a sitch (.readasitch)
					Read a person (.readaperson)
					Open your brain (.openyourbrain)
					Cover fire (.coverfire)
					Maintin Position (.maintainposition)
					Stay teh fuck down (.staythefuckdown)
					Follow other move (.followothermove)
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#follwothermove
	elif message.content.startswith(".followothermove"):
		msg - """```When you follow through on someone else’s move, roll+Hx.
If it’s one of the MC’s characters’, roll+sharp. On a 10+, the MC
chooses one of the following for you, as appropriate:
• you inflict +1harm
• you dominate someone’s position
• you make an untenable position or course secure
• you avoid all fire
• you create an opportunity and follow through to full effect
On a 7–9, you create an opportunity, but you haven’t seized it
or followed through on it yet. e MC will tell you what it is.
On a miss, the MC chooses one of the above for an appropriate
character of her own.
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#stay the fuck down
	elif message.content.startswith(".staythefuckdown"):
		msg - """```When you stay the fuck down, roll+sharp. On a hit, you’re in
a relatively safe spot for the rest of the battle. On a 10+, you
come under no fire. On a 7–9, you come under only incidental
fire. On a miss, you have to break position now or come under
concentrated fire.
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#maintainposition
	elif message.content.startswith(".maintainposition"):
		msg - """```
		When you maintain an untenable position or course,
roll+hard. On a 10+, you can hold it, and for 3 ticks you’ll come
under only incidental fire, even past 9:00. On a 7–9, you can hold
it, and for a tick you’ll come under only incidental fire. Either way
you can abandon it before your time is up to avoid concentrated
fire. On a miss, abandon it now or suffer concentrated fire. (If it’s
before 9:00, now it’s 9:00.)		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#coverfire	
	elif message.content.startswith(".coverfire"):
		msg - """```When you provide covering fire for someone, roll+cool. On a
10+, you keep them from coming under concentrated fire, even
past 9:00. On a 7–9, their position or course is untenable, and
they proceed accordingly. On a miss, they suffer concentrated
fire now. (If it’s before 9:00, now it’s 9:00.)
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#open your brain
	elif message.content.startswith(".openyourbrain"):
		msg - """```OPEN YOUR BRAIN
When you open your brain to the world’s psychic maelstrom,
roll+weird. On a hit, the MC will tell you something new and
interesting about the current situation, and might ask you a
question or two; answer them. On a 10+, the MC will give you
good detail. On a 7–9, the MC will give you an impression. If you
already know all there is to know, the MC will tell you that.
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#read a person
	elif message.content.startswith(".readaperson"):
		msg - """```READ A PERSON
When you read a person in a charged interaction, roll+sharp.
On a 10+, hold 3. On a 7–9, hold 1. While you’re interacting with
them, spend your hold to ask their player questions, 1 for 1:
• is your character telling the truth?
• what’s your character really feeling?
• what does your character intend to do?
• what does your character wish I’d do?
• how could I get your character to __?		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#read a sitch
	elif message.content.startswith(".readasitch"):
		msg - """```
		READ A SITCH
When you read a charged situation, roll+sharp. On a hit, you
can ask the MC questions. Whenever you act on one of the MC’s
answers, take +1. On a 10+, ask 3. On a 7–9, ask 1:
• where’s my best escape route / way in / way past?
• which enemy is most vulnerable to me?
• which enemy is the biggest threat?
• what should I be on the lookout for?
• what’s my enemy’s true position?
• who’s in control here?
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#seize by force
	elif message.content.startswith(".seizebyforce"):
		msg - """```SEIZE BY FORCE
When you try to seize something by force, or to secure your
hold on something, roll+hard. On a hit, choose options. On a
10+, choose 3. On a 7–9, choose 2:
• you take definite hold of it
• you suffer little harm
• you inflict terrible harm
• you impress, dismay or frighten your enemy
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#go aggro
	elif message.content.startswith(".goaggro"):
		msg - """```GO AGGRO
When you go aggro on someone, roll+hard. On a 10+, they have
to choose: force your hand and suck it up, or cave and do what
you want. On a 7–9, they can instead choose 1:
• get the hell out of your way
• barricade themselves securely in
• give you something they think you want
• back off calmly, hands where you can see
• tell you what you want to know (or what you want to hear)
		
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#dosomethignunderfire
	elif message.content.startswith(".dosomethingunderfire"):
		msg - """```DO SOMETHING UNDER FIRE
When you do something under fire, or dig in to endure fire, roll+cool. 
On a 10+, you do it.
 On a 7–9, you flinch, hesitate, or stall: the MC can offer you a worse outcome, a hard bargain, or
an ugly choice
		```"""
		#Send the message
		await client.send_message(message.channel, msg.format(message))
	#added apoc books
	elif message.content.startswith(".apocbooks"):
		msg - """```Angel
					Battlebabe
					Brainer
					Chopper
					Driver
					Gunslinger 
		```"""
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

	elif message.content.startswith(".remember"):

		#Generates random number to get remember message from  events that have happened in sprawl. Feel free to add more.

		member = random.randint(1,116)
		msg = ""
		
		#Christof
		if member == 1:
			msg = "```Remember that time Christof tackled a Robot Synth thing to save Seraph?```"
		elif member == 2:
			msg ="```Remember that time Christof said he wasn't going to bring Waleed but did but never used him?```"
		elif member == 3:
			msg = "```Remember that time Christof forgot Waleed in a drug den and Waleed got picked up the Police and Medtech?```"
		elif member == 4:
			msg = "```when Christof didn\'t use Waleed to sniff for a bomb then dived in front of Maxine when it exploded?```"
		elif member == 5:
			msg = "```Remember that time Christof was doubting that Syntax Terror was a junkie, whilest Syntax Terrror had no pants on in a drug den?```"    
		elif member == 6:
			msg = "```Remember that time Christof brutally killed a bunch of goons all at once with his barehands```"
		elif member == 7:
			msg = "```Ever been to a Vet for serious medical attention? because Christoff has.```"
		elif member == 8:
			msg = "```Christof threw H4KKK3R out of the way of a building falling down, fun times for everyone.```"
		elif member == 9:
			msg = "```Christof charged into heavily armed police and took a shotgun to the face before finally dying to Syntax Terrors drones. F is chat please...```"
		#laramy Fisk
		elif member == 10:
			msg = "```That Laramy stabbed Noor with with some drugs and Noor then ran out infront of a truck. Good times. ```" 
		elif member == 11:
			msg = "```That time Laramy didn't show up cause he was super high at home. Hope that mission went well.```"
		elif member == 12:
			msg = "```Keep the drugs away from Laramy cause he's been known to take some Meatloaf followed by other drugs and go on a killing spree both friend and foe```" 
		elif member == 13:
			msg = "```That time Laramy had Meatloaf and  rocket launcher thing and proceeded to shot the building to get the mission done!```" 
		#Seraph
		elif member == 14:
			msg = "```That time Seraph parkoured up a convayor belt, jumped into the air and dabbed their way onto the next floor up!```"
		elif member == 15:
			msg = "```How long did Seraph drag Christoff's body around when he died?```" 
		elif member == 16:
			msg = "```*Looks in window* shots a goon in the face, gets a van. Good job Seraph.```" 
		elif member == 17:
			msg = "``` Seraph somehow snuck a grendade into a pot plant while being watched by gaurds and managed to get Noor to take the full on it.```"
		elif member == 18:
			msg = "```Remember when Seraph tried killing Tony and had their arm broken and sent to jail?```" 
		elif member == 19:
			msg = "```Who's got a cyber arm thanks to the Thing? Thats right Seraph does.```" 
		#Syntax Terror
		elif member == 21:
			msg = "```I used my  bear drones (thats right more than one) to win the slaughterfest, -syntax terror```" 
		elif member == 22:
			msg = "```With enough cred Syntax terror managed to buy Seraph. Good job Syntax Terror!```" 
		elif member == 23:
			msg = "```Getting bear drones to blow up police to help us escapse, no problem for Syntax Terror```" 
		#H4KKK3R
		elif member == 24:
			msg = "```H4KKK3R can hack a aircon, and make the room a little cold. Nice hacking right there!```" 
		elif member == 25:
			msg = "```H4KKK3R just jackin into the Matrix while standing in a bar, it happens more than you think. ```" 
		elif member == 26:
			msg = "```When H4KKK3R tried fleeing the scene only to be shot and lose some memory```" 
		elif member == 27:
			msg = "```That time H4KKK3R took some braind damage from failing to get past some black ice```" 
		elif member == 28:
		#Noor
			msg = "```Whats for lunch?```" 
		elif member == 29:
			msg = "```That time Noor said they were responsible for putting a grenade in the pot plant only to then shoot themself. F in chat if you really want to but probs dont bother...```" 
		elif member == 30:
			msg = "```Noors good at talking and seducing people. Just kidding probably being thrown out by gaurds or getting attacked or something instead.```" 
		elif member == 31:
			msg = "```That time Noor was useful by having a gun out that Laramy stole and shot gaurds with.```" 
		elif member == 32:
			msg = "```Remember when Noor got shot because Laramy tried to steal Seraphs gun?```" 
		#Martin Jr
		elif member == 33:
			msg = "```When we all tried to kill Martin JR and that manged to tank and seriously harm the entire group.```" 
		elif member == 34:
			msg = "```Martin JR gets injured at a bar from a gun fight, walks out of said bar into a sniper bullet, some how still managing to live and get taken to a hospital, only to then die. F in chat if you think Martin JR deserves it.```" 
		#Azrael
		elif member == 35:
			msg = "```Who hides in a dumpster and 'provides'sniper cover? Azrael (to the tune of Spongebob)```" 
		elif member == 36:
			msg = "```When Azrael doesn't snipe people so Syntax gives their position away with a smoke grenade```" 
		elif member == 37:
			msg = "```Syntax Terror pinned some stuff on Azrael causing Azrael to get killed, please don't F in chat.```" 
		#MC
		elif member == 38:
			msg = "```That time the MC sounds like a robot just after introducing the Thing.```" 
		elif member == 39:
			msg = "```MC makes somekind of robot noise... MC clock advances.```" 
		elif member == 40:
			msg = "```Who's getting more drunk and making the outcomes worse and worse? Thats right the MC```" 
		elif member == 41:
			msg = "```*Bans Waleed from the chat*```" 
		#Last Mission Chapater 1?
		elif member == 42:
			msg ="```H4KKK3R crashed his moterbike looking like an idiot when trying to buy his shiper rifle so Seraph held everyone at gun point and demanded H4KKK3R modified it so they could also use it.```"
		elif member == 43:
			msg ="```I'm the best hacker. -Syntax Terror```"
		elif member == 44:
			msg ="```When Laramy punched H4KKK3R out(on purpose) and immidiatly patched H4KKK3R up afterwards.```"
		elif member == 45:
			msg ="```Syntax Terror actually walked Waleed, and used his senses (Slightly) WOW!```"
		elif member == 46:
			msg ="```Remember that time Syntax Terror betrayed us all by rigging his Drone to remember? Because I fucking remember that.```"
		elif member == 47:
			msg ="```Remember when Laramy accused Syntax Terror of why the van had blown up resulting in Seraph trying to also kill Laramy and H4KKK3R```"
		elif member == 48:
			msg ="```Remember when all H4KKK3R wanted was a sniper rifle but the team nearly stole or killed him over it?```"
		elif member == 49:
			msg ="```Remember when Laramy tried throwing a grenade at Seraph after Seraph tried running him over, only to have the grenade explode on Laramy from a shit through?```"
		elif member == 50:
			msg ="```Remember when Seraph outright shot H4KKK3R in the head  while sneaking past police? F in chat please.```"
		elif member == 51:
			msg ="```That time Syntax Terrors drone blew the van up and Laramy applied first aid to himself, Seraph and H4KKK3R while being questioned by police```"
		elif member == 52:
			msg ="```When Laramy nearly blew himself trying to throw a grenade at Seraph and Seraph than shot what was left of Laramy dead. F in chat please.```"
		elif member == 53:
			msg ="```When Laramy postioned garden Gnomes in a triangle or something to make a call```"
		elif member == 54:
			msg ="```When Laramy was trying to get more armor or heavy ammo from Ken Tenma but butchered it by saying something stupid about marmalade?```"
		elif member == 55:
			msg ="```When we got into an argument about how far and fast Syntax Terror could run?```"
		elif member == 56:
			msg ="```*More robot noises*```"
		elif member == 57:
			msg ="```When Seraph used their plan B to escape by stealing a bikers bike and was gonna ride away to safety until a certain call with Syntax Terror occured.```"
		elif member == 58:
			msg ="```When Seraph told Syntax Terror that Laramy and H4KKK3R were dead and then Syntax Terror triggered a tracking becon resuling in Seraph being snipped dead. F in chat please or Seraph will add you to a hitlist.```"
		elif member == 59:
			msg ="```When Seraph was dying and their last words to Syntax Terror were 'Im pregnant with H4KKK3R'```"
		elif member == 60:
			msg ="```They say Syntax Terror managed to escape the buisness after he betrayed everyone. People he failed (occasionly finished) missions with, the infiltrator be paid lots of Cred for, and even one of his own drones. They also say Syntax Terror spent the rest of his days being more and more paranoid, keeping an eye behind him.  ```"
		#Campaign 2 session 1 and 2.
		elif member == 61:
			msg = "```That time Daiki did some sick driving```"
		elif member == 62:
			msg = "```Can they see my car? Good I aim my missiles at them - Daiki```"
		elif member == 63:
			msg = "```That time Daiki and Swarf put Numberphille on suicide watch```"
		elif member == 64:
			msg = "```When Swarf paid Numberphille to take him off suicide watch.```"
		elif member == 65:
			msg = "```That time Mercer played the Obo and made some cred in the process```"
		elif member == 66:
			msg = "```*Plays the slide whistle*```"
		elif member == 67:
			msg = "```I'm going to start shitting on his lawn -Daiki```"
		elif member == 68:
			msg = "```So Daiki smellls like shit -MC ```"
		elif member == 69:
			msg = "```That time Mercer tried having a vision thing without actually taking the time to talk to someone remotely well.```"
		elif member == 70:
			msg = "```What if I drive really fast? -Daiki```"
		elif member == 71:
			msg = "```All those times Swarf threw a flash grenade and blinded everyone.```"
		elif member == 72:
			msg = "```That time Daiki got into a chase to try to impress Elina ```"
		elif member == 73:
			msg = "```Swarf flashbanged himself to death to avoid hearing Mercers music. F in chat please.```"
		elif member == 74:
			msg = "```That time Daiki became a stalker```"
		elif member == 75:
			msg = "```MC: You're a rapist. Daiki: NOOO!```"
		elif member == 76:
			msg = "```That time Daiki stalked numberphille so he could get a chicks number```"
		elif member == 77:
			msg = "```That time Mercer played the Keytar resulting in even more attention ebing drawn on the team```"
		elif member == 78:
			msg = "```That time Merver was distracted while walking to gang members resulting in a shoot out and no talking as planned.```"
		elif member == 79:
			msg = "```Swarf: I'm going to shoot everyone.\n MC: Even the baby?\n Swarf: Yes, even the baby. ```"
		elif member == 80:
			msg = "```That time everyone had to wait, because Mercer only meets TikTakToe on a Wednesday.```"
		elif member == 81:
			msg = "```That time Mercer helped Daiki somehow, by Daiki having 'Don't sue me' playing in the background.```"
		#GoofyGoober
		elif member == 82:
			msg = "```When Daiki didn't have the right permit for a car with bullet holes and shot up passengers inside it, resulting in police being shot and a high speed chase.```" 
		elif member == 83:
			msg = "```When Daiki's missile hit The Trump.```" 
		elif member == 84:
			msg = "```When Mercer actually stopped and got out of a truck when asked by Skorpio-tensi despite knowing it was stolen.```" 
		elif member == 85:
			msg = "``` When Mercer manged to pretend to faint when Skorpio-tensi were trying to arrest him.```" 
		elif member == 86:
			msg = "```That time Mercer played Goofy Goober Rock on his Keytar and kept two gaurds frozen with pure awe. ```" 
		elif member == 87:
			msg = "``` That time The Donald dropped the wall. ```" 
		elif member == 88:
			msg = "```Remember when The Donald slammed the wall into a Skorpio-tensi gaurd against a truck, so hard it went through the truck and resulted in Mercer pretty much being dead.```" 
		elif member == 89:
			msg = "```That time Mercer didn't die cause The Donald dropped him off at a hosptial and didn't just kick him out of a truck onto the street.```" 
		elif member == 90:
			msg = "```Tgat tune Mercer jumped back into the truck and kept failing to start it resulting in lots of bullets being shot at him.```" 
		elif member == 91:
			msg = "```That time Daiki remote controlled their car to lead the police off the trail a little bit```" 
		elif member == 92:
			msg = "```That time Daiki shot missiles at a drone. Oh how the turntables.```" 
		elif member == 93:
			msg = "```That time Mercer actually pulled over with a stolen truck to Skorpio-tensi who knew it was stolen, then pretended to faint, stabbing one of the skorpio-tensi gaurds in the throat with his retractable knife blades, busting his Keytar out and played Goofy Goober Rock freezing the gaurds in awe.```" 
		elif member == 94:
			msg = "```Remember when Mercers voice kept changing?```" 
		elif member == 95:
			msg = "```That time the team kept doing the same thing untill something happened```" 
		elif member == 96:
			msg ="```Remember how Mercer walked into a bar and advanced the legwork clock before even having a mission. Good times.```"
		#Honestly fuck Tony.
		elif member == 97:
			msg ="```Mercer walks into a bar thursting his arms around, Daiki akwardly follows by doing the virgin walk. The Donald then shows up late, doing the chad stride over to the meeting.```"
		elif member == 98:
			msg ="```That time Desperato, Daiki, and The Donald, did some surveillance in Mercer's helicopter, but didn't even take off from the ground or go anywhere. No wonder they didn't see anything.```"
		elif member == 99:
			msg ="```That time Mercer and Desperato got a little drunk, and then into a bar fight because people didn't like how Mercer played the triangle.```"
		elif member == 100:
			msg ="```That time Desperato got punched, threw their drink at the attack, dabbed, and managed to leave without a problem.```"
		elif member == 101:
			msg ="```That time Mercer punched Desperato in his now empty eye socket, knocking him over.```"
		elif member == 102:
			msg ="```That time Daiki, and Mercer hid in plain sight, while obviously with The Donald, tricking the Valencia gang, and more importantly Mendel that Daiki had been delt with and we stole his van as proof. Then convincing Mendel to look in the hood resulting in Mendel being gunned to death by the van. ```"
		elif member == 103:
			msg ="```That time Daiki got Mendel to look into his van, under the hood, with hidden automated guns that outright killed Mendel alerting the Valencia gang to come investigate, which Daiki than got his van to shot everyone with an auto canon. Daiki than drove out of the building, giving the finger to the Valencia gang,  getting away, while impressing them so much with his brutal attack so much they lowered their hatred for us a tad.  ```"
		elif member == 104:
			msg ="```That time Mercer and Desperato stayed back after Daiki and The Donald, drove away as a decoy, so Mercer and Desperato could maintain cover. Mercer and Desperato than ignored beeping resulting in Valencia, Mercer and Desperato to be blown up from an orbital strike.```"
		elif member == 105:
			msg ="```Tony = A bad fucking time. ```"
		elif member == 106:
			msg ="```That time Martin got salty at the MC becuase Mercer got blasted by an orbital strike, if only Martin had remembered what Tony was capable of in the first campaign, and how Tony played a role in how Christoff died.```"
		elif member == 107:
			msg ="```Fuck Tony, except that time he let Laramy use prototype rocket launcher```"
		elif member == 108:
			msg ="```That time The Donald ate a taco from the latino(Desperato) and everything was fine.```"
		#What a clusterfuck final session. Spoilers we all died.
		elif member == 109:
			msg == "```That time Daiki tried getting Velvet thunder to go deaf?```"
		elif member == 110:
			msg == "```Remember when Daiki was driving a destroyed car like in simpsons hit and run```"
		elif member == 111:
			msg == "```Remember that time Velvet Thunder tazzed Daiki, and the Donald then smashed Velvet with his wall.```"
		elif member == 112:
			msg == "```That time Velvet Thunder used his synth ears to listen to stuff```"
		elif member == 113:
			msg == "```That time Daiki wanted a fist bump from Velvet Thunder```"
		elif member == 114:
			msg == "```When Velvet Thunder broke his phone so The Donald no longer had his number```"
		elif member == 115:
			msg == "```Remember that time the Valencia gang said dont move and the Donald shot Velvet thunder resulting in the Valencia gang killing The Donald. Daiki then blew up everyone else, themself included.```"
		elif member == 116:
			msg == "```That time Daiki started driving his car remotely freaking Velvet Thunder out```"	
		#Sends the message. 
		await client.send_message(message.channel, msg.format(message))

	# Sends the map
	elif message.content.startswith(".map"):
		await client.send_file(message.channel, "Map_Sprawl.jpg")

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
