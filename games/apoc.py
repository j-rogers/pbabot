import random

    ###############################################################################################################################################
	###############################################################################################################################################
	############################################################ Apocalpyse world #################################################################
	###############################################################################################################################################
	###############################################################################################################################################
	
def handle(message):
    messageString = message.content
    messageString = messageString.replace (" ", "")
    messageString = messageString.lower()
    msg = ''
    switch = {
		# Help.
        '.list': apoclist,
		'.books': book, 
        '.basic':basic,
        #basic moves
        '.combat': combat,
        '.psyharm': psyharm,
        '.harm': harm,
        '.readasitch': readasitch,
        '.firstaid': firstaid,
        '.surpriseattack':supriseattack,
        '.coverfire' : coverfire,
        '.shootsomeone': shootsomeone,
        '.hitsomeone': hitsomeone,
        '.setanambush': setanambush,
        '.fasttalk': fasttalk,
        '.barter': barter,
        '.gounderknife': gounderknife,
        '.playhardball': playhardball,
        '.workajob': workajob,
        '.workagig':workajob,
        '.situation': situation,
        '.actunderpressure': actunderpressure,
        '.investigate': investigate,
        '.doiknowthings': doiknowthings,
        '.weirdapocstuff': weirdapocstuff,
        '.openyourbrain': openyourbrain,
        'seizebyforce': seizebyforce,
        '.social': social,
        '.augury': augury,
        '.costofliving':costofliving,
        '.didntgetfood': didntgetfood,
        #Angel
        '.sixthsense': sixthsense,
        '.infirmary': infirmary,
        '.professionalcompassion': professionalcompassion,
        '.battlefieldgrace': battlefieldgrace,
        '.healingtouch': healingtouch,
        '.touchedbydeath': touchedbydeath,
        '.angel': angel,
        #brainer	 	
        '.dangerousandsexy': dangerousandsexy,
        '.icecold': icecold,
        '.merciless': 	merciless,
        '.visionsofdeath': visionsofdeath,
        '.perfectinstincts': perfectinstincts,
        '.impossiblereflexes': impossiblereflexes,
        '.unnaturallusttransfixion': unnaturallusttransfixion,
        '.casualbrainreceptivity': casualbrainreceptivity,
        '.pretnernatual': 	pretnernatual,
        '.deepbrainscan': deepbrainscan,
        '.directbrainwhisperprojection':directbrainwhisperprojection, 	
        '.inbrainpupperstrings': inbrainpupperstrings,
        '.brainer': brainer,
        #driver
        '.packalpha': packalpha, 	
        '.fuckingthieves': 	fuckingthieves,
        '.chopper': chopper,
        '.noshitdriver': noshitdriver,
        '.goodintheclinch': 	goodintheclinch,
        '.weathereye': 	weathereye,
        '.daredevil': 	daredevil,
        '.myothercarisatank': myothercarisatank,
        '.combatdriver':combatdriver,
        '.eyeonthedoor':eyeonthedoor,
        '.reputation':reputation,
        '.driver': driver,
        #gunslinger
        '.battlehardended': battlehardended,
        '.fuckthisshit':  fuckthisshit,
        '.battlefieldinstincts': battlefieldinstincts,
        '.bloodcrazed': bloodcrazed,
        '.nottobefuckedwith': nottobefuckedwith,
        '.insanolikedrano': insanolikedrano,
        '.preparedfortheinevitable': 	preparedfortheinevitable,
        '.gunslinger': gunslinger,
        #quarantine	
        '.quarantine': 	quarantine,
        '.combatveteran': 	combatveteran,
        '.disciplinedengagement': 	disciplinedengagement,
        '.leavenoonebehind': leavenoonebehind,
        '.eagertoknow': eagertoknow,
        '.inspiring': inspiring,
        '.fortunes': fortunes,
        '.frenzy': frenzy,
        '.charismatic': charismatic,	
        '.fuckingwacknut': 	fuckingwacknut,
        '.seeingsouls': 	seeingsouls,
        '.divineprotection': divineprotection,
        #hocus	
        '.hocus': hocus,
        '.breathtaking': breathtaking,
        '.lost': lost,
        '.artfulandgracious': artfulandgracious, 	
        '.anarrestingskinner': 	anarrestingskinner,
        '.hypnotic': 	hypnotic,
        '.skinner': skinner,
        #faceless	
        '.faceless': faceless,
        '.pitbull': pitbull,
        '.rasputin': rasputin,
        '.juggernaut': juggernaut,
        '.ohyeah': ohyeah,
        '.scentofblood': scentofblood,	
        '.norman': 	norman,
        '.asone': 	asone,
        '.beastly': beastly,
        #maestroD	
        '.maestro': maestro,
        '.youcallthishot': 	youcallthishot, 
        '.devilwithablade': 	devilwithablade,
        '.fingersineverypie': fingersineverypie,
        '.everybodyeats': 	everybodyeats,
        '.justgivemeamotive': 	justgivemeamotive,
        #child thing
        '.childthing': childthing,
        '.mercurial':mercurial,
        '.sniffingtheair':sniffingtheair,
        '.mothersheartbeat':mothersheartbeat,
        '.feral':feral,
        '.ferocious':ferocious,

	}
    for case in switch:
		#Checks first for if case == messagestring
        if case == messageString: msg = switch[case](messageString)
    

    
    msg = msg.replace("\t","")
    return msg


#####################
## list apoc moves ##
#####################
def apoclist(messageString):
    msg ="""```
    .books - Lists all playbooks.
    .combat - Lists all combat moves (like shoot someone)
    .social - Lists all social moves (like fasttalk)
    .situtation - Lists all situtaional moves (like acting under pressure)
    .weirdapocstuff - Lists weird apoc moves (like open your brain.)
    .basic - lists all basic moves 
    ```"""
    return msg

