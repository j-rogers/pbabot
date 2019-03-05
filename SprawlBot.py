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
