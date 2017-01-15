# Cycle detection: Is a given graph acylic?
from graph import Graph

class Cycle(object):
    marked = {}
    hasCycle = False

    def __init__(self, g):
        for s in g.adj:
            if (s not in self.marked) or (not self.marked[s]):
                self.dfs(g, s, s)

    def dfs(self, g, v, u):
        self.marked[v] = True
        for w in g.adj[v]:
            if (w not in self.marked) or (not self.marked[w]):
                self.dfs(g, w, v)
            elif (w != v):
                self.hasCycle = True


if __name__ == '__main__':
    fn = "../algs4-data/tinyG.txt"
    g = Graph.fromFile(fn)
    g.printGraph()
    cycle = Cycle(g)
    print ("Has cycle: {0}".format(cycle.hasCycle))