def basic (messageString):
    msg = """```
    Weird apoc stuff: 
    .openyourbrain - When you open your brain to the world’s psychic maelstrom
    .psyharm - When you take psychic harm
    .augury - When you use your followers or your workspace for augury, roll+weird.

    Situational
    .actunderpressure - When you race against the clock, act while in danger or act to avoid danger, roll+Cool.
    .investigate -  When you closely study a place, or situation, roll + Sharp.
    .doiknowthings - When you consult your accumulated knowledge about something, roll + sharp.

    Social
    .fasttalk - When you try to convince someone to do what you want with promises, lies or bluster, roll+Hot.
    .barter - When you're looking to buy something roll + sharp.
    .gounderknife - When you  want to and are able to have a new implant installed, roll + barter spent,
    .playhardball - When you get in someone’s face threatening violence and you intend to carry through, roll+hard.
    .workajob - When you negotiate the terms of a job, roll + hot.

    Combat
    .harm  - When you suffer harm, roll+harm suffered (after armor, if you’re wearing any). 
    .readasitch - When you read a charged situation, roll+cool.
    .firstaid - When you treat someone’s wounds using appropriate medical equipment, roll +sharp,
    .seizebtforce -  When you try to seize something by force, or to secure your hold on something, roll+hard.
    .surpriseattack - When you attack someone unprepared, unsuspecting, or helpless, roll+hard.
    .coverfire - When you want to lay down lots fire or provide cover fire roll+cool 
    .shootsomeone - When you want to shoot someone roll + hard:
    .hitsomeone - When you want to hit someone roll + hard:
    .setanambush - When you want to set an ambush for someone, Describe your ambush, and assign allies as fiction dictates. roll + sharp.
    ```"""
    return msg
################
## Play Books ##
################
def book (messageString):
    msg = """```
    .angel
    .battlebabe
    .brainer
    .chopper
    .driver
    .gunslinger
    .hocus
    .quarantine
    .faceless
    .maestro```"""
    return msg

#Sixthsense
def sixthsense (messageString):
	msg = """``` Sixth sense:\n When you open your brain to the world’s psychic maelstrom roll+sharp instead of roll+weird.```""" 
	return msg	
 
	#infirmary	
def infirmary (messageString):
	msg = """```Infirmary:\n you get an infirmary a workspace with life support a drug lab and a crew of 2 (Shigusa & Mox maybe). Get patients into it and you can work on them like a savvyhead on tech (cf ). ```""" 
	return msg	
 
#Professional compassion
def professionalcompassion (messageString):
	msg = """```Professonal compassion:\n 
	you can choose to roll+sharp instead of roll+Hx when you help someone who’s rolling.```""" 
	return msg
 
#Battlefield grace
def battlefieldgrace (messageString):
    msg = """``` Battlefield grace\n while you are caring for people not fighting you get +1 armor.```""" 
    return msg
 
#Healing touch	
def healingtouch (messageString):
	msg = """```Healing touch:\n when you put your hands skin-to-skin on a wounded person and open your brain to them roll+weird.\n On a 10+ heal 1 segment \n
			On a 7–9 heal 1 segment but you’re acting under fire from your patient’s brain.\n
			On a miss: first\n
			you don’t heal them. Second you’ve opened both your brain and theirs to the world’s psychic maelstrom without protection or preparation. 
			For you and for your patient if your patient’sa fellow player’s character treat it as though you’ve made that move and missed the roll. For patients belonging to the MC their experience and fate are up to the MC.```""" 
	return msg	
 
#Touched by death
def touchedbydeath (messageString):
    msg = """```Touched by death:\n whenever someone in your care dies you get +1weird (max +3). ```""" 
    return msg
 	
#Àngel Move Lists
def angel (messageString):
	msg = """```
    .sixthsense
    .infirmary
    .professionalcompassion
    .battlefieldgrace
    .healingtouch
    .touchedbydeath```""" 
	return msg

######################
## Battlebabe Moves ##
######################
#Dangerous and Sexy
def dangerousandsexy(messageString):
    msg = """```Dangerous & sexy:\n
    when you enter into a charged situation roll+hot.\n
    On a 10+ hold 2.\n
    On a 7–9 hold 1.\n 
    Spend your hold 1 for 1 to make eye contact with an NPC present who freezes or flinches and can’t take action until you break it off.  On a miss your enemies identify you immediately as their foremost threat. ```"""
    return msg
#Ice Cold
def icecold(messageString):
    msg = """```Ice cold:\n when you go aggro on an NPC roll+cool instead of roll+hard.\n When you go aggro on another player’s character roll+Hx instead of roll+hard.```"""
    return msg
#Merciless
def merciless(messageString):
    msg = """```Merciless:\n when you inflict harm inflict +1harm.```"""
    return msg
#Viions of death.
def visionsofdeath(messageString):
    msg = """```Visions of death:\n when you go into battle roll+weird.\n
    On a 10+ name one person who’ll die and one who’ll live.\n 
    On a 7–9 name one person who’ll die OR one person who’ll live.\n
    Don’t name a player’s character; name NPCs only. The MC will make your vision come true if it’s even remotely possible.\n
    On a miss you foresee your own death and accordingly take -1 throughout the battle.```"""
    return msg	
#Perfect Insticts
def perfectinstincts(messageString):
    msg = """```Perfect instincts:\nwhen you’ve read a charged situation and you’re acting on the MC’s answers take +2 instead of +1.```"""
    return msg		
#Impossible Reflexes.
def impossiblereflexes(messageString):
    msg = """```Impossible reflexes:\n the way you move unencumbered counts as armor.\n If you’re naked or nearly naked 2-armor; if you’re wearing non-armor fashion 1-armor. If you’re wearing armor use it instead.```"""
    return msg
def battlebabe(messageString):
    msg = """```
    .dangerousandsexy
    .icecold
    .merciless
    .visionsofdeath
    .perfectinstincts
    .impossiblereflexes
    ```"""
    return msg


###################
## Brainer Moves ##
###################
#Unnatural lust transfixion
def unnaturallusttransfixion(messageString):
    msg = """```Unnatural lust transiixion:\n when you try to seduce someone roll+weird instead of roll+hot.```"""
    return msg
#Casual brain receptivity
def casualbrainreceptivity(messageString):
    msg = """```Casual brain receptivity:\nwhen you read someone roll+weird instead of roll+sharp.\nYour victim has to be able to see you but you don’t have to interact. 		```"""
    return msg	
#preternatural at will brain atturnment
def pretnernatual(messageString):
    msg = """```Preternatural at-will brain attunement:\nyou get +1weird (weird+3).```"""
    return msg
