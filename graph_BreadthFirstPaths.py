# Breadth-first search to find paths in a graph
from collections import deque
from graph import Graph

class BreadthFirstPaths(object):
    marked = {} # Is a shortest path to this vertex known?
    edgeTo = {} # last vertex on known path to this vertex
    s = ''      # source

    def __init__(self, g, s):
        self.s = s
        self.bfs(g, s)

    def bfs(self, g, s):
        queue = deque()

        self.marked[s] = True
        queue.append(s)
        while (queue):
            v = queue.popleft()
            for w in g.adj[v]:
                if (w not in self.marked) or (not self.marked[w]):
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    queue.append(w)

    def hasPathTo(self, v):
        if (self.marked[v]):
            return self.marked[v]

        return False

    def pathTo(self, v):
        if (not self.hasPathTo(v)):
            return None

        path = []
        x = v
        while (x != self.s):
            path.append(x)
            x = self.edgeTo[x]

        # add source path to list
        path.append(self.s)

        return path

    def printPathToSource(self, g):
        print ("Path to source: %s" % str(self.s))
        for v in g.adj:
            print (str(self.s) + " to " + str(v) + ": ", end='')
            if (self.hasPathTo(v)):
                path = self.pathTo(v)
                for x in range(len(path)):
                    p = path.pop()  # source appended at the end
                    if (p == self.s):
                        print (str(p), end="")
                    else:
                        print ("-" + str(p), end="")
                print ("")


if __name__ == '__main__':
    fn = "../algs4-data/tinyCG.txt"
    g = Graph.fromFile(fn)
    g.printGraph()
    bfspath = BreadthFirstPaths(g, 0)
    bfspath.printPathToSource(g)
