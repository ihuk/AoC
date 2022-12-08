import sys


def main():
    m = [[int(c) for c in l] for l in [l.strip() for l in sys.stdin] for c in l.split()]
    visible = []
    scenic = []
    for i, r in enumerate(m):
        for c, h in enumerate(r):
            left = r[:c]
            right = r[c + 1:] 
            top = [rt[c] for rt in m[:i]]
            bottom = [rb[c] for rb in m[i + 1: ]]
            if any([all(lh < h for lh in left), all(rh < h for rh  in right), all(th < h for th in top), all(bh < h for bh  in bottom)]):
                visible.append((i, c))
            scenic.append(dist(h, reversed(left)) * dist(h, right) * dist(h, reversed(top)) * dist(h, bottom))
    print len(visible)
    print max(scenic)


def dist(h, l):
    dist = 0
    for e in l:
        dist += 1
        if e >= h:
            break
    return dist


if '__main__' == __name__:
    main()


