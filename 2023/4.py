import re
import sys


def main():
    points = 0
    copies = {}
    for l in [l.strip()for l in sys.stdin]:
        cs, cnss = [s.strip() for s in l.split(':')]
        c = int(cs.split()[-1])
        wss, nss = cnss.split('|')
        wns = set([int(n) for n in wss.split()])
        cns = set([int(n) for n in nss.split()])
        ps = len(cns.intersection(wns))
        if ps:
            points += 2**(ps - 1)
        copies[c] = copies.get(c, 0) + 1
        for cn in range(c + 1, c + ps + 1):
            copies[cn] = copies.get(cn, 0) + copies[c]
    print(points)
    print(sum(copies.values()))


if '__main__' == __name__:
    main()

