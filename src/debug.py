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
print 'Context contains players %s' % context.players.keys()

print '\n######## Testing Dijkstras ########\n'

try:
    print 'Testing DiGiTALQU33F - Roll 1...'
    result = ShortestPath.calculate(context.players['DiGiTALQU33F'].location, context.world.links, 1)
    print 'Test results: %s\n' % result

    print 'Testing DiGiTALQU33F - Roll 2...'
    result = ShortestPath.calculate(context.players['DiGiTALQU33F'].location, context.world.links, 2)
    print 'Test results: %s\n' % result

    print 'Testing DiGiTALQU33F - Roll 6...'
    result = ShortestPath.calculate(context.players['DiGiTALQU33F'].location, context.world.links, 6)
    print 'Test results: %s\n' % result

    print 'Testing iRONVAGiNA - Roll 1...'
    result = ShortestPath.calculate(context.players['iRONVAGiNA'].location, context.world.links, 1)
    print 'Test results: %s\n' % result

    print 'Testing iRONVAGiNA - Roll 2...'
    result = ShortestPath.calculate(context.players['iRONVAGiNA'].location, context.world.links, 2)
    print 'Test results: %s\n' % result
    
    print 'Testing iRONVAGiNA - Roll 6...'
    result = ShortestPath.calculate(context.players['iRONVAGiNA'].location, context.world.links, 6)
    print 'Test results: %s\n' % result

except Exception as e:
    print 'Failed shortest path test:\n%s: %s' % (type(e).__name__, e)

print '\n######################## END OF TEST ########################\n'

crap = raw_input()
