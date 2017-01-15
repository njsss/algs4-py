# Symbol graphs:
# Vertex names are strings
# A specified delimiter separates vertex names
# Each line reprents a set of edges,
# The number of vertices V and the number of edges E
# are both implicitly defined.
from graph import Graph

class SymbolGraph(object):
    g = ''
    def __init__(self, fn, sp):
        self.g = Graph()
        with open(fn) as f:
            for line in f:
                l = line.rstrip().split(sp)
                # print (l)
                v = l[0]
                for i in range(1,len(l)):
                    self.g.addEdge(v, l[i])
        # self.g.reverseAdjList()

if __name__ == '__main__':
    fn = "../algs4-data/routes.txt"
    sg = SymbolGraph(fn, ' ')
    s = ''
    while (s != 'quit'):
        s = str(input())
        print (sg.g.adj[s])
        # for v in sg.g.adj[s]:
        #     print (v)
    # sg.g.printGraph()
