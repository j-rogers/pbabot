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

playbooks = {}
matrix = []

data = {
    'basic': basic,
    'playbooks': playbooks,
    'matrix': matrix
}

with open('sprawl_data.pickle', 'wb') as file:
    file.write(pickle.dumps(data))