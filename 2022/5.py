import sys
from itertools import takewhile
from collections import defaultdict


def main():
    img = reversed(list(takewhile(lambda l: l, (l.strip('\n') for l in sys.stdin))))
    cls = dict([(c, l) for l, c in enumerate(next(img)) if c.strip()])
    stacks = defaultdict(lambda: [])
    #for l in img:
    #    for c in sorted(cls.keys()):
    #        v = l[cls[c]].strip()
    #        if not v:
    #            continue
    #        stacks[c].append(v)
    stacks = {c: [l[cls[c]].strip() for l in img if l[cls[c]].strip()] for c in sorted(cls.keys())}
    print stacks
    src = [l.strip().split() for l in sys.stdin if l]
    commands = [(int(n), s, d) for _, n, _, s, _, d in src]
    for n, s, d in commands:
        stacks[d] += stacks[s][-n:]
        stacks[s] = stacks[s][:-n]
    print ''.join([stacks[c][-1] for c in sorted(cls.keys()) if stacks[c]])

    
if '__main__' == __name__:
    main()

