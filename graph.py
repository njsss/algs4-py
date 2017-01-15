from collections import defaultdict

class Graph(object):
    nV = 0    # number of vertices
    nE = 0    # number of edges
    adj = defaultdict(list)    # graph data in adjency list

    def __init__(self, edges=[]):
        """ construct graph"""
        for e in edges:
            (v, w) = e
            self.adj[v].append(w)
            self.adj[w].append(v)

        self.reverseAdjList()

    def reverseAdjList(self):
        # reverse -> stack like
        for k in self.adj:
            self.adj[k].reverse() # inline reverse

    @classmethod
    def fromFile(cls, fn):
        "read graph data from file"
        with open(fn) as f:
            cls.nV = int(f.readline().split('\n')[0])
            cls.nE = int(f.readline().split('\n')[0])
            lines = f.readlines()

        edges = []
        for l in lines:
            (v, w) = l.rstrip().split(' ')
            edges.append((int(v), int(w)))

        return cls(edges)

    def printGraph(self):
        print ("-----------------")
        print ("%d vetices & %d edges:" % (self.nV, self.nE))
        # print ("Constucted Graph:")
        for k in self.adj:
            print ("{0}: {1}".format(k, self.adj[k]))
        print ("-----------------")

    def numberOfSelfLoops(self):
        cnt = 0
        for v in self.adj:
            for w in self.adj[v]:
                if (v == w):
                    cnt += 1
        return cnt/2

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.nE += 1


if __name__ == '__main__':
    fn = "../algs4-data/tinyCG.txt"
    g = Graph.fromFile(fn)
