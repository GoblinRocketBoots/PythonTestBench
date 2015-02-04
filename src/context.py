"""

Contains generic data for game context. 

To do: Monster / Map / Old One / Curse data

Notes:
	Should players be stored as name/object pair? 

"""
from player import Player
from worldmap import Worldmap
from constants import *

from random import randint

class Context:

        # Context class variables
	numplayers = -1 
	players = {} 
        world = None

	"""	
	# Old one stats
	_oldone = 'SUPER DUPER SPOOKY'

	# World stats -  placeholder for now
	_curse = 'SPOOKY CURSE'
	"""
	
	def __init__(self, numplayers, playerchars):

                # Set how many players are playing
		self.numplayers = numplayers

                # For each player, create a player object to contain player data
		for x in xrange(self.numplayers):
			self.players[playerchars[x][0]] = Player(playerchars[x][0], playerchars[x][1])

                # Create map object, which automatically builds map from world data
                self.world = Worldmap()
                
                # Set player starting position in map object from player object data
                for playername in self.players:
                    self.world.set_location(self.players[playername], self.players[playername].get_pos())

	# Might not be needed
	def set_old_one(self, placeholder):
		pass

	# Player moving logic
	def move_player(self, placeholder):
		pass

	# Monster moving logic
	def move_monster(self, placeholder):
		pass

	# Might move this function to another file once more utils surface
	def roll(self):
		return randint(1, 6)
