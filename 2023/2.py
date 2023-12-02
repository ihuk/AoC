import sys

LIMITS = {
    'red': 12,
    'green': 13, 
    'blue': 14
}

def main():
    gs = [(int(g.split()[1]), [(c, int(n)) for n, c in [cs.split() for s in ss.split(';') for cs in s.split(',')]]) for g, ss in (l.strip().split(':') for l in sys.stdin)]
    print(sum(g for g, ss in gs if all(n <= LIMITS[c] for c, n in ss)))
    print(sum(reduce(lambda x, y: x * y, [max(n for c, n in ss if c == k) for k in LIMITS.keys()]) for _, ss in gs))
        

if '__main__' == __name__:
    main()



