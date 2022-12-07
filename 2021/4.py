import sys

def main():
    nums = [int(n.strip()) for n in sys.stdin.readline().split(',')]
    sys.stdin.readline()
    tables = []
    table = []
    for l in sys.stdin:
        if not l.strip():
            tables.append(table)
            table = []
        table += [int(n.strip()) for n in l.strip().split(' ') if n]
    tables.append(table)
    solutions = set()
    for n in nums:
        for t, _ in enumerate(tables):
            if t in solutions:
                continue
            tables[t] = [-1 if x == n else x for x in tables[t]]
            for r in range(5):
                if all([-1 == x for x in tables[t][r * 5:r * 5 + 5]]):
                    score = sum(x for x in tables[t] if x > -1) * n
                    print "bingo!", score
                    solutions.add(t)
                    if len(solutions) == len(tables):
                        return
            for c in range(5):
                if all([-1 == x for x in tables[t][c::5]]):
                    score = sum(x for x in tables[t] if x > -1) * n
                    print "bingo!", score
                    solutions.add(t)
                    if len(solutions) == len(tables):
                        return

if '__main__' == __name__:
    main()
