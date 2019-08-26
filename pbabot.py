import discord #version 0.16.12
import random
import pickle
import argparse
from games import *

# requires python 3.6.8

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

# Functions
def help(message):
	return """```Use \".command\" when using this bot.\n
.help: Displays this help message.
.roll: Rolls 2d6 dice.
.moves: Displays a list of basic moves.
.playbooks: Displays a list of playbooks.
.matrix: Displays a list of matrix-specific moves. [SPRAWL ONLY]
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
.ripsprawl1: Detailed deaths from the Sprawl1
.ripsprawl2: Detailed deaths from Sprawl2 
.ripapoc: Detailed deaths from Apoc World
.rip: List all dead characters.
.rememberlist: Displays rough numbers for specific moments. 
.remember: Displays a message of a memorable moment.
.refresh: Reloads the clock and contact data.
.log <message>: Saves a message to the log file.
.links: Displays a link to all the PBA games. 
```"""

def invalid(message):
	return "```Invalid command. Type '.help' for a list of commands.```"

def showclocks(message):
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

	return msg

def showcontacts(message):
	msg = "```"
	global contacts
	for contact in contacts:
		name = contact[0]
		desc = contact[1]
		msg += name + ": " + desc + "\n"

	if msg == "```":
		msg += "No contacts have been added."

	msg += "```"

	return msg

