import unittest

from pbabot.games import sprawl

class SprawlTest(unittest.TestCase):
    def setUp(self):
        self.sprawl = sprawl.Sprawl()

    def test_basicmoves(self):
        print(self.sprawl.handle('.assess', ''))