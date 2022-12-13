import sys
from collections import defaultdict


def main():
    heightmap = []
    for i, l in enumerate([l.strip() for l in sys.stdin]):
        heightmap.append([])
        for j, c in enumerate(l):
            if 'S' == c:
                start = (j, i)
                c = 'a'
            if 'E' == c:
                end = (j, i)
                c = 'z'
            heightmap[i].append(ord(c) - ord('a'))
    graph = defaultdict(list)
    for i, r in enumerate(heightmap):
        for j, w in enumerate(r):
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if j + dx < 0 or j + dx > len(r) - 1 or i + dy < 0 or i + dy > len(heightmap) - 1:
                    continue
                w = heightmap[i + dy][j + dx] - heightmap[i][j]
                if w > 1:
                    continue
                graph[(j, i)].append((j + dx, i + dy))
    rs = []
    #ss = [start]
    ss = [(x, y) for y in range(len(heightmap)) for x in range(len(heightmap[0])) if 0 == heightmap[y][x]]
    for s in ss:
        ps = bfs(graph, s, end)
        p = []
        v = end
        while True:
            u = ps.get(v, None)
            if not u:
                break
            p.append(u)
            v = u
        if p:
            rs.append(len(p))
    print min(rs) 


def bfs(g, r, t):
    q = [r]
    vs = set([r])
    ps = {r: []} 
    while q:
        v = q.pop(0)
        if v == t:
            return ps 
        for e in g[v]:
            if e in vs:
                continue 
            ps[e] = v
            vs.add(e)
            q.append(e)
    return ps


if '__main__' == __name__:
    main()