def f(message):
	msg = ""
	ripMsg = message.split()
	if len(ripMsg)>1:
		ripMsg = ripMsg[1] #will look up specific player or character. If not in switch, will return not found msg. 
	else:
		ripMsg = "list" #.rip will list all deaths simply.

	switch = {
		'list': """```
					  Martin: Christof Romulad, Laramy Fisk, Mercer De'am, Velvet Thunder, Carth\n
					  Waleed: Noor 'Shareef' Jerkof, Martin Monis Jr, Azrael\n
					  Josh F: H4KKKE3R\n
					  Josh R: Seraph, Daiki, Ligma, In[Spectre] Gadget, Jerry, Tat, Fluffy\n
					  Jayden: Syntax Terror, Swarf Gander, Der/Dur Fuhrer\n
					  Cayden: Desperato\n
					  Matt: The Donald, True Saviour\n
					  Lloyd: Korea, Cowboy/Cow-boy\n```""",
		'martin': """```
					  Christof Romuald: Died to Syntax Terror's Bear Drones while being pounded on by Police. F in chat please.\n
					  Laramy Fisk: Was murdered by Seraph. After Laramy blammed Syntax Terror on why the van blew up, Seraph didn't take kindly, resulting in Seraph running Laramy over and shotting him after he manged to live.\n
					  Mercer De'am: Died by the hands of Tony when an orbital strike was set upon his location.\n
					  Velvet Thunder: Died to The Donald, bashed by the wall, and then shot in the head.\n
 					  Carth: Nearly died from a bomb in Syntax Terror's place, only to run away in a firetruck, get in an accident and be gunned down crawling out of the window.\n```""",
		'josh': """```
					  Seraph: Seraph thought they were safe, thought Syntax Terror would be happy, were on their way to Byntax Berror, when a secret chip Syntax had implanted alerted a sniper from The business to shot Seraph dead.\n
					  Daiki: Upon being tazzed by Velvet Thunder, and the Valencia gang going to take their shot, Daiki had his car blow everyone up, not just taking his on life but 8 of the Valencia gang.\n
					  Ligma: Ligma came out of hinding and did a hypnotic strip dance for Korea. Korea than proceeded to try and eat Ligma instead of patching Ligma up, resulting in Ligmas death.\n
					  In[Spectre] Gadget: After being sent to prison, Carth bashed Spectre around a lot to blend in with the guards, and when it came to escape, Spectre obtained too many injuries and easily had their skull smashed in by actual gaurds.\n
					  Jerry: Jerry was really a nobody, like an NPC, but aren't we all in a dystopian future ran by mega corps? Jerry managed to show promise as he helped Carth with escape Sandstone, only to be blown up by Syntax Terror, F in chat please.\n
					  Tat: Tat kept popping in and out of his Mothers Heartbeat. It was only a matter of time untill he pulled a Nazi with him, resulting in a bloodbath, an army of more chilidren appearing, and wolves. Wolves proceeded to maul his face off this time, in one final ditch for the safety within Mothers heartbeat.\n
					  Fluffy: Fluffy picked up a nuke in a pokeball after using an online map to navigate the Maze. Later playing hot potato with the nuke, Coqboy blew up, and everyone nearby also blew up.\n```""",
		'joshf': "```H4KKK3R: H4KKK3R was in the car with Seraph, trying to guide Laramy to where Syntax Terror was so we could take our revenge. While Jacked into police cameras, Seraph shot them in the head.\n```",
		'jayden': """```
					  Syntax Terror: Syntax Terror managed to live out his days, always being paranoid and on edge.\n
					  Swarf Gander: Killed himself with flashbangs to try avoid hearing Mercer's music.\n
					  Der Fuhrer: Dur Fuhrer died pretty much the same time as Cowboy did, when Cowbow blew up while holding a nuke Fluffy picked up, in a game of hot potato. Der Fuhrers hands and leg grew back a long time after.\n```""",
		'waleed': """```
					  Noor 'Shareef' Jerkof: Noor's death was on their own account, they ended up shooting themself in the head when they realized they couldn't talk to people and were on their way to jail.\n
					  Martin Monis Jr: MartinJr took the entire team on in bar shoot up, manged to walk out mostly fine then was shot in the head by a sniper.\n
					  Azrael: Azrael was a shit sniper and wouldn't follow the plan, resulting in complications for Laramy and Syntax Terror. Bad mistake Azrael as we framed him resulting in a brutal death.\n```""",	
		'lloyd': """```
		              Korea: Korea lived as a cannibal and died as a cannibal. Especially when True Surveyor shot them in the head when they tried eating Ligma.\n
		              Cow-boy: Cowboy had enough medical supplies and fuel to last a life time, upon playing hot potato with a nuke contained in ball that Fluffy picked up.\n```""",
		'cayden':"```Desperato: Also died to the hands of Tony when an orbital strike was set upon their location.\n```",
		'matt': """```
					  The Donald: Died to the Valencia gang, if only he didn't shoot Velvet Thunder, but that's not how the art of the deal.\n
					  True Saviour: After being lead into Nora's vault and then shot down by their turrets, True Saviour managed to make it back to town before bleading out.\n```""",
		'sprawl1': """```
					  Christof Romuald: Died to Syntax Terror's Bear Drones while being pounded on by Police. F in chat please.\n
					  Noor 'Shareef' Jerkof: Noor's death was on their own account, they ended up shooting themself in the head when they realized they couldn't talk to people and were on their way to jail.\n
					  Martin Monis Jr: MartinJr took the entire team on in bar shoot up, manged to walk out mostly fine then was shot in the head by a sniper.\n
					  Azrael: Azrael was a shit sniper and wouldn't follow the plan, resulting in complications for Laramy and Syntax Terror. Bad mistake Azrael as we framed him resulting in a brutal death.\n
					  H4KKK3R: H4KKK3R was in the car with Seraph, trying to guide Laramy to where Syntax Terror was so we could take our revenge. While Jacked into police cameras, Seraph shot them in the head. \n
					  Laramy Fisk: Was murdered by Seraph. After Laramy blammed Syntax Terror on why the van blew up, Seraph didn't take kindly, resulting in Seraph running Laramy over and shotting him after he manged to live.\n
					  Seraph: Seraph thought they were safe, thought Syntax Terror would be happy, were on their way to Byntax Berror, when a secret chip Syntax had implanted alerted a sniper from The business to shot Seraph dead.\n
					  Syntax Terror: Syntax Terror managed to live out his days, always being paranoid and on edge.\n```""",
		'sprawl2':"""```
					  Swarf Gander: Killed himself with flashbangs to try avoid hearing Mercer's music.\n
					  Mercer De'am: Died by the hands of Tony when an orbital strike was set upon his location.\n 
					  Desperato: Also died to the hands of Tony when an orbital strike was set upon their location.\n
					  Velvet Thunder: Died to The Donald, bashed by the wall, and then shot in the head.\n
					  The Donald: Died to the Valencia gang, if only he didn't shoot Velvet Thunder, but that's not how the art of the deal.\n
					  Daiki: Upon being tazzed by Velvet Thunder, and the Valencia gang going to take their shot, Daiki had his car blow everyone up, not just taking his on life but 8 of the Valencia gang.\n```""",
		'sprawl3': """```
					 In[Spectre] Gadget: After being sent to prison, Carth bashed Spectre around a lot to blend in with the guards, and when it came to escape, Spectre obtained too many injuries and easily had their skull smashed in by actual gaurds.\n
					 Beep. Beep BOOOOOOM! another death caused by Syntax Terror. No one knew who Jerry was, or why they helped Carth with his rescue, despite, not really being anyone, Jerry did pretty well. Good job Jerry. F in chat please.\n
					 After nearly dieing to Syntax Terrors bomb, Carth stole a firetruck, and tried driving to safety online for a tank or something to crash into him, and gun him down as he crawled out the window in a final ditch attempt```""",
		'apoc1':"""```
					  Korea: Korea lived as a cannibal and died as a cannibal. Especially when True Surveyor shot them in the head when they tried eating Ligma.\n
					  Ligma: Ligma came out of hinding and did a hypnotic strip dance for Korea. Korea than proceeded to try and eat Ligma instead of patching Ligma up, resulting in Ligmas death.\n
					  True Saviour: After being lead into Nora's vault and then shot down by their turrets, True Saviour managed to make it back to town before bleading out.\n```""",
		'apoc2':"""```
					  Tat: Tat kept popping in and out of his Mothers Heartbeat. It was only a matter of time untill he pulled a Nazi with him, resulting in a bloodbath, an army of more chilidren appearing, and wolves. Wolves proceeded to maul his face off this time, in one final ditch for the safety within Mothers heartbeat\n
					  Cow-boy: Cowboy had enough medical supplies and fuel to last a life time, upon playing hot potato with a nuke contained in ball that Fluffy picked up.\n
					  Der Fuhrer: Dur Fuhrer died pretty much the same time as Cowboy did, when Cowbow blew up while holding a nuke Fluffy picked up, in a game of hot potato. Der Fuhrers hands and leg grew back a long time after.\n
					  Fluffy: Fluffy picked up a nuke in a pokeball after using an online map to navigate the Maze. Later playing hot potato with the nuke, Coqboy blew up, and everyone nearby also blew up.\n```""",
										
										
	}
	msg = switch.get(ripMsg, switch["list"])
	#print(msg)
	msg = msg.replace("\t", "")
	msg = msg.replace ("					  ", "")
	return msg


def roll(message):
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

	return msg

