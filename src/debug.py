import pygame

from player import Player
from context import Context
from constants import *
from worldmap import ShortestPath

numplayers = 2
testplayers = []

testplayers.append(('DiGiTALQU33F', 'test_guy_1'))
testplayers.append(('iRONVAGiNA', 'test_guy_2'))

context = Context(numplayers, testplayers)

print '\n#################### STARTING BASIC TEST ####################'

print '\n############ Locations ############\n'
for loc in context.world.locations:
    print 'Location: %s Players: %s' % (loc, context.world.locations[loc])

print '\n############# Players #############\n'

player_list = []

for player in context.players:
    player_list.append(player.name)

print 'Context contains players %s' % player_list

print '\n######## Testing Dijkstras ########\n'

try:
    print 'Testing DiGiTALQU33F - Roll 1...'
    result = ShortestPath.calculate(context.players[0].location, context.world.links, 1)
    print 'Test results: %s\n' % result

    print 'Testing DiGiTALQU33F - Roll 2...'
    result = ShortestPath.calculate(context.players[0].location, context.world.links, 2)
    print 'Test results: %s\n' % result

    print 'Testing DiGiTALQU33F - Roll 6...'
    result = ShortestPath.calculate(context.players[0].location, context.world.links, 6)
    print 'Test results: %s\n' % result

    print 'Testing iRONVAGiNA - Roll 1...'
    result = ShortestPath.calculate(context.players[1].location, context.world.links, 1)
    print 'Test results: %s\n' % result

    print 'Testing iRONVAGiNA - Roll 2...'
    result = ShortestPath.calculate(context.players[1].location, context.world.links, 2)
    print 'Test results: %s\n' % result
    
    print 'Testing iRONVAGiNA - Roll 6...'
    result = ShortestPath.calculate(context.players[1].location, context.world.links, 6)
    print 'Test results: %s\n' % result

except Exception as e:
    print 'Failed shortest path test:\n%s: %s' % (type(e).__name__, e)

    
print '\n######## Testing SUCCESS/COMBAT ########\n'

print 'Testing dice success iRONVAGiNA, CURSE = %s\n' % context.players[1].stats[9]
result = context.success(1)
print ' Test results: %s\n' % result


print 'Testing dice success diGiTALQU33F, CURSE = %s\n' % context.players[0].stats[9]
result = context.success(0)
print ' Test results: %s\n' % result

print 'Testing skillcheck logic with 5 dices, difficulty 2 for iRONVAGiNA'
result = context.skillcheck(0, 2, 1)
print 'Test Results: %s\n' % result
print '\n######################## END OF TEST ########################\n'