from graph-SymbolGraph import SymbolGraph
from graph-BreadthFirstPaths import BreadthFirstPaths

class DegreesOfSeparation(object):
    def main(self, fn, sp, s):
        sg = SymbolGraph(fn, sp)
        g = sg.g
        bfs = BreadthFirstPaths(g, s)
        sink = str(input())
        while (sink != 'quit'):
            if (sg.contains(sink)):
                if (bfs.hasPathTo(sink)):
                    for (v in bfs.pathTo(sink)):
                        print ("   " + v)
            else:
                print ("Not in database.")

            sink = str(input())


if __name__ == '__main__':
    fn = "../algs4-data/routs.txt"
    sp = ' '
    s  = 'JFK'
    DegreesOfSeparation().main(fn, sp, s)