def remember(message):
	#Generates random number to get remember message from  events that have happened.
	min = 1
	max = 244
	member = random.randint(min,max)
	notRandom = message.split() #puts message into a string array seperated by " "
	
	if len(notRandom)>1: #If more values other than .remember
		number = int(notRandom[1]) #converts stringArray  (['.remember' 'num']) to int 
		if number >=min and number<=max: #Ensures it will exist within the range of .remember
			member = number #sets member to the number. 
#	print ("Remember val = ")
#	print(member)
		

	switch = {
		#Christof focused
		1: "```Remember that time Christof tackled a Robot Synth thing to save Seraph?```",
		2: "```Remember that time Christof said he wasn't going to bring Waleed but did but never used him?```",
		3: "```Remember that time Christof forgot Waleed in a drug den and Waleed got picked up the Police and Medtech?```",
		4: "```when Christof didn't use Waleed to sniff for a bomb then dived in front of Maxine when it exploded?```",
		5: "```Remember that time Christof was doubting that Syntax Terror was a junkie, whilest Syntax Terrror had no pants on in a drug den?```",
		6: "```Remember that time Christof brutally killed a bunch of goons all at once with his barehands```",
		7: "```Ever been to a Vet for serious medical attention? because Christoff has.```",
		8: "```Christof threw H4KKK3R out of the way of a building falling down, fun times for everyone.```",
		9: "```Christof charged into heavily armed police and took a shotgun to the face before finally dying to Syntax Terrors drones. F is chat please...```",
		#Laramy focused
		10: "```That Laramy stabbed Noor with with some drugs and Noor then ran out infront of a truck. Good times. ```",
		11: "```That time Laramy didn't show up cause he was super high at home. Hope that mission went well.```",
		12: "```Keep the drugs away from Laramy cause he's been known to take some Meatloaf followed by other drugs and go on a killing spree both friend and foe```",
		13: "```That time Laramy had Meatloaf and  rocket launcher thing and proceeded to shot the building to get the mission done!```",
		#Seraph focused
		14: "```That time Seraph parkoured up a convayor belt, jumped into the air and dabbed their way onto the next floor up!```",
		15: "```How long did Seraph drag Christoff's body around when he died?```",
		16: "```*Looks in window* shots a goon in the face, gets a van. Good job Seraph.```",
		17: "``` Seraph somehow snuck a grendade into a pot plant while being watched by gaurds and managed to get Noor to take the full on it.```",
		18: "```Remember when Seraph tried killing Tony and had their arm broken and sent to jail?```",
		19: "```Who's got a cyber arm thanks to the Thing? Thats right Seraph does.```",
		#Syntax Terror focused.
		21: "```I used my  bear drones (thats right more than one) to win the slaughterfest, -syntax terror```",
		22: "```With enough cred Syntax terror managed to buy Seraph. Good job Syntax Terror!```",
		23: "```Getting bear drones to blow up police to help us escapse, no problem for Syntax Terror```",
		#HKKK3R focused
		24: "```H4KKK3R can hack a aircon, and make the room a little cold. Nice hacking right there!```",
		25: "```H4KKK3R just jackin into the Matrix while standing in a bar, it happens more than you think. ```",
		26: "```When H4KKK3R tried fleeing the scene only to be shot and lose some memory```",
		27: "```That time H4KKK3R took some braind damage from failing to get past some black ice```",
		#Noor focused.
		28: "```Whats for lunch?```",
		29: "```That time Noor said they were responsible for putting a grenade in the pot plant only to then shoot themself. F in chat if you really want to but probs dont bother...```",
		30: "```Noors good at talking and seducing people. Just kidding probably being thrown out by gaurds or getting attacked or something instead.```",
		31: "```That time Noor was useful by having a gun out that Laramy stole and shot gaurds with.```",
		32: "```Remember when Noor got shot because Laramy tried to steal Seraphs gun?```",
		#Other random stuff from Sprawl Campaign 1.
		33: "```When we all tried to kill Martin JR and that manged to tank and seriously harm the entire group.```",
		34: "```Martin JR gets injured at a bar from a gun fight, walks out of said bar into a sniper bullet, some how still managing to live and get taken to a hospital, only to then die. F in chat if you think Martin JR deserves it.```",
		35: "```Who hides in a dumpster and 'provides'sniper cover? Azrael (to the tune of Spongebob)```",
		36: "```When Azrael doesn't snipe people so Syntax gives their position away with a smoke grenade```",
		37: "```Syntax Terror pinned some stuff on Azrael causing Azrael to get killed, please don't F in chat.```",
		38: "```That time the MC sounds like a robot just after introducing the Thing.```",
		39: "```MC makes somekind of robot noise... MC clock advances.```",
		40: "```Who's getting more drunk and making the outcomes worse and worse? Thats right the MC```",
		41: "```*Bans Waleed from the chat*```",
		42: "```H4KKK3R crashed his moterbike looking like an idiot when trying to buy his shiper rifle so Seraph held everyone at gun point and demanded H4KKK3R modified it so they could also use it.```",
		43: "```I'm the best hacker. -Syntax Terror```",
		44: "```When Laramy punched H4KKK3R out(on purpose) and immidiatly patched H4KKK3R up afterwards.```",
		45: "```Syntax Terror actually walked Waleed, and used his senses (Slightly) WOW!```",
		46: "```Remember that time Syntax Terror betrayed us all by rigging his Drone to remember? Because I fucking remember that.```",
		47: "```Remember when Laramy accused Syntax Terror of why the van had blown up resulting in Seraph trying to also kill Laramy and H4KKK3R```",
		48: "```Remember when all H4KKK3R wanted was a sniper rifle but the team nearly stole or killed him over it?```",
		49: "```Remember when Laramy tried throwing a grenade at Seraph after Seraph tried running him over, only to have the grenade explode on Laramy from a shit through?```",
		50: "```Remember when Seraph outright shot H4KKK3R in the head  while sneaking past police? F in chat please.```",
		51: "```That time Syntax Terrors drone blew the van up and Laramy applied first aid to himself, Seraph and H4KKK3R while being questioned by police```",
		52: "```When Laramy nearly blew himself trying to throw a grenade at Seraph and Seraph than shot what was left of Laramy dead. F in chat please.```",
		53: "```When Laramy postioned garden Gnomes in a triangle or something to make a call```",
		54: "```When Laramy was trying to get more armor or heavy ammo from Ken Tenma but butchered it by saying something stupid about marmalade?```",
		55: "```When we got into an argument about how far and fast Syntax Terror could run?```",
		56: "```*More robot noises*```",
		57: "```When Seraph used their plan B to escape by stealing a bikers bike and was gonna ride away to safety until a certain call with Syntax Terror occured.```",
		58: "```When Seraph told Syntax Terror that Laramy and H4KKK3R were dead and then Syntax Terror triggered a tracking becon resuling in Seraph being snipped dead. F in chat please or Seraph will add you to a hitlist.```",
		59: "```When Seraph was dying and their last words to Syntax Terror were 'Im pregnant with H4KKK3R'```",
		60: "```They say Syntax Terror managed to escape the buisness after he betrayed everyone. People he failed (occasionly finished) missions with, the infiltrator be paid lots of Cred for, and even one of his own drones. They also say Syntax Terror spent the rest of his days being more and more paranoid, keeping an eye behind him.  ```",
		#Start of Sprawl campaign 2. 
		61: "```That time Daiki did some sick driving```",
		62: "```Can they see my car? Good I aim my missiles at them - Daiki```",
		63: "```That time Daiki and Swarf put Numberphille on suicide watch```",
		64: "```When Swarf paid Numberphille to take him off suicide watch.```",
		65: "```That time Mercer played the Obo and made some cred in the process```",
		66: "```*Plays the slide whistle*```",
		67: "```I'm going to start shitting on his lawn -Daiki```",
		68: "```So Daiki smellls like shit -MC ```",
		69: "```That time Mercer tried having a vision thing without actually taking the time to talk to someone remotely well.```",
		70: "```What if I drive really fast? -Daiki```",
		71: "```All those times Swarf threw a flash grenade and blinded everyone.```",
		72: "```That time Daiki got into a chase to try to impress Elina ```",
		73: "```Swarf flashbanged himself to death to avoid hearing Mercers music. F in chat please.```",
		#Just after Swarf Gander left and The Donlad joined in. 
		74: "```That time Daiki became a stalker```",
		75: "```MC: You're a rapist. Daiki: NOOO!```",
		76: "```That time Daiki stalked numberphille so he could get a chicks number```",
		77: "```That time Mercer played the Keytar resulting in even more attention ebing drawn on the team```",
		78: "```That time Merver was distracted while walking to gang members resulting in a shoot out and no talking as planned.```",
		79: "```That time everyone had to wait, because Mercer only meets TikTakToe on a Wednesday.```",
		80: "```That time Mercer helped Daiki somehow, by Daiki having 'Don't sue me' playing in the background.```",
		81: "```When Daiki didn't have the right permit for a car with bullet holes and shot up passengers inside it, resulting in police being shot and a high speed chase.```",
		82: "```When Daiki's missile hit The Trump.```",
		83: "```When Mercer actually stopped and got out of a truck when asked by Skorpio-tensi despite knowing it was stolen.```",
		84: "``` When Mercer manged to pretend to faint when Skorpio-tensi were trying to arrest him.```",
		85: "```That time Mercer played Goofy Goober Rock on his Keytar and kept two gaurds frozen with pure awe. ```",
		86: "``` That time The Donald dropped the wall. ```",
		87: "```Remember when The Donald slammed the wall into a Skorpio-tensi gaurd against a truck, so hard it went through the truck and resulted in Mercer pretty much being dead.```",
		88: "```That time Mercer didn't die cause The Donald dropped him off at a hosptial and didn't just kick him out of a truck onto the street.```",
		89: "```Tgat tune Mercer jumped back into the truck and kept failing to start it resulting in lots of bullets being shot at him.```",
		90: "```That time Daiki remote controlled their car to lead the police off the trail a little bit```",
		91: "```That time Daiki shot missiles at a drone. Oh how the turntables.```",
		92: "```That time Mercer actually pulled over with a stolen truck to Skorpio-tensi who knew it was stolen, then pretended to faint, stabbing one of the skorpio-tensi gaurds in the throat with his retractable knife blades, busting his Keytar out and played Goofy Goober Rock freezing the gaurds in awe.```",
		93: "```Remember when Mercers voice kept changing?```",
		94: "```That time the team kept doing the same thing untill something happened```",
		95: "```Remember how Mercer walked into a bar and advanced the legwork clock before even having a mission. Good times.```",
		96: "```Mercer walks into a bar thursting his arms around, Daiki akwardly follows by doing the virgin walk. The Donald then shows up late, doing the chad stride over to the meeting.```",
		97: "```That time Desperato, Daiki, and The Donald, did some surveillance in Mercer's helicopter, but didn't even take off from the ground or go anywhere. No wonder they didn't see anything.```",
		98: "```That time Mercer and Desperato got a little drunk, and then into a bar fight because people didn't like how Mercer played the triangle.```",
		99: "```That time Desperato got punched, threw their drink at the attack, dabbed, and managed to leave without a problem.```",
		100: "```That time Mercer punched Desperato in his now empty eye socket, knocking him over.```",
		101: "```That time Daiki, and Mercer hid in plain sight, while obviously with The Donald, tricking the Valencia gang, and more importantly Mendel that Daiki had been delt with and we stole his van as proof. Then convincing Mendel to look in the hood resulting in Mendel being gunned to death by the van. ```",
		102: "```That time Daiki got Mendel to look into his van, under the hood, with hidden automated guns that outright killed Mendel alerting the Valencia gang to come investigate, which Daiki than got his van to shot everyone with an auto canon. Daiki than drove out of the building, giving the finger to the Valencia gang,  getting away, while impressing them so much with his brutal attack so much they lowered their hatred for us a tad.  ```",
		103: "```That time Mercer and Desperato stayed back after Daiki and The Donald, drove away as a decoy, so Mercer and Desperato could maintain cover. Mercer and Desperato than ignored beeping resulting in Valencia, Mercer and Desperato to be blown up from an orbital strike.```",
		104: "```Tony = A bad fucking time. ```",
		105: "```That time Martin got salty at the MC becuase Mercer got blasted by an orbital strike, if only Martin had remembered what Tony was capable of in the first campaign, and how Tony played a role in how Christoff died.```",
		106: "```Fuck Tony, except that time he let Laramy use prototype rocket launcher```",
		#Just after Martin got really salty at the MC for blowing him up with an orbital strike. Introducing Velvet thunder breifly.
		107: "```That time The Donald ate a taco from the latino(Desperato) and everything was fine.```",
		108: "```That time Daiki tried getting Velvet thunder to go deaf?```",
		109: "```Remember when Daiki was driving a destroyed car like in simpsons hit and run```",
		110: "```Remember that time Velvet Thunder tazzed Daiki, and the Donald then smashed Velvet with his wall.```",
		111: "```That time Velvet Thunder used his synth ears to listen to stuff```",
		112: "```That time Daiki wanted a fist bump from Velvet Thunder```",
		113: "```When Velvet Thunder broke his phone so The Donald no longer had his number```",
		114: "```Remember that time the Valencia gang said dont move and the Donald shot Velvet thunder resulting in the Valencia gang killing The Donald. Daiki then blew up everyone else, themself included.```",
		#Trying Apoc world for the first time, what a mess and a lot of pvp.
		115: "```That time Daiki started driving his car remotely freaking Velvet Thunder out```",
		116: "```That time Korea slashed at the bicep of the first npc they saw.```",
		117: "```That time Ligma hypnotized an intruding criminal and got them to slit their own throat.```",
		118: "```That time True Saviour just sat around town selling things.```",
		119: "```That time Korea was chained in an arena and lashed out and caused lots of canibals to run rampert in the town *blood is in the air*```",
		120: "```That time the MC(Martin) vagually descriped something causing confusion for all.```",
		121: "```That time Ligma tried to hypnotize Number 8 and faied.```",
		122: "```That time Ligma tried again to hypnotize Number 8 into giving his guitar resulting in Ligma cutting himself on razor sharp strings.```",
		123: "```That time Korea tried patching up a 3 arm(was 4 armed) mutant, but instead cut his head of and drank the mutants blood, cause the mutant wouldn't take their help.```",
		124: "```that time Ligma threw a bottle of water at Korea, but Korea didn't catch it due to vomiting acid.```",
		125: "```That time Korea drank toxic blood and started radiating heat.```",
		126: "```that time Ligma jsut accepted that Korea was a complete whackjob.```",
		127: "```That time Ligma cut their hand on razor sharp guitar strings and Korea lept at them in an attempt 'fix them up' but Ligma jumped out the way in fear.```",
		128: "```That time the MC vagually described a well and changed measurment and distance often.```",
		129: "```That time True Surveyor climbed a ladder and instantly began opening fire on the first person they saw.```",
		130: "```That time Ligma emerged from hiding and started slowly stripping off```",
		131: "```That time Korea was hypnotised by Ligma's dancing ```",
		132: "```That time Ligma hypnotised Korea into dealing with the random Columbian, and Korea patched them up.```",
		133: "```Remember when Ligma tried to get Korea to patch them up, but Korea lost control and started trying to eat them. Ligma was stabbed to death with a cannibal on them. F in chat please.```",
		134: "```That time True Surveyor took control of the situation by beaking the Columbian mans hand with a solid kick, and catching his gun, arming himself wit ha shotgun and small revolver. He killed Korea with thses for being a cannibal. F is chat if you miss cannibals.```",
		#Ligma and Korea are gone, say hello to Q and Nora.
		135: "```That time Nora tried to get an extra water from True Saviour. Fun times. ```",
		136: "```Remember when Q jumped back and forth a mind warping reality, causing them to have a seizure```",
		137: "```What does the mask say?```",
		138: "```That time Nora readied turrets to try and get more water from True Saviour```",
		139: "```That time True Saviour was brutally beaten by Q as Q decided to side with Nora```",
		140: "```That time True Saviour was mowed down with fire from Nora's turrets. MC probably should have let someone die.```",
		141: "```That time Q saw this glowing magical fox dissapear under some rubble or man hole and jumped down it. Somebody nearly died from the fall alone that day```",
		142: "```That time when all hell broke lose in the Nora's vault.```",
		143: "```That time you tried to use a move to get a better understanding or gain knowledge on something, and the MC provided something very vauge, and probably made your understanding worse```",
		144: "```That time Q and Nora got sidetracked looking around the Metro tunnels  because Q was convinced that there was a glowing fox```",
		145: "```That time Q saw some glowing bushes, shrubberies, and other stuff (I forget what exactly). Q started squatting behind one, and Nora just saw Q squatting.```",
		146: "```That time Q found a group of old people and tried to scare them into talking about the fox```",
		147: "```Remember when Q jumped on a made up glowing fox, and it formed a Torus (a doughnut) around them and then exploded as Q hit them with an axe```",
		148: "```That time Q got a fox skull from an immaginary fox. Good job Q.```",
		149: "```That time Q ran into a wall. Good times. ```",
		150: "``` That time Nora actually talked to people and defuse the situation instead of probably just killing them. Good job Nora```",
		151: "```That time Nora made a bridge while Q kind of tripped out looking at a made up bridge.```",
		152: "```That time Q saw through the eyes of a fox and found lizard people.```",
		153: "```That time Q and Nora reported back to Number 8, and got them excited for Lizard people ```",
		154: "```That time Nora shot Q and the bullets just rolled off as if nothing happened. Q is a literal tank now.```",
		155: "```That time Nora told 'The funny man' the orange you glad I didn't say banana joke.```",
		156: "```That time Q told 'The funny man' a knock knock joke, and 'The funny man' responded with the KGB knock knock joke.```",
		157: "```That time Q killed Beets. F in chat please.```",
		158: "```That time Q spoke to H. HR.```",
		159: "```That time Nora ate a bean from an unmarked can, and the MC gave them -1 to all stats for a second.```",
		160: "```That time Q found a bell.```",
		161: "```That time Nora got trapped by one of Beets beartraps.```",
		162: "```That time Q tried saving Beets, and ended up with Nora's fun through their arm```",
		163: "```OFFICE THEME PLAYS AND DEAFENS LLOYD```",
		164: "```that time Nora stoped 'the funny man' from jumping.```",
		165: "```That time Q fell into a wall and was at the bottom of a void.```",
		166: "```That time Nora touched a wall and decicded it was safe to avoid the illusion wall. Good job.```",
		167: "```That Nora used Number 8 as bait, and ambused some of lizard people.```",
		168: "```That time Q ran along the wall and jumped up to the roof and sliced a bunch of lizard people mid air.```",
		169: "```That time Nora lead an army to take over the town.```",
		170: "```That time Q embedded their axe into Number 7.```",
		171: "```That time Q cut number 7's head off and their body fell on Nora, crusing them a little.```",
		172: "```*Plays the triangle* No that wasn't Mercer, it was Q.```",
		173: "```That time Number 8 got thrown to the ground and screamed launching them into the air and slowly fell down? What was the MC on..```",
		174: "```That time the MC made lots of things random illusions in peoples head..```",
		175: "```That time Nora and Q took over the town```",
		176: "```When Q and Nora found Number 6, and were suprised they weren't hostile, despite trying to take over the town.```",
		177: "```That time Nora commanded their army to strategically fire upon Varmos.```",
		178: "```When Q cut off Varmos's arm then proceed to split the other in half instead of dodgeing. Took the acid blood that fell on them like a champ.```",
		#Back to the Sprawl, oh how we missed how well the Sprawl was written compared to Apoc. A short oneshot over a few sessions.
		179: "```That time Carth threw some random trashcan to test if drones were gonan auto fire on location.```",
		180: "```That time In[Spectre] Gadget met Syntax Terrror and almost died.```",
		181: "```That time In[Spectre] Gadget met Syntax Terror again, and also almost died.```",
		182: "```That time Carth saved In[Spectre] Gadget from being killed by Syntax Terror's drone.```",
		183: "```That time In[Spectre] Gadget lost two fingers, their pants, and was also shot in the leg by Syntax Terror```",
		184:"```I'm Inspectre gadget. who? ```",
		185:"```When the MC (Lloyd) does the nerd voice```",
		186:"```Goes into a magnetic room with infinite knives. As if that wasn't going to be a problem```",
		187:"```That time Carth had to wear a giant Hazard label on them due to the giant sword.```",
		188:"```That time Spectre went to jail , and then arrested a nerd in the same cell, causing the nerd to cry, alerting the guards.```",
		189:"```That time Carth responded as a guard, and smashed Spectres head into the wall, very very forcefully with their cyberarm.```",
		190:"```That time Carth tried using a dead guard as a puppet to ensure everything was fine. Didn't work but the nail grenade did!```",
		191: "```That time Spectre was tied up in a mental harness, and then used infinite knives, cutting themself to escape, instead of asking the other nerds to help..```",
		192: "```Spectre's skull got smashed in. f in chat please. ```",
		193: "```That time Carth used a giant sword to try place baseball with charging synth attack dogs.```",
		194: "```That time Spectre got a nerd army, only for them to shit themselves and die pretty quickly.```",
		195: "```That time Spectre nearly made a vector field using infinite knives.```",
		196: """**```css
[FAILS SYNTAX TERROR]```**\n```Syntax Terror clock increased to 1500``` ```Syntax Terror clock increased to 1800``` ```Syntax Terror clock increased to 2100``` ```Syntax Terror clock increased to 2200``` ```Syntax Terror clock increased to 2300``` ```Syntax Terror clock increased to 0000```""",
		197: "```That time  Carth just happened to find a nobody named Jerry to escape Sandstone, good driving Jerry!```",
		198: "```What do we do Jerry? Keep on livin' and save lives```",
		199: "```TIPS THE FIRETRUCK FROM BEING RAMMED climb out hte window and gets shot to death. Thats right Carth did```",
		200: "```That time Carth stole a firetruck after nearly being blown up at Syntax Terror's place```",
		202: "```That time Carth made Jerry eat a battery to pretend it was a tracking chip```",
		203: "```That time when everyone was blown up by Syntax Terror, no the other time with Carth and Jerry.```",
		204: "```That time Carth threw his bag of useless junk at a drone, to try and lose it```",
		205: "```That time Jerry managed to keep on livin' till they died.```",
		206: "```we keep on livin Jerry```",
		#Welcome back to Apoc Campaign 2.
		207: "```That time Tat screamed static to lure a giant worm over```",
		208: "```That time Cowboy kicked Tat and Tat just vanished.```",
		209: "```That time Tat managed to speak and understand static```",
		210: "```That time a giant worm thing came out of nowhere.```",
		211: "```That time Tat ate sunglasses. Cowboys Sunglasses.```",
		212: "```'You will need to find some food for us'\n'How about those lightbulbs mister.'```",
		213: "```That time Cowboy stole everything from a mutant doctor while Tat just screemed static and nearly died...```",
		214: "```That time Tat went through a mail slot and pretended to be dead to ambush a mutant doctor. ```",
		215: "```That time Tat and a Super mutant doctor appeared infront of Cowboy as they drove```",
		216: "```That time Cowboy put a leash on Tat and then put him on the handle bars of a rusted bike```",
		216: "```Things going down? Better hide with my mothers heartbeat```",
		217: "```That time Cowboy kept trying to fix things and bring peice, but Tat had other ideas.```",
		218:"```That time Tat cannibalised a doctor, nearly killed a sherif, and then proceeded to try killing another doctor right after..```",
		219: "```Who needs a doctor? Hopefully not you after Tat killed or attacked the doctors nearby.```",
		#Welcome back Jayden and hello Fluffy.
		220: "```That time Tat was mauled  to death by the wolves in the malestorm.```",
		221: "```That time Der showed up and tried to kidnap Cowboy cause he thought he was a doctor.```",
		222: "```That time Tat followed someone other than Cowboy. Then died.```",
		223: "```That time when Fluffy and Cowboy had drinks together.```",
		224: "```That time someone got into trouble, when the MC asked how far Fluffy and Cowboy planned on going...```",
		225: "```That time Der Fuhrer took random chilidren to start inducting them into his gang. ```",
		226: "```Remember that time Lloyd Identified the map before we even started, Free exp that time.```",
		227: "```Remember when Der Fuhrer just chucked down a bunch of explosive collars blowing up the professors rooms.```",
		228: "```That time Cowboy gave Fluffy oxygen while swimming underwater```",
		229: "```That Der Fuhrer passed out while picking up the soap.```",
		230: "```That time Der Fuhrer recruited blue Zoidberg to be his doctor.```",
		231:  "``` That time Cowboy and Der Fuhrer saw avoid while Fluffy saw the room properly.```",
		232: "```Let me roll to see how well I keep my cool while talking to...```",
		233: "```Why are you gree? Gets kicked out the the town..```",
		234: "```That time Dur Fuhrer made freinds with a cactus with sombrero ```",
		235: "```Is this from pokemon```",
		236: "```That time Der Fuhrer had their name changed to Dur Fuhrer.```",
		237: "```That time Cowboys name changed to Cow-boy```",
		238: "```That time Der Fuhrer lost their leg to a random explosion.```",
		239: "```That time Der Fuhrer got given a ghoul leg that was smaller than his other leg.```",
		240: "```That time Cowboy leveled up 4 levels just from spinning. Spinnings a cool trick```",
		241:"```That time Der Fuhrer played hot potatoe with ghould and lost his arms.```",
		242: "```That time Fluffy  looked up a map the MC used, and got a free item out of it.```",
		243:"```That time everyone just played Hot potato with ghouls.```",
		244: "```That time we decided to have enough of Apoc World, and instead of ending with retiring characters, the MC blew everyone up with a nuke Fluffy picked up in a final game of Hot Potato.```",
		#AYYY SPRAWL TIME!

	}

	return switch[member]
