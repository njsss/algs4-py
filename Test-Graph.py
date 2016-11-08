from collections import defaultdict

# readin files
fn = '../algs4-data/tinyG.txt'
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
    print(g[k])
