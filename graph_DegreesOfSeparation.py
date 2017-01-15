from graph_SymbolGraph import SymbolGraph
from graph_BreadthFirstPaths import BreadthFirstPaths

class DegreesOfSeparation(object):
    def main(self, fn, sp, s):
        sg = SymbolGraph(fn, sp)
        g = sg.g
        g.reverseAdjList()
        bfs = BreadthFirstPaths(g, s)
        sink = str(input())
        while (sink != 'quit'):
            if (sg.contains(sink)):
                if (bfs.hasPathTo(sink)):
                    path = bfs.pathTo(sink)
                    path.reverse()
                    for v in path:
                        print ("   " + v)
            else:
                print ("Not in database.")

            sink = str(input())


if __name__ == '__main__':
    # fn = "../algs4-data/routes.txt"
    # sp = ' '
    # s  = 'JFK'
    fn = "../algs4-data/movies.txt"
    sp = '/'
    s = 'Animal House (1978)'
    DegreesOfSeparation().main(fn, sp, s)