def rememberlist(message):
	msg = """```
	1-9: Christoff focused
	10-13: Laramy focused
	14-19: Seraph focused
	20: I missed a number..
	21-23:  Syntax Terror focused
	24-27: H4KKK3R focused
	28-32: Noor focused
	33-60: Reat of Sprawl campaign 1 (in order things happened after I stopped grouping by character.)
	61-73: Sprawl campaign 2, while Jayden(swarf) was still playing
	74-106: Sprawl 2 while Mercer was still alive.
	107-114: The last of Sprawl 2.
	115-134: First time playing Apoc world, what a mess that was, also lots of pvp.
	135-178: The last of Apoc world campaign 1, lots of weird stuff and overtrowing.
	179-206: Back to the Sprawl, oh how we missed the Sprawls writing. A one shot spanned over a couple of sessions.
	207-219: Apoc world, Tat and Cowboy.
	220-244 Jayden comes back and Tat dies.
	```"""
	msg = msg.replace("\t","")
	return msg

def links(message):
	msg = """
	**Apocalpyse World:** https://www.dropbox.com/sh/fmsh9kyaiplqhom/AACw1iLMQ7f53Q40FUnMjlz4a?dl=0
	**The Sprawl:** https://www.dropbox.com/sh/9fr35ivzbvfh06p/AACarsYBpNXxBpEUk_-fz_PXa?dl=0
	**Tremulas:** https://www.dropbox.com/sh/tbhk0w0zgihrf2h/AACtvyv9l5ruLBE6UG3XeGfba?dl=0
	**Dungeon World:** https://www.dropbox.com/sh/p61lutt9m6dfpa3/AACTvHhbJa7K1RIHFYVvJqIza?dl=0
	"""
	msg = msg.replace("\t","")
	return msg




