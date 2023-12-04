import re
import sys


def main():
    result = 0
    for ps in [ps.split('|') for _, ps in [l.strip().split(':') for l in sys.stdin]]:
        wss, nss = ps
        wns = set([int(w) for w in wss.split()])
        cns = set([int(n) for n in nss.split()])
        pns = cns.intersection(wns)
        if not pns:
            continue
        result += 2 ** (len(pns) - 1)
    print(result)


if '__main__' == __name__:
    main()



