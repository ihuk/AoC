import sys

def main():
    def bf(ns, b):
        os = sum([n >> b & 1 for n in ns])
        return os, len(ns) - os
    ogrs = []
    csrs = []
    nbits = 0
    for l in sys.stdin:
        ogrs.append(int(l, 2))
        csrs.append(int(l, 2))
        nbits = len(l.strip())
    for b in reversed(range(nbits)):
        obs, zbs = bf(ogrs, b)
        ogrsb = 1 if obs >= zbs else 0
        ogrs = [n for n in ogrs if (n >> b) & 1 == ogrsb]
        if len(ogrs) < 2:
            break
    for b in reversed(range(nbits)):
        obs, zbs = bf(csrs, b)
        csrsb = 1 if obs < zbs else 0
        csrs = [n for n in csrs if (n >> b) & 1 == csrsb]
        if len(csrs) < 2:
            break
    print ogrs[0] * csrs[0]


if '__main__' == __name__:
    main()