def addclock(message):
	# Get the clock name and assign it default value of 1200
	tokens = message.split(".addclock ")
	print(tokens)
	clock = (tokens[1], "1200")

	# Checks if clock has already been added
	for c in clocks:
		# Case insensitive
		name = c[0].lower()
		inName = tokens[1].lower()

		if name == inName:
			return "```Clock already exists.```"


	# Append to clocks list
	clocks.append(clock)

	# Update and refresh file
	updateAndRefreshData("clocks", clocks)
	print("Clock added to file: {" + tokens[1] + ", 1200}")

	# Form message and send
	return "```Clock added: " + tokens[1] + " at 1200.```"

def deleteclock(message):
	# Get the clock name
	tokens = message.split(".deleteclock ")
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
	return "```Deleted clock " + name + ".```"

def increaseclock(message):
	# Get the clock name
	tokens = message.split(".increaseclock ")
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
				return "```Clock is already at midnight.```"

			# Create new tuple and replace previous one
			updatedClock = (clock[0], value)
			index = clocks.index(clock)
			clocks[index] = updatedClock

	# Check if the clock was found
	if not found:
		return "```Clock \"" + name + "\" not found.```"

	# Update and refresh file
	updateAndRefreshData("clocks", clocks)
	print("Clock update reflected in file (INCREASE): (" + updatedClock[0] + ", " + updatedClock[1] + ")")

	# Form message and send
	return "```" + updatedClock[0] + " clock increased to " + updatedClock[1] + ".```"