#Deep brain scan
def deepbrainscan(messageString):
    msg = """```Deep brain scan:\n when you have time and physical intimacy with someone — mutual intimacy like holding them in your arms or 1-sided intimacy like they’re restrained to a table — you can read them more deeply than normal. Roll+weird.\n
    On a 10+hold 3.\n
    On a 7–9 hold 1.\n
    While you’re reading them spend your hold to ask their player questions 1 for 1:\n
    • what was your character’s lowest moment?\n
    • for what does your character crave forgiveness and of whom?\n
    • what are your character’s secret pains?\n
    • in what ways are your character’s mind and soul vulnerable?\n
    On a miss you inflict 1-harm (ap) upon your subject to no benefit.```"""
    return msg	
#Direct brain whisper projection
def directbrainwhisperprojection(messageString):
    msg = """```Direct-brain whisper projection:\nyou can roll+weird to get the effects of going aggro without going aggro.\n
    Your victim has to be able to see you but you don’t have to interact.\n
    If your victim forces your hand your mind counts as a weapon (1-harm apclose loud-optional).```"""
    return msg	
#in brain puppet string
def inbrainpupperstrings(messageString):
    msg = """```In-brain puppet strings:\nwhen you have time and physical intimacy with someone — again mutual or 1-sided — you can plant a command inside their mind. Roll+weird.\n
    On a 10+ hold 3.\n 
    On a 7–9 hold 1.\n 
    At your will no matter the circumstances you can spend your hold 1 for 1:\n
    • inflict 1-harm (ap)\n
    • they take -1 right now\n
    If they fulfill your command that counts for all your remaining
    hold.\n 
    On a miss you inflict 1-harm (ap) upon your subject to no benefit.```"""
    return msg
#Brainer Move list
def brainer(messageString):
    msg = """```..unnaturallusttransfixion\n.casualbrainreceptivity\n.pretnernatual\n.deepbrainscan\n.directbrainwhisperprojection\n.inbrainpupperstrings```"""
    return msg
    
###################
## Chopper moves ##
###################
#pack alpha
def packalpha(messageString):
    msg = """```Pack alpha:\nWhen you try to impose your will on your gang roll+hard.\n
    On a 10+ all 3.\n 
    On a 7–9 choose 1:\n
    • they do what you want\n
    • they don’t fight back over it\n
    • you don’t have to make an example of one of them\n
    On a miss someone in your gang makes a dedicated bid to replace you for alpha.```"""
    return msg	
#fuckingthieves
def fuckingthieves(messageString):
    msg = """```
    Fucking thieves: when you have your gang search their pockets and saddlebags for something roll+hard. 
    It has to be something small enough to fit. 
    On a 10+ one of you happens to have just the thing or close enough. 
    On a 7–9 one of you happens to have
    something pretty close unless what you’re looking for is hi-tech
    in which case no dice. On a miss one of you used to have just the
    thing but it turns out that some asswipe stole it from you.
    ```"""
    return msg
#Chopper Moves List
def chopper(messageString):
    msg = """```.packalpha\n.fuckingthieves```"""
    return msg

    
    

##################
## Driver moves ##
##################
#a no shit driver
def noshitdriver(messageString):
    msg = """``` A no shit driver: \n when behind the wheel…\n
    …if you do something under fire add your car’s power to your roll.\n
    …if you try to seize something by force add your car’s power to your roll.\n
    …if you go aggro add your car’s power to your roll.\n
    …if you try to seduce or manipulate someone add your car’s looks to your roll.\n
    …if you help or interfere with someone add your car’s power to
    your roll.\n
    …if someone interferes with you add your car’s weakness to
    their roll.\n
    ```"""
    return msg
#Good in the clinch
def goodintheclinch(messageString):
    msg = """```Good in the clinch:\nwhen you do something under fire roll+sharp instead of roll+cool.```"""
    return msg
#weather eye
def weathereye(messageString):
    msg = """```Weather eye:\n when you open your brain to the world’s psychicmaelstrom roll+sharp instead of roll+weird.```"""
    return msg			
#daredevil
def daredevil(messageString):
    msg = """``` Daredevil:\nif you go straight into danger without hedging your bets you get +1armor. If you happen to be leading a gang or convoy it gets +1armor too.```"""
    return msg
#my other car is a tank
def myothercarisatank(messageString):
    msg = """```My other car is a tank:\nyou get an additional car. Give it mounted machine guns (3-harm close/far area messy) or grenade launchers (4-harm close area messy) and +1armor.```"""
    return msg
def combatdriver(messageString):
    msg = """``` When you use your vehicle as a weapon, inflict +1harm. When you inflict v-harm, add +1 to your targets roll. When you suffer v-harm, take -1 to your roll.```"""
    return msg
def eyeonthedoor(messageString):
    msg ="""```Name your escape route and roll+cool.
    10+ You're gone.
    7-9: You can go or stay, but if you go it costs you. leave something of take something with you, the MC will tell you what.
    On a miss, you're caught, vulenerable, half in and half out.```"""
    return msg

def reputation(messageString):
    msg ="""```When you meet somoene important (your call) roll +cool.
    On a hit, they've heard of you, and say what they've heard; The MC has them respond accordingly.
    On a 10+ take +1forward for dealing with them as well.
    On a miss, they've heard of you, but the MC decides what the've heard.```"""
    return msg

#Driver Moves List
def driver(messageString):
    msg = """```
    .noshitdriver
    .goodintheclinch
    .weathereye
    .daredevil
    .myothercarisatank
    .combatdriver
    .eyeonthedoor
    .reputation```"""
    return msg
    

######################
## Gunslinger moves ##
######################
#battle-hardened
def battlehardended(messageString):
    msg = """```Battle-hardened:\nwhen you act under fire roll+hard instead of roll+cool. ```"""
    return msg
#fuck this shit
def fuckthisshit(messageString):
    msg = """```Fuck this shit:\n
        name your escape route and roll+hard.\n
        On a 10+sweet you’re gone.\n
        On a 7–9 you can go or stay but if you go it costs you: leave something behind or take something with you the MC will tell you what.\n
        On a miss you’re caught vulnerable half in and half out.\n
    ```"""
    return msg
