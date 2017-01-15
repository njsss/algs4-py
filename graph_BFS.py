from collections import defaultdict, deque

class BreadthFirstPaths(object):
    nV = 0
    nE = 0
    marked = {} # Is a shortest path to this vertex known?
    edgeTo = {} # last vertex on known path to this vertex


    def constructGraph(self, edges):
        # construct graph
        g = defaultdict(list)
        for e in edges:
            (v, w) = e
            g[v].append(w)
            g[w].append(v)

        # reverse -> stack like
        for k in g:
            g[k].reverse() # inline reverse

        print ("Constucted Graph:")
        for k in g:
            print (g[k])
        print ("-----------------")

        return g

    def loadTextData(self, fn):
        with open(fn) as f:
            self.nV = f.readline().split('\n')[0]
            self.nE = f.readline().split('\n')[0]
            lines = f.readlines()

        edges = []
        for l in lines:
            (v, w) = l.rstrip().split(' ')
            edges.append((int(v), int(w)))

        # print (edges)
        return edges

    def breadthFirstPaths(self, fn, s):
        edges = self.loadTextData(fn)
        g = self.constructGraph(edges)
        self.bfs(g, s)

        self.printPathToSource(g, s)

    def bfs(self, g, s):
        queue = deque()

        self.marked[s] = True
        queue.append(s)
        while (queue):
            v = queue.popleft()
            for w in g[v]:
                if (w not in self.marked) or (not self.marked[w]):
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    queue.append(w)

        return

    def hasPathTo(self, v):
        if (self.marked[v]):
            return self.marked[v]

        return False

    def pathTo(self, s, v):
        if (not self.hasPathTo(v)):
            return None

        path = []
        x = v
        while (x != s):
            path.append(x)
            x = self.edgeTo[x]

        # add source path to list
        path.append(s)

        return path

    def printPathToSource(self, g, s):
        print ("Path to Source: %s" % str(s))
        for v in g:
            print (str(s) + " to " + str(v) + ": ", end='') #end with ''
            if (self.hasPathTo(v)):
                path = self.pathTo(s, v)
                for x in range(len(path)):
                    p = path.pop()
                    if (p == s):
                        print (str(p),end="")
                    else:
                        print ("-" + str(p),end="")
                print ("")



if __name__ == '__main__':
    fn = "../algs4-data/tinyCG.txt"
    BreadthFirstPaths().breadthFirstPaths(fn,0)
