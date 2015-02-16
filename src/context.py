"""

Contains generic data for game context. 

To do: Monster / Map / Old One / Curse data

"""
from player import Player
from worldmap import Worldmap
from constants import *

from random import randint

class Context:

    def __init__(self, numplayers, playerchars):
        """
        The number of players is passed in, along with the 
        name and class of each character in a list.
        """
        self.state = STARTUP

        # Set how many players are playing
        self.numplayers = numplayers
        self.players = []

        # For each player, create a player object to contain player data
        for x in xrange(self.numplayers):
            player_name, player_class = playerchars[x] 
            self.players.append(Player(player_name, player_class))

        # Create map object, which automatically builds map from world data
        self.world = Worldmap()
                
        # Set player starting position in map object from player object data
        for player in self.players:
            player_location = player.location 
            player_name = player.name
            self.world.locations[player_location].append(player_name)

    def run_game(self):
        """
        Main game loop, will contain state machine
        """

        while self.state != ENDING:
            pass

    def move_player(self, player, newloc):
        """
        Move player to nearby node. Ideally called after
        nearnode returns and graphics call is made.
        """
        self.world.update_player(player, self.players[player].location, newloc)
        self.players[player].location = newloc

    def roll(self):
        return randint(1, 6)
