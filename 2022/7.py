import sys
from collections import defaultdict

def main():
    ds = defaultdict(lambda: 0)
    cwd = []
    for o in [l.strip().split() for l in sys.stdin]:
        if 'dir' == o[0]:
            continue
        if '$' == o[0]:
            if 'cd' == o[1]:
                if '/' == o[2]:
                    cwd = ['/']
                    continue
                if '..' == o[2]:
                    cwd.pop()
                    continue
                cwd.append(o[2].strip()) 
            continue
        for p in [''.join(cwd[:i + 1]) for i in range(len(cwd))]:
            ds[p] += int(o[0])
    print sum([v for k, v in ds.items() if v <= 100000])
    print min([v for k, v in ds.items() if v >= 30000000 - (70000000 - ds['/'])])

if '__main__' == __name__:
    main()

