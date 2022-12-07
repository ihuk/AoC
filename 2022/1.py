#!/usr/bin/env python
import sys

def main():
    weights = []
    weight = 0
    for l in sys.stdin:
        print l
        if not l.strip():
            weights.append(weight)
            weight = 0
            continue
        weight += int(l.strip())
    elf_weights = sorted(enumerate(weights), key=lambda e: e[1])
    elf, weight = elf_weights[-1]
    print "mve: elf {} with total weight of {} calories".format(elf, weight)
    result = sum([ew[1] for ew in elf_weights[-3:]])
    print "total wight by top 3 elfs: {}".format(result)


if '__main__' == __name__:
    main()