#battlefieldinstincts
def battlefieldinstincts(messageString):
    msg = """```Battlefield instincts:\nwhen you open your brain to the world’s psychic maelstrom roll+hard instead of roll+weird but only in battle.```"""
    return msg
#blood craze
def bloodcrazed(messageString):
    msg = """```Bloodcrazed:\n whenever you inflict harm inflict +1harm.```"""
    return msg
#not to be fucked with
def nottobefuckedwith(messageString):
    msg = """```NOT TO BE FUCKED WITH:\n in battle you count as a gang (3-harm gang small) with armor according to the circumstances. ```"""
    return msg
#in sano like drano
def insanolikedrano(messageString):
    msg = """```Insano like Drano:\n you get +1hard (hard+3).```"""
    return msg
#prepared for the inevitable
def preparedfortheinevitable(messageString):
    msg = """```Prepared for the inevitable:\nyou have a well-stocked and highquality first aid kit. It counts as an angel kit (cf ) with a capacity of 2-stock.```"""
    return msg
#Gunslinger Moves List
def gunslinger(messageString):
    msg = """```.battlefieldinstincts\n.bloodcrazed\n.nottobefuckedwith\n.insanolikedrano\n.preparedfortheinevitable```"""
    return msg

######################
## Quarantine moves ##
######################
#Quarantine moves:
def quarantine(messageString):
    msg = """```
    .combatveteran\n
    .disciplinedengagement\n
    .leavenoonebehind\n
    .eagertoknow\n
    .inspiring\n
    ```"""
    return msg
#Combat Veteran
def combatveteran(messageString):
    msg = """```Combat Veteran:\nYou get +1cool (cool+3).```"""
    return msg
#disciplined engagement:
def disciplinedengagement(messageString):
    msg = """```Disiclined Engagement:\n 
        when you inflict harm you can choose to inflict an amount of harm you like less than or up to your harm as established including s-harm.\n
        Decide at the moment you inflict the harm; you need not tell anyone in advance how much harm you intend to inflict
    ```"""
    return msg
#Leave no one behind:
def leavenoonebehind(messageString):
    msg = """```Leave no one behind:\n
    in battle when you help someone who’s rolling don’t roll+Hx. You help them as though you’d hit the roll with a 10+.
    ```"""
    return msg
#Eager to know 
def eagertoknow(messageString):
    msg = """```Eager to know:\n 
    When you go to someone for advice they must tell you honestly what they think the best course is.\n
    If you pursue that course take +1 to any rolls you make in the pursuit. If you pursue that course but don’t accomplish your ends you mark experience
    ```"""
    return msg
#inspiring:
def inspiring(messageString):
    msg = """```Inspiring:\n
    when another player’s character rolls+Hx to help you they mark experience
    ```"""
    return msg



#################
## Hocus moves ##
#################
#Fortunes
def fortunes(messageString):
    msg = """```Fortunes:\nfortune surplus and want all depend on your followers. At the beginning of the session roll+fortune.\n
    On a 10+ your followers have surplus.\nOn a 7–9 they have surplus but choose 1 want.\n
    On a miss they are in want. If their surplus lists barter like 1-barter or 2-barter that’s your personal share.```"""
    return msg
#Frenzy
def frenzy(messageString):
    msg = """```Frenzy:\n
    When you speak the truth to a mob roll+weird.\n On a 10+ hold 3.\n
    On a 7–9 hold 1.\n
    Spend your hold 1 for 1 to make the mob:\n\n
    • bring people forward and deliver them.\n
    • bring forward all their precious things.\n
    • unite and fight for you as a gang (2-harm 0-armor size appropriate).\n
    • fall into an orgy of uninhibited emotion: fucking lamenting fighting sharing celebrating as you choose.\n
    • go quietly back to their lives.\n
    On a miss the mob turns on you.\n
```"""
    return msg
#Charismatic
def charismatic(messageString):
    msg = """```Charismatic:\n when you try to manipulate someone roll+weird instead of roll+hot.```"""
    return msg
#fucking wacknut
def fuckingwacknut(messageString):
    msg = """```Fucking wacknut:\n you get +1weird (weird+3).```"""
    return msg
#seeing souls
def seeingsouls(messageString):
    msg = """```Seeing souls:\n when you help or interfere with someone roll+weird instead of roll+Hx.```"""
    return msg
#Divine Protection
def divineprotection(messageString):
    msg = """```Divine protection:\n your gods give you 1-armor. If you wear armor use that instead they don’t add.```"""
    return msg
#Hocus Moves List
def hocus(messageString):
    msg = """```.fortunes\n.frenzy\n.charismatic\n.fuckingwacknut\n.seeingsouls\n.divineprotection```"""
    return msg
    
#############
## Skinner ##
#############
#Breathtaking
def breathtaking(messageString):
    msg = """```Breathtaking:\n you get +1hot (hot+3).```"""
    return msg
#lost
def lost(messageString):
    msg = """``` Lost:\n when you whisper someone’s name to the world’s psychic maelstrom roll+weird.\n
    On a hit they come to you with or without any clear explanation why.\n 
    On a 10+ take +1forward against them.\n
    On a miss the MC will ask you 3 questions; answer them truthfully.
    ```"""
    return msg
#artful and gracious
def artfulandgracious(messageString):
    msg = """```Artful & gracious:\n
    when you perform your chosen art — any act of expression or culture — or when you put its product before an audience roll+hot.\n
    On a 10+ spend 3.\n
    On a 7–9 spend 1.\n
    Spend 1 to name an NPC member of your audience and choose one:\n
    • this person must meet me\n
    • this person must have my services\n
    • this person loves me\n
    • this person must give me a gift\n
    • this person admires my patron\n
    On a miss you gain no benefit but suffer no harm or lost opportunity. You simply perform very well.\n
    ```"""
    return msg
#an arresting skinner
def anarrestingskinner(messageString):
    msg = """``` An arresting skinner:\n when you remove a piece of clothing your own or someone else’s no one who can see you can do anything but watch.\n
    You command their absolute attention\n
    If you choose you can exempt individual people by name.
    ```"""
    return msg
