from collections import defaultdict

class Graph(object):
    # graph
    def constructGraph(self, fn):
        # read in graph txt file
        with open(fn) as f:
            v = f.readline().split('\n')[0]
            e = f.readline().split('\n')[0]
            # print ("vetex: {0:1s}\n edges: {1:1s}".format(v,e))
            lines = f.readlines()

        # construct graph
        g = defaultdict(list)    # graph
        for l in lines:
            v, w = l.rstrip().split(' ')
            v = int(v)
            w = int(w)
            g[v].append(w)
            g[w].append(v)

        # reverse it like a stack
        for k in g:
            g[k].reverse()  # inline reverse
            print (g[k])

        return g

    def depthsFirstPaths(self, g, s):
        edgeTo = {}    # adjecent
        marked = {}    # visited vetex
        self.dfs(g, s, marked, edgeTo)

        for v in g:
            print (str(s) + " to " + str(v) + ": ", end='')
            if (marked[v]):
                path = self.pathTo(s, v, marked, edgeTo)
                for x in range(len(path)):
                    p = path.pop()
                    if (p == s):
                        print (str(p),end="")
                    else:
                        print ("-" + str(p),end="")
                print ("")

    def dfs(self, g, v, marked, edgeTo):
        marked[v] = True

        for w in g[v]:
            if ((w not in marked) or (not marked[w])):
                edgeTo[w] = v
                self.dfs(g, w, marked, edgeTo)

    def pathTo(self, s, v, marked, edgeTo):
        """
        :type: s: vetex, src vetex
        :type: v: vetex, dst vetex
        :type: makred: dict, visted vetext
        :type: edgeTo: dict, edge
        :rtype: path: List, return path
        """
        # no path to
        if (not marked):
            return None

        path = []
        x = v
        while (x != s):
            path.append(x)
            x = edgeTo[x]

        # add source path list
        path.append(s)
        return path





if __name__ == '__main__':
    fn = "../algs4-data/tinyCG.txt"
    g = Graph().constructGraph(fn)
    Graph().depthsFirstPaths(g, 0)
