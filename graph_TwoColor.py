# Two-colorability: Is the graph bipartite?
from graph import Graph

class TwoColor(object):
    marked = {}
    color = {}
    isTwoColorable = True

    def __init__(self, g):
        head = True
        for s in g.adj:
            if (head):
                self.color[s] = False
                head = False
            if (s not in self.marked) or (not self.marked[s]):
                self.dfs(g, s)

    def dfs(self, g, v):
        self.marked[v] = True
        # not connected graph
        if (v not in self.color):
            self.isTwoColorable = False
            return
        for w in g.adj[v]:
            if (w not in self.marked) or (not self.marked[w]):
                self.color[w] = not self.color[v]
                self.dfs(g, w)
            elif (self.color[w] == self.color[v]):
                self.isTwoColorable = False


if __name__ == '__main__':
    fn = "../algs4-data/tinyG.txt"
    g = Graph.fromFile(fn)
    g.printGraph()
    color = TwoColor(g)
    print ("Two-Colorable: {0}".format(color.isTwoColorable))