#Hypnotic
def hypnotic(messageString):
    msg = """``` Hypnotic:\n
    when you have time and solitude with someone they become fixated upon you. Roll+hot.\nOn
    On a 10+ hold 3.\n 
    On a 7–9 hold 2. they can spend your hold 1 for 1 by:\n
    • giving you something you \n
    • acting as your eyes and ears\n
    • fighting to protect you\n
    • doing something you tell them to\n
    For NPCs while you have hold over them they can’t act against you.\n
    For PCs instead any time you like you can spend your hold 1 for 1:\n
    • they distract themselves with the thought of you. they’re acting under fire.\n
    • they inspire themselves with the thought of you. they take +1 right now.\n
    On a miss they hold 2 over you on the exact same terms.\n
    ```"""
    return msg
#Skinner Moves List
def skinner(messageString):
    msg = """```.breathtaking\n.lost\n.artfulandgracious\n.anarrestingskinner\n.hypnotic```"""
    return msg


##################
## The Faceless ##
##################
#faceless moves
def faceless(messageString):
    msg = """```Faceless moves:\n
    .pitbull\n
    .rasputin\n
    .juggernaut\n
    .ohyeah\n
    .scentofblood\n
    .norman\n
    .asone\n
    .beastly\n
        ```"""
    return msg
#pitball
def pitbull(messageString):
    msg = """```Pitbull:\nwhenever your life becomes untenable name the person you hold most responsible.\n
    Take +1 ongoing to all rolls versus them forever.\n
    (All rolls with them directly as a target count of course.\n
    Rolls against their family and friends minions or property may count in the MC’s judgment. \n
    MCs remember your job is to make Apocalypse World seem real and keep the characters’ lives interesting not deny the PCs bonuses.)
    ```"""
    return msg
#rasputin
def rasputin(messageString):
    msg = """```Rasputin:\nshot stabbed and poisoned you just keep coming.\n
    When you are being scary as fuck and coming at someone you get +1armor.\n
    You still get shot and stabbed bleeding just doesn’t bother you that much anymore.
    ```"""
    return msg
#juggernaut
def juggernaut(messageString):
    msg = """```Juggernaut:\n
    take -2 on all “when you suffer harm” rolls
    ```"""
    return msg
#oh yeah
def ohyeah(messageString):
    msg = """```Oh yeah!:\n
    roll+hard to smash your way through scenery to get to or away from something.\n
    On a 10+ the scenery is moved or smashed and you get what you want.\n
    On a 7–9 you get what you want and smash or move the scenerybut you take 1-harm (ap)\n
    and are disoriented and under fire in follow-up actions leave something behind or take something with you. Think smashing through walls or pushing through burned out husks of cars.\n
    On a miss your foot gets pinned under something mid-smash.
    ```"""
    return msg
#scent of blood
def scentofblood(messageString):
    msg = """```Scent of blood:\nAt the beginning of the session roll+weird.\n
    On a 10+ hold 1+1.\n
    On a 7–9 hold 1.\n
    At any time you or the MC can spend your hold to have you at the scene of a battle (a real battle not intimate violence between a couple people).\n
    If your hold was 1+1 take +1forward now.\n
    On a miss the MC holds 1 and can spend it to have you there and pinned down.
    ```"""
    return msg
#norman
def norman(messageString):
    msg ="""```Norman:\nYou seek the advice of your mask. Roll+weird to see what it directs you to do.\n
    On a 10+ mark experience and take +1forward if you do as your mask wishes.\n
    On a 7–9 take a +1 if you do what it wants and act under fire if you don’t.\n
    On a miss it has its own agenda. Act under fire if you don’t follow it.
    ```"""
    return msg
#as one
def asone(messageString):
    msg ="""```As one:\nAttempts by other PCs to seize your mask by force or to get you to remove or give away your mask by going aggro or seduction/manipulation are at -2.\n
    NPCs will never succeed at unmasking you against your will even if you are completely at their mercy.
    ```"""
    return msg
#beastly
def beastly(messageString):
    msg = """```Beastly:\n
        You get +1hard (hard+3).
        ```"""
    return msg

####################
## The Maestro D' ##
####################
def maestro(messageString):
    msg = """```The Maestro D' moves
    .youcallthishot
    .devilwithablade
    .fingersineverypie
    .everybodyeats
    .justgivemeamotive`
    ```"""
    return msg
#You call this hot? 
def youcallthishot(messageString):
    msg = """```You call this hot?
    when you do something under fire roll+hot instead of roll + cool.
    ```"""
    return msg
#A devil with a blade 
def devilwithablade(messageString):
    msg = """```A devil with a blade: 
    When you use a blade to go aggro roll+hot instead of roll+hard.
    ```"""
    return msg
#Fingers in every pie
def fingersineverypie(messageString):
    msg = """```Fingers in every pie:
    Put out the word that you want a thing - could be a person could be somethin somethin could even just be a thing - and roll+hot.
    On a 10+ it shows up in your establishment for you like magic.
    On a 7-9: Well your people make an effort and everybody wants to please you and close is close right? 
    On a miss it shows in your establishment for you with strings wicked attached.
    ```"""
    return msg
def everybodyeats(messageString):
    msg = """```Everybody eats even that guy:
    When you want to know something about someone important (your call) roll + hot.
    10+ Ask 3 questions.
    7-9: Ask 1.
    On a miss ask one anywaybut they hear about your interest in them.

    •How are they doing? what's up with them?
    •Who do they knowlike and/or trust?
    •How could I get to to them physically or emotionally?
    • What or who do they love the best?
    •When next should I expect to see them?
    ```"""
    return msg	
def justgivemeamotive(messageString):
    msg = """```Just give me a motive:
    Name somebody who might conceivably eat drink or otherwise ingest something you've touched. If its an NPC roll+hard or roll+HX for PC.
    10+ They do and suffer 4-harm (ap) in the next 24 hours.
    7-9: They do and suffer 2-harm (ap).
    On a miss some several people of the MC's choice maybe including your guy maybe not get it and all suffer 3-harm (ap).
    ```"""
    return msg

def childthing(messageString):
    msg="""```
    .mercurial
    .sniffingtheair
    .mothersheartbeat
    .feral
    .ferocious
    ```"""

def mercurial (messageString):
    msg = """```
    Mercurial: whenever you want, change any or all of your looks. Those who know you can still recognize you, but only if they look closely.
    ```"""
    return msg
