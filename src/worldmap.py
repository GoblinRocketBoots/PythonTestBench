from constants import *

class Worldmap:

    # Build world map
    def __init__(self):

        # Links dictionary is used to calculate shortest paths for dice rolls
        self.links = {}

        # Locations stores location specific data
        self.locations = {}

        try:
       	    world_dat = open('../bin/world.dat')

       	except:
       	    # Switch to proper logging later
       	    print 'MISSING WORLD DATA - FATAL ERROR'

       	numlocations = int(world_dat.readline().split()[0])
       	numlinks = int(world_dat.readline().split()[0])

       	for lines in xrange(numlinks):
            firstloc, secondloc = world_dat.readline().split()

            if firstloc not in self.links:
                self.links[firstloc] = {}
                self.locations[firstloc] = []

            self.links[firstloc][secondloc] = 1


class ShortestPath:

    not_visited = {}
    distance = {}
    predecessor = {}
    links = {}
    
    @classmethod
    def dijkstra(self, current_node, current_distance, depth):

        if depth == 0 or not self.not_visited:
            return

        for near in self.links[current_node]:
            if near in self.not_visited:
                if near not in self.distance:
                    self.distance[near] = current_distance + self.links[current_node][near]
                    #predecessor[near] = current_node

                elif self.distance[near] > current_distance + self.links[current_node][near]:
                    self.distance[near] = current_distance + self.links[current_node][near]
                    #predecessor[near] = current_node

        del self.not_visited[current_node]   

        neighboors = self.links[current_node].keys()

        shortest = -1
        next_node = ''

        for node in neighboors:
            if node in self.not_visited:
                if shortest == -1:
                    shortest = self.distance[node] 
                    next_node = node

                elif shortest > self.distance[node]:
                    shortest = self.distance[node]
                    next_node = node
        
        if  next_node != '':
            self.dijkstra(next_node, self.distance[next_node], depth-1)
        
    @classmethod
    def calculate(self, loc, conns, roll):
        self.links = dict(conns)
        self.not_visited = dict(conns)
        self.distance = {}
        #self.predecessor = {}
        
        self.dijkstra(loc, 0, roll)

        return self.distance
