    ###############################################################################################################################################
	###############################################################################################################################################
	############################################################ Apocalpyse world #################################################################
	###############################################################################################################################################
	###############################################################################################################################################
	
def handle(message):
	msg = ''

	###############
	##Angel Moves##
	###############
	#Sixth Sense
	if message.content.startswith(".sixthsense"):
		msg = """``` Sixth sense:\n When you open your brain to the world’s psychic maelstrom, roll+sharp instead of roll+weird.```"""		
	#infirmary	
	elif message.content.startswith(".infirmary"):
		msg = """```Infirmary:\n you get an infirmary, a workspace with life support, a drug lab and a crew of 2 (Shigusa & Mox, maybe). Get patients into it and you can work on them like a savvyhead on tech (cf ). ```"""	
	#Professional compassion
	elif message.content.startswith(".professionalcompassion"):
		msg = """```Professonal compassion:\n 
		you can choose to roll+sharp instead of roll+Hx when you help someone who’s rolling.```"""
	#Battlefield grace
	elif message.content.startswith(".battlefieldgrace"):
		msg = """``` Battlefield grace\n while you are caring for people, not fighting, you get +1 armor.```"""
	#Healing touch	
	elif message.content.startswith(".healingtouch"):
		msg = """```Healing touch:\n when you put your hands skin-to-skin on a wounded person and open your brain to them, roll+weird.\n On a 10+, heal 1 segment \n
					On a 7–9, heal 1 segment, but you’re acting under fire from your patient’s brain.\n
					On a miss: first,\n
					you don’t heal them. Second, you’ve opened both your brain and theirs to the world’s psychic maelstrom, without protection or preparation. 
					For you, and for your patient if your patient’sa fellow player’s character, treat it as though you’ve made that move and missed the roll. For patients belonging to the MC, their experience and fate are up to the MC.```"""	
	#Touched by death
	elif message.content.startswith(".touchedbydeath"):
		msg = """```Touched by death:\n whenever someone in your care dies, you get +1weird (max +3). ```"""
 	
	#Àngel Move Lists
	elif message.content.startswith(".angel"):
		msg = """```.sixthsense\n.infirmary\n.professionalcompassion\n.battlefieldgrace\n.healingtouch\n.touchedbydeath```"""
		 
		
	####################
	##Battlebabe Moves##
	####################
	#Dangerous and Sexy
	elif message.content.startswith(".dangerousandsexy"):
		msg = """```Dangerous & sexy:\n
		when you enter into a charged situation, roll+hot.\n
		On a 10+, hold 2.\n
		On a 7–9, hold 1.\n 
		Spend your hold 1 for 1 to make eye contact with an NPC present, who freezes or flinches and can’t take action until you break it off.  On a miss, your enemies identify you immediately as their foremost threat. ```"""
	#Ice Cold
	elif message.content.startswith(".icecold"):
		msg = """```Ice cold:\n when you go aggro on an NPC, roll+cool instead of roll+hard.\n When you go aggro on another player’s character, roll+Hx instead of roll+hard.```"""
	#Merciless
	elif message.content.startswith(".merciless"):
		msg = """```Merciless:\n when you inflict harm, inflict +1harm.```"""
	#Viions of death.
	elif message.content.startswith(".visionsofdeath"):
		msg = """```Visions of death:\n when you go into battle, roll+weird.\n
		On a 10+, name one person who’ll die and one who’ll live.\n 
		On a 7–9, name one person who’ll die OR one person who’ll live.\n
		Don’t name a player’s character; name NPCs only. The MC will make your vision come true, if it’s even remotely possible.\n
		On a miss, you foresee your own death, and accordingly take -1 throughout the battle.```"""	
	#Perfect Insticts
	elif message.content.startswith(".perfectinstincts"):
		msg = """```Perfect instincts:\nwhen you’ve read a charged situation and you’re acting on the MC’s answers, take +2 instead of +1.```"""		
	#Impossible Reflexes.
	elif message.content.startswith(".impossiblereflexes"):
		msg = """```Impossible reflexes:\n the way you move unencumbered counts as armor.\n If you’re naked or nearly naked, 2-armor; if you’re wearing non-armor fashion, 1-armor. If you’re wearing armor, use it instead.```"""
	
	#################
	##Brainer Moves##
	#################
	#Unnatural lust transfixion
	elif message.content.startswith(".unnaturallusttransfixion"):
		msg = """```Unnatural lust transiixion:\n when you try to seduce someone, roll+weird instead of roll+hot.```"""
	#Casual brain receptivity
	elif message.content.startswith(".casualbrainreceptivity"):
		msg = """```Casual brain receptivity:\nwhen you read someone, roll+weird instead of roll+sharp.\nYour victim has to be able to see you, but you don’t have to interact. 		```"""	
	#preternatural at will brain atturnment
	elif message.content.startswith(".pretnernatual"):
		msg = """```Preternatural at-will brain attunement:\nyou get +1weird (weird+3).```"""
	#Deep brain scan
	elif message.content.startswith(".deepbrainscan"):
		msg = """```Deep brain scan:\n when you have time and physical intimacy with someone — mutual intimacy like holding them in your arms, or 1-sided intimacy like they’re restrained to a table — you can read them more deeply than normal. Roll+weird.\n
		On a 10+,hold 3.\n
		On a 7–9, hold 1.\n
		While you’re reading them, spend your hold to ask their player questions, 1 for 1:\n
		• what was your character’s lowest moment?\n
		• for what does your character crave forgiveness, and of whom?\n
		• what are your character’s secret pains?\n
		• in what ways are your character’s mind and soul vulnerable?\n
		On a miss, you inflict 1-harm (ap) upon your subject, to no benefit.```"""	
	#Direct brain whisper projection
	elif message.content.startswith(".directbrainwhisperprojection"):
		msg = """```Direct-brain whisper projection:\nyou can roll+weird to get the effects of going aggro, without going aggro.\n
		Your victim has to be able to see you, but you don’t have to interact.\n
		If your victim forces your hand, your mind counts as a weapon (1-harm apclose loud-optional).```"""	
	#in brain puppet string
	elif message.content.startswith(".inbrainpupperstrings"):
		msg = """```In-brain puppet strings:\nwhen you have time and physical intimacy with someone — again, mutual or 1-sided — you can plant a command inside their mind. Roll+weird.\n
		On a 10+, hold 3.\n 
		On a 7–9, hold 1.\n 
		At your will, no matter the circumstances, you can spend your hold 1 for 1:\n
		• inflict 1-harm (ap)\n
		• they take -1 right now\n
		If they fulfill your command, that counts for all your remaining
		hold.\n 
		On a miss, you inflict 1-harm (ap) upon your subject, to no benefit.```"""
	#Brainer Move list
	elif message.content.startswith(".brainer"):
		msg = """```..unnaturallusttransfixion\n.casualbrainreceptivity\n.pretnernatual\n.deepbrainscan\n.directbrainwhisperprojection\n.inbrainpupperstrings```"""
		
	#################
	##Chopper moves##
	#################
	#pack alpha
	elif message.content.startswith(".packalpha"):
		msg = """```Pack alpha:\nWhen you try to impose your will on your gang, roll+hard.\n
		On a 10+, all 3.\n 
		On a 7–9, choose 1:\n
		• they do what you want\n
		• they don’t fight back over it\n
		• you don’t have to make an example of one of them\n
		On a miss, someone in your gang makes a dedicated bid to replace you for alpha.```"""	
	#fuckingthieves
	elif message.content.startswith(".fuckingthieves"):
		msg = """```
		Fucking thieves: when you have your gang search their pockets and saddlebags for something, roll+hard. 
		It has to be something small enough to fit. 
		On a 10+, one of you happens to have just the thing, or close enough. 
		On a 7–9, one of you happens to have
		something pretty close, unless what you’re looking for is hi-tech,
		in which case no dice. On a miss, one of you used to have just the
		thing, but it turns out that some asswipe stole it from you.
		```"""
	#Chopper Moves List
	elif message.content.startswith(".chopper"):
		msg = """```.packalpha\n.fuckingthieves```"""

		
		

	#################
	##Driver moves##
	#################
	#a no shit driver
	elif message.content.startswith(".noshitdriver"):
		msg = """``` A no shit driver: \n when behind the wheel…\n
		…if you do something under fire, add your car’s power to your roll.\n
		…if you try to seize something by force, add your car’s power to your roll.\n
		…if you go aggro, add your car’s power to your roll.\n
		…if you try to seduce or manipulate someone, add your car’s looks to your roll.\n
		…if you help or interfere with someone, add your car’s power to
		your roll.\n
		…if someone interferes with you, add your car’s weakness to
		their roll.\n
		```"""
	#Good in the clinch
	elif message.content.startswith(".goodintheclinch"):
		msg = """```Good in the clinch:\nwhen you do something under fire, roll+sharp instead of roll+cool.```"""
	#weather eye
	elif message.content.startswith(".weathereye"):
		msg = """```Weather eye:\n when you open your brain to the world’s psychicmaelstrom, roll+sharp instead of roll+weird.```"""			
	#daredevil
	elif message.content.startswith(".daredevil"):
		msg = """``` Daredevil:\nif you go straight into danger without hedging your bets, you get +1armor. If you happen to be leading a gang or convoy, it gets +1armor too.```"""
	#my other car is a tank
	elif message.content.startswith(".myothercarisatank"):
		msg = """```My other car is a tank:\nyou get an additional car. Give it mounted machine guns (3-harm close/far area messy) or grenade launchers (4-harm close area messy) and +1armor.```"""
	#Driver Moves List
	elif message.content.startswith("driver"):
		msg = """```.noshitdriver\n.goodintheclinch\n.weathereye\n.daredevil\n.myothercarisatank```"""
		

	####################
	##Gunslinger moves##
	####################
	#battle-hardened
	elif message.content.startswith(".battlehardended"):
		msg = """```Battle-hardened:\nwhen you act under fire, roll+hard instead of roll+cool. ```"""
	#fuck this shit
	elif message.content.startswith(".fuckthisshit"):
		msg = """```Fuck this shit:\n
		 name your escape route and roll+hard.\n
		 On a 10+,sweet, you’re gone.\n
		 On a 7–9, you can go or stay, but if you go it costs you: leave something behind, or take something with you, the MC will tell you what.\n
		 On a miss, you’re caught vulnerable, half in and half out.\n
		```"""
	#battlefieldinstincts
	elif message.content.startswith(".battlefieldinstincts"):
		msg = """```Battlefield instincts:\nwhen you open your brain to the world’s psychic maelstrom, roll+hard instead of roll+weird, but only in battle.```"""
	#blood craze
	elif message.content.startswith(".bloodcrazed"):
		msg = """```Bloodcrazed:\n whenever you inflict harm, inflict +1harm.```"""
	#not to be fucked with
	elif message.content.startswith(".nottobefuckedwith"):
		msg = """```NOT TO BE FUCKED WITH:\n in battle, you count as a gang (3-harm gang small), with armor according to the circumstances. ```"""
	#in sano like drano
	elif message.content.startswith(".insanolikedrano"):
		msg = """```Insano like Drano:\n you get +1hard (hard+3).```"""
	#prepared for the inevitable
	elif message.content.startswith(".preparedfortheinevitable"):
		msg = """```Prepared for the inevitable:\nyou have a well-stocked and highquality first aid kit. It counts as an angel kit (cf ) with a capacity of 2-stock.```"""
	#Gunslinger Moves List
	elif message.content.startswith(".gunslinger"):
		msg = """```.battlefieldinstincts\n.bloodcrazed\n.nottobefuckedwith\n.insanolikedrano\n.preparedfortheinevitable```"""


	
	###############
	##Hocus moves##
	###############
	#Fortunes
	elif message.content.startswith(".fortunes"):
		msg = """```Fortunes:\nfortune, surplus and want all depend on your followers. At the beginning of the session, roll+fortune.\n
		On a 10+, your followers have surplus.\nOn a 7–9, they have surplus, but choose 1 want.\n
		On a miss, they are in want. If their surplus lists barter, like 1-barter or 2-barter, that’s your personal share.```"""
	#Frenzy
	elif message.content.startswith(".frenzy"):
		msg = """```Frenzy:\n
		When you speak the truth to a mob, roll+weird.\n On a 10+, hold 3.\n
		On a 7–9, hold 1.\n
		Spend your hold 1 for 1 to make the mob:\n\n
		• bring people forward and deliver them.\n
		• bring forward all their precious things.\n
		• unite and fight for you as a gang (2-harm 0-armor size appropriate).\n
		• fall into an orgy of uninhibited emotion: fucking, lamenting, fighting, sharing, celebrating, as you choose.\n
		• go quietly back to their lives.\n
		On a miss, the mob turns on you.\n
	```"""
	#Charismatic
	elif message.content.startswith(".charismatic"):
		msg = """```Charismatic:\n when you try to manipulate someone, roll+weird instead of roll+hot.```"""
	#fucking wacknut
	elif message.content.startswith(".fuckingwacknut"):
		msg = """```Fucking wacknut:\n you get +1weird (weird+3).```"""
	#seeing souls
	elif message.content.startswith(".seeingsouls"):
		msg = """```Seeing souls:\n when you help or interfere with someone, roll+weird instead of roll+Hx.```"""
	#Divine Protection
	elif message.content.startswith(".divineprotection"):
		msg = """```Divine protection:\n your gods give you 1-armor. If you wear armor, use that instead, they don’t add.```"""
	#Hocus Moves List
	elif message.content.startswith("hocus"):
		msg = """```.fortunes\n.frenzy\n.charismatic\n.fuckingwacknut\n.seeingsouls\n.divineprotection```"""
		
	###########
	##Skinner##
	###########
	#Breathtaking
	elif message.content.startswith(".breathtaking"):
		msg = """```Breathtaking:\n you get +1hot (hot+3).```"""
	#lost
	elif message.content.startswith(".lost"):
		msg = """``` Lost:\n when you whisper someone’s name to the world’s psychic maelstrom, roll+weird.\n
		On a hit, they come to you, with or without any clear explanation why.\n 
		On a 10+, take +1forward against them.\n
		On a miss, the MC will ask you 3 questions; answer them truthfully.
		```"""
	#artful and gracious
	elif message.content.startswith(".artfulandgracious"):
		msg = """```Artful & gracious:\n
		when you perform your chosen art — any act of expression or culture — or when you put its product before an audience, roll+hot.\n
		On a 10+, spend 3.\n
		On a 7–9, spend 1.\n
		Spend 1 to name an NPC member of your audience and choose one:\n
		• this person must meet me\n
		• this person must have my services\n
		• this person loves me\n
		• this person must give me a gift\n
		• this person admires my patron\n
		On a miss, you gain no benefit, but suffer no harm or lost opportunity. You simply perform very well.\n
		```"""
	#an arresting skinner
	elif message.content.startswith(".anarrestingskinner"):
		msg = """``` An arresting skinner:\n when you remove a piece of clothing, your own or someone else’s, no one who can see you can do anything but watch.\n
		You command their absolute attention\n
		If you choose, you can exempt individual people, by name.
		```"""
 	#Hypnotic
	elif message.content.startswith(".hypnotic"):
		msg = """``` Hypnotic:\n
		when you have time and solitude with someone, they become fixated upon you. Roll+hot.\nOn
		On a 10+, hold 3.\n 
		On a 7–9, hold 2. they can spend your hold, 1 for 1, by:\n
		• giving you something you \n
		• acting as your eyes and ears\n
		• fighting to protect you\n
		• doing something you tell them to\n
		For NPCs, while you have hold over them they can’t act against you.\n
		For PCs, instead, any time you like you can spend your hold, 1 for 1:\n
		• they distract themselves with the thought of you. they’re acting under fire.\n
		• they inspire themselves with the thought of you. they take +1 right now.\n
		On a miss, they hold 2 over you, on the exact same terms.\n
		```"""
	#Hocus Moves List
	elif message.content.startswith(".hocus"):
		msg = """```.breathtaking\n.lost\n.artfulandgracious\n.anarrestingskinner\n.hypnotic```"""

	#####################
	##Apoc Custom Moves##
	#####################
	#List custom move
	#elif message.content.startswith(".apoccustom"):
	#	msg ="""```.radiatedblood\n```"""
	#elif message.content.startswith(".radiatedblood"):
	#	msg ="""``````"""

	####################
	##Apoc Basic Moves##
	####################
	#Basic moves List
	elif message.content.startswith(".apocbasic"):
		msg = """```Do something under fire (.dosomethingunderfire)\n
					Go Aggro (.goaggro)\n
					Seize by force (.seizebyforce)\n
					Read a sitch (.readasitch)\n
					Read a person (.readaperson)\n
					Open your brain (.openyourbrain)\n
					Cover fire (.coverfire)\n
					Maintin Position (.maintainposition)\n
					Stay teh fuck down (.staythefuckdown)\n
					Follow other move (.followothermove)\n
					Ψ-harm (.psyharm)\n
					barter (.barter)\n
					harm (.harm)\n
					attack someone (.attacksomeone)\n
					Do something Under fire (.dosomethingunderfire)
					Seduce or Manipulate (.seduce)\n
					single combat (.singlecombat)\n
					Free for all comabt (.freeforall)\n
					firefight/shoot out (.gunfight)

		
		```"""
	#Barter
	elif message.content.startswith("barter"):
		msg = """```When you go into a holding’s bustling market, looking for some particular thing to buy, and it’s not obvious whether you should be able to just like go buy one like that, roll+sharp.\n
	On a 10+, yes, you can just go can buy it like that.\n
	On a 7–9, the MC chooses one of the following:\n
	• it costs 1-barter more than you’d expect\n
	• it’s available, but only if you meet with a guy who knows a guy\n
	• damn, I had one, I just sold it to this guy named Rolfball, maybeyou can go get it off him?\n
	• sorry, I don’t have that, but maybe this will do instead?```"""
	
	#follwothermove
	elif message.content.startswith(".followothermove"):
		msg = """```Follow other Move:\nWhen you follow through on someone else’s move, roll+Hx.\n
		If it’s one of the MC’s characters’, roll+sharp.\n On a 10+, the MC chooses one of the following for you, as appropriate:\n
		• you inflict +1harm\n
		• you dominate someone’s position\n
		• you make an untenable position or course securen\n
		• you avoid all fire\n
		• you create an opportunity and follow through to full effect\n
		On a 7–9, you create an opportunity, but you haven’t seized it
		or followed through on it yet. the MC will tell you what it is.\n
		On a miss, the MC chooses one of the above for an appropriate character of her own.
		```"""	
	#stay the fuck down
	elif message.content.startswith(".staythefuckdown"):
		msg = """```When you stay the fuck down, roll+sharp\n.
		On a hit, you’re in a relatively safe spot for the rest of the battle.\n 
		On a 10+, you come under no fire.\n
		On a 7–9, you come under only incidental fire.\n
		On a miss, you have to break position now or come under concentrated fire.
		```"""
	#maintainposition
	elif message.content.startswith(".maintainposition"):
		msg = """```When you maintain an untenable position or course, roll+hard.\n
		On a 10+, you can hold it, and for 3 ticks you’ll come under only incidental fire, even past 9:00.\n
		On a 7–9, you can hold it, and for a tick you’ll come under only incidental fire.\nOn
		Either way you can abandon it before your time is up to avoid concentrated fire.\n
		On a miss, abandon it now or suffer concentrated fire. (If it’s before 9:00, now it’s 9:00.)		
		```"""
	#coverfire	
	elif message.content.startswith(".coverfire"):
		msg = """```When you provide covering fire for someone, roll+cool.\n
		On a 10+, you keep them from coming under concentrated fire, even past 9:00.\n
		On a 7–9, their position or course is untenable, and they proceed accordingly.\n
		On a miss, they suffer concentrated fire now. (If it’s before 9:00, now it’s 9:00.)
		```"""
	#open your brain
	elif message.content.startswith(".openyourbrain"):
		msg = """```OPEN YOUR BRAIN:\n
		When you open your brain to the world’s psychic maelstrom,
		roll+weird.\n
		On a hit, the MC will tell you something new and interesting about the current situation, and might ask you a question or two; answer them.\n
		On a 10+, the MC will give you good detail.\n
		On a 7–9, the MC will give you an impression.\n
		If you already know all there is to know, the MC will tell you that.
		```"""
	#read a person
	elif message.content.startswith(".readaperson"):
		msg = """```READ A PERSON\n
		When you read a person in a charged interaction, roll+sharp.\n
		On a 10+, hold 3.\n
		On a 7–9, hold 1.\n
		While you’re interacting with them, spend your hold to ask their player questions, 1 for 1:\n
		• is your character telling the truth?\n
		• what’s your character really feeling?\n
		• what does your character intend to do?\n
		• what does your character wish I’d do?\n
		• how could I get your character to __?\n	
		```"""	
	#read a sitch
	elif message.content.startswith(".readasitch"):
		msg = """```READ A SITCH\n
		When you read a charged situation, roll+sharp.\n
		On a hit, you can ask the MC questions. Whenever you act on one of the MC’s answers, take +1.\n
		On a 10+, ask 3\n
		On a 7–9, ask 1:\n
		• where’s my best escape route / way in / way past?\n
		• which enemy is most vulnerable to me?\n
		• which enemy is the biggest threat?\n
		• what should I be on the lookout for?\n
		• what’s my enemy’s true position?\n
		• who’s in control here?\n
		```"""
	#seize by force
	elif message.content.startswith(".seizebyforce"):
		msg = """```SEIZE BY FORCE\n
		When you try to seize something by force, or to secure you hold on something, roll+hard.\n
		On a hit, choose options.\n
		On a 10+, choose 3.\n
		On a 7–9, choose 2:\n
		• you take definite hold of it\n
		• you suffer little harm\n
		• you inflict terrible harm\n
		• you impress, dismay or frighten your enemy\n
		```"""	
	#go aggro
	elif message.content.startswith(".goaggro"):
		msg = """```GO AGGRO\nWhen you go aggro on someone, roll+hard.\nO
		On a 10+, they have to choose: force your hand and suck it up, or cave and do what you want.\n
		On a 7–9, they can instead choose 1:\n
		• get the hell out of your way\n
		• barricade themselves securely in\n
		• give you something they think you want\n
		• back off calmly, hands where you can see\n
		• tell you what you want to know (or what you want to hear)\n
		```"""
	#dosomethignunderfire
	elif message.content.startswith(".dosomethingunderfire"):
		msg = """```DO SOMETHING UNDER FIRE\n
		When you do something under fire, or dig in to endure fire, roll+cool.\n
		On a 10+, you do it.\n
		On a 7–9, you flinch, hesitate, or stall: the MC can offer you a worse outcome, a hard bargain, or an ugly choice
		```"""
	#Ψ-harm
	elif message.content.startswith(".psyharm"):
		msg = """```When you suffer Ψ-harm, roll+Ψ-harm suffered (typically, roll+1).\n
		On a 10+, the MC can choose 1:\n
		• You’re out of action: unconscious, trapped, incoherent or panicked.\n
		• You’re out of your own control. You come to yourself again a few seconds later, having done I-don’t-know-what\n
		• Choose 2 from the 7–9 list below.\n
		On a 7–9, the MC can choose 1:\n
		• You lose your footing\n
		• You lose your grip on whatever you’re holding.\n
		• You lose track of someone or something you’re attending to.\n
		• You miss noticing something important.\n
		• You take a single concrete action of the MC’s choosing.\n
		On a miss, you keep it together and overcome the -harm with no effect.\n```"""
		
	#Augury
	elif message.content.startswith("augury"):
		msg = """``` When you use your followers or your workspace for augury, roll+weird.\n
		On a hit, you can choose 1:\n
		• Reach through the world’s psychic maelstrom to something or someone connected to it.\n
		• Isolate and protect a person or thing from the world’s psychic maelstrom.\n
		• Isolate and contain a fragment of the world’s psychic maelstrom itself.\n
		• Insert information into the world’s psychic maelstrom.\n
		• Open a window into the world’s psychic maelstrom.\n
		By default, the effect will last only as long as you maintain it, will reach only shallowly into the world’s psychic maelstrom as it is local to you, and will bleed instability.\n
		On a 10+, choose 2;\n
		on a 7–9, choose 1:\n
		• It’ll persist (for a while) without your actively maintaining it.\n
		• It reaches deep into the world’s psychic maelstrom.\n
		• It reaches broadly throughout the world’s psychic maelstrom.\n
		• It’s stable and contained, no bleeding.\n
		On a miss, whatever\n
		```"""
	#harm
	elif message.content.startswith(".harm"):
		msg = """```When you suffer harm, roll+harm suffered (after armor, if you’re wearing any).\n 
		On a 10+, the MC can choose 1:\n
		• You’re out of action: unconscious, trapped, incoherent or panicked.\n
		• It’s worse than it seemed. Take an additional 1-harm.\n
		• Choose 2 from the 7–9 list below.\n
		On a 7–9, the MC can choose 1:\n
		• You lose your footing.\n
		• You lose your grip on whatever you’re holding\n• You lose track of someone or something you’re attending to.\n
		• You miss noticing something important.\n
		On a miss, the MC can nevertheless choose something from the 7–9 list above. If she does, though, it’s instead of some of the harm you’re suffering, so you take -1harm. the suffering harm move adds a wrinkle, a little
		```"""	
	#Do something under fire
	elif message.content.startswith(".dosomethingunderfire"):
		msg = """```When you do something under fire, or dig in to endure fire, roll+cool.\n
		On a 10+, you do it.\n
		On a 7–9, you flinch, hesitate, or stall:\n
		the MC can offer you a worse outcome, a hard bargain, or an ugly choice.\n
		On a miss, be prepared for the worst.
		```"""
	#Attack someone
	elif message.content.startswith(".attacksomeone"):
		msg = """```When you attack someone unprepared, unsuspecting, or helpless, roll+hard.\n
		On a 10+, inflict full harm as established.\n
		On a 7–9, they’re able somehow to dodge, block, or duck, or else you just don’t quite strike home; inflict little harm.\n
		In either case, if they can and do choose to fight back, now you’re doing battle them.\n
		On a miss, be prepared for the worst.```"""
	#seduce or manipulate
	elif message.content.startswith(".seduce"):
		msg = """```When you try to seduce or manipulate someone, tell them what you want and roll+hot.\n
		For NPCs: on a hit, they ask you to promise something first, and do it if you promise.\n 
		On a 10+, whether you keep your promise is up to you, later.\n
		On a 7–9, they need some concrete assurance right now.\n
		For PCs: on a 10+, both.\n
		On a 7–9, choose 1:\n
		• if they do it, they mark experience\n
		• if they refuse, erase one of their stat highlights for the remainder of the session\n
		What they do then is up to them.\n
		On a miss, for either NPCs or PCs, be prepared for the worst.```"""
	
	#single combat
	elif message.content.startswith(".singlecombat"):
		msg = """```When you do single combat with someone, both you and your enemy inflict and suffer harm as established. Roll+hard.\n
		On a 10+, spend 3.\n
		On a 7–9, spend 2.\n 
		On a miss, spend 1. Spend them blind, on the following:\n
		• Strike hard. Inflict +1harm.\n
		• Defend yourself. Gain +1armor\n
		• Seize the victory. Whichever of you spends more on this, wins the round.\n
		If your enemy is an NPC, the MC gets to spend 2 for her as well. The MC may
		choose to spend 1 or 3 instead, but must declare that she’s doing so.\n
		1 is for an NPC weak, afraid, or lacking will; 3 is for an NPC distinguished by her bloodlust.\n
		Whichever of you wins, if the loser is still alive, the loser chooses:\n
		• You have me at your mercy. What do you do to me?\n
		• You drive me into terrified flight. Do you pursue me?\n
		• this is a fight to the death. We continue to another round.\n
		If it’s a tie, then if both of you want to end the fight, it ends, but if either of you want to fight on, it continues to another round
		```"""
	#Free for all comabt
	elif message.content.startswith(".freeforall"):
		msg = """```When you’re involved in a chaotic free-for-all, the mass of combatants as a whole takes harm as established, as a single gang inflicting harm on itself. Roll+hard.\n
		On 10+, spend 3. On 7-9, spend 2.\n On a miss, spend 1. Spend them blind, on the following:\n
		• Add to the chaos. the combatants as a whole suffer +1harm.\n
		• Defend yourself. Gain +1armor.\n
		• Defend someone else. they gain +1armor.\n
		• Take a single, short, personal action.\n
		For each named NPC in the fight, the MC gets to spend 1 as well. the MC can choose to spend 0 or 2 instead, but must declare that she’s doing so.\n
		0 is for unarmed or otherwise semi-incapacitated NPCs;\n
		3 is for NPCs distinguished by their violent competence and calm in chaos.\n
		If the number of named NPCs is large, be patient while the MC lists her spends.\n
		After the exchange of harm, the fight ends, unless or until someone reignites it.
		```"""
	#Gun fight
	elif message.content.startswith(".gunfight"):
		msg ="""Both sides inflict and suffer harm as established. Roll+hard.\n
		 On 10+, spend 3.\n 
		 On 7-9, spend 2.\n
		 On a miss, spend 1.\n
		 Spend them blind, on the following:\n
		 • Provide supporting fire. Add +1harm to the harm your side inflicts\n
		 • Provide covering fire. Add +1armor to your side.\n
		 • Cover ground. Whichever side spends more on this, wins the round.\n
		 • Take a single, short, personal action.\n
		```"""

		#Need to add road war moves such as boarding a moving car or tacking v-harm.
	
	
	#added apoc books
	elif message.content.startswith(".apocbooks"):
		msg = """```Angel\n
		Battlebabe\n
		Brainer\n
		Chopper\n
		Driver\n
		Gunslinger\n 
		Hocus\n				
		```"""
		
	

	return msg