def sniffingtheair(messageString):
    msg = """```
    Sniffing the air: when you read a situation, ask 1 of these questions, in addition to the other questions you ask:
    • Who here is most afraid?
    • Who here is keeping secrets from the rest?
    • How close are the wolves?
    • What or who is the source of the most pain or fear here?
    • Who here would do what I ask?
    ```"""
    return msg
def mothersheartbeat(messageString):
    msg = """```
    The mother’s heartbeat: when you withdraw into the world’s psychic maelstrom, roll+weird. On a 10+, choose 2. On a 7–9, choose 1. You emerge again, about an hour later, and…
    • …Meanwhile, you can still watch and hear what’s happening where you were.
    • …You can re-emerge in a different place altogether.
    • …You are healed of all harm.
    • …You can bring someone in and out with you.

    On a miss, you are in the dark and warm, listening to the mother’s heartbeat, and many hours pass.
    ```"""
    return msg
def feral(messageString):
    msg = """```
    Feral: at the beginning of the session, you can choose to spend 0-barter for the equivalent of a 1-barter lifestyle. You can survive happily on whatever you can find.
    ```"""
    return msg
def ferocious(messageString):
    msg = """```
    Ferocious, snarling, shrieking, biting, and quite possibly rabid: when you go aggro on someone, roll+weird instead of roll+hard.
    ```"""
    return msg


##################
## Combat Moves ##
##################

def combat(messageString):
    msg = """```
    .harm  - When you suffer harm, roll+harm suffered (after armor, if you’re wearing any). 
    .readasitch - When you read a charged situation, roll+cool.
    .firstaid - When you treat someone’s wounds using appropriate medical equipment, roll +sharp,
    .seizebtforce -  When you try to seize something by force, or to secure your hold on something, roll+hard.
    .surpriseattack - When you attack someone unprepared, unsuspecting, or helpless, roll+hard.
    .coverfire - When you want to lay down lots fire or provide cover fire roll+cool 
    .shootsomeone - When you want to shoot someone roll + hard:
    .hitsomeone - When you want to hit someone roll + hard:
    .setanambush - When you want to set an ambush for someone, Describe your ambush, and assign allies as fiction dictates. roll + sharp.
    ```"""
    return msg

	#harm
def harm(messageString):
    msg = """```
    When you suffer harm, roll+harm suffered (after armor, if you’re wearing any). 
	On a 10+, the MC can choose 1:
	• You’re out of action: unconscious, trapped, incoherent or panicked.
    • It’s worse than it seemed. Take an additional 1-harm.
    • Choose 2 from the 7–9 list below.
    On a 7–9, the MC can choose 1:
    • You lose your footing.
    • You lose your grip on whatever you’re holding• You lose track of someone or something you’re attending to.
    • You miss noticing something important.
    On a miss, the MC can nevertheless choose something from the 7–9 list above. If she does, though, it’s instead of some of the harm you’re suffering, so you take -1harm. the suffering harm move adds a wrinkle, a little
    ```"""	
    return msg

    #read a sitch.
def readasitch(messageString):
    msg = """```
    READ A SITCH
    When you read a charged situation, roll+cool.
    On a hit, you can ask the MC questions. Whenever you act on one of the MC’s answers, take +1.
    On a 10+, ask 3
    On a 7–9, ask 1:
    • where’s my best escape route / way in / way past?
    • which enemy is most vulnerable to me?
    • which enemy is the biggest threat?
    • what should I be on the lookout for?
    • what’s my enemy’s true position?
    • who’s in control here?
    ```"""
    return msg

def seizebyforce (messageString):
    msg = """```
    When you try to seize something by force, or to secure your hold on something, roll+hard. 
    On a hit, choose options. 
    10+, choose 3. 
    On a 7–9, choose 2:
    • you take definite hold of it
    • you suffer little harm
    • you inflict terrible harm
    • you impress, dismay or frighten your enemy```"""
    return msg

def firstaid(messageString):
    msg ="""``` 
    When you treat someone’s wounds using appropriate medical equipment, roll +sharp .
    10+: if their Harm Clock is at 2100 or less, reduce their harm by two segments.
    If their Harm Clock is at more than 2100, reduce their harm by one segment
    7-9: reduce their harm by one segment. If their Harm Clock is still at more than 2100, they take -1 ongoing until they receive proper medical attention
    ```"""
    return msg

def supriseattack(messageString):
    msg = """```
    When you attack someone unprepared, unsuspecting, or helpless, roll+hard.
    10+, Inflict full harm as established.
    7–9, You don't hit quite as hard, or stumble a little, inflict partial harm (as established by fiction)
    In either case, if they can and do choose to fight back, now you’re doing battle them.
    On a miss, Jokes on you, they were ready, the MC will make a move.
    ```"""
    return msg

def coverfire(messageString):
    msg ="""```
    When you want to laydown fire or provide cover fire roll+cool 
	10+, choose 3.
	7–9,  choose 1.
        • People are focused on you, your allies may subtley move around.
        • You are able to prevent or reduce someone from harm.
		• You supply  surpressing fire, pick an ally, they get +1 forward in this situation 
        • You supply surpressing fire, restricting someones (your pick), actions as established by fiction. (pc takes -1 forward)
		• You manage to shot somebody in the process (-1 harm (min 1))
    On a miss pick 1:
        • You accidently hurt an ally in the process. 
        • Your guns jammed up, and  its out of action for now. 
        • You take harm before managing to shoot.
        • You manage to provide cover (pick 1 from the hit list) but something happens (The MC will make a move)
    ```"""
    return msg

def shootsomeone(messageString):
    msg ="""```
    When you want to shoot someone roll + hard:
    10+: You manage to shoot them no problem inflict harm as established and pick 1:
         • You manage to shoot them in a vital spot, +2 harm.
         • You manage to damage their weapon or armor, making them deal less damage or take more harm in future.
         • You manage to wound/cripple them, making them have a harder time to move (+1 harm when they move ongoing.)
         • You manage to shoot accuratly and ignore armor for dealing damage (if AP round +3 damage)
    7-9: Pick 1. 
        • You manage to shoot them, but get hurt in the process.
        • You manage to shoot them, but an ally gets hurt in the process
        • You miss, but luckliy they miss too.
        • You manage to shoot them but miss something in the process (the MC makes a move)
    on a miss pick 1.
        • You're a bad aim, but an easy target and take harm as established.
        • You manage to shot them, sadly you shoot an ally in the process (+1 harm to an ally)
        • You shot something, not them, but something. The MC will make a move.
        • You manage to shot them, but something gets damaged in the process (MC picks)
    ```"""
    return msg

