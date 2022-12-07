import sys


def main():
    cwd = []
    ds = {'/': 0}
    for l in [l.strip().split() for l in sys.stdin]:
        if 'dir' == l[0]:
            ds[''.join(cwd) + l[1]] = 0 
            continue
        if '$' == l[0]:
            if 'cd' == l[1]:
                if '/' == l[2]:
                    cwd = ['/']
                    continue
                if '..' == l[2]:
                    cwd.pop()
                    continue
                cwd.append(l[2].strip()) 
            continue
        for p in [''.join(cwd[:i + 1]) for i in range(len(cwd))]:
            ds[p] += int(l[0])
    print sum([v for k, v in ds.items() if v <= 100000])
    print min([v for k, v in ds.items() if v >= 30000000 - (70000000 - ds['/'])])


if '__main__' == __name__:
    main()

