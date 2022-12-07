import sys


def main():
    o = { 'A': 'r', 'B': 'p', 'C': 's' }
    a = { 'X': {'r': 's', 'p': 'r', 's': 'p'}, 'Y': {'r': 'r', 'p': 'p', 's': 's'}, 'Z': {'r': 'p', 'p': 's', 's': 'r'}}
    rs = { 'rr': 4, 'rp': 8, 'rs': 3, 'pp': 5, 'pr': 1, 'ps': 9, 'ss': 6, 'sr': 7, 'sp': 2}
    print sum(map(lambda g: rs[g], map(lambda r: o[r[0]] + a[r[1]][o[r[0]]], (l.split() for l in sys.stdin))))


if '__main__' == __name__:
    main()
