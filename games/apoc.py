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