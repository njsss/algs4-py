# connected component
from graph import Graph

class CC(object):
    marked = {} # Is a shortest path to this vertex known?
    cid = {}    # component index
    count = 0    # count of connected component

    def __init__(self, g):
        for v in g.adj:
            if (v not in self.marked) or (not self.marked[v]):
                self.dfs(g, v)
                self.count += 1

    def dfs(self, g, v):
        self.marked[v] = True
        self.cid[v] = self.count
        for w in g.adj[v]:
            if (w not in self.marked) or (not self.marked[v]):
                self.dfs(g, w)

    def connected(self, v, w):
        return (self.cid[v] == self.cid[w])


if __name__ == '__main__':
    fn = "../algs4-data/tinyG.txt"
    g = Graph.fromFile(fn)
    g.printGraph()
    cc = CC(g)

    print ("%d components" % cc.count)
    components = [[] for x in range(cc.count)] # init 2d-empty-list
    for v in g.adj:
        components[cc.cid[v]].append(v)
    for c in components:
        c.reverse()
        print (c)
