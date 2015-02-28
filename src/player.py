# Models generic player statistics REVIEW PYTHONIC SETTERS/GETTERS
from constants import *

class Player:

    def __init__(self, player_name, character):
        # Initialize player data
        self.name = player_name
        self.character = character
        self.stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.location = 'Unknown'

        if character == 'test_guy_1':
            self.stats[STAMINA] = 5
            self.stats[SANITY] = 5
            self.stats[FIGHT] = 3
            self.stats[LORE] = 5
            self.stats[WILL] = 4
            self.stats[SPEED] = 3
            self.stats[SNEAK] = 2
            self.stats[LUCK] = 3
            self.stats[FOCUS] = 2
            self.stats[CURSE] = 1
            self.location = 'loc1'
        
        elif character == 'test_guy_2':
            self.stats[STAMINA] = 10
            self.stats[SANITY] = 2
            self.stats[FIGHT] = 6
            self.stats[LORE] = 2
            self.stats[WILL] = 5
            self.stats[SPEED] = 4
            self.stats[SNEAK] = 1
            self.stats[LUCK] = 2
            self.stats[FOCUS] = 2
            self.stats[CURSE] = 0
            self.location = 'loc5'

