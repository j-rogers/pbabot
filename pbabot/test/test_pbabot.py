import unittest

from pbabot.pbabot import PBABot, Clock, Contact


class PBABotTest(unittest.TestCase):
    def setUp(self):
        self.bot = PBABot(datafile='pbabot/test/test_data/test_data.pickle', personaldata='pbabot/test/test_data/personal')

        self.bot.clocks = [
            Clock('Kind of good guys', '1200'),
            Clock('Cult', '1500'),
            Clock('A homeless man', '1800'),
            Clock('Pet store', '2100'),
            Clock('Police', '2200'),
            Clock('MC', '2300'),
            Clock('Evil bad guys', '0000')

        ]

        self.bot.contacts = [
            Contact('James', 'Cool dude'),
            Contact('Jeremey', 'Not so cool dude'),
            Contact('Jeff Jefferson', 'Really cool dude')
        ]

    def test_printclocks(self):
        clocks = """Kind of good guys: □□□□ □□□□ □□□□ □ □ □
Cult: ■■■■ □□□□ □□□□ □ □ □
A homeless man: ■■■■ ■■■■ □□□□ □ □ □
Pet store: ■■■■ ■■■■ ■■■■ □ □ □
Police: ■■■■ ■■■■ ■■■■ ■ □ □
MC: ■■■■ ■■■■ ■■■■ ■ ■ □
Evil bad guys: ■■■■ ■■■■ ■■■■ ■ ■ ■
"""
        self.assertEqual(clocks, self.bot.printclocks(''))

    def test_printcontacts(self):
        contacts = """James: Cool dude
Jeremey: Not so cool dude
Jeff Jefferson: Really cool dude
"""
        self.assertEqual(contacts, self.bot.printcontacts(''))

    def test_addclock(self):
        clocks = """Kind of good guys: □□□□ □□□□ □□□□ □ □ □
Cult: ■■■■ □□□□ □□□□ □ □ □
A homeless man: ■■■■ ■■■■ □□□□ □ □ □
Pet store: ■■■■ ■■■■ ■■■■ □ □ □
Police: ■■■■ ■■■■ ■■■■ ■ □ □
MC: ■■■■ ■■■■ ■■■■ ■ ■ □
Evil bad guys: ■■■■ ■■■■ ■■■■ ■ ■ ■
Yes man: □□□□ □□□□ □□□□ □ □ □
"""

        self.bot.addclock('Yes man')
        self.assertEqual(clocks, self.bot.printclocks(''))

    def test_deleteclock(self):
        clocks = """Kind of good guys: □□□□ □□□□ □□□□ □ □ □
Cult: ■■■■ □□□□ □□□□ □ □ □
A homeless man: ■■■■ ■■■■ □□□□ □ □ □
Pet store: ■■■■ ■■■■ ■■■■ □ □ □
MC: ■■■■ ■■■■ ■■■■ ■ ■ □
Evil bad guys: ■■■■ ■■■■ ■■■■ ■ ■ ■
"""
        self.bot.deleteclock('Police')
        self.assertEqual(clocks, self.bot.printclocks(''))

    def test_increaseclock(self):
        clocks = """Kind of good guys: ■■■■ ■■■■ □□□□ □ □ □
Cult: ■■■■ □□□□ □□□□ □ □ □
A homeless man: ■■■■ ■■■■ □□□□ □ □ □
Pet store: ■■■■ ■■■■ ■■■■ □ □ □
Police: ■■■■ ■■■■ ■■■■ ■ □ □
MC: ■■■■ ■■■■ ■■■■ ■ ■ □
Evil bad guys: ■■■■ ■■■■ ■■■■ ■ ■ ■
"""
        self.bot.increaseclock('Kind of good guys')
        self.bot.increaseclock('Kind of good guys')
        self.bot.increaseclock('Evil bad guys')
        self.assertEqual(clocks, self.bot.printclocks(''))

    def test_decreaseclock(self):
        clocks = """Kind of good guys: □□□□ □□□□ □□□□ □ □ □
Cult: ■■■■ □□□□ □□□□ □ □ □
A homeless man: ■■■■ ■■■■ □□□□ □ □ □
Pet store: ■■■■ ■■■■ ■■■■ □ □ □
Police: ■■■■ ■■■■ ■■■■ ■ □ □
MC: ■■■■ ■■■■ ■■■■ □ □ □
Evil bad guys: ■■■■ ■■■■ ■■■■ ■ ■ ■
"""
        self.bot.decreaseclock('MC')
        self.bot.decreaseclock('MC')
        self.bot.decreaseclock('Kind of good guys')
        self.assertEqual(clocks, self.bot.printclocks(''))

    def test_addcontact(self):
        contacts = """James: Cool dude
Jeremey: Not so cool dude
Jeff Jefferson: Really cool dude
Stacy: word friend
Ben Ben: ben 10
"""
        self.bot.addcontact('Stacy word friend')
        self.bot.addcontact('"Ben Ben" ben 10')
        self.assertEqual(contacts, self.bot.printcontacts(''))

    def test_deletecontact(self):
        contacts = """James: Cool dude
Jeff Jefferson: Really cool dude
"""
        self.bot.deletecontact('Jeremey')
        self.assertEqual(contacts, self.bot.printcontacts(''))

    def test_rip(self):
        rip = """Big: Got stabbed
Small: Crashed his car"""
        self.assertEqual(rip, self.bot.rip('dave'))

        rip = """dave: Big, Small, 
jeff: Boss,"""
        self.assertEqual(rip, self.bot.rip(''))

    def test_remember(self):
        remember = 'Boss got beat up by Small'
        self.assertEqual(remember, self.bot.remember('2'))


if __name__ == '__main__':
    unittest.main()