def decreaseclock(message):
	# Get the clock name
	tokens = message.split(".decreaseclock ")
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
				return "```Clock is already at 1200.```"

			# Create new tuple and replace previous one
			updatedClock = (clock[0], value)
			print(updatedClock)
			index = clocks.index(clock)
			clocks[index] = updatedClock

	# Check if the clock was found
	if not found:
		return "```Clock \"" + name + "\" not found.```"

	# Update and refresh file
	updateAndRefreshData("clocks", clocks)
	print("Clock update reflected in file (DECREASE): (" + updatedClock[0] + ", " + updatedClock[1] + ")")

	# Form message and send
	return "```" + updatedClock[0] + " clock decreased to " + updatedClock[1] + ".```"

def addcontact(message):
	# Get the contact name and description
	tokens = message.split()
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
			return "```Contact already exists.```"

	# Append to contacts list
	contacts.append(contact)

	# Update and refresh file
	updateAndRefreshData("contacts", contacts)
	print("Contact added to file: {" + tokens[1] + ", " + description + "}")

	# Form message and send
	return "```Contact added: " + tokens[1] + ".```"

def deletecontact(message):
	# Get the clock name
	tokens = message.split()
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
	return "```Deleted contact " + name + ".```"

def refresh(message):
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

	return msg

