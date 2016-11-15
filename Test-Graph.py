from collections import defaultdict

def dfs(g, v, marked, edgeTo, count):
    marked[v] = True
    count += 1
    for w in g[v]:
        if ((w not in marked) or (not marked[w])):
            edgeTo[w] = v
            dfs(g, w, marked, edgeTo, count)

def pathTo(s, v, marked, edgeTo):
    if (not marked):
        return None
        
    path = []
    x = v
    while (x != s):
        path.append(x)
        x = edgeTo[x]
    
    path.append(s)
    
    return path

# readin files
fn = '../algs4-data/tinyCG.txt'
with open(fn) as f:
    v = f.readline().split('\n')[0]
    e = f.readline().split('\n')[0]
    print (v, e)

    lines = f.readlines()


# construct graph, adj
g = defaultdict(list)
for l in lines:
    v,w = l.rstrip().split(' ')
    v = int(v)
    w = int(w)
    # print (v,w)
    g[v].append(w)
    g[w].append(v)

for k in g:
    g[k].reverse()
    print(g[k])

count = 0
marked = {}
edgeTo = {}
s = 0
dfs(g, s, marked, edgeTo, count)

for v in g:
    print (str(s) + " to " + str(v) + ": ", end="")
    if (marked[v]):
        path = pathTo(s, v, marked, edgeTo)
        for x in range(len(path)):
            p = path.pop()
            if (p == s):
                print (str(p),end="")
            else:
                print ("-" + str(p),end="")
        print ("")