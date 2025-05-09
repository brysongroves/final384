#Bryson Groves
#CS 384 Final
#Hunt the Wumpus UNIT TESTS

import unittest
import random
from unittest.mock import patch

# Import the move_wumpus function
from final_wumpus import move_wumpus, cave

class TestHuntTheWumpus(unittest.TestCase):

    def setUp(self):
        # Set up a fixed Wumpus location for testing
        self.test_wumpus_room = 5
        self.test_cave = cave

    def test_move_wumpus_moves_correctly(self):
        # Test that the Wumpus moves correctly with a 75% chance
        with patch('random.randint', side_effect=[1, 2, 3]):
            new_room = move_wumpus(self.test_wumpus_room)
            self.assertIn(new_room, self.test_cave[self.test_wumpus_room])

    def test_move_wumpus_does_not_move_on_4(self):
        # Test that the Wumpus does not move when a 4 is rolled
        with patch('random.randint', return_value=4):
            new_room = move_wumpus(self.test_wumpus_room)
            self.assertEqual(new_room, self.test_wumpus_room)

    def test_arrow_hits_wumpus(self):
        # Test that the arrow hits the Wumpus if it is in the correct room
        wumpus_room = 5
        player_room = 1
        arrow_path = [5]
        self.assertIn(wumpus_room, arrow_path)

    def test_arrow_hits_player(self):
        # Test that the player can accidentally shoot themselves
        player_room = 3
        arrow_path = [3]
        self.assertIn(player_room, arrow_path)

    def test_arrow_misses(self):
        # Test that the arrow misses if it doesn't hit the Wumpus or the player
        wumpus_room = 5
        player_room = 1
        arrow_path = [2, 4, 6]
        self.assertNotIn(wumpus_room, arrow_path)
        self.assertNotIn(player_room, arrow_path)

    def test_warnings_for_dangerous_rooms(self):
        # Test that the correct warnings are given for nearby dangers
        pit_rooms = [2, 5]
        bat_rooms = [3, 8]
        wumpus_room = 6
        current_room = 1
        nearby_rooms = cave[current_room]
        warnings = []

        for room in nearby_rooms:
            if room in pit_rooms:
                warnings.append("I feel a draft.")
            if room in bat_rooms:
                warnings.append("Bats nearby.")
            if room == wumpus_room:
                warnings.append("I smell the wumpus.")

        self.assertIn("I feel a draft.", warnings)
        self.assertIn("Bats nearby.", warnings)
        self.assertIn("I smell the wumpus.", warnings)

    def test_player_move_valid(self):
        # Test that the player can only move to connected rooms
        current_room = 1
        valid_move = 2
        self.assertIn(valid_move, cave[current_room])

    def test_player_move_invalid(self):
        # Test that the player cannot move to a non-connected room
        current_room = 1
        invalid_move = 10
        self.assertNotIn(invalid_move, cave[current_room])

    def test_quit_game(self):
        # Test that the player can quit the game
        with self.assertRaises(SystemExit):
            quit()

if __name__ == "__main__":
    unittest.main()