def hitsomeone(messageString):
    msg ="""```
    When you want to hit somoene, either with fist or a weapon roll+hard.
    10+ You manage to inflict harm as established +pick 1.
        • You hit them in the head, and they are knocked out or +1 harm if they have a helmet or something.
        • You manage to get a good hit in (+2 harm)
        • You manage to knock something out of their hands or possession.
    7-9: Pick 1:
        • You manage to hit them, but get hurt in the process (take harm as established)
        • You manage to hit them, but something happens to your weapon in the process (the mc will make a move)
        • You manage to hit them, but it was pretty weak (-2 harm (min 1))
    On a miss pick 1:
        • You get hit first, and hard take harm as established (roll harm move) and then land your hit if you're still able.
        • You miss them, but they don't miss you, take harm as established.
        • You manage to get a weak hit on them (half round down) but break something in the process (the mc will make a move)
        • You manage to hit something, not them, but something. (The mc will make a move)
    ```"""
    return msg 

def setanambush(messageString):
    msg = """```
    When you want to set an ambush for someone, Describe your ambush, and assign allies as fiction dictates. roll + sharp.
    10+ : All allies acting according to your ambush take +1 forward in this situation. also Pick 3.
    7-9: Pick 1.
        • Your target is completely unaware of this ambush (unware they are walking into it).
        • Your target is walking right into your trap/location of your choice(otherwise will be in the ambush but maybe not ideal spot).
		• You target isn't sharp or cool enough to react effectively. (PC -2 forward or as fiction dictates)
		• Others don't notice you setting/talking/preparing your ambush.
        • Anyone acting in setting up or carrying out actions while this amush takes place has +1 forward.
        • Anyone being used as bait for this ambush, is safe (+2 armor while being the bait)
        • Your ambush is well crafted (+2 harm when triggered.)
    On a miss pick 1:
        • Your ambush is very obvious, your target might not fall for it(MC dictacts fiction)
        • Everyone partaking is very nervious about this , -1 forward.
        • Your target is very sharp or cool and ready to deal with this situation (as fiction dictates or +2 forward if a PC)
        • Your target isn't aware of the ambush but everyone else is. 
        • Your ambush seems fine. The MC will make a move.
        ```"""
    return msg

    



############
## Social ##
############

def social(messageString):
    msg = """```
    .fasttalk - When you try to convince someone to do what you want with promises, lies or bluster, roll+Hot.
    .barter - When you're looking to buy something roll + sharp.
    .gounderknife - When you  want to and are able to have a new implant installed, roll + barter spent,
    .playhardball - When you get in someone’s face threatening violence and you intend to carry through, roll+hard.
    .workajob - When you negotiate the terms of a job, roll + hot.
    ```"""
    return msg

def barter(messageString):
    msg = """```
    When you go into a holding’s bustling market, looking for some particular thing to buy, and it’s not obvious whether you should be able to just like go buy one like that, roll + sharp 
	On a 10+, yes, you can just go can buy it like that.
	On a 7–9, the MC chooses one of the following:
	• it costs 1-barter more than you’d expect
	• it’s available, but only if you meet with a guy who knows a guy
	• damn, I had one, I just sold it to this guy named Rolfball, maybe you can go get it off him?
	• sorry, I don’t have that, but maybe this will do instead?
    ```"""
    return msg

def fasttalk (messageString):
    msg = """```
    When you try to convince someone to do what you want with promises, lies or bluster, roll+hot.
	10+: NPCs do what you want. PCs choose whether to do it or not. If they do, they mark experience. If they don’t, they must act under pressure to go against your stated wishes.
	7-9: NPCs do it, but someone will find out: the MC will advance the appropriate Countdown Clock. For PCs choose one:
		• If they do what you want, they mark experience
		• If they don’t do it, they must act under pressure to go against your stated wishes
	Then its up to them.
    ```"""
    return msg

def gounderknife(messageString):
    msg = """```
    When you  want to and are able to have a new implant iinstalled, roll + barter spent (max +2).
	10+: the operation was a complete success.
	7-9: the implant was a little too makeshift, choose one: +unreliable, +substandard, +hardware decay, +damaging, +reqires abnormal power supply.
	6-: there have been... complications
    ```"""
    return msg

def readaperson(messageString):
    msg ="""```
    When you read a person in a charged interaction, roll+hot. 
    10+, hold 3. 
    On a 7–9, hold 1.
    • is your character telling the truth?
    • what’s your character really feeling?
    • what does your character intend to do?
    • what does your character wish I’d do?
    • how could I get your character to __?
    ```"""
    return msg

def playhardball(messageString):
    msg ="""```
    When you get in someone’s face threatening violence and you intend to carry through, roll+hard.
    10+: NPCs do what you want. PCs choose: do what you want, or suffer the established consequences
    7–9: For NPCs, the MC chooses 1:
    • they attempt to remove you as a threat, but not before suffering the established consequences
    • they do it, but they want payback. Add them as a Threat
    • they do it, but someone finds out.
    PCs choose: do what you want, or suffer the established consequences. They gain +1 forward to act against you.
    ```"""
    return msg

def workajob(messageString):
    msg = """```
    When you negotiate the terms of a job, roll + hot.
    10+: choose 3 from the list below
    7-9: choose 1 from the list below
    • the employer provides useful information [intel]
    • the employer provides useful assets [gear]
    • the job pays well
    • the meeting doesn’t attract attention
    • The employer is convinved a larger team is needed, and will cover an additional person (if you can find someone)
    • The employer will help keep your asserts safe while on the job.
    • If possible the employer will shelter your mind/brain from the psychic malestorm
    • Your reputation has increased (reduce relevent clock)
    ```"""
    return msg


#################
## Situational ##
#################
def situation(messageString):
    msg ="""```
    .actunderpressure - When you race against the clock, act while in danger or act to avoid danger, roll+Cool.
    .investigate -  When you closely study a place, or situation, roll + Sharp.
    .doiknowthings - When you race against the clock, act while in danger or act to avoid danger, roll+Cool.

    ```"""
    return msg

