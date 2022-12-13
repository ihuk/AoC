import sys
from itertools import groupby


def main():
    gs = groupby(enumerate((l.strip() for l in sys.stdin)), lambda (i, _): i / 3)
    ps = []
    for _, r in gs:
        c = set.intersection(*map(lambda (_, l): set(l), r))
        ps.append(sum(map(lambda i: ord(i) - ord('A') + 27 if i.isupper() else ord(i) - ord('a') + 1, c)))
    print sum(ps) 


if '__main__' == __name__:
    main()

