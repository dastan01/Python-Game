import unittest
from frogger import Game


class TestFrogger(unittest.TestCase):

    def test_class11(self):
        new_game = Game(1, 1)

        self.assertEqual(new_game.level, 1)
        self.assertEqual(new_game.speed, 1)
        self.assertEqual(new_game.time, 30)

        print("Tests Passed")


if __name__ == '__main__':
    unittest.main()