def investigate(messageString):
    msg = """```
    When you closely study a place, situation, roll + Sharp. 
    10+ ask the MC three questions from the list below.    
    7–9 ask only one. 
    Take +1 forward when acting on the answers.
    • What happened here recently?
    • What is about to happen?
    • What should I be on the lookout for?
    • What here is useful or valuable to me?
    • Who’s really in control here?
    • What here is not what it appears to be?
    ```"""
    return msg

def doiknowthings(messageString):
    msg ="""```
    When you consult your accumulated knowledge about something, roll + sharp. 
    10+ the MC will tell you something interesting and useful about the subject relevant to your situation. 
    On a 7–9 the MC will only tell you something interesting it’s on you to make it useful. 
    The MC might ask you “How do you know this?” Tell them the truth, now.
    ```"""
    return msg

def actunderpressure(messageString):
    msg = """```
    When you race against the clock, act while in danger or act to avoid danger, roll+Cool.
	10+: you do it, no problem
	7-9: you stumble, hesitate, or flinch: the MC will offer you a worse outcome, hard bargain, or ugly choice
    6-: Looks like you are fucked, the MC will make a move.
    ```"""
    return msg


def weirdapocstuff(messateString):
    msg ="""```
    .openyourbrain - When you open your brain to the world’s psychic maelstrom
    .psyharm - When you take psychic harm
    .augury - When you use your followers or your workspace for augury, roll+weird.
    ```"""
    return msg

def openyourbrain(messageString):
    msg = """```OPEN YOUR BRAIN:
		When you open your brain to the world’s psychic maelstrom,
		roll+weird.
		On a hit, the MC will tell you something new and interesting about the current situation, and might ask you a question or two; answer them.
		On a 10+, the MC will give you good detail.
		On a 7–9, the MC will give you an impression.
		If you already know all there is to know, the MC will tell you that.
		```"""
    return msg

#Ψ-harm
def psyharm (messageString):
    msg = """```
    When you suffer Ψ-harm, roll+Ψ-harm suffered (typically, roll+1).
    On a 10+, the MC can choose 1:
    • You’re out of action: unconscious, trapped, incoherent or panicked.
    • You’re out of your own control. You come to yourself again a few seconds later, having done I-don’t-know-what
    • Choose 2 from the 7–9 list below.
    On a 7–9, the MC can choose 1:
    • You lose your footing
    • You lose your grip on whatever you’re holding.
    • You lose track of someone or something you’re attending to.
    • You miss noticing something important.
    • You take a single concrete action of the MC’s choosing.
    On a miss, you keep it together and overcome the -harm with no effect.```"""
    return msg


def augury (messageString):
    msg = """```
    When you use your followers or your workspace for augury, roll+weird.\n
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
    return msg


def costofliving(messageString):

    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1+dice2
    msg = """```When you are unable or refuse to get/use rations and resources to maintain a your lifestyle (ie living),\nroll + nothing (Starvation doesn't care if you're hard or sharp, or anything really).
    """ 
    if total >=10:
        msg +="\nlucky this time, you rolled a " +str(total)+"""

        Pick 1.
        • You've managed to fight of dehydration and stavation, but not for much longer, if you don't find both food and water very soon, This becomes a miss with 3 failure options instead of 2. (.didntgetfood)
        • You've managed to fight of starvation for now, however you are dying of first, take 2 harm(internal).
        • You've somehow managed to not die of dehydration,  but you are starving, take -2 on forward till you get some food.
        • Somebody has offered you basic supplies to survive this time, but it will require you to do something for them. [Only if fiction allows.]
        ```"""
    elif total >=7 and total <10:
        msg+= "\nEh, it'll do, you rolled a "+str(total)
        msg+="""
        
        Pick 1.
        • You've partially managed to fight of hunger and thirst, [take 1 harm, and -1] on going, and if you don't find something soon, this becomes a miss with 3 options instead of 2.
        • Your thirst has overcome your need to eat, take -3 harm, and -1 ongoig till you find food.
        • Your hunger has overcome your need to drink, take -3 forward and -1 harm.
        • Someone has offered you basic supplies to survive in exchange for something or service right now (if fiction allows)
        ```"""
    else:
        msg += "\nFuck, only a " +str(total)+"""
        Pick 2:
        • Your stomach is trying to eat itself take -2 harm and -2 forward.
        • Lack of water in your system, is giving your organs a hard time, -4 harm, but its not serious damage.
        • Your body has no energy, take -4 on going
        • You're in a weakend state, and going a little delusional, you gain +2 to weird, but all other stats have -1 till you get food and water.
        • You've done some serious damage to yourself from lack of water and food, -1 harm, but requires serious medical attention to fix.
        • This has taken a toll on your body, pick a stat and take -1 permanently or until you can find a good vailid reason to restore the damage.
        • You lose all senses and try to cannibalise the closest person to you(or yourself if no one around). 
        • Your body is kind of shutting down, weak hits are are now 10 (11, or 12 if already 10.) until you find food and water. 
    ```"""
    msg = msg.replace("\t","")
    msg = msg.replace("\t","")
    msg = msg.replace("        ","")

    return msg

def didntgetfood(messageString):
    msg = """```
    Looks like you failed to get food and/or water, and now it seems like you're really fucked. Pick 3.

    • Your stomach is trying to eat itself take -2 harm and -2 forward.
    • Lack of water in your system, is giving your organs a hard time, -4 harm, but its not serious damage.
    • Your body has no energy, take -4 on going
    • You're in a weakend state, and going a little delusional, you gain +2 to weird, but all other stats have -1 till you get food and water.
    • You've done some serious damage to yourself from lack of water and food, -1 harm, but requires serious medical attention to fix.
    • This has taken a toll on your body, pick a stat and take -1 permanently or until you can find a good vailid reason to restore the damage.
    • You lose all senses and try to cannibalise the closest person to you(or yourself if no one around). 
    • Your body is kind of shutting down, weak hits are are now 10 (11, or 12 if already 10.) until you find food and water. 
    ```"""
    msg = msg.replace("\t", "")
    return msg
