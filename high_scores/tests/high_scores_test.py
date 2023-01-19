import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    scores = [12, 5, 2, 7, 5, 10, 15]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(15, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(15, personal_best(self.scores))

    # Test top three from list of scores
    def test_top_three(self):
        self.assertEqual((15, 12, 10), top_three(self.scores))


    # Test ordered from highest to lowest
    def test_high_to_low(self):
        self.assertEqual([15, 12, 10, 7, 5, 5, 2], high_to_low(self.scores))
        
        
    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