def log(message):
	# Get log message from message
	tokens = message.split(".log ")
	log = tokens[1]

	# Write to the file
	file = open("log.txt", "a")
	file.write(log + "\n")
	file.close()
	print("Log saved: \"" + log + "\"")

	# Form and send message
	return "```Log saved.```"

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--game', type=str, required=True, choices=['sprawl', 'apoc'])
args = parser.parse_args()
game = vars(args)['game']

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

# Discord client functions
@client.event
async def on_message(message):
	msg = ""

	# Prevents bot replying to itself
	if message.author == client.user:
		return

	# Prevents bot responding to regular messages
	if not message.content.startswith("."):
		return

	# determine which game is being played
	if game == 'sprawl':
		msg = sprawl.handle(message)
	elif game == 'apoc':
		msg = apoc.handle(message)
		
	messageString = message.content
	messageString = messageString.lower()
	

	switch = {
		# Listing commands
		'.help': help,
		'.links': links,
		'.clocks': showclocks,
		'.contacts': showcontacts,
		'.rememberlist':rememberlist,
		# Functional commands
		'.roll': roll,
		'.dice': roll,
		'.addclock': addclock,
		'.deleteclock': deleteclock,
		'.increaseclock': increaseclock,
		'.decreaseclock': decreaseclock,
		'.addcontact': addcontact,
		'.deletecontact': deletecontact,
		# Miscellaneous commands
		'.rip': f,
		'.f': f,
		'.remember': remember,
		# Dev commands
		'.refresh': refresh,
		'.log': log,
	}
	check = False
	if msg !="":
		check = True
	#print (msg)
	if messageString in switch:
		msg = switch[messageString](messageString)
		check = True
	elif check == False:
		for case in switch:
			if case in messageString:
				msg = switch[case](messageString)

	if not msg: msg = invalid(messageString)

	# Sends the map
	if messageString==".map":
		await client.send_file(message.channel, "map.jpg")
	
	elif messageString ==".fuckmendle":
		await client.send_file(message.channel, "mendle.png")
	elif messageString ==".fridge":
		await client.send_file(message.channel, "FRIDGE.jpg")

	elif  messageString != ".map" and messageString != ".fuckmendle" and messageString != ".factorymap":
		await client.send_message(message.channel, msg.format(message))
	else:
		pass

# CONSOLE LOGGING
@client.event
async def on_ready():
	print("Logged in as")
	print (client.user.name)
	print(client.user.id)
	print("------")

client.run(TOKEN)