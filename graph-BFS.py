from collections import defaultdict, deque

class BreadthFirstPaths(object):
    self.nV = 0
    self.nE = 0

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
            print (g[k])

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

    def breadthFirstPaths(self, fn):
        edges = self.loadTextData(fn)
        g = self.constructGraph(edges)


    def bfs(self, g, v, marked, edgeTo):
        queue = deque()
        marked[s] = True
        queue.append(s)
        while (queue):
            v = queue.popleft()
            for w in g[v]:
                if (not marked[w]):
                    edgeTo[w] = v
                    makred[w] = True
                    queue.append(w)
        return


if __name__ == '__main__':
    fn = "../algs4-data/tinyCG.txt"
    BreadthFirstPaths().breadthFirstPaths(fn)
